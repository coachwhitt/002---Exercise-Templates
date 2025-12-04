#!/usr/bin/env python3
"""
Compare exercises in our research database with Origym CSV.
Identify which Origym exercises are missing from our research.
"""

import csv
import re
from difflib import SequenceMatcher

def normalize_exercise_name(name):
    """Normalize exercise names for comparison."""
    # Convert to lowercase
    name = name.lower().strip()
    # Replace hyphens and underscores with spaces
    name = name.replace('-', ' ').replace('_', ' ')
    # Remove extra spaces
    name = ' '.join(name.split())
    # Remove common variations
    name = name.replace('dumbbell', 'db')
    name = name.replace('barbell', 'bb')
    name = name.replace('machine', 'mach')
    return name

def similarity_ratio(a, b):
    """Calculate similarity ratio between two strings."""
    return SequenceMatcher(None, normalize_exercise_name(a), normalize_exercise_name(b)).ratio()

def load_our_exercises():
    """Load exercises from our v3 CSV."""
    exercises = set()

    with open('/mnt/z/coachwhitt/ai/002 - Exercise Templates/comprehensive_exercise_database_v3.csv', 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            exercises.add(row['Exercise'].strip())

    return exercises

def load_origym_exercises():
    """Load all unique exercises from Origym CSV."""
    exercises = set()

    with open('/mnt/z/coachwhitt/ai/002 - Exercise Templates/Exercise data.csv', 'r', encoding='utf-8-sig') as f:
        reader = csv.reader(f)
        # Skip header row
        next(reader)

        for row in reader:
            for cell in row:
                cell = cell.strip()
                # Skip empty cells and separator lines
                if cell and not cell.startswith('---') and cell != '':
                    # Clean up the exercise name
                    cell = cell.replace('_', '-')
                    exercises.add(cell)

    return exercises

def main():
    print("📋 Loading exercises from our research database (v3)...")
    our_exercises = load_our_exercises()
    print(f"   Found {len(our_exercises)} exercises in our database")

    print("\n📋 Loading exercises from Origym CSV...")
    origym_exercises = load_origym_exercises()
    print(f"   Found {len(origym_exercises)} unique exercises in Origym CSV")

    print("\n🔍 Comparing databases...")

    # Find missing exercises (in Origym but not in our database)
    missing_exercises = []

    for origym_ex in origym_exercises:
        # Try exact match first
        found_exact = False
        for our_ex in our_exercises:
            if normalize_exercise_name(origym_ex) == normalize_exercise_name(our_ex):
                found_exact = True
                break

        if not found_exact:
            # Try fuzzy match (85% similarity threshold)
            found_fuzzy = False
            best_match = None
            best_ratio = 0

            for our_ex in our_exercises:
                ratio = similarity_ratio(origym_ex, our_ex)
                if ratio > best_ratio:
                    best_ratio = ratio
                    best_match = our_ex

            if best_ratio >= 0.85:
                found_fuzzy = True
                print(f"   ✓ Fuzzy match ({best_ratio:.0%}): '{origym_ex}' ≈ '{best_match}'")

            if not found_fuzzy:
                missing_exercises.append({
                    'origym_name': origym_ex,
                    'best_match': best_match,
                    'similarity': best_ratio
                })

    print(f"\n📊 Comparison Results:")
    print(f"   Our database: {len(our_exercises)} exercises")
    print(f"   Origym CSV: {len(origym_exercises)} exercises")
    print(f"   Missing from our database: {len(missing_exercises)} exercises")

    if missing_exercises:
        print("\n❌ Missing Exercises (in Origym but NOT in our database):")
        print("\nHigh confidence missing (< 60% similarity):")

        high_confidence = [ex for ex in missing_exercises if ex['similarity'] < 0.60]
        medium_confidence = [ex for ex in missing_exercises if 0.60 <= ex['similarity'] < 0.85]

        print(f"\n🔴 HIGH PRIORITY - Definitely missing ({len(high_confidence)} exercises):")
        for ex in sorted(high_confidence, key=lambda x: x['origym_name']):
            print(f"   - {ex['origym_name']}")
            if ex['best_match']:
                print(f"     (Closest match: '{ex['best_match']}' - {ex['similarity']:.0%} similar)")

        print(f"\n🟡 MEDIUM PRIORITY - Possibly missing ({len(medium_confidence)} exercises):")
        for ex in sorted(medium_confidence, key=lambda x: x['origym_name']):
            print(f"   - {ex['origym_name']}")
            if ex['best_match']:
                print(f"     (Closest match: '{ex['best_match']}' - {ex['similarity']:.0%} similar)")

        # Write to file for easier review
        print("\n📄 Writing missing exercises to file...")
        with open('/mnt/z/coachwhitt/ai/002 - Exercise Templates/missing_exercises_list.txt', 'w', encoding='utf-8') as f:
            f.write("# Missing Exercises from Origym CSV\n")
            f.write(f"# Total missing: {len(missing_exercises)}\n")
            f.write(f"# Generated: 2025-12-04\n\n")

            f.write(f"## HIGH PRIORITY - Definitely Missing ({len(high_confidence)} exercises)\n")
            f.write("## These exercises are in Origym but NOT in our research database\n\n")
            for ex in sorted(high_confidence, key=lambda x: x['origym_name']):
                f.write(f"{ex['origym_name']}\n")
                if ex['best_match']:
                    f.write(f"  # Closest match: '{ex['best_match']}' ({ex['similarity']:.0%})\n")

            f.write(f"\n## MEDIUM PRIORITY - Possibly Missing ({len(medium_confidence)} exercises)\n")
            f.write("## These might be variations or similar exercises we already have\n\n")
            for ex in sorted(medium_confidence, key=lambda x: x['origym_name']):
                f.write(f"{ex['origym_name']}\n")
                if ex['best_match']:
                    f.write(f"  # Similar to: '{ex['best_match']}' ({ex['similarity']:.0%})\n")

        print(f"   ✅ Created missing_exercises_list.txt")

        # Also create a clean list for research batch
        with open('/mnt/z/coachwhitt/ai/002 - Exercise Templates/missing_exercises_clean.txt', 'w', encoding='utf-8') as f:
            f.write("# Missing Exercises - Clean List for Research\n\n")
            for ex in sorted(high_confidence, key=lambda x: x['origym_name']):
                f.write(f"{ex['origym_name']}\n")

        print(f"   ✅ Created missing_exercises_clean.txt ({len(high_confidence)} exercises)")

    else:
        print("\n✅ All Origym exercises are in our database!")

    print("\n📈 Coverage Analysis:")
    coverage = ((len(origym_exercises) - len(missing_exercises)) / len(origym_exercises)) * 100
    print(f"   Database coverage: {coverage:.1f}%")
    print(f"   Exercises to research: {len([ex for ex in missing_exercises if ex['similarity'] < 0.60])}")

if __name__ == '__main__':
    main()
