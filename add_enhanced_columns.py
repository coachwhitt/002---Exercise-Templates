#!/usr/bin/env python3
"""
Add 3 enhanced filtering columns to comprehensive_exercise_database_v3.md
- Training_Goal
- Movement_Pattern
- Equipment_Type

Based on taxonomy defined in enhanced_columns_taxonomy.md
"""

import re

def determine_training_goal(exercise_name, exercise_type, equipment, level, movement):
    """
    Determine Training_Goal based on exercise characteristics
    Returns: Single value (Strength, Hypertrophy, Power, Endurance, Stability, Mobility)
    """
    name_lower = exercise_name.lower()

    # Power movements (Olympic lifts, plyometrics)
    power_keywords = ['clean', 'snatch', 'jerk', 'jump', 'box jump', 'broad jump',
                      'squat jump', 'thruster', 'swing', 'kettlebell swing', 'prowler']
    if any(keyword in name_lower for keyword in power_keywords):
        return "Power"

    # Stability movements (planks, holds, anti-rotation)
    stability_keywords = ['plank', 'hold', 'superman', 'bird dog', 'pallof',
                         'mountain climber', 'jack knife', 'reverse mountain']
    if any(keyword in name_lower for keyword in stability_keywords):
        return "Stability"

    # Strength movements (compound barbell/heavy loads)
    if exercise_type == "Compound" and equipment in ["Barbell", "Barbell, Bench",
                                                      "Barbell, Flat Bench",
                                                      "Barbell, Incline Bench",
                                                      "Barbell, Decline Bench"]:
        if 'press' in name_lower or 'squat' in name_lower or 'deadlift' in name_lower or 'row' in name_lower:
            return "Strength"

    # Isolation movements → Hypertrophy
    if exercise_type == "Isolation":
        return "Hypertrophy"

    # Default: Compound exercises → Hypertrophy (most common training goal)
    return "Hypertrophy"


def determine_movement_pattern(exercise_name, exercise_type, movement, body_region):
    """
    Determine Movement_Pattern(s) based on exercise characteristics
    Returns: Semicolon-separated values
    """
    name_lower = exercise_name.lower()
    patterns = []

    # Vertical Push
    if any(word in name_lower for word in ['overhead press', 'military press', 'shoulder press',
                                             'arnold press', 'dumbbell press' and 'standing',
                                             'thruster', 'push press', 'jerk']):
        patterns.append("Push_Vertical")

    # Horizontal Push
    if any(word in name_lower for word in ['bench press', 'push-up', 'push up', 'dips',
                                             'chest press', 'pec deck', 'flye', 'fly',
                                             'crossover', 'dumbbell press' and 'lying']):
        patterns.append("Push_Horizontal")

    # Vertical Pull
    if any(word in name_lower for word in ['pull-up', 'pull up', 'chin-up', 'chin up',
                                             'lat pulldown', 'pulldown']):
        patterns.append("Pull_Vertical")

    # Horizontal Pull
    if 'row' in name_lower or 'reverse fly' in name_lower or 'face pull' in name_lower:
        patterns.append("Pull_Horizontal")

    # Squat pattern
    if 'squat' in name_lower and 'jump' not in name_lower:
        patterns.append("Squat")

    # Hinge pattern
    if any(word in name_lower for word in ['deadlift', 'good morning', 'hip thrust',
                                             'swing', 'clean', 'snatch', 'rdl',
                                             'romanian', 'glute bridge']):
        patterns.append("Hinge")

    # Lunge pattern
    if any(word in name_lower for word in ['lunge', 'split squat', 'step up', 'step-up']):
        patterns.append("Lunge")

    # Rotation
    if any(word in name_lower for word in ['bicycle', 'twist', 'chop', 'rotation', 'rotating']):
        patterns.append("Rotation")

    # Anti-Rotation
    if 'single-arm' in name_lower or 'single arm' in name_lower or 'one-arm' in name_lower:
        if 'row' in name_lower or 'press' in name_lower:
            patterns.append("Anti-Rotation")

    if any(word in name_lower for word in ['pallof', 'plank', 'mountain climber', 'bird dog']):
        patterns.append("Anti-Rotation")

    # Isometric
    if any(word in name_lower for word in ['hold', 'plank', 'wall sit', 'superman hold', 'l-sit']):
        patterns.append("Isometric")

    # Isolation for single-joint movements
    if exercise_type == "Isolation":
        if any(word in name_lower for word in ['curl', 'extension', 'raise', 'lateral',
                                                 'front raise', 'shrug', 'calf']):
            patterns.append("Isolation")

    # If no pattern detected, assign based on movement column
    if not patterns:
        if movement == "Push":
            patterns.append("Push_Horizontal")
        elif movement == "Pull":
            patterns.append("Pull_Horizontal")
        elif movement in ["Static Hold", "Isometric"]:
            patterns.append("Isometric")

    return "; ".join(patterns) if patterns else "Compound"


