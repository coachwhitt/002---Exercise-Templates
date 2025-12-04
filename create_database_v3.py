#!/usr/bin/env python3
"""
Create comprehensive_exercise_database_v3.md with functional group filtering columns.

This script:
1. Extracts all exercises from v2 database
2. Maps exercises to functional groups based on muscle targets
3. Creates a clean, filterable table structure
4. Generates comparison with Origym CSV
"""

import re
import csv
from collections import defaultdict

def extract_exercises_from_v2(filepath):
    """Extract all exercise rows from the v2 database markdown file."""
    exercises = []

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split by table rows (| ... |)
    lines = content.split('\n')

    current_section = ""
    for line in lines:
        # Track section headers
        if line.startswith('## ') and not line.startswith('## SESSION') and not line.startswith('## Enhanced'):
            current_section = line.replace('##', '').strip()

        # Find table rows (must start with | and have multiple |)
        if line.startswith('|') and line.count('|') > 10:
            # Skip header rows (Exercise, Primary Muscles, etc.)
            if 'Exercise' in line and 'Primary Muscles' in line:
                continue
            # Skip separator rows (|---|---|)
            if '---' in line:
                continue

            # Split by | and clean
            cells = [cell.strip() for cell in line.split('|')]
            # Remove empty first/last elements
            cells = [c for c in cells if c]

            # Should have 16 columns
            if len(cells) >= 15:  # At least 15 to be valid
                exercises.append({
                    'section': current_section,
                    'row': cells
                })

    return exercises

def determine_functional_groups(exercise_name, primary_muscles, secondary_muscles, exercise_type, body_region):
    """
    Determine which functional groups an exercise belongs to.
    Returns a list of functional group tags.
    """
    groups = []

    # Normalize inputs
    primary = primary_muscles.lower()
    secondary = secondary_muscles.lower()
    ex_name = exercise_name.lower()
    ex_type = exercise_type.lower()
    region = body_region.lower()

    # CHEST
    if 'pectoralis' in primary or 'pec' in primary or 'chest' in ex_name:
        groups.append('Chest_Pectoralis')

    # BACK
    if 'latissimus' in primary or 'lat' in primary:
        groups.append('Back_Latissimus_Dorsi')
    if 'trapezius' in primary or 'rhomboid' in primary or 'trap' in primary:
        groups.append('Trapezius_and_Rhomboids')

    # SHOULDERS
    if 'deltoid' in primary or 'delt' in ex_name or 'shoulder' in ex_name:
        groups.append('Shoulders_Delts_and_Traps')

    # ARMS - BICEPS
    if 'biceps' in primary or 'curl' in ex_name:
        groups.append('Arms_Biceps')

    # ARMS - TRICEPS
    if 'triceps' in primary or 'tricep' in ex_name or 'dip' in ex_name or 'pushdown' in ex_name or 'extension' in ex_name and 'tricep' in ex_name:
        groups.append('Arms_Triceps')

    # CORE - ABDOMINALS
    if 'rectus abdominis' in primary or 'abdomin' in primary:
        # Determine sub-region
        if 'lower' in ex_name or 'reverse' in ex_name or 'hip thrust' in ex_name or 'leg lift' in ex_name:
            groups.append('Abdominal_Lower')
        if 'upper' in ex_name or 'crunch' in ex_name or 'sit-up' in ex_name or 'sit up' in ex_name:
            groups.append('Abdominal_Upper')
        if not any(x in groups for x in ['Abdominal_Lower', 'Abdominal_Upper']):
            groups.append('Abdominal_Total')

    if 'oblique' in primary or 'oblique' in ex_name or 'twist' in ex_name or 'rotation' in ex_name or 'chop' in ex_name:
        groups.append('Abdominal_Obliques')

    # CORE - LOWER BACK
    if 'erector spinae' in primary or 'lower back' in ex_name or 'back raise' in ex_name or 'hyperextension' in ex_name or 'superman' in ex_name:
        groups.append('Lower_Back_Erector_Spinae')

    # CORE - FULL CORE (planks, stabilization)
    if 'plank' in ex_name or ('core' in secondary and ex_type == 'compound'):
        groups.append('Full_Core')

    # LEGS - QUADRICEPS
    if 'quadriceps' in primary or 'rectus femoris' in primary or 'vastus' in primary:
        groups.append('Legs_Quadriceps')

    # LEGS - HAMSTRINGS
    if 'hamstring' in primary or 'biceps femoris' in primary or 'semitendinosus' in primary or 'semimembranosus' in primary:
        groups.append('Legs_Hamstrings')

    # GLUTES
    if 'gluteus' in primary or 'glute' in primary or 'glute' in ex_name or 'hip thrust' in ex_name:
        groups.append('Gluteals')

    # CALVES
    if 'gastrocnemius' in primary:
        groups.append('Calves_Gastrocnemius')
    if 'soleus' in primary:
        groups.append('Calves_Soleus')

    # FOREARMS
    if 'forearm' in primary or 'wrist' in primary or 'grip' in ex_name:
        groups.append('Forearms_Grip')

    # NECK
    if 'sternocleidomastoid' in primary or 'neck' in ex_name:
        groups.append('Neck')

    # ROTATOR CUFF
    if 'rotator cuff' in primary or 'infraspinatus' in primary or 'teres minor' in primary or 'supraspinatus' in primary or 'subscapularis' in primary:
        groups.append('Rotator_Cuff')

    # COMBO GROUPS
    # Quads + Hamstrings + Glutes
    if ('Legs_Quadriceps' in groups and 'Legs_Hamstrings' in groups) or \
       ('Legs_Quadriceps' in groups and 'Gluteals' in groups) or \
       ('squat' in ex_name or 'lunge' in ex_name or 'deadlift' in ex_name):
        groups.append('Quads_Hamstrings_Glutes')

    # Hamstrings + Quadriceps (compound leg)
    if 'Legs_Hamstrings' in groups and 'Legs_Quadriceps' in groups:
        groups.append('Hamstrings_and_Quadriceps')

    # Chest + Back (push-pull combo)
    if 'Chest_Pectoralis' in groups and ('Back_Latissimus_Dorsi' in groups or 'Trapezius_and_Rhomboids' in groups):
        groups.append('Chest_and_Back')

    # Deltoids + Lats
    if 'Shoulders_Delts_and_Traps' in groups and 'Back_Latissimus_Dorsi' in groups:
        groups.append('Deltoids_and_Lats')

    # Full Body Movements (compound exercises hitting 3+ regions)
    if ex_type == 'compound':
        body_parts_hit = 0
        if any(g in groups for g in ['Chest_Pectoralis']):
            body_parts_hit += 1
        if any(g in groups for g in ['Back_Latissimus_Dorsi', 'Trapezius_and_Rhomboids']):
            body_parts_hit += 1
        if any(g in groups for g in ['Shoulders_Delts_and_Traps']):
            body_parts_hit += 1
        if any(g in groups for g in ['Legs_Quadriceps', 'Legs_Hamstrings', 'Gluteals']):
            body_parts_hit += 1

        if body_parts_hit >= 2:  # At least 2 major body regions
            groups.append('Full_Body_Movements')

    # Total Core (exercises hitting multiple core regions)
    core_regions = sum(1 for g in groups if 'Abdominal' in g or 'Lower_Back' in g or 'Full_Core' in g)
    if core_regions >= 2:
        groups.append('Total_Core')

    return list(set(groups))  # Remove duplicates

