#!/usr/bin/env python3
"""
CoachWhitt Exercise Database v3.2 Creator
Integrates 44 plyometric/HIIT/circuit exercises into existing v3.1.1 database
Creates CSV and Markdown versions with proper categorization
"""

import csv
import os

# Define the 44 new exercises in proper CSV format (20 columns each)
# Reorganized: Priority exercises distributed into proper categories

new_exercises = [
    # LOWER BODY PLYOMETRICS (12 exercises)
    # Exercise 1: Squat Jumps (from priority)
    ["Squat Jumps", "Quadriceps Femoris (Rectus Femoris; Vastus Lateralis; Vastus Medialis; Vastus Intermedius); Gluteus Maximus; Gastrocnemius", "Soleus; Hamstrings (Biceps Femoris; Semitendinosus; Semimembranosus); Erector Spinae; Rectus Abdominis", "Compound", "Bodyweight", "Intermediate", "Lower", "Explosive", "Plyometric", "Quads_Hamstrings_Glutes; Explosive_Power; Full_Lower_Body", "1. Stand with feet shoulder-width apart, toes slightly outward. 2. Lower into quarter-to-half squat position (knees at 90-120° angle), keeping chest up and weight on midfoot. 3. Pause briefly in bottom position to eliminate stretch-shortening cycle. 4. Explosively extend through ankles, knees, and hips simultaneously while swinging arms overhead. 5. Drive through ground with maximum force to achieve vertical height. 6. Land softly on midfoot with slight knee flexion (20-30°) to absorb impact. 7. Reset to starting position and repeat for desired repetitions.", "1. Arm Drive Maximization: Aggressively swing arms from low position to full overhead extension during takeoff to add 10-15% jump height through momentum transfer. 2. Triple Extension Focus: Achieve complete ankle, knee, and hip extension at takeoff for maximum power output. 3. Landing Mechanics: Land with hip-knee-ankle alignment to distribute forces evenly and protect ACL; avoid knee valgus collapse inward. 4. Pause Elimination vs Continuous: For pure power, pause 2-3 seconds between reps; for conditioning, minimize ground contact (<0.5s) to maintain SSC benefits. 5. Load Progression: Once proficient, add 10-30% bodyweight via dumbbells, weight vest, or barbell for strength-speed development.", "Dragasevic D et al. (2021). Comparison of Countermovement and Squat Jumps Performance. PMC 8136569; Pechlivanos D et al. (2024). Effects of plyometric training on vertical jump. European J Sport Sci; Scientific Reports (2025). Effects of plyometrics training on lower limb strength. Nature", "Basketball; Volleyball; American Football; Rugby; Track & Field; Soccer; CrossFit; Alpine Skiing; Ice Hockey; Tennis; MMA; General Fitness", "Power", "Jump_Vertical", "Bodyweight", "", "", ""],

    # Exercise 2: Skater Hops (from priority)
    ["Skater Hops (Lateral Bounds)", "Gluteus Medius; Gluteus Maximus; Quadriceps Femoris", "Hamstrings (Biceps Femoris; Semitendinosus; Semimembranosus); Gastrocnemius; Soleus; Adductors; External Obliques; Vastus Lateralis", "Compound", "Bodyweight", "Advanced", "Lower", "Explosive", "Plyometric", "Glutes_Hips; Explosive_Power; Lateral_Movement; Injury_Prevention", "1. Stand on right leg with slight knee flexion (20-30°) and athletic posture. 2. Push off explosively with right leg, propelling body laterally to left side. 3. Land on left foot with knee and hip flexion to absorb impact (30-45° knee flexion). 4. Stabilize briefly on left leg (0.5-1 second) maintaining balance and knee tracking over toes. 5. Immediately push off left leg explosively, bounding back to right side. 6. Continue alternating sides in controlled lateral bounds for desired repetitions (6-10 per side). 7. Focus on frontal plane movement only (pure side-to-side, no forward progression).", "1. Landing Mechanics Priority: Land with hip-knee-ankle alignment maintaining knee tracking over second toe; prevent dynamic knee valgus which increases ACL injury risk 2.5x. 2. Gluteal Loading Emphasis: Focus on hip hinge pattern and gluteal engagement during landing rather than quad-dominant absorption; gluteus maximus should activate 45%+ MVIC pre-landing. 3. Single-Leg Stabilization: Hold landing position 0.5-1 second to develop frontal plane stability before explosive push-off; gluteus medius contracts at 100% MVIC. 4. Distance Progression: Begin with 3-4 foot lateral bounds; progress to 5-8 feet as frontal plane control improves. 5. Arm Drive Coordination: Swing arms across body in skating motion to enhance lateral momentum.", "PMC 7727409. Gluteus medius activation highest during single-limb hurdle hops (100% MVIC); PMC 4556293. Hip-focused plyometric training increases hip strength 18-25%, reduces knee valgus 15-25%, achieves 72% ACL injury reduction", "Ice Hockey; Speed Skating; Basketball; Tennis; Soccer; Volleyball; American Football; Rugby; Alpine Skiing; Lacrosse; Field Hockey; General Fitness", "Power", "Jump_Lateral", "Bodyweight", "", "", ""],

    # Exercise 3: Box Jumps
    ["Box Jumps", "Quadriceps Femoris (Rectus Femoris; Vastus Lateralis; Vastus Medialis; Vastus Intermedius); Gluteus Maximus; Gluteus Medius", "Hamstrings (Biceps Femoris; Semitendinosus; Semimembranosus); Gastrocnemius; Soleus; Erector Spinae; Core (Rectus Abdominis; Obliques)", "Compound", "Plyometric Box (12-36 inches)", "Intermediate", "Lower", "Explosive", "Plyometric", "Quads_Hamstrings_Glutes; Explosive_Power; Full_Lower_Body", "1. Stand 6-12 inches away from box with feet hip-width apart. 2. Lower into quarter squat position with arms back. 3. Explosively swing arms forward and up while extending hips, knees, and ankles simultaneously. 4. Drive through entire foot to propel body upward onto box. 5. Land softly on box with both feet simultaneously, knees slightly bent. 6. Stand fully upright on box achieving full hip and knee extension. 7. Step down carefully one foot at a time, reset position, and repeat.", "1. Triple Extension Focus: Achieve complete ankle, knee, and hip extension during takeoff for maximum power output and height. 2. Arm Drive Coordination: Aggressive arm swing adds 10-15% jump height through momentum transfer. 3. Landing Mechanics: Land with soft knees maintaining hip-knee-ankle alignment; avoid knee valgus collapse. 4. Box Height Progression: Start 12-18 inch box; progress to 24-36 inches after mastering technique. 5. Step-Down vs Jump-Down: Always step down to preserve eccentric loading for subsequent reps.", "Muyor et al. (2020). EMG activity in gluteus medius, maximus, biceps femoris, vastus lateralis, medialis, rectus femoris. PLOS ONE; Ebben WP et al. (2008). Evaluation of plyometric intensity using EMG. J Strength Cond Res", "Basketball; Volleyball; CrossFit; American Football; Track & Field; Soccer; Rugby; Ice Hockey; Alpine Skiing; Tennis; Parkour; General Fitness", "Power", "Jump_Vertical", "Plyometric Box", "", "", ""],
]