def determine_equipment_type(equipment_column):
    """
    Determine Equipment_Type based on equipment column
    Returns: Semicolon-separated values
    """
    equipment_lower = equipment_column.lower()
    equipment_types = []

    # Direct mappings
    if 'barbell' in equipment_lower:
        equipment_types.append("Barbell")
    if 'dumbbell' in equipment_lower:
        equipment_types.append("Dumbbell")
    if 'kettlebell' in equipment_lower:
        equipment_types.append("Kettlebell")
    if 'machine' in equipment_lower or 'selectorized' in equipment_lower:
        equipment_types.append("Machine")
    if 'cable' in equipment_lower:
        equipment_types.append("Cable")
    if 'bodyweight' in equipment_lower:
        equipment_types.append("Bodyweight")
    if 'suspension' in equipment_lower or 'trx' in equipment_lower or 'rings' in equipment_lower:
        equipment_types.append("Suspension_Trainer")
    if 'band' in equipment_lower:
        equipment_types.append("Resistance_Band")
    if 'medicine ball' in equipment_lower:
        equipment_types.append("Medicine_Ball")
    if 'stability ball' in equipment_lower or 'swiss ball' in equipment_lower:
        equipment_types.append("Stability_Ball")
    if 'box' in equipment_lower and 'plyometric' in equipment_lower:
        equipment_types.append("Plyometric_Box")
    if 'prowler' in equipment_lower or 'sled' in equipment_lower:
        equipment_types.append("Sled")
    if 'landmine' in equipment_lower or 't-bar' in equipment_lower:
        equipment_types.append("Landmine")
    if 'ez bar' in equipment_lower or 'ez-bar' in equipment_lower:
        equipment_types.append("EZ_Bar")
    if 'trap bar' in equipment_lower or 'hex bar' in equipment_lower:
        equipment_types.append("Trap_Bar")
    if 'smith machine' in equipment_lower:
        equipment_types.append("Smith_Machine")
    if 'bench' in equipment_lower:
        equipment_types.append("Bench")
    if 'pull-up bar' in equipment_lower or 'pullup bar' in equipment_lower:
        equipment_types.append("Pull-Up_Bar")

    return "; ".join(equipment_types) if equipment_types else equipment_column


def process_database():
    """
    Read database v3, add 3 enhanced columns, write to new file
    """
    input_file = "comprehensive_exercise_database_v3.md"
    output_file = "comprehensive_exercise_database_v3_with_enhanced_columns.md"

    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    output_lines = []
    data_row_count = 0

    for i, line in enumerate(lines):
        # Skip until we reach the table header
        if line.startswith("| Exercise | Primary Muscles"):
            # This is the header row - add 3 new columns
            header = line.rstrip(" |\n") + " | Training_Goal | Movement_Pattern | Equipment_Type |\n"
            output_lines.append(header)
            continue

        # Handle separator row
        if line.startswith("|----------|"):
            # Add separators for 3 new columns
            separator = line.rstrip(" |\n") + "|-------------------|---------------------|----------------|\n"
            output_lines.append(separator)
            continue

        # Process data rows (rows that start with | and contain exercise data)
        if line.startswith("|") and not line.startswith("|-------"):
            # Parse the row into columns
            columns = [col.strip() for col in line.split("|")[1:-1]]  # Remove empty first/last

            if len(columns) >= 14:  # Should have 14 columns
                exercise_name = columns[0]
                exercise_type = columns[3]
                equipment = columns[4]
                level = columns[5]
                body_region = columns[6]
                movement = columns[7]

                # Determine values for 3 new columns
                training_goal = determine_training_goal(exercise_name, exercise_type, equipment, level, movement)
                movement_pattern = determine_movement_pattern(exercise_name, exercise_type, movement, body_region)
                equipment_type = determine_equipment_type(equipment)

                # Reconstruct row with 3 new columns
                new_row = "| " + " | ".join(columns) + f" | {training_goal} | {movement_pattern} | {equipment_type} |\n"
                output_lines.append(new_row)
                data_row_count += 1
            else:
                # Keep line as-is if it doesn't match expected format
                output_lines.append(line)
        else:
            # Keep all non-table lines as-is (headers, separators, etc.)
            output_lines.append(line)

    # Update the total exercises count in header
    for i, line in enumerate(output_lines):
        if line.startswith("**Total Exercises:**"):
            output_lines[i] = f"**Total Exercises:** {data_row_count}\n"

    # Write output file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(output_lines)

    print(f"✅ Successfully processed {data_row_count} exercises")
    print(f"📝 Output file: {output_file}")
    print(f"📊 Added 3 columns: Training_Goal, Movement_Pattern, Equipment_Type")
    print(f"📊 Database now has 17 columns (14 original + 3 new)")

    return data_row_count


if __name__ == "__main__":
    count = process_database()
    print(f"\n🎉 Database enhancement complete! Total exercises: {count}")
