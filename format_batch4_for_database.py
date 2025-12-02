#!/usr/bin/env python3
"""
Format Batch 4 research into database table format
Extracts key fields from research markdown and formats for comprehensive_exercise_database_v2.md
"""

import re

# Read the research file
with open("batch_4_chest_exercises_research.md", "r", encoding="utf-8") as f:
    content = f.read()

# Split into exercise sections (looking for ### followed by number and name)
exercise_pattern = r'###\s+(\d+)\.\s+([^\n]+)\n\n\*\*Primary Muscles:\*\*\s+([^\n]+)\n\*\*Secondary Muscles:\*\*\s+([^\n]+)\n\*\*Type:\*\*\s+([^\n]+)\n\*\*Equipment:\*\*\s+([^\n]+)\n\n\*\*Step-by-Step Instructions.*?\n(.*?)\n\n\*\*Key Points for Advanced Users.*?\n(.*?)\n\n\*\*Scientific References.*?\n(.*?)\n\n\*\*Applicable Sports Tags.*?\n([^\n]+)'

exercises = re.findall(exercise_pattern, content, re.DOTALL)

print(f"Found {len(exercises)} exercises\n")
print("=" * 80)

# Format each exercise for database table
for idx, exercise in enumerate(exercises, 1):
    ex_num, name, primary, secondary, ex_type, equipment, steps, key_points, refs, sports = exercise

    # Clean up steps (extract just the numbered list items)
    steps_lines = [line.strip() for line in steps.split('\n') if re.match(r'^\d+\.', line.strip())]
    steps_clean = ' '.join(steps_lines)

    # Clean up key points (extract bullet/numbered items)
    key_points_lines = []
    for line in key_points.split('\n'):
        line = line.strip()
        if line.startswith('-') or line.startswith('**-'):
            # Remove markdown and bullet
            line = re.sub(r'\*\*', '', line)
            line = line.lstrip('- ').strip()
            if line:
                key_points_lines.append(line)
    key_points_clean = ' '.join(key_points_lines[:5])  # Max 5 points

    # Extract first 3-4 references (just the main citation)
    refs_lines = []
    for line in refs.split('\n'):
        line = line.strip()
        if re.match(r'^\d+\.', line):
            # Clean up markdown links
            line = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', line)
            line = re.sub(r'https?://[^\s]+', '', line)
            refs_lines.append(line.strip())
    refs_clean = ' | '.join(refs_lines[:4])  # Max 4 refs

    # Clean sports tags
    sports_clean = sports.strip()

    # Determine level based on exercise name and type
    if 'kneeling' in name.lower() or 'elevated' in name.lower():
        level = "Beginner"
    elif 'alternating' in name.lower() or 'twisting' in name.lower() or 'medicine ball' in name.lower():
        level = "Advanced"
    elif 'single-arm' in name.lower():
        level = "Intermediate"
    elif 'incline' in name.lower():
        level = "Intermediate"
    else:
        level = "Beginner"

    # Determine modality
    if 'cable' in equipment.lower():
        modality = "Cables"
    elif 'machine' in equipment.lower():
        modality = "Fixed Resistance"
    elif 'dumbbell' in equipment.lower() or 'barbell' in equipment.lower():
        modality = "Free Weight"
    elif 'bodyweight' in equipment.lower() or 'medicine ball' in equipment.lower():
        modality = "Bodyweight"
    else:
        modality = "Free Weight"

    print(f"\nExercise {idx}: {name}")
    print(f"Primary: {primary[:60]}...")
    print(f"Secondary: {secondary[:60]}...")
    print(f"Type: {ex_type} | Level: {level} | Modality: {modality}")
    print(f"Steps: {steps_clean[:100]}...")
    print(f"Key Points: {key_points_clean[:100]}...")
    print(f"Sports: {sports_clean[:60]}...")
    print("-" * 80)

print("\n" + "=" * 80)
print(f"Total exercises processed: {len(exercises)}")
print("\nNote: This script extracts the key data. Use this output to manually format")
print("the table rows for comprehensive_exercise_database_v2.md")
