#!/usr/bin/env python3
"""
Add 'Skiing' tag to Sports Tags column for skiing-applicable exercises.
Based on gemini-research analysis from skiing_exercises_analysis.md
"""

import csv

# List of 156 exercises that should have "Skiing" tag added
# From skiing_exercises_analysis.md - CONSOLIDATED UNIQUE EXERCISE LIST
SKIING_EXERCISES = [
    "Ab Wheel Rollout",
    "Assisted Pull-Up",
    "Back Squat",
    "Barbell Bent-Over Row",
    "Barbell Calf Raise",
    "Barbell Lunge",
    "Barbell Reverse Lunge",
    "Barbell Side Lunge",
    "Barbell Split Squat",
    "Barbell Squat",
    "Barbell Step-Up",
    "Barbell Walking Lunge",
    "Bent-Knee Crunch",
    "Bent-Knee Medicine Ball Hip Rotation",
    "Bent-Knee Single-Leg Hip Lift",
    "Bent-Over Barbell Row (Pronated Grip)",
    "Bent-Over Reverse-Grip Barbell Row",
    "Bird Dog",
    "Box Jump (Calf Emphasis Landing)",
    "Box Jumps",
    "Broad Jumps",
    "Bulgarian Split Squat",
    "Cable Chop",
    "Cable Crunch (Kneeling)",
    "Cable Pull-Through",
    "Cable Woodchop (High to Low)",
    "Calf Press",
    "Calf Press on Leg Press",
    "Calf Raise - Seated",
    "Calf Raise - Standing",
    "Chin-Ups (Supinated Grip)",
    "Clean (Power Clean)",
    "Clean and Jerk",
    "Close-Grip Lat Pulldown",
    "Conventional Deadlift",
    "Cross Crunch",
    "Cross Crunch w/ Medicine Ball",
    "Crunch (Standard)",
    "Dead Bug",
    "Deadlift",
    "Diagonal Lunge",
    "Donkey Calf Raise",
    "Dumbbell Calf Raise",
    "Dumbbell Diagonal Lunge",
    "Dumbbell Lunge",
    "Dumbbell Reverse Lunge",
    "Dumbbell Side Lunge (Lateral Lunge)",
    "Dumbbell Split Squat (Bulgarian Split Squat)",
    "Dumbbell Squat (Goblet Squat)",
    "Dumbbell Step-Up",
    "Dumbbell Walking Lunge",
    "Elevated Hip Lift",
    "Elevated Single-Leg Hip Lift",
    "Farmer's Walk (Calf Emphasis)",
    "Forward Lunge",
    "Front Plank (Tripod - 1 arm and 2 legs or 2 arms and 1 leg)",
    "Front Plank (from knees)",
    "Front Plank (from toes)",
    "Front Squat",
    "Full Reverse Crunch",
    "Glute-Ham Raise",
    "Goblet Squat",
    "Good Morning",
    "Hack Squat (Machine)",
    "Hang Clean",
    "Hanging Leg Raise",
    "Hip Lift (Glute Bridge)",
    "Hip Thrust (Barbell)",
    "Incline Hip Thrust",
    "Incline Reverse Crunch",
    "Inverted Bodyweight Row",
    "Jump Rope (Calf Focus)",
    "Kettlebell Swings",
    "Kneeling Ab Rollout",
    "Lat Pulldown (Front)",
    "Lateral Barbell Squat",
    "Lateral Barbell Step-Up",
    "Lateral Squat",
    "Lateral Step-Up",
    "Leg Curl",
    "Leg Extension",
    "Leg Press",
    "Lunge",
    "Lying Alternating Leg Curl",
    "Lying Hip Thrust",
    "Lying Leg Curl",
    "Lying Single-Leg Curl",
    "Machine Hack Squat",
    "Machine Row",
    "Medicine Ball V-Up",
    "Nordic Hamstring Curl",
    "One-Arm Dumbbell Row (Supported)",
    "Pallof Press",
    "Plank (Front)",
    "Prowler Push",
    "Pull-Up (Pronated Grip)",
    "Pull-Ups (Wide Grip)",
    "Reverse Cable Chop",
    "Reverse Crunch",
    "Reverse Medicine Ball Crunch",
    "Reverse-Grip Lat Pulldown",
    "Reverse-Grip Pull-Up (Chin-Up)",
    "Reverse Lunge",
    "Romanian Deadlift (RDL)",
    "Russian Twist",
    "Seated Cable Row",
    "Seated Cable Row (V-Bar/Close Grip)",
    "Seated Calf Raise",
    "Seated Calf Raise (Machine)",
    "Seated Leg Curl",
    "Seated Medicine Ball Twist",
    "Seated Single-Leg Calf Raise",
    "Side Plank",
    "Side-Plank (from knees)",
    "Side-Plank (from toes)",
    "Side-Plank (hip lift)",
    "Single-Arm Barbell Side Squat",
    "Single-Arm Dumbbell Side Squat",
    "Single-Arm Dumbbell Row",
    "Single-Arm Lat Pulldown",
    "Single-Leg Barbell Squat",
    "Single-Leg Box Squat",
    "Single-Leg Calf Press",
    "Single-Leg Calf Raise (Bodyweight/Dumbbell)",
    "Single-Leg Dumbbell Box Squat",
    "Single-Leg Dumbbell Calf Raise",
    "Single-Leg Dumbbell Squat",
    "Single-Leg Hip Lift",
    "Single-Leg Romanian Deadlift",
    "Single-Leg Squat",
    "Sissy Squat",
    "Sled Push (Toe Push)",
    "Smith Machine Calf Raise",
    "Smith Machine Squat",
    "Snatch (Power Snatch)",
    "Squat Jumps",
    "Standing Calf Raise (Machine)",
    "Step-Up",
    "Step-Ups",
    "Sumo Deadlift",
    "Superman",
    "Superman Hold",
    "Suspended Row",
    "T-Bar Row",
    "Thruster",
    "Towel Pull-Ups",
    "Trunk Rotator",
    "V-Bar Pull-Up (Neutral Grip)",
    "V-Up",
    "Walking Lunges",
    "Weighted Crunch",
    "Weighted V-Up",
    "Wide-Grip Lat Pulldown",
    "Lying Machine Squat"
]

