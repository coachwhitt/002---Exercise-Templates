#!/usr/bin/env python3
"""
Convert CSV database to markdown table format.
"""

import csv

def csv_to_markdown(csv_file, md_file):
    """
    Convert CSV to markdown table format.

    Args:
        csv_file: Path to CSV file
        md_file: Path to output markdown file
    """
    with open(csv_file, 'r', encoding='utf-8') as infile, \
         open(md_file, 'w', encoding='utf-8') as outfile:

        reader = csv.reader(infile)

        # Read header
        header = next(reader)

        # Write markdown table header
        outfile.write('| ' + ' | '.join(header) + ' |\n')
        outfile.write('|' + '|'.join(['---' for _ in header]) + '|\n')

        # Write data rows
        row_count = 0
        for row in reader:
            if len(row) == 0:
                continue

            # Escape pipe characters in cell content
            escaped_row = [cell.replace('|', '\\|') for cell in row]

            outfile.write('| ' + ' | '.join(escaped_row) + ' |\n')
            row_count += 1

    print(f"✓ Converted {row_count} exercises to markdown format")
    print(f"Output: {md_file}")

if __name__ == "__main__":
    csv_file = "/mnt/z/coachwhitt/ai/002 - Exercise Templates/comprehensive_exercise_database_v3.1.1.csv"
    md_file = "/mnt/z/coachwhitt/ai/002 - Exercise Templates/comprehensive_exercise_database_v3.1.1.md"

    print("Converting CSV to Markdown...")
    csv_to_markdown(csv_file, md_file)
    print("✓ Complete!")
