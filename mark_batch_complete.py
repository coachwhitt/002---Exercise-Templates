#!/usr/bin/env python3
"""
Mark the first 20 exercises in Origym.csv as COMPLETE
"""

import csv

def main():
    # Read the CSV
    with open('Origym.csv', 'r', encoding='utf-8-sig', newline='') as f:
        lines = f.readlines()

    # Keep header lines (first 4 lines)
    header_lines = lines[:4]

    # Process the data section
    data_lines = lines[4:]

    # Parse CSV and update status
    reader = csv.DictReader(data_lines)
    fieldnames = reader.fieldnames

    rows = []
    count = 0
    for row in reader:
        if count < 20:  # First 20 exercises
            row['Status'] = 'COMPLETE'
            count += 1
        rows.append(row)

    # Write back to file
    with open('Origym.csv', 'w', encoding='utf-8', newline='') as f:
        # Write header lines
        for line in header_lines:
            f.write(line)

        # Write CSV data with updated Status
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"✓ Marked first 20 exercises as COMPLETE")
    print(f"✓ Total exercises: {len(rows)}")
    print(f"✓ Complete: {sum(1 for r in rows if r['Status'] == 'COMPLETE')}")
    print(f"✓ Pending: {sum(1 for r in rows if r['Status'] == 'PENDING')}")

if __name__ == '__main__':
    main()
