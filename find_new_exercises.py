#!/usr/bin/env python3
"""
Find new exercises from Origym CSV that aren't already in our database
"""

import csv
import re

def normalize_name(name):
    """Normalize exercise names for comparison"""
    # Remove special characters, convert to lowercase, remove extra spaces
    name = name.lower()
    name = re.sub(r'[^\w\s-]', '', name)
    name = re.sub(r'\s+', ' ', name)
    name = name.strip()
    return name

def main():
    # Read existing exercises from our CSV
    existing_exercises = set()
    with open('exercise_database_complete_v2.csv', 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            normalized = normalize_name(row['Exercise'])
            existing_exercises.add(normalized)

    print(f"Existing exercises in database: {len(existing_exercises)}\n")

    # Read Origym CSV and find new exercises
    new_exercises = []
    duplicates = []

    with open('Origym.csv', 'r', encoding='utf-8-sig', newline='') as f:
        lines = f.readlines()
        # Start from line 4 (index 4) which is the header line
        # Lines 0-3 are preamble text
        data_lines = lines[4:]

        # Parse CSV
        reader = csv.DictReader(data_lines)
        for row in reader:
            if not row.get('Exercise'):
                continue

            normalized = normalize_name(row['Exercise'])

            if normalized in existing_exercises:
                duplicates.append(row['Exercise'])
            else:
                new_exercises.append(row)

    print(f"Total in Origym CSV: {len(new_exercises) + len(duplicates)}")
    print(f"Duplicates (skipped): {len(duplicates)}")
    print(f"New exercises available: {len(new_exercises)}\n")

    # Group by muscle group
    by_muscle_group = {}
    for ex in new_exercises:
        muscle = ex['Muscle Group']
        if muscle not in by_muscle_group:
            by_muscle_group[muscle] = []
        by_muscle_group[muscle].append(ex)

    print("New exercises by muscle group:")
    for muscle, exercises in sorted(by_muscle_group.items()):
        print(f"  {muscle}: {len(exercises)} exercises")

    # Output first 50 new exercises for Session 7
    print(f"\n--- FIRST 50 NEW EXERCISES FOR SESSION 7 ---\n")
    for i, ex in enumerate(new_exercises[:50], 1):
        print(f"{i}. [{ex['Muscle Group']}] {ex['Exercise']} ({ex['Level']})")

    # Save all new exercises to a file for reference
    with open('new_exercises_list.txt', 'w', encoding='utf-8') as f:
        for i, ex in enumerate(new_exercises, 1):
            f.write(f"{i}. [{ex['Muscle Group']}] {ex['Exercise']} ({ex['Level']}) - {ex['Modality']}/{ex['Joint']}\n")

    print(f"\nFull list saved to: new_exercises_list.txt")

if __name__ == '__main__':
    main()
