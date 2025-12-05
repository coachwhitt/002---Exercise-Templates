#!/usr/bin/env python3
"""
Fix missing Primary/Secondary muscles for Batch 1 exercises.
Re-extract from the research file with better parsing.
"""

import re
import csv

# Manual extraction for the 6 exercises based on research file
batch1_fixes = {
    "Ab-Cycle (Bicycle Crunches)": {
        "Primary_Muscles": "Rectus Abdominis (entire length, both upper and lower portions), Obliquus Externus Abdominis (external obliques, bilateral activation with contralateral dominance during rotation)",
        "Secondary_Muscles": "Obliquus Internus Abdominis (internal obliques), Transversus Abdominis, Iliopsoas (hip flexors), Rectus Femoris (quadriceps)",
        "Type": "Isolation"
    },
    "Box Jumps": {
        "Primary_Muscles": "Quadriceps (Vastus Lateralis, Vastus Medialis, Vastus Intermedius, Rectus Femoris), Gluteus Maximus, Gastrocnemius, Soleus",
        "Secondary_Muscles": "Hamstrings (Biceps Femoris, Semitendinosus, Semimembranosus), Hip Flexors (Iliopsoas), Erector Spinae, Core stabilizers (Rectus Abdominis, Obliques)",
        "Type": "Compound"
    },
    "Broad Jumps (Standing Long Jump)": {
        "Primary_Muscles": "Gluteus Maximus (primary force producer), Quadriceps (Rectus Femoris, Vastus Lateralis, Vastus Medialis, Vastus Intermedius), Gastrocnemius, Soleus",
        "Secondary_Muscles": "Hamstrings (Biceps Femoris, Semitendinosus, Semimembranosus), Hip Flexors (Iliopsoas, Rectus Femoris), Core stabilizers (Rectus Abdominis, Erector Spinae), Anterior Tibialis",
        "Type": "Compound"
    },
    "Squat Jumps": {
        "Primary_Muscles": "Quadriceps (Vastus Lateralis, Vastus Medialis, Vastus Intermedius, Rectus Femoris), Gluteus Maximus, Gastrocnemius, Soleus",
        "Secondary_Muscles": "Hamstrings (Biceps Femoris, Semitendinosus, Semimembranosus), Erector Spinae, Core stabilizers (Rectus Abdominis, Obliques), Hip adductors",
        "Type": "Compound"
    },
    "Superman": {
        "Primary_Muscles": "Erector Spinae (Iliocostalis, Longissimus, Spinalis), Multifidus (lumbar region), Gluteus Maximus",
        "Secondary_Muscles": "Hamstrings (Biceps Femoris, Semitendinosus, Semimembranosus), Trapezius (Middle and Lower fibers), Rhomboids, Posterior Deltoids",
        "Type": "Isolation"
    },
    "Superman Hold (Isometric Back Extension Hold)": {
        "Primary_Muscles": "Erector Spinae (Iliocostalis, Longissimus, Spinalis), Multifidus (lumbar and thoracic), Gluteus Maximus",
        "Secondary_Muscles": "Hamstrings (Biceps Femoris, Semitendinosus, Semimembranosus), Trapezius (Middle and Lower fibers), Rhomboids, Posterior Deltoids, Latissimus Dorsi (lower fibers)",
        "Type": "Isolation"
    }
}

# Load current v3.1
with open('comprehensive_exercise_database_v3_1.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    exercises = list(reader)
    fieldnames = reader.fieldnames

# Fix the exercises
fixed_count = 0
for ex in exercises:
    if ex['Exercise'] in batch1_fixes:
        fixes = batch1_fixes[ex['Exercise']]
        ex['Primary_Muscles'] = fixes['Primary_Muscles']
        ex['Secondary_Muscles'] = fixes['Secondary_Muscles']
        ex['Type'] = fixes['Type']
        fixed_count += 1
        print(f"✅ Fixed: {ex['Exercise']}")

# Write back
with open('comprehensive_exercise_database_v3_1.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(exercises)

print(f"\n🎯 Fixed {fixed_count} exercises")
print("✅ Database updated: comprehensive_exercise_database_v3_1.csv")
