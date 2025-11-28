#!/usr/bin/env python3
"""
Extract the next 20 PENDING exercises from Origym.csv for Batch 1b
"""

import csv

def main():
    # Read the CSV
    with open('Origym.csv', 'r', encoding='utf-8-sig', newline='') as f:
        lines = f.readlines()

    # Process the data section (skip first 4 lines)
    data_lines = lines[4:]

    # Parse CSV and find next 20 PENDING exercises
    reader = csv.DictReader(data_lines)

    batch_1b = []
    for row in reader:
        if row['Status'] == 'PENDING':
            batch_1b.append(row)
            if len(batch_1b) == 20:
                break

    # Save to file
    with open('batch_1b_exercises.txt', 'w', encoding='utf-8') as f:
        for i, ex in enumerate(batch_1b, 1):
            f.write(f"{i}. {ex['Exercise']}|{ex['Muscle Group']}|{ex['Level']}|{ex['Modality']}|{ex['Joint']}|{ex['U/L/C']}|{ex['P / P']}\n")

    print(f"✓ Extracted {len(batch_1b)} exercises for Batch 1b")
    print(f"✓ Saved to: batch_1b_exercises.txt")

    # Group by muscle group
    by_muscle = {}
    for ex in batch_1b:
        muscle = ex['Muscle Group']
        if muscle not in by_muscle:
            by_muscle[muscle] = []
        by_muscle[muscle].append(ex['Exercise'])

    print(f"\nBreakdown by muscle group:")
    for muscle, exercises in sorted(by_muscle.items()):
        print(f"  {muscle}: {len(exercises)} exercises")
        for ex_name in exercises:
            print(f"    - {ex_name}")

if __name__ == '__main__':
    main()
