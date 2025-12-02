#!/usr/bin/env python3
"""
Simple fix: Find ANY row with 20 fields that looks like a data row and fix it
Don't rely on table detection - just fix rows that match the pattern
"""

import re

with open("comprehensive_exercise_database_v2.md", "r", encoding="utf-8") as f:
    lines = f.readlines()

fixed_lines = []
fixes = 0

for i, line in enumerate(lines, 1):
    # Check if this is a data row (starts with | and has content, not a separator)
    if line.startswith('|') and not re.match(r'^\|[-\s|]+\|$', line) and '| Exercise |' not in line:
        parts = line.split('|')

        # If it has 20 fields, merge columns 13, 14, 15
        if len(parts) == 20:
            ref1 = parts[13].strip()
            ref2 = parts[14].strip()
            ref3 = parts[15].strip()
            merged = f" {ref1} ; {ref2} ; {ref3} "
            fixed_parts = parts[:13] + [merged] + parts[16:]
            fixed_line = '|'.join(fixed_parts)
            fixed_lines.append(fixed_line)
            fixes += 1
            exercise = parts[2].strip() if len(parts) > 2 else "unknown"
            print(f"Line {i}: Fixed 20 → 18 | {exercise[:50]}")
        else:
            fixed_lines.append(line)
    else:
        fixed_lines.append(line)

# Write output
with open("comprehensive_exercise_database_v2_FINAL.md", "w", encoding="utf-8") as f:
    f.writelines(fixed_lines)

print(f"\n{'='*70}")
print(f"Applied {fixes} fixes")
print(f"{'='*70}")

# Validate
print("\nValidating...")
with open("comprehensive_exercise_database_v2_FINAL.md", "r") as f:
    data_rows = [line for line in f if line.startswith('|') and not re.match(r'^\|[-\s|]+\|$', line) and '| Exercise |' not in line]

column_counts = {}
for row in data_rows:
    count = len(row.split('|'))
    column_counts[count] = column_counts.get(count, 0) + 1

print("\nColumn distribution:")
for c in sorted(column_counts.keys()):
    print(f"  {c} fields: {column_counts[c]} rows")

if len(column_counts) == 1 and 18 in column_counts:
    print(f"\n✅ SUCCESS! All {column_counts[18]} rows now have 18 fields!")
    print("\nReplace original with:")
    print("  mv comprehensive_exercise_database_v2_FINAL.md comprehensive_exercise_database_v2.md")
else:
    print("\n⚠️  Still have inconsistent columns")
