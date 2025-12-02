#!/usr/bin/env python3
"""
Definitive fix for column alignment in comprehensive_exercise_database_v2.md
Problem: Some rows have 20 fields because 3 scientific references are in separate columns (13, 14, 15)
Solution: Merge columns 13, 14, 15 into single column 13 with semicolon separator
"""

import re

def fix_table_row(line):
    """Fix a single table row by merging Scientific Reference columns"""
    parts = line.split('|')

    # Should have 18 fields total
    if len(parts) == 18:
        return line, False  # Already correct

    if len(parts) < 18:
        return line, False  # Don't modify incomplete rows

    # For rows with 19 fields: merge columns 13 and 14 into 13
    if len(parts) == 19:
        ref1 = parts[13].strip()
        ref2 = parts[14].strip()
        merged = f" {ref1} ; {ref2} "
        fixed_parts = parts[:13] + [merged] + parts[15:]
        return '|'.join(fixed_parts), True

    # For rows with 20 fields: merge columns 13, 14, and 15 into 13
    if len(parts) == 20:
        ref1 = parts[13].strip()
        ref2 = parts[14].strip()
        ref3 = parts[15].strip()
        merged = f" {ref1} ; {ref2} ; {ref3} "
        fixed_parts = parts[:13] + [merged] + parts[16:]
        return '|'.join(fixed_parts), True

    # For rows with 21+ fields: merge all extra fields starting at 13
    if len(parts) > 20:
        extra = len(parts) - 18
        refs = [parts[i].strip() for i in range(13, 13 + extra + 1) if parts[i].strip()]
        merged = f" {' ; '.join(refs)} "
        fixed_parts = parts[:13] + [merged] + parts[13 + extra + 1:]
        return '|'.join(fixed_parts), True

    return line, False

# Read file
with open("comprehensive_exercise_database_v2.md", "r", encoding="utf-8") as f:
    lines = f.readlines()

fixed_lines = []
in_table = False
fixes_by_type = {18: 0, 19: 0, 20: 0, 21: 0}
total_fixes = 0

for i, line in enumerate(lines, 1):
    # Detect table start
    if re.match(r'^\| Exercise \|', line):
        in_table = True
        fixed_lines.append(line)
        continue

    # Detect table end
    if in_table and not line.startswith('|'):
        in_table = False
        fixed_lines.append(line)
        continue

    # Process table rows (skip separator line)
    if in_table and line.startswith('|') and not re.match(r'^\|[-\s|]+\|$', line):
        original_parts = line.split('|')
        original_count = len(original_parts)

        if original_count != 18:
            fixed_line, was_fixed = fix_table_row(line)
            if was_fixed:
                exercise = original_parts[2].strip() if len(original_parts) > 2 else "unknown"
                fixes_by_type[original_count] = fixes_by_type.get(original_count, 0) + 1
                total_fixes += 1
                print(f"Line {i}: {original_count} → 18 fields | {exercise[:50]}")
                fixed_lines.append(fixed_line)
            else:
                fixed_lines.append(line)
        else:
            fixed_lines.append(line)
    else:
        fixed_lines.append(line)

# Write output
with open("comprehensive_exercise_database_v2_FIXED.md", "w", encoding="utf-8") as f:
    f.writelines(fixed_lines)

print(f"\n{'='*70}")
print(f"SUMMARY")
print(f"{'='*70}")
print(f"Total lines processed: {len(lines)}")
print(f"Total fixes applied: {total_fixes}")
print(f"\nFixes by original field count:")
for count in sorted(fixes_by_type.keys()):
    if fixes_by_type[count] > 0:
        print(f"  {count} fields → 18 fields: {fixes_by_type[count]} rows")
print(f"{'='*70}")

# Validate
print("\n✓ Validating output...")
with open("comprehensive_exercise_database_v2_FIXED.md", "r") as f:
    fixed_content = f.read()

table_rows = [line for line in fixed_content.split('\n')
              if line.startswith('|') and not re.match(r'^\|[-\s|]+\|$', line)]

column_distribution = {}
for row in table_rows:
    col_count = len(row.split('|'))
    column_distribution[col_count] = column_distribution.get(col_count, 0) + 1

print("\nColumn distribution in FIXED file:")
for cols in sorted(column_distribution.keys()):
    print(f"  {cols} fields: {column_distribution[cols]} rows")

if len(column_distribution) == 1 and 18 in column_distribution:
    print(f"\n{'='*70}")
    print("✅ SUCCESS! All {column_distribution[18]} table rows now have 18 fields.")
    print(f"{'='*70}")
    print("\nYou can now replace the original database:")
    print("  mv comprehensive_exercise_database_v2_FIXED.md comprehensive_exercise_database_v2.md")
else:
    print(f"\n{'='*70}")
    print("⚠️  WARNING: Some rows still have inconsistent field counts")
    print(f"{'='*70}")
    print("Manual review recommended for remaining issues.")
