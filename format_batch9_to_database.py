#!/usr/bin/env python3
"""
Format Batch 9 research into database-ready table rows.
Reads batch_9_final_30_exercises_research.md and outputs formatted table rows.
"""

import re

def parse_exercise_from_research(text):
    """Parse individual exercise section from research document."""
    exercises = []

    # Split by exercise headers (### followed by number and name)
    exercise_sections = re.split(r'###\s+\d+\.\s+', text)[1:]  # Skip intro

    for section in exercise_sections:
        lines = section.strip().split('\n')
        if not lines:
            continue

        # Extract exercise name from first line
        exercise_name = lines[0].strip()

        # Initialize exercise data
        exercise = {'name': exercise_name}

        # Parse metadata fields
        for line in lines[1:]:
            line = line.strip()
            if line.startswith('**Primary Muscles:**'):
                exercise['primary'] = line.replace('**Primary Muscles:**', '').strip()
            elif line.startswith('**Secondary Muscles:**'):
                exercise['secondary'] = line.replace('**Secondary Muscles:**', '').strip()
            elif line.startswith('**Type:**'):
                exercise['type'] = line.replace('**Type:**', '').strip()
            elif line.startswith('**Equipment:**'):
                exercise['equipment'] = line.replace('**Equipment:**', '').strip()
            elif line.startswith('**Level:**'):
                exercise['level'] = line.replace('**Level:**', '').strip()
            elif line.startswith('**Body Region:**'):
                exercise['body_region'] = line.replace('**Body Region:**', '').strip()
            elif line.startswith('**Movement Pattern:**'):
                exercise['movement'] = line.replace('**Movement Pattern:**', '').strip()
            elif line.startswith('**Modality:**'):
                exercise['modality'] = line.replace('**Modality:**', '').strip()
            elif line.startswith('**Steps for Beginners:**'):
                # Collect all numbered steps
                steps = []
                idx = lines.index(line) + 1
                while idx < len(lines):
                    step_line = lines[idx].strip()
                    if step_line and re.match(r'^\d+\.', step_line):
                        steps.append(step_line)
                        idx += 1
                    elif step_line.startswith('**'):
                        break
                    else:
                        idx += 1
                exercise['steps'] = ' '.join(steps)
            elif line.startswith('**Advanced Key Points:**'):
                # Collect all numbered points
                points = []
                idx = lines.index(line) + 1
                while idx < len(lines):
                    point_line = lines[idx].strip()
                    if point_line and re.match(r'^\d+\.', point_line):
                        points.append(point_line)
                        idx += 1
                    elif point_line.startswith('**'):
                        break
                    else:
                        idx += 1
                exercise['key_points'] = ' '.join(points)
            elif line.startswith('**Scientific References:**'):
                # Collect all numbered references
                refs = []
                idx = lines.index(line) + 1
                while idx < len(lines):
                    ref_line = lines[idx].strip()
                    if ref_line and re.match(r'^\d+\.', ref_line):
                        refs.append(ref_line)
                        idx += 1
                    elif ref_line.startswith('**'):
                        break
                    else:
                        idx += 1
                # Join with semicolon separator (consistent with database format)
                exercise['references'] = ' ; '.join(refs)
            elif line.startswith('**Sports Applications:**'):
                sports = line.replace('**Sports Applications:**', '').strip()
                exercise['sports'] = sports

        exercises.append(exercise)

    return exercises

def format_as_table_row(ex):
    """Format exercise data as markdown table row."""
    # 16 columns: Exercise | Primary | Secondary | Type | Equipment | Level | Body Region | Movement | Modality |
    #             Steps | Key Points | Scientific Reference | Sports Tags | ExRx Video | JEFIT Video | CoachWhitt Video

    return f"| {ex.get('name', '')} | {ex.get('primary', '')} | {ex.get('secondary', '')} | {ex.get('type', '')} | {ex.get('equipment', '')} | {ex.get('level', '')} | {ex.get('body_region', '')} | {ex.get('movement', '')} | {ex.get('modality', '')} | {ex.get('steps', '')} | {ex.get('key_points', '')} | {ex.get('references', '')} | {ex.get('sports', '')} | [TBD] | [TBD] | [TBD] |"

def main():
    # Read research document
    with open('batch_9_final_30_exercises_research.md', 'r', encoding='utf-8') as f:
        content = f.read()

    # Parse all exercises
    exercises = parse_exercise_from_research(content)

    print(f"Parsed {len(exercises)} exercises from research document\n")

    # Output formatted table rows
    with open('batch_9_database_rows.txt', 'w', encoding='utf-8') as f:
        # Write header
        f.write("BATCH 9: DATABASE-READY TABLE ROWS (30 exercises)\n")
        f.write("=" * 100 + "\n\n")
        f.write("16-COLUMN FORMAT:\n")
        f.write("Exercise | Primary Muscles | Secondary Muscles | Type | Equipment | Level | Body Region | Movement | Modality | Steps for Beginners | Advanced Key Points | Scientific Reference | Sports Tags | ExRx Video | JEFIT Video | CoachWhitt Video\n\n")
        f.write("=" * 100 + "\n\n")

        # Group by category
        f.write("## TRICEPS EXERCISES (22 exercises)\n\n")
        for i, ex in enumerate(exercises[:22], 1):
            row = format_as_table_row(ex)
            f.write(f"{i}. {row}\n\n")

        f.write("\n" + "=" * 100 + "\n\n")
        f.write("## NECK EXERCISES (6 exercises)\n\n")
        for i, ex in enumerate(exercises[22:28], 23):
            row = format_as_table_row(ex)
            f.write(f"{i}. {row}\n\n")

        f.write("\n" + "=" * 100 + "\n\n")
        f.write("## ROTATOR CUFF EXERCISES (2 exercises)\n\n")
        for i, ex in enumerate(exercises[28:30], 29):
            row = format_as_table_row(ex)
            f.write(f"{i}. {row}\n\n")

    print("✓ Formatted rows written to: batch_9_database_rows.txt")
    print(f"✓ Total exercises processed: {len(exercises)}")

    # Also create a clean CSV-style version
    with open('batch_9_clean_rows.txt', 'w', encoding='utf-8') as f:
        for ex in exercises:
            f.write(format_as_table_row(ex) + "\n")

    print("✓ Clean rows written to: batch_9_clean_rows.txt")

if __name__ == '__main__':
    main()
