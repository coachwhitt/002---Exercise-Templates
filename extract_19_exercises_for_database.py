#!/usr/bin/env python3
"""
Extract 19 exercises from research markdown files and prepare for database integration.

Reads:
- batch_supplementary_6_exercises_research.md (6 exercises)
- batch_supplementary_olympic_lifts_7_exercises_research.md (7 exercises)
- batch_supplementary_kettlebell_suspension_6_exercises_research.md (6 exercises)

Outputs:
- 19_exercises_formatted_for_database.csv (ready for v3.1 integration)
- 19_exercises_functional_groups.txt (functional group mappings)
"""

import re
import csv

def parse_research_file(filepath):
    """Extract exercise data from research markdown file."""
    exercises = []

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Try format 1: ## Exercise N: Name (Batch 1)
    sections = re.split(r'\n##\s+Exercise\s+\d+:', content)

    if len(sections) <= 1:
        # Try format 2: ## N. Name (Batch 2)
        sections = re.split(r'\n##\s+\d+\.\s+', content)

    if len(sections) <= 1:
        # Try format 3: ### Exercise Name (Batch 3 - no numbers)
        sections = re.split(r'\n###\s+(?!Steps|Advanced|Scientific|Sports|Primary|Secondary|Type|Equipment|Level|Body|Movement|Modality)', content)

    for section in sections[1:]:  # Skip header section
        exercise = {}

        # Extract exercise name (first line after split)
        lines = section.split('\n')
        exercise['name'] = lines[0].strip()

        # Check format type
        has_table = '| **Exercise Name**' in section or '| **Primary Muscles**' in section
        has_bold_format = '\n**Primary Muscles:**' in section or '\n**Type:**' in section

        if has_table:
            # Parse table format
            for line in lines:
                if '| **Primary Muscles**' in line:
                    # Next line has the value
                    match = re.search(r'\|\s*\*\*Primary Muscles\*\*\s*\|\s*(.+?)\s*\|', line)
                    if match:
                        exercise['primary'] = match.group(1).strip()
                elif '| **Secondary Muscles**' in line:
                    match = re.search(r'\|\s*\*\*Secondary Muscles\*\*\s*\|\s*(.+?)\s*\|', line)
                    if match:
                        exercise['secondary'] = match.group(1).strip()
                elif '| **Type**' in line:
                    match = re.search(r'\|\s*\*\*Type\*\*\s*\|\s*(.+?)\s*\|', line)
                    if match:
                        exercise['type'] = match.group(1).strip()
                elif '| **Equipment**' in line:
                    match = re.search(r'\|\s*\*\*Equipment\*\*\s*\|\s*(.+?)\s*\|', line)
                    if match:
                        exercise['equipment'] = match.group(1).strip()
                elif '| **Level**' in line:
                    match = re.search(r'\|\s*\*\*Level\*\*\s*\|\s*(.+?)\s*\|', line)
                    if match:
                        exercise['level'] = match.group(1).strip()
                elif '| **Body Region**' in line:
                    match = re.search(r'\|\s*\*\*Body Region\*\*\s*\|\s*(.+?)\s*\|', line)
                    if match:
                        exercise['body_region'] = match.group(1).strip()
                elif '| **Movement**' in line:
                    match = re.search(r'\|\s*\*\*Movement\*\*\s*\|\s*(.+?)\s*\|', line)
                    if match:
                        exercise['movement'] = match.group(1).strip()
                elif '| **Modality**' in line:
                    match = re.search(r'\|\s*\*\*Modality\*\*\s*\|\s*(.+?)\s*\|', line)
                    if match:
                        exercise['modality'] = match.group(1).strip()
        elif has_bold_format:
            # Parse **bold key:** value format (Batch 3)
            for line in lines:
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
                elif line.startswith('**Movement:**'):
                    exercise['movement'] = line.replace('**Movement:**', '').strip()
                elif line.startswith('**Modality:**'):
                    exercise['modality'] = line.replace('**Modality:**', '').strip()
        else:
            # Parse ### header format (Batch 1)
            # Primary Muscles
            primary_match = re.search(r'###\s+Primary Muscles\s*((?:[-\*].+?\n?)+)', section, re.DOTALL)
            if primary_match:
                muscles = primary_match.group(1).strip()
                # Clean bullet points and join
                muscles = ', '.join([m.strip('- *').strip() for m in muscles.split('\n') if m.strip().startswith(('-', '*'))])
                # Remove markdown **bold**
                muscles = re.sub(r'\*\*([^*]+)\*\*', r'\1', muscles)
                exercise['primary'] = muscles

            # Secondary Muscles
            secondary_match = re.search(r'###\s+Secondary Muscles\s*((?:[-\*].+?\n?)+)', section, re.DOTALL)
            if secondary_match:
                muscles = secondary_match.group(1).strip()
                muscles = ', '.join([m.strip('- *').strip() for m in muscles.split('\n') if m.strip().startswith(('-', '*'))])
                muscles = re.sub(r'\*\*([^*]+)\*\*', r'\1', muscles)
                exercise['secondary'] = muscles

            # Type
            type_match = re.search(r'###\s+Type\s*\*\*([^*]+)\*\*', section)
            if type_match:
                exercise['type'] = type_match.group(1).strip()

            # Equipment
            equip_match = re.search(r'###\s+Equipment\s*\*\*([^*]+)\*\*', section)
            if equip_match:
                exercise['equipment'] = equip_match.group(1).strip()

            # Level
            level_match = re.search(r'###\s+Level\s*\*\*([^*]+)\*\*', section)
            if level_match:
                exercise['level'] = level_match.group(1).strip()

            # Body Region
            region_match = re.search(r'###\s+Body Region\s*\*\*([^*]+)\*\*', section)
            if region_match:
                exercise['body_region'] = region_match.group(1).strip()

            # Movement
            movement_match = re.search(r'###\s+Movement\s*\*\*([^*]+)\*\*', section)
            if movement_match:
                exercise['movement'] = movement_match.group(1).strip()

            # Modality
            modality_match = re.search(r'###\s+Modality\s*\*\*([^*]+)\*\*', section)
            if modality_match:
                exercise['modality'] = modality_match.group(1).strip()

        # Steps for Beginners (both ### and #### formats)
        steps_match = re.search(r'#{3,4}\s+Steps for Beginners.*?\n\s*((?:\d+\..+?\n?)+)', section, re.DOTALL)
        if steps_match:
            steps = steps_match.group(1).strip()
            # Join steps into single text
            steps = ' '.join([s.strip() for s in steps.split('\n') if s.strip()])
            exercise['steps'] = steps

        # Advanced Key Points (both ### and #### formats)
        points_match = re.search(r'#{3,4}\s+Advanced Key Points.*?\n\s*((?:\d+\..+?\n?)+)', section, re.DOTALL)
        if points_match:
            points = points_match.group(1).strip()
            points = ' '.join([p.strip() for p in points.split('\n') if p.strip()])
            exercise['key_points'] = points

        # Scientific References (both ### and #### formats)
        refs_match = re.search(r'#{3,4}\s+Scientific References?\s*((?:\d+\..+?\n?)+)', section, re.DOTALL)
        if refs_match:
            refs = refs_match.group(1).strip()
            # Extract individual references
            refs_list = [r.strip() for r in refs.split('\n') if r.strip() and re.match(r'^\d+\.', r.strip())]
            # Remove leading numbers and clean
            refs_list = [re.sub(r'^\d+\.\s*', '', r) for r in refs_list]
            # Take only the main citation line (before sub-bullets)
            refs_list = [r.split('\n')[0].strip() for r in refs_list]
            exercise['references'] = '; '.join(refs_list)

        # Sports Tags (both ### and #### formats, and comma-separated format)
        sports_match = re.search(r'#{3,4}\s+Sports Tags.*?\n\s*(.+?)(?:\n\n|\n---|\Z)', section, re.DOTALL)
        if sports_match:
            sports = sports_match.group(1).strip()
            # Check if it's a numbered list or comma-separated
            if re.match(r'^\d+\.', sports):
                # Numbered list format (Batch 1)
                sports_list = [re.sub(r'^\d+\.\s*\*\*([^*]+)\*\*.*', r'\1', s.strip()) for s in sports.split('\n') if s.strip() and re.match(r'^\d+\.', s.strip())]
                exercise['sports'] = ', '.join(sports_list)
            else:
                # Comma-separated format (Batch 2/3)
                exercise['sports'] = sports.replace('\n', ' ').strip()

        # Only add if we have the essential fields
        if 'name' in exercise and 'primary' in exercise:
            exercises.append(exercise)

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
    if 'deltoid' in primary or 'delt' in ex_name or 'shoulder' in ex_name or 'press' in ex_name and 'overhead' in ex_name:
        groups.append('Shoulders_Delts_and_Traps')

    # ARMS - BICEPS
    if 'biceps' in primary or 'curl' in ex_name:
        groups.append('Arms_Biceps')

    # ARMS - TRICEPS
    if 'triceps' in primary or 'tricep' in ex_name or 'dip' in ex_name or 'pushdown' in ex_name:
        groups.append('Arms_Triceps')

    # CORE - ABDOMINALS
    if 'rectus abdominis' in primary or 'abdomin' in primary or 'abs' in ex_name:
        # Determine sub-region
        if 'lower' in ex_name or 'reverse' in ex_name or 'hip' in ex_name or 'leg lift' in ex_name or 'jack knife' in ex_name or 'mountain climber' in ex_name:
            groups.append('Abdominal_Lower')
        if 'upper' in ex_name or 'crunch' in ex_name or 'sit-up' in ex_name or 'sit up' in ex_name:
            groups.append('Abdominal_Upper')
        if 'bicycle' in ex_name or 'ab cycle' in ex_name or 'ab-cycle' in ex_name:
            groups.append('Abdominal_Obliques')
            groups.append('Abdominal_Total')
        if not any(x in groups for x in ['Abdominal_Lower', 'Abdominal_Upper', 'Abdominal_Obliques']):
            groups.append('Abdominal_Total')

    if 'oblique' in primary or 'oblique' in ex_name or 'twist' in ex_name or 'rotation' in ex_name or 'chop' in ex_name:
        groups.append('Abdominal_Obliques')

    # CORE - LOWER BACK
    if 'erector spinae' in primary or 'lower back' in ex_name or 'back raise' in ex_name or 'hyperextension' in ex_name or 'superman' in ex_name:
        groups.append('Lower_Back_Erector_Spinae')

    # CORE - FULL CORE (planks, stabilization, suspension exercises)
    if 'plank' in ex_name or 'suspension' in ex_name or 'trx' in ex_name or 'mountain climber' in ex_name or 'jack knife' in ex_name or ('core' in secondary and ex_type == 'compound') or 'stability ball' in ex_name or 'conditioning ball' in ex_name:
        groups.append('Full_Core')

    # LEGS - QUADRICEPS
    if 'quadriceps' in primary or 'rectus femoris' in primary or 'vastus' in primary or 'quad' in ex_name:
        groups.append('Legs_Quadriceps')

    # LEGS - HAMSTRINGS
    if 'hamstring' in primary or 'biceps femoris' in primary or 'semitendinosus' in primary or 'semimembranosus' in primary:
        groups.append('Legs_Hamstrings')

    # GLUTES
    if 'gluteus' in primary or 'glute' in primary or 'glute' in ex_name or 'hip' in ex_name:
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
    if 'rotator cuff' in primary or 'infraspinatus' in primary or 'teres minor' in primary:
        groups.append('Rotator_Cuff')

    # OLYMPIC LIFTS & EXPLOSIVE
    if any(x in ex_name for x in ['clean', 'snatch', 'jerk', 'thruster', 'jump', 'box jump', 'broad jump', 'squat jump']):
        groups.append('Full_Body_Movements')

        # Specific Olympic lift tagging
        if 'clean' in ex_name or 'snatch' in ex_name or 'jerk' in ex_name:
            groups.append('Back_Latissimus_Dorsi')
            groups.append('Shoulders_Delts_and_Traps')
            groups.append('Legs_Quadriceps')
            groups.append('Quads_Hamstrings_Glutes')

        # Plyometric tagging
        if 'jump' in ex_name:
            groups.append('Legs_Quadriceps')
            if 'squat' not in ex_name:  # Box jumps, broad jumps
                groups.append('Gluteals')
            groups.append('Quads_Hamstrings_Glutes')

    # KETTLEBELL EXERCISES
    if 'kettlebell' in ex_name.lower():
        if 'swing' in ex_name:
            groups.append('Gluteals')
            groups.append('Legs_Hamstrings')
            groups.append('Full_Body_Movements')
        elif 'row' in ex_name:
            groups.append('Back_Latissimus_Dorsi')
            groups.append('Trapezius_and_Rhomboids')

    # MACHINE EXERCISES
    if 'machine' in ex_name.lower() and 'row' in ex_name:
        groups.append('Back_Latissimus_Dorsi')
        groups.append('Trapezius_and_Rhomboids')

    # SLED/PROWLER
    if 'prowler' in ex_name or 'sled' in ex_name:
        groups.append('Legs_Quadriceps')
        groups.append('Full_Body_Movements')
        groups.append('Gluteals')

    # COMBO GROUPS
    # Quads + Hamstrings + Glutes
    if ('Legs_Quadriceps' in groups and 'Gluteals' in groups) or \
       ('squat' in ex_name or 'lunge' in ex_name or 'thruster' in ex_name):
        if 'Quads_Hamstrings_Glutes' not in groups:
            groups.append('Quads_Hamstrings_Glutes')

    # Total Core (exercises hitting multiple core regions)
    core_regions = sum(1 for g in groups if 'Abdominal' in g or 'Lower_Back' in g or 'Full_Core' in g)
    if core_regions >= 2:
        groups.append('Total_Core')

    return list(set(groups))  # Remove duplicates

