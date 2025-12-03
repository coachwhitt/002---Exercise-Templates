#!/usr/bin/env python3
"""
Complete formatting script for Batch 8 exercises.
Extracts full details from research file and creates database-ready entries.
"""

import re

# Read the research file
with open('batch_8_shoulder_triceps_exercises_research.md', 'r', encoding='utf-8') as f:
    research_content = f.read()

# Exercise list in order
exercises = [
    "Dumbbell Lateral Raise",
    "Front Plate Raise",
    "Kneeling Single-Arm Cable Rear Delt Raise",
    "Lying Dumbbell External Rotation",
    "Lying Dumbbell Rear Delt Raise",
    "Lying Single-Arm Dumbbell Rear Delt Raise",
    "Pec Deck Rear Delt Extensions",
    "Reverse Incline Dumbbell Rear Delt Raise",
    "Seated Dumbbell Rear Delt Raise",
    "Single-Arm Cable Lateral Raise",
    "Cable External Rotation",
    "Close-Grip Bench Press",
    "Forward Lean Dips",
    "Assisted Dips",
    "Bench Dips",
    "Diamond Push-Up",
    "Dips",
    "Machine Dips",
    "Decline Dumbbell Triceps Extension",
    "Decline EZ-Bar Tricep Extension",
    "Decline Single Dumbbell Triceps Extension",
    "Decline Single-Arm Dumbbell Triceps Extension",
    "Dumbbell Kickback",
    "Incline EZ-Bar Tricep Extension",
    "Kneeling Cable Triceps Extension"
]

def extract_section(content, exercise_name):
    """Extract the full section for an exercise."""
    # Handle variations in naming
    search_name = exercise_name.upper().replace("-", " ")
    pattern = rf'## EXERCISE \d+:\s*{re.escape(search_name)}.*?(?=## EXERCISE|## SUMMARY|---\n\n##|\Z)'
    match = re.search(pattern, content, re.DOTALL | re.IGNORECASE)
    if match:
        return match.group(0)
    return None

def extract_field(section, field_name):
    """Extract a specific field from the section."""
    pattern = rf'\*\*{field_name}:\*\*\s*(.+?)(?=\n\*\*|\n###|\n\n)'
    match = re.search(pattern, section, re.DOTALL)
    if match:
        return match.group(1).strip().replace('\n', ' ')
    return ""

def extract_beginner_steps(section):
    """Extract beginner steps."""
    pattern = r'\*\*Beginner Steps.*?\n((?:\d+\.\s+.+?\n)+)'
    match = re.search(pattern, section, re.DOTALL)
    if match:
        steps_text = match.group(1)
        steps = re.findall(r'\d+\.\s+(.+?)(?=\n\d+\.|\n\n|\Z)', steps_text, re.DOTALL)
        return ' '.join([f"{i+1}. {step.strip()}" for i, step in enumerate(steps)])
    return ""

def extract_advanced_cues(section):
    """Extract advanced cues."""
    pattern = r'\*\*Advanced Cues:\*\*\s*\n((?:\d+\.\s+.+?\n)+)'
    match = re.search(pattern, section, re.DOTALL)
    if match:
        cues_text = match.group(1)
        cues = re.findall(r'\d+\.\s+(.+?)(?=\n\d+\.|\n\n|\Z)', cues_text, re.DOTALL)
        return ' '.join([f"{i+1}. {cue.strip()}" for i, cue in enumerate(cues)])
    return ""

def extract_references(section):
    """Extract references."""
    pattern = r'\*\*References:\*\*\s*\n((?:\d+\.\s+.+?\n)+)'
    match = re.search(pattern, section, re.DOTALL)
    if match:
        refs_text = match.group(1)
        refs = re.findall(r'\d+\.\s+(.+?)(?=\n\d+\.|\n\n|\Z)', refs_text, re.DOTALL)
        cleaned = [ref.strip().replace('\n', ' ') for ref in refs]
        return '; '.join(cleaned[:4])  # Max 4 references
    return ""

def extract_sports(section):
    """Extract sports applications."""
    pattern = r'\*\*Sports Applications:\*\*\s*\n((?:\d+\.\s+.+?\n)+)'
    match = re.search(pattern, section, re.DOTALL)
    if match:
        sports_text = match.group(1)
        sports = re.findall(r'\d+\.\s+(.+?)(?=\n\d+\.|\n\n|\Z)', sports_text)
        return ', '.join([sport.strip() for sport in sports[:12]])  # Max 12
    return ""

# Process all exercises
output_rows = []

for exercise_name in exercises:
    print(f"Processing: {exercise_name}")

    section = extract_section(research_content, exercise_name)
    if not section:
        print(f"  ✗ Not found")
        continue

    # Extract all fields
    primary = extract_field(section, "Primary Muscles")
    secondary = extract_field(section, "Secondary Muscles")
    ex_type = extract_field(section, "Type")
    equipment = extract_field(section, "Equipment")
    level = extract_field(section, "Level")

    # Infer body region and movement
    if any(kw in exercise_name.lower() for kw in ['shoulder', 'delt', 'lateral', 'front', 'rear', 'external rotation']):
        body_region = "Upper"
        if 'rotation' in exercise_name.lower():
            movement = "Rotation"
        elif any(kw in exercise_name.lower() for kw in ['raise', 'lateral', 'front']):
            movement = "Isolation"
        else:
            movement = "Isolation"
    elif any(kw in exercise_name.lower() for kw in ['tricep', 'dip', 'press', 'extension', 'kickback', 'push']):
        body_region = "Upper"
        if 'press' in exercise_name.lower() or 'dip' in exercise_name.lower() or 'push' in exercise_name.lower():
            movement = "Push"
        else:
            movement = "Extension"
    else:
        body_region = "Upper"
        movement = "Push"

    # Modality
    if 'cable' in exercise_name.lower():
        modality = "Cables"
    elif 'machine' in exercise_name.lower() or 'pec deck' in exercise_name.lower():
        modality = "Machine"
    elif 'barbell' in exercise_name.lower() or 'dumbbell' in exercise_name.lower() or 'ez-bar' in exercise_name.lower() or 'plate' in exercise_name.lower():
        modality = "Free Weight"
    else:
        modality = "Bodyweight"

    beginner_steps = extract_beginner_steps(section)
    advanced_cues = extract_advanced_cues(section)
    references = extract_references(section)
    sports = extract_sports(section)

    # Create table row
    row = (
        f"{exercise_name} | "
        f"{primary} | "
        f"{secondary} | "
        f"{ex_type} | "
        f"{equipment} | "
        f"{level} | "
        f"{body_region} | "
        f"{movement} | "
        f"{modality} | "
        f"{beginner_steps} | "
        f"{advanced_cues} | "
        f"{references} | "
        f"[TBD] | "  # ExRx Video
        f"[TBD] | "  # JEFIT Video
        f"[TBD] | "  # CoachWhitt Video
        f"{sports}"
    )

    output_rows.append(row)
    print(f"  ✓ Formatted")

# Write output
with open('batch_8_table_rows.txt', 'w', encoding='utf-8') as f:
    f.write("# Batch 8 Formatted Database Rows\n")
    f.write("# Session 15 - 25 exercises (Lines 226-250)\n")
    f.write("# Shoulders (11) + Triceps (14)\n\n")

    for row in output_rows:
        f.write(row + "\n")

print(f"\n✅ Complete! {len(output_rows)} exercises formatted")
print(f"Output saved to: batch_8_table_rows.txt")
