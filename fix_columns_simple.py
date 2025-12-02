#!/usr/bin/env python3
"""
Simple fix as requested:
1. Append any references in column 14 (parts[14]) to column 13 (parts[13])
2. Remove references from column 14, keep only sports tags
3. Move any sports tags from column 15 (parts[15]) to column 14
4. Replace any blanks in column 15 with [TBD]
"""

import re

def is_reference(text):
    """Check if text looks like a scientific reference"""
    ref_patterns = [
        r'\(\d{4}\)',  # Year in parens
        r'et\s+al\.',  # et al.
        r'J\s+Strength',  # Journal
        r'Int\s+J',  # Journal
        r'StatPearls',
        r'\d+\(\d+\):\d+',  # Volume(issue):page
        r'DOI:',
    ]
    return any(re.search(p, text) for p in ref_patterns)

def split_refs_and_sports(text):
    """Split text into references and sports"""
    parts = [p.strip() for p in text.split(';')]
    refs = []
    sports = []

    for part in parts:
        if not part:
            continue
        if is_reference(part):
            refs.append(part)
        else:
            sports.append(part)

    return refs, sports

# Read file
with open("comprehensive_exercise_database_v2.md", "r") as f:
    lines = f.readlines()

fixed_lines = []
fixes = 0

for i, line in enumerate(lines, 1):
    # Only process data rows
    if line.startswith('|') and not re.match(r'^\|[-\s|]+\|$', line) and '| Exercise |' not in line:
        parts = line.split('|')

        if len(parts) >= 18:
            # Column 13 = parts[13] = Scientific Reference
            # Column 14 = parts[14] = Sports Tags
            # Column 15 = parts[15] = ExRx Video

            col13 = parts[13].strip()  # Scientific Reference
            col14 = parts[14].strip()  # Sports Tags
            col15 = parts[15].strip() if len(parts) > 15 else ''  # ExRx Video

            # Step 1 & 2: Extract references from col14, append to col13, keep only sports in col14
            refs_from_14, sports_from_14 = split_refs_and_sports(col14)

            if refs_from_14:
                # Append references to col13
                if col13:
                    new_col13 = f"{col13} ; {' ; '.join(refs_from_14)}"
                else:
                    new_col13 = ' ; '.join(refs_from_14)
                parts[13] = f" {new_col13} "

                # Keep only sports in col14
                if sports_from_14:
                    parts[14] = f" {', '.join(sports_from_14)} "
                else:
                    parts[14] = " "

                fixes += 1
                exercise = parts[2].strip() if len(parts) > 2 else "unknown"
                print(f"Line {i}: {exercise[:50]}")
                print(f"  Moved {len(refs_from_14)} ref(s) from col14 to col13")

            # Step 3 & 4: Move sports from col15 to col14 if col15 has sports, replace with [TBD]
            if col15 and col15 != '[TBD]' and not col15.startswith('http'):
                # col15 might have sports tags
                refs_from_15, sports_from_15 = split_refs_and_sports(col15)

                if sports_from_15:
                    # Move sports from col15 to col14
                    current_col14 = parts[14].strip()
                    if current_col14 and current_col14 != '[TBD]':
                        parts[14] = f" {current_col14}, {', '.join(sports_from_15)} "
                    else:
                        parts[14] = f" {', '.join(sports_from_15)} "

                    # Replace col15 with [TBD]
                    parts[15] = " [TBD] "

                    print(f"  Moved sports from col15 to col14")

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
print(f"Fixes applied: {fixes}")
print(f"Output: comprehensive_exercise_database_v2_FIXED.md")
print(f"{'='*70}")

# Validate
print("\nValidating...")
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
