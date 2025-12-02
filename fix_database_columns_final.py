#!/usr/bin/env python3
"""
Final fix for column alignment in comprehensive_exercise_database_v2.md
Scientific Reference is at field index 13 (when split by |)
When there are multiple references separated by |, merge them with semicolon
"""

import re

def fix_table_row(line):
    """Fix a single table row by merging Scientific Reference column"""
    parts = line.split('|')

    # Should have 18 fields total (including empty at positions 0 and -1)
    # If more than 18, we have extra pipes in the Scientific Reference column (position 13)
    if len(parts) == 18:
        return line  # Already correct

    if len(parts) < 18:
        print(f"WARNING: Row has too few columns ({len(parts)}): {parts[2][:50] if len(parts) > 2 else 'unknown'}")
        return line  # Don't modify

    # Calculate how many extra fields we have
    extra = len(parts) - 18

    # Merge fields from position 13 to position 13+extra (inclusive)
    # These are the Scientific Reference fields that got split
    ref_parts = [parts[i].strip() for i in range(13, 13 + extra + 1) if parts[i].strip()]
    merged_ref = " ; ".join(ref_parts)

    # Rebuild the parts list
    fixed_parts = parts[:13] + [' ' + merged_ref + ' '] + parts[13 + extra + 1:]

    # Rejoin
    return '|'.join(fixed_parts)

# Read file
with open("comprehensive_exercise_database_v2.md", "r", encoding="utf-8") as f:
    lines = f.readlines()

fixed_lines = []
in_table = False
fixes = 0

for i, line in enumerate(lines, 1):
    # Detect table start
    if re.match(r'^\| Exercise \|', line):
        in_table = True
        fixed_lines.append(line)
        continue

    # Detect table end (line doesn't start with |)
    if in_table and not line.startswith('|'):
        in_table = False
        fixed_lines.append(line)
        continue

    # Process table rows
    if in_table and line.startswith('|') and not re.match(r'^\|[-\s|]+\|$', line):
        original_parts = line.split('|')
        if len(original_parts) != 18:
            fixed_line = fix_table_row(line)
            fixed_parts = fixed_line.split('|')
            if len(fixed_parts) == 18:
                fixes += 1
                exercise_name = original_parts[2].strip() if len(original_parts) > 2 else "unknown"
                print(f"Line {i}: Fixed {len(original_parts)} -> 18 columns - {exercise_name[:40]}")
            fixed_lines.append(fixed_line)
        else:
            fixed_lines.append(line)
    else:
        fixed_lines.append(line)

# Write output
with open("comprehensive_exercise_database_v2_fixed.md", "w", encoding="utf-8") as f:
    f.writelines(fixed_lines)

print(f"\n{'='*60}")
print(f"Processed {len(lines)} lines")
print(f"Applied {fixes} fixes")
print(f"{'='*60}")

# Validate
print("\nValidating output...")
with open("comprehensive_exercise_database_v2_fixed.md", "r") as f:
    fixed_content = f.read()

table_rows = [line for line in fixed_content.split('\n') if line.startswith('|') and not re.match(r'^\|[-\s|]+\|$', line)]
column_distribution = {}
for row in table_rows:
    col_count = len(row.split('|'))
    column_distribution[col_count] = column_distribution.get(col_count, 0) + 1

print("\nColumn distribution in fixed file:")
for cols in sorted(column_distribution.keys()):
    print(f"  {cols} fields (|-separated): {column_distribution[cols]} rows")

if len(column_distribution) == 1 and 18 in column_distribution:
    print("\n✅ SUCCESS! All table rows now have 18 fields (16 data columns).")
    print("\nReplace the original file with:")
    print("  mv comprehensive_exercise_database_v2_fixed.md comprehensive_exercise_database_v2.md")
else:
    print("\n⚠️  Some rows still have inconsistent column counts.")
    print("Manual review may be needed for remaining issues.")
