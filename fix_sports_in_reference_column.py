#!/usr/bin/env python3
"""
Fix sports tags embedded in Scientific Reference column
Problem: Field 13 (Scientific Reference) has sports tags at the end
Solution: Extract sports from end of field 13, move to field 14
"""

import re

def is_reference_content(text):
    """Check if text contains reference indicators"""
    ref_patterns = [
        r'\(\d{4}\)',  # Year in parens
        r'et\s+al\.',  # et al.
        r'J\s+Strength',  # Journal name
        r'Int\s+J',  # Journal name
        r'StatPearls',
        r'\d+\(\d+\):\d+',  # Volume(issue):page
        r'DOI:',
    ]
    return any(re.search(p, text) for p in ref_patterns)

def split_references_from_sports(text):
    """Split Scientific Reference field into pure references and sports"""
    # Split by semicolon
    parts = [p.strip() for p in text.split(';')]

    refs = []
    sports = []

    for part in parts:
        if is_reference_content(part):
            refs.append(part)
        else:
            # Check if it's a list of sports (contains commas and sport names)
            if ',' in part or any(sport in part for sport in ['Football', 'Rugby', 'Wrestling', 'Baseball', 'Basketball', 'Tennis', 'Golf', 'Swimming', 'CrossFit', 'Powerlifting', 'Bodybuilding', 'MMA', 'Boxing', 'Volleyball', 'Soccer']):
                sports.append(part)
            elif len(part) > 50:  # Long text is probably a reference
                refs.append(part)
            else:
                # Short text without reference markers - probably sports
                sports.append(part)

    return refs, sports

# Read file
with open("comprehensive_exercise_database_v2_FIXED.md", "r", encoding="utf-8") as f:
    lines = f.readlines()

# Line ranges where we expect issues (after blank removal, numbers shifted)
# Original ranges: 41-57, 293-311, 403-427
# After removing 18 blank lines, these ranges will have shifted
# Let's just check all data rows instead

fixed_lines = []
fixes = 0

for i, line in enumerate(lines, 1):
    # Check if this is a table data row
    if line.startswith('|') and not re.match(r'^\|[-\s|]+\|$', line) and '| Exercise |' not in line:
        parts = line.split('|')

        if len(parts) == 18:
            sci_ref_field = parts[13].strip()
            sports_field = parts[14].strip()

            # Check if scientific reference field contains sports tags
            # Sports tags typically don't have parentheses with years or journal names
            if sci_ref_field and ',' in sci_ref_field:
                # Try to split
                refs, sports = split_references_from_sports(sci_ref_field)

                if sports and refs:
                    # We found both references and sports in field 13
                    exercise = parts[2].strip()

                    # Update fields
                    parts[13] = f" {' ; '.join(refs)} "
                    parts[14] = f" {', '.join(sports)} " if sports else sports_field

                    # Rebuild line
                    fixed_line = '|'.join(parts)
                    fixed_lines.append(fixed_line)
                    fixes += 1

                    print(f"Line {i}: Fixed | {exercise[:50]}")
                    print(f"  Refs: {len(refs)}")
                    print(f"  Sports moved: {', '.join(sports)[:80]}")
                else:
                    fixed_lines.append(line)
            else:
                fixed_lines.append(line)
        else:
            fixed_lines.append(line)
    else:
        fixed_lines.append(line)

# Write output
with open("comprehensive_exercise_database_v2_FINAL.md", "w", encoding="utf-8") as f:
    f.writelines(fixed_lines)

print(f"\n{'='*70}")
print(f"SUMMARY")
print(f"{'='*70}")
print(f"Total lines processed: {len(lines)}")
print(f"Fixes applied: {fixes}")
print(f"Output: comprehensive_exercise_database_v2_FINAL.md")
print(f"{'='*70}")

# Validate
print("\nValidating...")
with open("comprehensive_exercise_database_v2_FINAL.md", "r") as f:
    data_rows = [line for line in f if line.startswith('|') and not re.match(r'^\|[-\s|]+\|$', line) and '| Exercise |' not in line]

print(f"Total data rows: {len(data_rows)}")

column_counts = {}
for row in data_rows:
    count = len(row.split('|'))
    column_counts[count] = column_counts.get(count, 0) + 1

for c in sorted(column_counts.keys()):
    print(f"  {c} fields: {column_counts[c]} rows")

if len(column_counts) == 1 and 18 in column_counts:
    print(f"\n✅ All rows have 18 fields")
    print("\nReplace with:")
    print("  mv comprehensive_exercise_database_v2_FINAL.md comprehensive_exercise_database_v2.md")
