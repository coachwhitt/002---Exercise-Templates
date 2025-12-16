#!/usr/bin/env python3
"""
Add 3 video link placeholder columns to comprehensive_exercise_database_v3_17columns.md
- ExRx_Video_URL
- JEFIT_Video_URL
- CoachWhitt_Video_URL

All values will be empty strings as placeholders for future video links.
This creates the final 20-column database v3.1 structure.
"""

def add_video_columns():
    """
    Read 17-column database, add 3 video link columns, write to v3.1 file
    """
    input_file = "comprehensive_exercise_database_v3_17columns.md"
    output_file = "comprehensive_exercise_database_v3.1.md"

    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    output_lines = []
    data_row_count = 0

    for i, line in enumerate(lines):
        # Update header title from v3.0 to v3.1
        if line.startswith("# Comprehensive Scientific Exercise Database v3.0"):
            output_lines.append("# Comprehensive Scientific Exercise Database v3.1\n")
            continue

        # Skip until we reach the table header
        if "| Exercise | Primary Muscles" in line:
            # This is the header row - add 3 video link columns
            header = line.rstrip(" |\n") + " | ExRx_Video_URL | JEFIT_Video_URL | CoachWhitt_Video_URL |\n"
            output_lines.append(header)
            continue

        # Handle separator row
        if line.startswith("|----------|"):
            # Add separators for 3 video link columns
            separator = line.rstrip(" |\n") + "|-----------------|------------------|----------------------|\n"
            output_lines.append(separator)
            continue

        # Process data rows (rows that start with | and contain exercise data)
        if line.startswith("|") and not line.startswith("|-------"):
            # Parse the row into columns
            columns = [col.strip() for col in line.split("|")[1:-1]]  # Remove empty first/last

            if len(columns) >= 17:  # Should have 17 columns now
                # Add 3 empty video link columns as placeholders
                new_row = "| " + " | ".join(columns) + " |  |  |  |\n"
                output_lines.append(new_row)
                data_row_count += 1
            else:
                # Keep line as-is if it doesn't match expected format
                output_lines.append(line)
        else:
            # Keep all non-table lines as-is (headers, separators, etc.)
            output_lines.append(line)

    # Update the total exercises count in header if needed
    for i, line in enumerate(output_lines):
        if line.startswith("**Total Exercises:**"):
            output_lines[i] = f"**Total Exercises:** {data_row_count}\n"

    # Write output file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(output_lines)

    print(f"✅ Successfully processed {data_row_count} exercises")
    print(f"📝 Output file: {output_file}")
    print(f"📊 Added 3 video link columns: ExRx_Video_URL, JEFIT_Video_URL, CoachWhitt_Video_URL")
    print(f"📊 Database now has 20 columns (17 existing + 3 video links)")
    print(f"🎉 Database v3.1 complete!")

    return data_row_count


if __name__ == "__main__":
    count = add_video_columns()
    print(f"\n✨ Final database v3.1 complete! Total exercises: {count}")
    print(f"📋 Structure: 20 columns, {count} exercises")
