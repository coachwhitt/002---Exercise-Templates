#!/usr/bin/env python3
"""
Fix Batch 4 rows where references are split across parts[12] and parts[13]:
1. Merge parts[13] references into parts[12] with ; separator
2. Move parts[14] (sports) to parts[13]
3. Move parts[15] to parts[14]
4. Set parts[15] to [TBD]
"""

import re

def is_reference(text):
    """Check if text looks like a scientific reference"""
    text = text.strip()
    if not text or text == '[TBD]':
        return False
    ref_patterns = [
        r'\(\d{4}\)',  # Year
        r'et\s+al\.',  # et al.
        r'J\s+Strength',  # Journal
        r'Int\s+J',  # Journal
        r'StatPearls',
        r'\d+\(\d+\):',  # Volume(issue):
    ]
    return any(re.search(p, text) for p in ref_patterns)

# Read file
with open("comprehensive_exercise_database_v2.md", "r") as f:
    lines = f.readlines()

fixed_lines = []
fixes = 0

for i, line in enumerate(lines, 1):
    # Only process data rows
    if line.startswith('|') and not re.match(r'^\|[-\s|]+\|$', line) and '| Exercise |' not in line:
        parts = line.split('|')

        if len(parts) >= 16:
            part12 = parts[12].strip()
            part13 = parts[13].strip()
            part14 = parts[14].strip()
            part15 = parts[15].strip() if len(parts) > 15 else ''

            # Check if parts[13] has a reference (indicating Batch 4 structure issue)
            if is_reference(part12) and is_reference(part13):
                # Merge parts[13] into parts[12]
                parts[12] = f" {part12} ; {part13} "

                # Move parts[14] to parts[13]
                parts[13] = f" {part14} "

                # Move parts[15] to parts[14]
                parts[14] = f" {part15} " if part15 else " [TBD] "

                # Set parts[15] to [TBD]
                if len(parts) > 15:
                    parts[15] = " [TBD] "

                fixes += 1
                exercise = parts[2].strip() if len(parts) > 2 else "unknown"
                print(f"Line {i}: Fixed {exercise[:50]}")

            # Rebuild line
            fixed_lines.append('|'.join(parts))
        else:
            fixed_lines.append(line)
    else:
        fixed_lines.append(line)

# Write output
with open("comprehensive_exercise_database_v2_FIXED.md", "w") as f:
    f.writelines(fixed_lines)

print(f"\n{'='*70}")
print(f"Total fixes applied: {fixes}")
print(f"{'='*70}")

# Validate
print("\nValidating column counts...")
with open("comprehensive_exercise_database_v2_FIXED.md", "r") as f:
    data_rows = [line for line in f if line.startswith('|') and not re.match(r'^\|[-\s|]+\|$', line) and '| Exercise |' not in line]

column_counts = {}
for row in data_rows:
    count = len(row.split('|'))
    column_counts[count] = column_counts.get(count, 0) + 1

for c in sorted(column_counts.keys()):
    print(f"  {c} fields: {column_counts[c]} rows")

print("\nReplace with:")
print("  mv comprehensive_exercise_database_v2_FIXED.md comprehensive_exercise_database_v2.md")
