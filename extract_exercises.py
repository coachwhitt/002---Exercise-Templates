#!/usr/bin/env python3
"""
Extract exercises from markdown and create CSV
"""

import csv
import re

def main():
    input_file = 'comprehensive_exercise_database_v2.md'
    output_file = 'exercise_database_complete_v2.csv'

    exercises = []

    # CSV header
    header = ['Exercise', 'Primary Muscles', 'Secondary Muscles', 'Type', 'Equipment',
              'Level', 'Body Region', 'Movement', 'Modality', 'Steps for Beginners',
              'Advanced Key Points', 'Scientific Reference', 'Sports Tags', 'ExRx Video',
              'JEFIT Video', 'CoachWhitt Video']

    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find all table rows (lines starting with |)
    lines = content.split('\n')

    for i, line in enumerate(lines):
        # Skip if not a table row
        if not line.strip().startswith('|'):
            continue

        # Skip header rows
        if 'Exercise | Primary Muscles' in line:
            continue

        # Skip separator rows
        if '|---' in line:
            continue

        # Parse the row
        # Remove leading/trailing pipes
        line = line.strip()
        if line.startswith('|'):
            line = line[1:]
        if line.endswith('|'):
            line = line[:-1]

        # Split by pipe
        fields = [f.strip() for f in line.split('|')]

        # Filter out empty fields (from leading/trailing pipes)
        fields = [f for f in fields if f]

        # Only add if we have 16 fields and the first field is not empty and not "Exercise"
        if len(fields) == 16 and fields[0] and fields[0] != 'Exercise':
            exercises.append(fields)

    # Write CSV
    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        writer.writerow(header)

        for exercise in exercises:
            writer.writerow(exercise)

    print(f"✓ Converted {len(exercises)} exercises to {output_file}")
    print(f"✓ CSV has {len(header)} columns")
    print(f"\nFirst 5 exercises:")
    for i, ex in enumerate(exercises[:5]):
        print(f"  {i+1}. {ex[0]}")

if __name__ == '__main__':
    main()
