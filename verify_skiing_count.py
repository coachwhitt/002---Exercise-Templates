#!/usr/bin/env python3
"""Verify the count of exercises with Skiing tag."""

import csv

csv_file = "/mnt/z/coachwhitt/ai/002 - Exercise Templates/comprehensive_exercise_database_v3.1.1.csv"

with open(csv_file, 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    header = next(reader)

    sports_tags_idx = header.index('Sports Tags')

    count = 0
    skiing_exercises = []

    for row in reader:
        if len(row) > sports_tags_idx:
            sports_tags = row[sports_tags_idx]
            if 'Skiing' in sports_tags:
                count += 1
                skiing_exercises.append(row[0])

    print(f"Total exercises with 'Skiing' tag: {count}")
    print(f"\nFirst 10 exercises:")
    for i, ex in enumerate(skiing_exercises[:10], 1):
        print(f"  {i}. {ex}")
