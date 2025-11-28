#!/usr/bin/env python3
"""
Extract exercises 41-80 from Origym.csv and split into Batch 2a (41-60) and Batch 2b (61-80)
"""

import csv

def main():
    # Read the CSV
    with open('Origym.csv', 'r', encoding='utf-8-sig', newline='') as f:
        lines = f.readlines()

    # Process the data section (skip first 4 lines)
    data_lines = lines[4:]

    # Parse CSV and find next 40 PENDING exercises
    reader = csv.DictReader(data_lines)

    batch_2_all = []
    for row in reader:
        if row['Status'] == 'PENDING':
            batch_2_all.append(row)
            if len(batch_2_all) == 40:
                break

    # Split into 2a and 2b
    batch_2a = batch_2_all[:20]
    batch_2b = batch_2_all[20:40]

    # Save Batch 2a
    with open('batch_2a_exercises.txt', 'w', encoding='utf-8') as f:
        for i, ex in enumerate(batch_2a, 1):
            f.write(f"{i}. {ex['Exercise']}|{ex['Muscle Group']}|{ex['Level']}|{ex['Modality']}|{ex['Joint']}|{ex['U/L/C']}|{ex['P / P']}\n")

    # Save Batch 2b
    with open('batch_2b_exercises.txt', 'w', encoding='utf-8') as f:
        for i, ex in enumerate(batch_2b, 1):
            f.write(f"{i}. {ex['Exercise']}|{ex['Muscle Group']}|{ex['Level']}|{ex['Modality']}|{ex['Joint']}|{ex['U/L/C']}|{ex['P / P']}\n")

    print(f"✓ Extracted 40 exercises for Batch 2")
    print(f"✓ Batch 2a: exercises 41-60 saved to batch_2a_exercises.txt")
    print(f"✓ Batch 2b: exercises 61-80 saved to batch_2b_exercises.txt")

    # Group by muscle group for both batches
    print(f"\n--- BATCH 2A (Exercises 41-60) ---")
    by_muscle_2a = {}
    for ex in batch_2a:
        muscle = ex['Muscle Group']
        if muscle not in by_muscle_2a:
            by_muscle_2a[muscle] = []
        by_muscle_2a[muscle].append(ex['Exercise'])

    for muscle, exercises in sorted(by_muscle_2a.items()):
        print(f"  {muscle}: {len(exercises)} exercises")
        for ex_name in exercises:
            print(f"    - {ex_name}")

    print(f"\n--- BATCH 2B (Exercises 61-80) ---")
    by_muscle_2b = {}
    for ex in batch_2b:
        muscle = ex['Muscle Group']
        if muscle not in by_muscle_2b:
            by_muscle_2b[muscle] = []
        by_muscle_2b[muscle].append(ex['Exercise'])

    for muscle, exercises in sorted(by_muscle_2b.items()):
        print(f"  {muscle}: {len(exercises)} exercises")
        for ex_name in exercises:
            print(f"    - {ex_name}")

if __name__ == '__main__':
    main()