def main():
    print("🔍 Extracting exercises from v2 database...")
    exercises = extract_exercises_from_v2('/mnt/z/coachwhitt/ai/002 - Exercise Templates/comprehensive_exercise_database_v2.md')
    print(f"   Found {len(exercises)} exercises")

    print("\n🏷️  Mapping exercises to functional groups...")

    # Process each exercise
    exercise_data = []
    for ex in exercises:
        if len(ex['row']) < 15:
            continue  # Skip invalid rows

        exercise_name = ex['row'][0]
        primary_muscles = ex['row'][1]
        secondary_muscles = ex['row'][2]
        ex_type = ex['row'][3]
        equipment = ex['row'][4]
        level = ex['row'][5]
        body_region = ex['row'][6]
        movement = ex['row'][7]
        modality = ex['row'][8]
        steps = ex['row'][9]
        key_points = ex['row'][10]
        references = ex['row'][11]
        sports = ex['row'][12]

        # Determine functional groups
        functional_groups = determine_functional_groups(
            exercise_name,
            primary_muscles,
            secondary_muscles,
            ex_type,
            body_region
        )

        exercise_data.append({
            'Exercise': exercise_name,
            'Primary_Muscles': primary_muscles,
            'Secondary_Muscles': secondary_muscles,
            'Type': ex_type,
            'Equipment': equipment,
            'Level': level,
            'Body_Region': body_region,
            'Movement': movement,
            'Modality': modality,
            'Functional_Groups': functional_groups,
            'Steps': steps,
            'Key_Points': key_points,
            'References': references,
            'Sports': sports
        })

    print(f"   Mapped {len(exercise_data)} exercises to functional groups")

    # Create v3 markdown file
    print("\n📄 Creating comprehensive_exercise_database_v3.md...")

    with open('/mnt/z/coachwhitt/ai/002 - Exercise Templates/comprehensive_exercise_database_v3.md', 'w', encoding='utf-8') as f:
        f.write("# Comprehensive Scientific Exercise Database v3.0\n\n")
        f.write("**CLEAN TABLE STRUCTURE FOR GOOGLE SHEETS FILTERING**\n\n")
        f.write(f"**Total Exercises:** {len(exercise_data)}\n\n")
        f.write("**Purpose:** This version removes all session context and provides a clean, ")
        f.write("single-table structure with functional group columns for dropdown filtering in Google Sheets.\n\n")
        f.write("---\n\n")

        f.write("## Functional Group Filtering System\n\n")
        f.write("The `Functional_Groups` column contains tags that allow exercises to be filtered by:\n\n")

        f.write("**Primary Muscle Groups:**\n")
        f.write("- `Chest_Pectoralis`\n")
        f.write("- `Back_Latissimus_Dorsi`\n")
        f.write("- `Trapezius_and_Rhomboids`\n")
        f.write("- `Shoulders_Delts_and_Traps`\n")
        f.write("- `Arms_Biceps`\n")
        f.write("- `Arms_Triceps`\n")
        f.write("- `Legs_Quadriceps`\n")
        f.write("- `Legs_Hamstrings`\n")
        f.write("- `Gluteals`\n")
        f.write("- `Calves_Gastrocnemius`\n")
        f.write("- `Calves_Soleus`\n")
        f.write("- `Forearms_Grip`\n")
        f.write("- `Neck`\n")
        f.write("- `Rotator_Cuff`\n\n")

        f.write("**Core Regions:**\n")
        f.write("- `Abdominal_Lower`\n")
        f.write("- `Abdominal_Upper`\n")
        f.write("- `Abdominal_Total`\n")
        f.write("- `Abdominal_Obliques`\n")
        f.write("- `Lower_Back_Erector_Spinae`\n")
        f.write("- `Full_Core`\n")
        f.write("- `Total_Core`\n\n")

        f.write("**Combination Groups:**\n")
        f.write("- `Quads_Hamstrings_Glutes` (compound leg exercises)\n")
        f.write("- `Hamstrings_and_Quadriceps` (balanced leg work)\n")
        f.write("- `Chest_and_Back` (push-pull combinations)\n")
        f.write("- `Deltoids_and_Lats` (shoulder and back)\n")
        f.write("- `Full_Body_Movements` (compound multi-joint exercises)\n\n")

        f.write("---\n\n")

        f.write("## Complete Exercise Database\n\n")

        # Write header
        f.write("| Exercise | Primary Muscles | Secondary Muscles | Type | Equipment | Level | ")
        f.write("Body Region | Movement | Modality | Functional Groups | ")
        f.write("Steps for Beginners | Advanced Key Points | Scientific Reference | Sports Tags |\n")

        f.write("|----------|----------------|-------------------|------|-----------|-------|")
        f.write("-------------|----------|----------|-------------------|")
        f.write("---------------------|---------------------|---------------------|-------------|\n")

        # Write all exercises
        for ex in exercise_data:
            groups_str = '; '.join(ex['Functional_Groups'])

            f.write(f"| {ex['Exercise']} | {ex['Primary_Muscles']} | {ex['Secondary_Muscles']} | ")
            f.write(f"{ex['Type']} | {ex['Equipment']} | {ex['Level']} | ")
            f.write(f"{ex['Body_Region']} | {ex['Movement']} | {ex['Modality']} | ")
            f.write(f"{groups_str} | ")
            f.write(f"{ex['Steps']} | {ex['Key_Points']} | {ex['References']} | {ex['Sports']} |\n")

    print(f"   ✅ Created comprehensive_exercise_database_v3.md ({len(exercise_data)} exercises)")

    # Also create a CSV version for Google Sheets
    print("\n📊 Creating CSV version for Google Sheets...")

    with open('/mnt/z/coachwhitt/ai/002 - Exercise Templates/comprehensive_exercise_database_v3.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)

        # Header
        writer.writerow([
            'Exercise', 'Primary_Muscles', 'Secondary_Muscles', 'Type', 'Equipment',
            'Level', 'Body_Region', 'Movement', 'Modality', 'Functional_Groups',
            'Steps_for_Beginners', 'Advanced_Key_Points', 'Scientific_Reference', 'Sports_Tags'
        ])

        # Data
        for ex in exercise_data:
            writer.writerow([
                ex['Exercise'],
                ex['Primary_Muscles'],
                ex['Secondary_Muscles'],
                ex['Type'],
                ex['Equipment'],
                ex['Level'],
                ex['Body_Region'],
                ex['Movement'],
                ex['Modality'],
                '; '.join(ex['Functional_Groups']),
                ex['Steps'],
                ex['Key_Points'],
                ex['References'],
                ex['Sports']
            ])

    print(f"   ✅ Created comprehensive_exercise_database_v3.csv")

    # Analyze functional group distribution
    print("\n📈 Functional Group Distribution:")
    group_counts = defaultdict(int)
    for ex in exercise_data:
        for group in ex['Functional_Groups']:
            group_counts[group] += 1

    for group, count in sorted(group_counts.items(), key=lambda x: x[1], reverse=True):
        print(f"   {group}: {count} exercises")

    print("\n✅ Database v3 creation complete!")
    print(f"\nNext step: Compare with Origym CSV to identify missing exercises...")

if __name__ == '__main__':
    main()
