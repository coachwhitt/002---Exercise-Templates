#!/usr/bin/env python3
"""
Fix column alignment in comprehensive_exercise_database_v2.md
Problem: Multiple scientific references separated by | are creating extra columns
Solution: Replace | with a different separator (semicolon or line break) in the Scientific Reference column
"""

import re

# Read the database file
with open("comprehensive_exercise_database_v2.md", "r", encoding="utf-8") as f:
    lines = f.readlines()

fixed_lines = []
table_mode = False
header_pattern = r"^\| Exercise \|"
data_row_pattern = r"^\|[^-]"  # Starts with | but not the separator line

for line in lines:
    # Check if we're in a table
    if re.match(header_pattern, line):
        table_mode = True
        fixed_lines.append(line)
        continue

    # Check if table ended (non-table line)
    if table_mode and not line.startswith('|'):
        table_mode = False
        fixed_lines.append(line)
        continue

    # Process data rows in table
    if table_mode and re.match(data_row_pattern, line):
        # Split by | to get columns
        parts = line.split('|')

        # Expected structure (18 columns total including empty first and last):
        # 0: empty, 1: Exercise, 2: Primary, 3: Secondary, 4: Type, 5: Equipment,
        # 6: Level, 7: Body Region, 8: Movement, 9: Modality, 10: Steps,
        # 11: Advanced, 12: Scientific Reference, 13: Sports Tags, 14: ExRx,
        # 15: JEFIT, 16: CoachWhitt, 17: empty

        if len(parts) > 18:
            # We have extra columns - need to merge the Scientific Reference column
            # Scientific Reference is column 12 (index 12)
            # We need to merge columns 12 through (len(parts) - 6) back into column 12

            # Calculate how many extra columns we have
            extra_cols = len(parts) - 18

            # Merge the scientific reference columns (index 12 through 12+extra_cols)
            merged_refs = []
            for i in range(12, 12 + extra_cols + 1):
                if i < len(parts):
                    merged_refs.append(parts[i].strip())

            # Join with semicolon instead of pipe
            merged_ref_text = "; ".join(merged_refs)

            # Rebuild the line
            fixed_parts = parts[:12] + [merged_ref_text] + parts[12 + extra_cols + 1:]

            # Rejoin with |
            fixed_line = '|'.join(fixed_parts)
            fixed_lines.append(fixed_line)

            print(f"Fixed line with {len(parts)} columns -> {len(fixed_parts)} columns")
        else:
            # Line is correct, keep as is
            fixed_lines.append(line)
    else:
        # Not a data row, keep as is
        fixed_lines.append(line)

# Write the fixed file
with open("comprehensive_exercise_database_v2_fixed.md", "w", encoding="utf-8") as f:
    f.writelines(fixed_lines)

print("\nSummary:")
print(f"Total lines processed: {len(lines)}")
print(f"Fixed database saved to: comprehensive_exercise_database_v2_fixed.md")
print("\nPlease review the fixed file and then replace the original:")
print("  mv comprehensive_exercise_database_v2_fixed.md comprehensive_exercise_database_v2.md")
