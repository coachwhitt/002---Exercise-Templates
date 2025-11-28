#!/usr/bin/env python3
"""
Add a Status column to Origym.csv to track processing
"""

import csv

def main():
    # Read the original CSV
    with open('Origym.csv', 'r', encoding='utf-8-sig', newline='') as f:
        lines = f.readlines()

    # Keep header lines (first 4 lines)
    header_lines = lines[:4]

    # Process the data section
    data_lines = lines[4:]

    # Parse CSV and add Status column
    reader = csv.DictReader(data_lines)
    fieldnames = reader.fieldnames + ['Status']

    rows = []
    for row in reader:
        row['Status'] = 'PENDING'  # Default status
        rows.append(row)

    # Write back to file
    with open('Origym.csv', 'w', encoding='utf-8', newline='') as f:
        # Write header lines
        for line in header_lines:
            f.write(line)

        # Write CSV data with new Status column
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"✓ Added Status column to Origym.csv")
    print(f"✓ Total exercises: {len(rows)}")
    print(f"✓ All marked as PENDING")

if __name__ == '__main__':
    main()
