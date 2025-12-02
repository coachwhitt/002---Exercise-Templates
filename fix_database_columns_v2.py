#!/usr/bin/env python3
"""
Fix column alignment in comprehensive_exercise_database_v2.md - Version 2
Problem: Multiple scientific references separated by | are creating extra columns
Solution: Replace | with ; in the Scientific Reference field (column 12)
"""

import re

# Read the database file
with open("comprehensive_exercise_database_v2.md", "r", encoding="utf-8") as f:
    lines = f.readlines()

fixed_lines = []
table_mode = False
header_pattern = r"^\| Exercise \|"
separator_pattern = r"^\|[-\s|]+\|$"  # The |-------|----| separator line
data_row_pattern = r"^\|[^-]"  # Starts with | but not a dash

fixes_applied = 0

for line_num, line in enumerate(lines, 1):
    # Check if we're entering a table
    if re.match(header_pattern, line):
        table_mode = True
        fixed_lines.append(line)
        continue

    # Check if this is the separator line
    if table_mode and re.match(separator_pattern, line):
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
        parts = [p.strip() for p in line.split('|')]

        # Expected: 18 columns including empty first [0] and last [17]
        # 0: '', 1: Exercise, 2: Primary, 3: Secondary, 4: Type, 5: Equipment,
        # 6: Level, 7: Body Region, 8: Movement, 9: Modality, 10: Steps,
        # 11: Advanced, 12: Scientific Reference, 13: Sports Tags, 14: ExRx,
        # 15: JEFIT, 16: CoachWhitt, 17: ''

        original_col_count = len(parts)

        if len(parts) > 18:
            # We have extra columns
            extra_cols = len(parts) - 18

            # The extra columns are in the Scientific Reference field (starting at index 12)
            # We need to merge columns 12 through (12 + extra_cols) inclusive

            # Extract all the scientific reference parts
            ref_parts = []
            for i in range(12, 12 + extra_cols + 1):
                if i < len(parts) and parts[i]:
                    ref_parts.append(parts[i])

            # Merge with semicolon
            merged_refs = " ; ".join(ref_parts)

            # Rebuild parts list
            fixed_parts = (
                parts[:12] +  # Everything before Scientific Reference
                [merged_refs] +  # Merged Scientific Reference
                parts[12 + extra_cols + 1:]  # Everything after
            )

            # Rejoin into line
            fixed_line = '| ' + ' | '.join(fixed_parts[1:-1]) + ' |\n'
            fixed_lines.append(fixed_line)
            fixes_applied += 1

            print(f"Line {line_num}: Fixed {original_col_count} -> {len(fixed_parts)} columns")
            print(f"  Exercise: {parts[1][:50]}")
        else:
            # Line is correct length, keep as is
            fixed_lines.append(line)
    else:
        # Not a data row, keep as is
        fixed_lines.append(line)

# Write the fixed file
with open("comprehensive_exercise_database_v2_fixed.md", "w", encoding="utf-8") as f:
    f.writelines(fixed_lines)

print(f"\nSummary:")
print(f"Total lines processed: {len(lines)}")
print(f"Fixes applied: {fixes_applied}")
print(f"\nFixed database saved to: comprehensive_exercise_database_v2_fixed.md")
print("\nValidating...")

# Validate the output
import subprocess
result = subprocess.run(
    ["grep", "^|", "comprehensive_exercise_database_v2_fixed.md"],
    capture_output=True,
    text=True
)

column_counts = {}
for table_line in result.stdout.split('\n'):
    if table_line:
        col_count = table_line.count('|')
        column_counts[col_count] = column_counts.get(col_count, 0) + 1

print("\nColumn distribution in fixed file:")
for cols in sorted(column_counts.keys()):
    print(f"  {cols} columns: {column_counts[cols]} rows")

if len(column_counts) == 1 and 18 in column_counts:
    print("\n✓ SUCCESS: All rows have 18 columns!")
    print("\nYou can now replace the original file:")
    print("  mv comprehensive_exercise_database_v2_fixed.md comprehensive_exercise_database_v2.md")
else:
    print("\n✗ WARNING: Still have inconsistent column counts. Manual review needed.")
