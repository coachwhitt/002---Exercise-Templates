#!/usr/bin/env python3
"""
Fix misplaced scientific references in Sports Tags column
Problem: Some rows have references mixed with sports tags in field 14
Solution: Extract references from field 14, append to field 13, keep only sports in field 14
"""

import re

def is_reference(text):
    """Check if text looks like a scientific reference"""
    # References typically have author names, year in parens, and journal info
    patterns = [
        r'\w+\s+[A-Z]\s+.*?\(\d{4}\)',  # Author A et al. (YEAR)
        r'\w+\s+et\s+al\.',               # et al.
        r'J\s+Strength\s+Cond\s+Res',     # Journal name
        r'Int\s+J\s+Environ\s+Res',       # Journal name
        r'StatPearls',                     # StatPearls
        r'DOI:',                           # DOI
        r'\d+\(\d+\):\d+',                # Volume(issue):page format
    ]

    for pattern in patterns:
        if re.search(pattern, text):
            return True
    return False

def is_sport(text):
    """Check if text looks like a sport name"""
    # Sports are typically just names without citations
    sport_keywords = [
        'Football', 'Rugby', 'Wrestling', 'Baseball', 'Basketball',
        'Tennis', 'Golf', 'Swimming', 'CrossFit', 'Powerlifting',
        'Bodybuilding', 'MMA', 'Boxing', 'Volleyball', 'Soccer',
        'Hockey', 'Track', 'Field', 'Running', 'Cycling', 'Rowing',
        'Climbing', 'Gymnastics', 'Martial Arts', 'General Fitness',
        'Rehabilitation', 'Strongman', 'Olympic Weightlifting'
    ]

    for keyword in sport_keywords:
        if keyword in text:
            return True
    return False

def split_references_and_sports(mixed_text):
    """Split mixed field into references and sports"""
    # Split by semicolon first
    parts = [p.strip() for p in mixed_text.split(';')]

    references = []
    sports = []

    for part in parts:
        if not part or part == '[TBD]':
            continue
        elif is_reference(part):
            references.append(part)
        elif is_sport(part):
            sports.append(part)
        else:
            # If unclear, check length - references are usually longer
            if len(part) > 50:
                references.append(part)
            else:
                sports.append(part)

    return references, sports

# Read file
with open("comprehensive_exercise_database_v2.md", "r", encoding="utf-8") as f:
    lines = f.readlines()

# Target line ranges
target_ranges = [
    (41, 57),    # rows 41-57
    (293, 311),  # rows 293-311
    (403, 427),  # rows 403-427
]

fixed_lines = []
fixes = 0
blank_lines_removed = 0

for i, line in enumerate(lines, 1):
    # Check if this line is in target range and is a data row
    in_target = any(start <= i <= end for start, end in target_ranges)

    # Check if line is blank
    if line.strip() == '':
        if in_target:
            blank_lines_removed += 1
            print(f"Line {i}: Removing blank line")
            continue  # Skip blank lines in target ranges
        else:
            fixed_lines.append(line)
            continue

    # Check if this is a table data row
    if in_target and line.startswith('|') and not re.match(r'^\|[-\s|]+\|$', line) and '| Exercise |' not in line:
        parts = line.split('|')

        if len(parts) == 18:
            # Extract fields
            exercise = parts[2].strip()
            sci_ref_field = parts[13].strip()  # Field 13: Scientific Reference
            sports_field = parts[14].strip()    # Field 14: Sports Tags

            # Check if sports field contains references
            if is_reference(sports_field):
                # Split the mixed sports field
                extracted_refs, extracted_sports = split_references_and_sports(sports_field)

                if extracted_refs:
                    # Append extracted references to scientific reference field
                    if sci_ref_field:
                        new_sci_ref = f"{sci_ref_field} ; {' ; '.join(extracted_refs)}"
                    else:
                        new_sci_ref = ' ; '.join(extracted_refs)

                    # Update fields
                    parts[13] = f" {new_sci_ref} "
                    parts[14] = f" {', '.join(extracted_sports)} " if extracted_sports else " [TBD] "

                    # Rebuild line
                    fixed_line = '|'.join(parts)
                    fixed_lines.append(fixed_line)
                    fixes += 1

                    print(f"Line {i}: Fixed | {exercise[:40]}")
                    print(f"  Moved {len(extracted_refs)} ref(s) from Sports to Sci Ref")
                    print(f"  Sports now: {', '.join(extracted_sports[:5])}")
                else:
                    fixed_lines.append(line)
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
print(f"Fixes applied: {fixes}")
print(f"Blank lines removed: {blank_lines_removed}")
print(f"Output written to: comprehensive_exercise_database_v2_FIXED.md")
print(f"{'='*70}")

# Validate
print("\nValidating field counts...")
with open("comprehensive_exercise_database_v2_FIXED.md", "r") as f:
    data_rows = [line for line in f if line.startswith('|') and not re.match(r'^\|[-\s|]+\|$', line) and '| Exercise |' not in line]

column_counts = {}
for row in data_rows:
    count = len(row.split('|'))
    column_counts[count] = column_counts.get(count, 0) + 1

for c in sorted(column_counts.keys()):
    print(f"  {c} fields: {column_counts[c]} rows")

if len(column_counts) == 1 and 18 in column_counts:
    print(f"\n✅ SUCCESS! All rows have 18 fields")
    print("\nReplace with:")
    print("  mv comprehensive_exercise_database_v2_FIXED.md comprehensive_exercise_database_v2.md")
