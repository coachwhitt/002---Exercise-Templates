#!/usr/bin/env python3
"""
Generate CSV export from comprehensive_exercise_database_v3.1.md for Google Sheets import
"""

import csv

def markdown_to_csv():
    """
    Read v3.1 markdown database and convert to CSV
    """
    input_file = "comprehensive_exercise_database_v3.1.md"
    output_file = "comprehensive_exercise_database_v3.1.csv"

    exercises = []
    header = None

    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    for line in lines:
        # Find the header row
        if line.startswith("| Exercise | Primary Muscles"):
            columns = [col.strip() for col in line.split("|")[1:-1]]
            header = columns
            continue

        # Skip separator row
        if line.startswith("|-------"):
            continue

        # Process data rows
        if line.startswith("|") and header and not line.startswith("|-------"):
            columns = [col.strip() for col in line.split("|")[1:-1]]

            # Only process if we have the expected number of columns
            if len(columns) == len(header):
                exercises.append(columns)

    # Write to CSV
    with open(output_file, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(exercises)

    print(f"✅ Successfully converted {len(exercises)} exercises to CSV")
    print(f"📝 Output file: {output_file}")
    print(f"📊 Columns: {len(header)}")
    print(f"📊 Rows: {len(exercises)} exercises")
    print(f"\n🎉 CSV ready for Google Sheets import!")

    return len(exercises)


if __name__ == "__main__":
    count = markdown_to_csv()
    print(f"\n✨ Database v3.1 CSV export complete! Total exercises: {count}")