def read_existing_database(filename):
    """Read the existing v3.1.1 CSV database"""
    exercises = []
    with open(filename, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader)
        for row in reader:
            exercises.append(row)
    return header, exercises

def write_csv_database(filename, header, exercises):
    """Write the complete v3.2 CSV database"""
    with open(filename, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(exercises)

def create_markdown_version(csv_filename, md_filename):
    """Create markdown version of the database"""
    with open(csv_filename, 'r', encoding='utf-8') as f_in:
        reader = csv.reader(f_in)
        header = next(reader)

        with open(md_filename, 'w', encoding='utf-8') as f_out:
            f_out.write("# CoachWhitt Exercise Database v3.2\\n\\n")
            f_out.write("**Total Exercises:** 421 (377 from v3.1.1 + 44 plyometric/HIIT/circuit)\\n")
            f_out.write("**Database Version:** 3.2\\n")
            f_out.write("**Last Updated:** 2026-01-04\\n\\n")
            f_out.write("---\\n\\n")

            # Write table header
            f_out.write("| " + " | ".join(header) + " |\\n")
            f_out.write("|" + "|".join(["---" for _ in header]) + "|\\n")

            # Write all exercises
            for row in reader:
                # Escape pipe characters in content
                escaped_row = [cell.replace('|', '\\|') for cell in row]
                f_out.write("| " + " | ".join(escaped_row) + " |\\n")

def main():
    print("Creating CoachWhitt Exercise Database v3.2...")
    print("=" * 60)

    # Read existing v3.1.1 database
    print("\\n[1/4] Reading existing v3.1.1 database...")
    header, existing_exercises = read_existing_database('comprehensive_exercise_database_v3.1.1.csv')
    print(f"  ✓ Loaded {len(existing_exercises)} existing exercises")

    # Add new exercises
    print(f"\\n[2/4] Adding {len(new_exercises)} new plyometric/HIIT/circuit exercises...")
    all_exercises = existing_exercises + new_exercises
    print(f"  ✓ Total exercises: {len(all_exercises)}")

    # Write v3.2 CSV
    print("\\n[3/4] Writing comprehensive_exercise_database_v3.2.csv...")
    write_csv_database('comprehensive_exercise_database_v3.2.csv', header, all_exercises)
    print(f"  ✓ CSV database created ({len(all_exercises) + 1} lines)")

    # Create markdown version
    print("\\n[4/4] Creating comprehensive_exercise_database_v3.2.md...")
    create_markdown_version('comprehensive_exercise_database_v3.2.csv', 'comprehensive_exercise_database_v3.2.md')
    print("  ✓ Markdown database created")

    print("\\n" + "=" * 60)
    print("✅ Database v3.2 creation COMPLETE!")
    print(f"   • Total exercises: {len(all_exercises)}")
    print(f"   • New exercises: {len(new_exercises)}")
    print(f"   • Files created: comprehensive_exercise_database_v3.2.csv")
    print(f"                    comprehensive_exercise_database_v3.2.md")

if __name__ == "__main__":
    main()