def main():
    print("🔍 Extracting 19 exercises from research files...\n")

    # Load all three batches
    batch1 = parse_research_file('/mnt/z/coachwhitt/ai/002 - Exercise Templates/batch_supplementary_6_exercises_research.md')
    batch2 = parse_research_file('/mnt/z/coachwhitt/ai/002 - Exercise Templates/batch_supplementary_olympic_lifts_7_exercises_research.md')
    batch3 = parse_research_file('/mnt/z/coachwhitt/ai/002 - Exercise Templates/batch_supplementary_kettlebell_suspension_6_exercises_research.md')

    all_exercises = batch1 + batch2 + batch3

    print(f"   Batch 1: {len(batch1)} exercises")
    print(f"   Batch 2: {len(batch2)} exercises")
    print(f"   Batch 3: {len(batch3)} exercises")
    print(f"   Total: {len(all_exercises)} exercises\n")

    # Map functional groups
    print("🏷️  Mapping functional groups...")
    for ex in all_exercises:
        groups = determine_functional_groups(
            ex.get('name', ''),
            ex.get('primary', ''),
            ex.get('secondary', ''),
            ex.get('type', ''),
            ex.get('body_region', '')
        )
        ex['functional_groups'] = '; '.join(groups)

    # Write to CSV
    print("📄 Creating CSV file...")
    with open('/mnt/z/coachwhitt/ai/002 - Exercise Templates/19_exercises_formatted_for_database.csv', 'w', newline='', encoding='utf-8') as f:
        fieldnames = [
            'Exercise', 'Primary_Muscles', 'Secondary_Muscles', 'Type', 'Equipment',
            'Level', 'Body_Region', 'Movement', 'Modality', 'Functional_Groups',
            'Steps_for_Beginners', 'Advanced_Key_Points', 'Scientific_Reference', 'Sports_Tags'
        ]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

        for ex in all_exercises:
            writer.writerow({
                'Exercise': ex.get('name', ''),
                'Primary_Muscles': ex.get('primary', ''),
                'Secondary_Muscles': ex.get('secondary', ''),
                'Type': ex.get('type', ''),
                'Equipment': ex.get('equipment', ''),
                'Level': ex.get('level', ''),
                'Body_Region': ex.get('body_region', ''),
                'Movement': ex.get('movement', ''),
                'Modality': ex.get('modality', ''),
                'Functional_Groups': ex['functional_groups'],
                'Steps_for_Beginners': ex.get('steps', ''),
                'Advanced_Key_Points': ex.get('key_points', ''),
                'Scientific_Reference': ex.get('references', ''),
                'Sports_Tags': ex.get('sports', '')
            })

    print(f"   ✅ Created 19_exercises_formatted_for_database.csv\n")

    # Write functional group summary
    print("📊 Creating functional group summary...")
    with open('/mnt/z/coachwhitt/ai/002 - Exercise Templates/19_exercises_functional_groups.txt', 'w', encoding='utf-8') as f:
        f.write("# Functional Group Mappings for 19 New Exercises\n\n")
        for ex in all_exercises:
            f.write(f"{ex['name']}\n")
            f.write(f"  Groups: {ex['functional_groups']}\n\n")

    print(f"   ✅ Created 19_exercises_functional_groups.txt\n")

    # Summary
    print("✅ Extraction complete!\n")
    print("📈 Exercise breakdown:")
    for i, ex in enumerate(all_exercises, 1):
        print(f"   {i}. {ex['name']}")

    print(f"\n🎯 Next step: Integrate into database v3 to create v3.1 (377 exercises)")

if __name__ == '__main__':
    main()
