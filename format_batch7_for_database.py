#!/usr/bin/env python3
"""
Format Batch 7 exercises for database integration.
Extracts data from research files and creates pipe-delimited table rows.
"""

import re

# Exercise list in order
exercises = [
    "Split Squat",
    "Step-Up",
    "Walking Lunge",
    "Alternating Leg Extension",
    "Leg Extension",
    "Single-Leg Extension",
    "Alternating Superman",
    "Back Raise",
    "Quadruped Alternating Superman",
    "Superman",
    "Superman Hold",
    "Arnold Dumbbell Press",
    "Barbell Shoulder Press",
    "Dumbbell Alternating Shoulder Press",
    "Dumbbell Front Raise",
    "Dumbbell Shoulder Press",
    "Dumbbell Twisting Shoulder Press",
    "Machine Shoulder Press",
    "Seated Dumbbell Rear Delt Elbow Raise",
    "Single-Arm Dumbbell Shoulder Press",
    "Smith Machine Shoulder Press",
    "Barbell Front Raise",
    "Bent-Over Cable Rear Delt Raise",
    "Bent-Over Dumbbell Rear Delt Raise",
    "Cable Front Raise"
]

def extract_exercise_data(research_file, exercise_name):
    """Extract structured data for an exercise from research file."""

    with open(research_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find exercise section - case insensitive, handle variations
    name_upper = exercise_name.upper()
    pattern = rf'## EXERCISE \d+:\s*{re.escape(name_upper)}(?:\n|\s).*?(?=## EXERCISE|\Z)'
    match = re.search(pattern, content, re.DOTALL | re.IGNORECASE)

    if not match:
        return None

    section = match.group(0)

    # Extract data fields
    data = {
        'name': exercise_name,
        'primary_muscles': '',
        'secondary_muscles': '',
        'type': '',
        'equipment': '',
        'level': '',
        'body_region': '',
        'movement_pattern': '',
        'modality': '',
        'beginner_steps': '',
        'advanced_cues': '',
        'references': '',
        'sports': ''
    }

    # Primary muscles
    prim_match = re.search(r'\*\*Primary Muscles?:\*\*\s*(.+?)(?=\n\*\*|\n\n|$)', section, re.DOTALL)
    if prim_match:
        data['primary_muscles'] = prim_match.group(1).strip().replace('\n', ' ')

    # Secondary muscles
    sec_match = re.search(r'\*\*Secondary Muscles?:\*\*\s*(.+?)(?=\n\*\*|\n\n|$)', section, re.DOTALL)
    if sec_match:
        data['secondary_muscles'] = sec_match.group(1).strip().replace('\n', ' ')

    # Type
    type_match = re.search(r'\*\*Type:\*\*\s*(.+?)(?=\n\*\*|\n\n|$)', section)
    if type_match:
        data['type'] = type_match.group(1).strip()

    # Equipment
    equip_match = re.search(r'\*\*Equipment:\*\*\s*(.+?)(?=\n\*\*|\n\n|$)', section, re.DOTALL)
    if equip_match:
        data['equipment'] = equip_match.group(1).strip().replace('\n', ' ')

    # Level
    level_match = re.search(r'\*\*Level:\*\*\s*(.+?)(?=\n\*\*|\n\n|$)', section)
    if level_match:
        data['level'] = level_match.group(1).strip()

    # Body region (infer from exercise type)
    if any(kw in exercise_name.lower() for kw in ['squat', 'lunge', 'step', 'leg', 'quad']):
        data['body_region'] = 'Lower'
    elif any(kw in exercise_name.lower() for kw in ['superman', 'back raise']):
        data['body_region'] = 'Core'
    elif 'shoulder' in exercise_name.lower() or 'press' in exercise_name.lower() or 'raise' in exercise_name.lower():
        data['body_region'] = 'Upper'

    # Movement pattern
    if 'press' in exercise_name.lower():
        data['movement_pattern'] = 'Push'
    elif 'raise' in exercise_name.lower():
        data['movement_pattern'] = 'Isolation'
    elif 'superman' in exercise_name.lower() or 'hold' in exercise_name.lower():
        data['movement_pattern'] = 'Static'
    elif any(kw in exercise_name.lower() for kw in ['squat', 'lunge', 'step']):
        data['movement_pattern'] = 'Push'
    elif 'extension' in exercise_name.lower():
        data['movement_pattern'] = 'Extension'

    # Modality
    if 'barbell' in exercise_name.lower():
        data['modality'] = 'Free Weight'
    elif 'dumbbell' in exercise_name.lower():
        data['modality'] = 'Free Weight'
    elif 'cable' in exercise_name.lower():
        data['modality'] = 'Cables'
    elif 'machine' in exercise_name.lower() or 'smith' in exercise_name.lower():
        data['modality'] = 'Machine'
    else:
        data['modality'] = 'Bodyweight'

    # Beginner steps - look for "Beginner Steps:" heading
    steps_match = re.search(r'\*\*Beginner Steps:\*\*(.+?)(?=\n\*\*[A-Z]|###|\Z)', section, re.DOTALL)
    if steps_match:
        steps_text = steps_match.group(1).strip()
        # Extract numbered steps
        steps = re.findall(r'\d+\.\s*\*?\*?([^*\n]+?)(?:\*\*)?(?=\n\d+\.|\Z)', steps_text, re.DOTALL)
        data['beginner_steps'] = ' '.join([f"{i+1}. {step.strip()}" for i, step in enumerate(steps) if step.strip()])

    # Advanced cues - look for "Advanced Cues:" heading
    cues_match = re.search(r'\*\*Advanced Cues:\*\*(.+?)(?=\n\*\*[A-Z]|###|\Z)', section, re.DOTALL)
    if cues_match:
        cues_text = cues_match.group(1).strip()
        cues = re.findall(r'\d+\.\s*\*?\*?([^*\n]+?)(?:\*\*)?(?=\n\d+\.|\Z)', cues_text, re.DOTALL)
        data['advanced_cues'] = ' '.join([f"{i+1}. {cue.strip()}" for i, cue in enumerate(cues) if cue.strip()])

    # Scientific references - look in "References:" section
    refs_match = re.search(r'\*\*References:\*\*(.+?)(?=\n\*\*[A-Z]|###|\Z)', section, re.DOTALL)
    if refs_match:
        refs_text = refs_match.group(1).strip()
        # Extract references (numbered list format)
        refs = re.findall(r'\d+\.\s*(.+?)(?=\n\d+\.|\Z)', refs_text, re.DOTALL)
        # Clean and join with semicolon
        cleaned_refs = [ref.strip().replace('\n', ' ') for ref in refs if ref.strip()]
        data['references'] = '; '.join(cleaned_refs[:4])  # Max 4 references

    # Sports applications
    sports_match = re.search(r'\*\*Sports Applications:\*\*(.+?)(?=\n\*\*[A-Z]|###|## EXERCISE|\Z)', section, re.DOTALL)
    if sports_match:
        sports_text = sports_match.group(1).strip()
        # Extract sport names from numbered list
        sports = re.findall(r'\d+\.\s*\*?\*?([^*:\n]+?)(?:\*\*)?(?:\s*[-:]|(?=\n\d+\.|\Z))', sports_text)
        cleaned_sports = [sport.strip() for sport in sports if sport.strip()]
        data['sports'] = ', '.join(cleaned_sports[:12])  # Max 12 sports

    return data

def format_table_row(data):
    """Format exercise data as pipe-delimited table row."""

    # Order: Name | Primary | Secondary | Type | Equipment | Level | Body Region | Movement | Modality |
    #        Beginner Steps | Advanced Cues | Reference | ExRx Video | JEFIT Video | CoachWhitt Video | Sports Tags

    row = (
        f"{data['name']} | "
        f"{data['primary_muscles']} | "
        f"{data['secondary_muscles']} | "
        f"{data['type']} | "
        f"{data['equipment']} | "
        f"{data['level']} | "
        f"{data['body_region']} | "
        f"{data['movement_pattern']} | "
        f"{data['modality']} | "
        f"{data['beginner_steps']} | "
        f"{data['advanced_cues']} | "
        f"{data['references']} | "
        f"[TBD] | "  # ExRx Video
        f"[TBD] | "  # JEFIT Video
        f"[TBD] | "  # CoachWhitt Video
        f"{data['sports']}"
    )

    return row

def main():
    """Main execution."""

    print("Formatting Batch 7 exercises for database integration...")
    print(f"Processing {len(exercises)} exercises\n")

    # Read both research files
    file1 = "batch_6_quadriceps_core_exercises_research.md"  # Actually Batch 7a
    file2 = "batch_7b_shoulder_exercises_research.md"

    formatted_rows = []

    for i, exercise_name in enumerate(exercises, start=1):
        print(f"Processing {i}/25: {exercise_name}...")

        # Try both files
        data = extract_exercise_data(file1, exercise_name)
        if not data:
            data = extract_exercise_data(file2, exercise_name)

        if data:
            row = format_table_row(data)
            formatted_rows.append(row)
            print(f"  ✓ Formatted successfully")
        else:
            print(f"  ✗ Exercise not found in research files")

    # Write output
    output_file = "batch_7_table_rows.txt"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("# Batch 7 Formatted Database Rows\n")
        f.write("# Session 14 - 25 exercises (Lines 201-225)\n")
        f.write("# Ready for integration into comprehensive_exercise_database_v2.md\n\n")

        for row in formatted_rows:
            f.write(row + "\n")

    print(f"\n✅ Complete! {len(formatted_rows)} exercises formatted")
    print(f"Output saved to: {output_file}")

if __name__ == "__main__":
    main()