# Convert to set for faster lookup
SKIING_EXERCISES_SET = set(SKIING_EXERCISES)

def add_skiing_tags(input_file, output_file):
    """
    Read CSV, add 'Skiing' to Sports Tags column for applicable exercises.

    Args:
        input_file: Path to comprehensive_exercise_database_v3.1.csv
        output_file: Path to comprehensive_exercise_database_v3.1.1.csv
    """
    rows_updated = 0
    total_rows = 0

    with open(input_file, 'r', encoding='utf-8') as infile, \
         open(output_file, 'w', encoding='utf-8', newline='') as outfile:

        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        # Read and write header
        header = next(reader)
        writer.writerow(header)

        # Find Sports Tags column index (should be column 14, index 13)
        try:
            sports_tags_idx = header.index('Sports Tags')
            print(f"Sports Tags column found at index {sports_tags_idx}")
        except ValueError:
            print("ERROR: 'Sports Tags' column not found in header")
            return

        # Process each exercise row
        for row in reader:
            total_rows += 1

            if len(row) == 0:
                continue

            exercise_name = row[0].strip()

            # Check if this exercise should have Skiing tag
            if exercise_name in SKIING_EXERCISES_SET:
                # Get existing sports tags
                existing_tags = row[sports_tags_idx].strip() if sports_tags_idx < len(row) else ""

                # Check if "Skiing" already in tags
                if "Skiing" not in existing_tags:
                    # Add Skiing tag
                    if existing_tags:
                        # Append with semicolon separator (database uses ; not ,)
                        row[sports_tags_idx] = existing_tags + "; Skiing"
                    else:
                        # No existing tags, just add Skiing
                        row[sports_tags_idx] = "Skiing"

                    rows_updated += 1
                    print(f"✓ Added 'Skiing' to: {exercise_name}")
                else:
                    print(f"  Already has 'Skiing': {exercise_name}")

            writer.writerow(row)

    print(f"\n=== Summary ===")
    print(f"Total exercises processed: {total_rows}")
    print(f"Exercises updated with 'Skiing' tag: {rows_updated}")
    print(f"Output written to: {output_file}")

    # Report any exercises from the list that weren't found
    with open(input_file, 'r', encoding='utf-8') as infile:
        reader = csv.reader(infile)
        next(reader)  # Skip header
        database_exercises = {row[0].strip() for row in reader if len(row) > 0}

    missing_exercises = SKIING_EXERCISES_SET - database_exercises
    if missing_exercises:
        print(f"\n⚠ Warning: {len(missing_exercises)} exercises from skiing list NOT found in database:")
        for ex in sorted(missing_exercises):
            print(f"  - {ex}")

if __name__ == "__main__":
    input_csv = "/mnt/z/coachwhitt/ai/002 - Exercise Templates/comprehensive_exercise_database_v3.1.csv"
    output_csv = "/mnt/z/coachwhitt/ai/002 - Exercise Templates/comprehensive_exercise_database_v3.1.1.csv"

    print("Adding 'Skiing' tags to exercise database...")
    print(f"Input:  {input_csv}")
    print(f"Output: {output_csv}")
    print(f"Target: {len(SKIING_EXERCISES)} exercises\n")

    add_skiing_tags(input_csv, output_csv)
    print("\n✓ Complete!")
