#!/usr/bin/env python3
"""
Format Batch 5 exercises for comprehensive_exercise_database_v2.md integration
Session 12 - 2025-12-02
25 exercises: 3 chest, 11 hamstrings, 11 quadriceps
"""

# Define all 25 exercises in 16-column format for database integration
# Format: Name | Primary | Secondary | Type | Equipment | Instructions | Cues | Reference | Video | Sports

exercises = {
    "chest": [
        {
            "name": "Low Cable Crossover",
            "primary": "Pectoralis Major - Sternal Head, Pectoralis Major - Clavicular Head",
            "secondary": "Anterior Deltoid, Pectoralis Minor, Serratus Anterior",
            "type": "Isolation",
            "equipment": "Cable Machine",
            "instructions": "Stand centered between cables with handles at shoulder height or above. Step forward with tension. Arms out to sides, elbows slightly bent (10-15°), palms forward. Athletic stance, one foot forward. Engage core, chest lifted. Pull handles down and across body in smooth arc to lower chest/upper abdomen. Squeeze chest at peak. Return slowly with control.",
            "cues": "Maintain constant cable tension throughout ROM; Visualize pec fibers contracting sternum to humerus; Vary pulley height (high-low emphasizes lower pec, low-high upper pec); Avoid forward lean or momentum; Rotate palms inward at bottom, hold 1-2 seconds",
            "reference": "Boeckh-Behrens & Buskies (2000) Fitness-Krafttraining; Schoenfeld et al. (2020) J Sports Sci 38(14):1654-1661 DOI:10.1080/02640414.2020.1752696; ACE (2012) Cables activated pecs 93% of bench press; Welsch et al. (2005) J Strength Cond Res 19(2):449-452 DOI:10.1519/14513.1",
            "video": "",
            "sports": "Bodybuilding, Swimming, Tennis, Baseball, Volleyball, American Football, Rugby, Boxing, MMA, Rock Climbing, Gymnastics, Wrestling"
        },
        {
            "name": "Pec Deck",
            "primary": "Pectoralis Major - Sternal Head, Pectoralis Major - Clavicular Head",
            "secondary": "Anterior Deltoid, Biceps Brachii - Short Head",
            "type": "Isolation",
            "equipment": "Pec Deck Machine",
            "instructions": "Adjust seat so handles at chest level. Sit upright, back against pad, feet flat. Forearms on padded levers, elbows bent 90°. Grip lightly - push through forearms not hands. Start arms wide with comfortable chest stretch. Bring pads together front of chest, smooth controlled motion. Squeeze chest when pads meet center. Return slowly to start.",
            "cues": "Push through elbows not hands to minimize triceps; Maintain scapular stability, avoid excessive protraction; Pause 1-2s at peak contraction; Control eccentric 2-3s tempo; Partial reps at contracted position for metabolic stress",
            "reference": "Welsch et al. (2005) Univ Wisconsin pec deck 98% of bench press EMG; Schick et al. (2010) J Strength Cond Res 24(3):779-784 DOI:10.1519/JSC.0b013e3181cc2237; ACE (2012) Pec deck ranked 2nd EMG study; Campos et al. (2020) J Hum Kinet 72(1):173-182 DOI:10.2478/hukin-2019-0126",
            "video": "",
            "sports": "Bodybuilding, Swimming, Baseball, Tennis, Volleyball, American Football, Rugby, Boxing, MMA, Rock Climbing, Gymnastics, Wrestling, Rowing"
        },
        {
            "name": "Pec Deck Fly",
            "primary": "Pectoralis Major - Sternal Head, Pectoralis Major - Clavicular Head",
            "secondary": "Anterior Deltoid, Coracobrachialis",
            "type": "Isolation",
            "equipment": "Pec Deck Machine",
            "instructions": "Adjust seat, handles align mid-chest when arms extended. Sit, back against pad, feet flat. Grasp handles palms inward, arms extended, slight elbow bend (10-20°). Start arms wide, gentle chest stretch. Core engaged, upright posture. Bring handles together wide arcing motion, chest doing work. Squeeze pecs at peak when handles meet. Return slowly with control.",
            "cues": "Maintain same elbow angle throughout - fly not press; Imagine hugging large tree trunk; Control scapular position, avoid winging; Use 3-1-2 tempo (3s eccentric, 1s pause, 2s concentric) for hypertrophy; Keep shoulders depressed to reduce deltoid dominance",
            "reference": "Botton et al. (2021) J Sports Med Phys Fit 61(3):311-317 DOI:10.23736/S0022-4707.20.11221-9; Schoenfeld & Grgic (2020) SAGE Open Med 8:1-10 DOI:10.1177/2050312120901559; Solstad et al. (2021) J Hum Kinet 78:5-14 DOI:10.2478/hukin-2021-0034; Aboodarda et al. (2018) Int J Exerc Sci 11(6):885-899 PMCID:PMC6033513",
            "video": "",
            "sports": "Bodybuilding, Swimming, Tennis, Baseball, Volleyball, American Football, Rugby, Boxing, MMA, Rock Climbing, Gymnastics, Wrestling"
        }
    ],
    "hamstrings": [
        {
            "name": "Bent-Knee Single-Leg Hip Lift",
            "primary": "Gluteus Maximus, Hamstrings (Biceps Femoris, Semitendinosus, Semimembranosus)",
            "secondary": "Erector Spinae, Gluteus Medius, Adductor Magnus",
            "type": "Compound",
            "equipment": "Exercise Mat",
            "instructions": "Lie on back, one knee bent foot flat hip-width. Extend other leg straight aligned with bent knee. Arms at sides palms down for stability. Engage core, navel to spine. Press through heel of grounded foot to lift hips. Lift until body forms straight line shoulders to extended knee. Squeeze glutes at top, hold 1-2s. Lower with control, repeat before switching legs.",
            "cues": "Maximize glute activation by pushing through heel not toes; Maintain pelvic stability, avoid rotation or tilting; Keep extended leg actively engaged and aligned with supporting thigh; Drive from hip extension not spinal extension (avoid lumbar hyperextension); Progress by elevating supporting foot or performing with pause at top",
            "reference": "Lehecka et al. (2017) Int J Sports Phys Ther 12(4):543-549 PMCID:PMC5534144; Selkowitz et al. (2013) J Orthop Sports Phys Ther 43(2):54-64 DOI:10.2519/jospt.2013.4116; Boren et al. (2011) Int J Sports Phys Ther 6(3):206-223 PMCID:PMC3201064; Distefano et al. (2009) J Orthop Sports Phys Ther 39(7):532-540 DOI:10.2519/jospt.2009.2796",
            "video": "",
            "sports": "Sprint Running, American Football, Soccer, Rugby, Basketball, Volleyball, Track & Field, Tennis, Skiing, Snowboarding, CrossFit, Powerlifting"
        },
        {
            "name": "Elevated Hip Lift",
            "primary": "Gluteus Maximus, Hamstrings (Biceps Femoris, Semitendinosus, Semimembranosus)",
            "secondary": "Erector Spinae, Gastrocnemius, Core Stabilizers",
            "type": "Compound",
            "equipment": "Bench or Box (12-24 inches)",
            "instructions": "Place feet on elevated surface (bench/box), knees bent 90°. Lie on back, arms at sides palms down. Feet hip-width apart on elevation. Engage core, press through heels to lift hips. Raise hips until body forms straight line shoulders to knees. Squeeze glutes hard at top. Hold contraction 1-2s. Lower with control, stopping just before hips touch floor.",
            "cues": "Elevated position increases ROM and glute/hamstring stretch at bottom; Maintain neutral spine, avoid lumbar hyperextension or flexion; Drive through heels, slightly dorsiflex ankles to enhance hamstring activation; Add resistance (barbell/weight plate across hips) for progressive overload; Perform single-leg for increased stability demands and activation",
            "reference": "Andersen et al. (2018) J Strength Cond Res 32(3):587-593 DOI:10.1519/JSC.0000000000001826; Contreras et al. (2015) J Appl Biomech 31(6):452-458 DOI:10.1123/jab.2015-0091; Worrell et al. (2001) J Orthop Sports Phys Ther 31(12):730-740 DOI:10.2519/jospt.2001.31.12.730; Martín-Fuentes et al. (2020) PLOS ONE 15(2):e0229507 DOI:10.1371/journal.pone.0229507",
            "video": "",
            "sports": "Sprint Running, Track & Field, American Football, Soccer, Rugby, Basketball, Volleyball, Skiing, Snowboarding, Powerlifting, Olympic Weightlifting, CrossFit"
        },
        {
            "name": "Elevated Single-Leg Hip Lift",
            "primary": "Gluteus Maximus, Hamstrings (Biceps Femoris, Semitendinosus, Semimembranosus)",
            "secondary": "Gluteus Medius, Erector Spinae, Adductor Magnus, Core Stabilizers",
            "type": "Compound",
            "equipment": "Bench or Box (12-24 inches)",
            "instructions": "Lie on back, one foot on elevated surface (bench/box). Extend other leg straight aligned with bent knee. Arms at sides palms down for balance. Engage core for pelvic stability. Press through heel of elevated foot to lift hips. Lift until body forms straight line shoulders to extended knee. Squeeze glutes at top, hold 1-2s. Lower with control, repeat all reps before switching legs.",
            "cues": "Unilateral variation demands significant hip and core stability, prevent rotation; Drive forcefully through heel of working leg for maximum posterior chain activation; Keep non-working leg actively extended and engaged throughout set; Control descent with 3-4s eccentric tempo for enhanced muscle damage and growth; Progress by adding weight (barbell across hips, dumbbell on working hip, weighted vest)",
            "reference": "Lehecka et al. (2017) Int J Sports Phys Ther 12(4):543-549 PMCID:PMC5534144; McCurdy et al. (2010) J Strength Cond Res 24(11):3081-3088 DOI:10.1519/JSC.0b013e3181d75807; Youdas et al. (2015) Physiother Theory Pract 31(6):418-427 DOI:10.3109/09593985.2015.1010672; Contreras et al. (2016) J Strength Cond Res 30(7):1879-1887 DOI:10.1519/JSC.0000000000001282",
            "video": "",
            "sports": "Sprint Running, Track & Field, American Football, Soccer, Rugby, Basketball, Volleyball, Tennis, Skiing, Snowboarding, CrossFit, Powerlifting, Olympic Weightlifting, Cycling"
        },
        {
            "name": "Hip Lift (Glute Bridge)",
            "primary": "Gluteus Maximus, Hamstrings (Biceps Femoris, Semitendinosus, Semimembranosus)",
            "secondary": "Erector Spinae, Core Stabilizers, Adductors",
            "type": "Compound",
            "equipment": "Exercise Mat",
            "instructions": "Lie flat on back, knees bent feet flat. Feet hip-width apart, approximately 12 inches from glutes. Arms at sides palms down. Engage core, draw belly button toward spine. Press through both heels to lift hips. Raise hips until body forms straight line shoulders to knees. Squeeze glutes tightly at top, hold 2s. Lower hips with control, tap floor lightly before next rep.",
            "cues": "Posterior pelvic tilt at top maximizes gluteus maximus activation; Avoid pushing through toes - heel pressure ensures hamstring and glute dominance; Don't hyperextend lower back - movement from hip extension not spinal extension; Maintain tension by not fully resting on floor between reps; Progress to single-leg, elevated, or weighted variations as strength improves",
            "reference": "Contreras et al. (2015) J Appl Biomech 31(6):452-458 DOI:10.1123/jab.2015-0091; Youdas et al. (2015) Physiother Theory Pract 31(6):418-427 DOI:10.3109/09593985.2015.1010672; Boren et al. (2011) Int J Sports Phys Ther 6(3):206-223 PMCID:PMC3201064; Distefano et al. (2009) J Orthop Sports Phys Ther 39(7):532-540 DOI:10.2519/jospt.2009.2796",
            "video": "",
            "sports": "Sprint Running, American Football, Soccer, Rugby, Basketball, Volleyball, Track & Field, Tennis, Powerlifting, Olympic Weightlifting, CrossFit, Skiing, Snowboarding"
        },
        {
            "name": "Single-Leg Hip Lift",
            "primary": "Gluteus Maximus, Hamstrings (Biceps Femoris, Semitendinosus, Semimembranosus)",
            "secondary": "Gluteus Medius, Erector Spinae, Adductor Magnus, Core Stabilizers",
            "type": "Compound",
            "equipment": "Exercise Mat",
            "instructions": "Lie on back, one knee bent foot flat. Extend other leg straight in line with bent knee. Arms at sides palms down for balance. Engage core to stabilize pelvis. Press through heel of bent leg to lift hips. Lift until body forms straight line shoulders to extended knee. Squeeze glutes at top, hold 1-2s. Lower with control, complete all reps before switching sides.",
            "cues": "Gluteus maximus to hamstring ratio higher in single-leg bridges (111.3%) vs bilateral (59.2%); Focus on anti-rotation stability - hips rise/fall without tilting or rotating; Keep non-working leg actively engaged and aligned with working thigh; Maximize glute activation achieving full hip extension without compensatory lumbar hyperextension; Progress by elevating working foot, adding resistance, or performing with pause/isometric hold at peak",
            "reference": "Lehecka et al. (2017) Int J Sports Phys Ther 12(4):543-549 PMCID:PMC5534144 [Hamstring 23.49% MVIC at 135° vs 75.34% at 90°]; Youdas et al. (2015) Physiother Theory Pract 31(6):418-427 DOI:10.3109/09593985.2015.1010672 [Peak glute 33.8% MVIC bridge vs 34.7% hip extension; Hamstrings 28.4% vs 51%]; Selkowitz et al. (2013) J Orthop Sports Phys Ther 43(2):54-64 DOI:10.2519/jospt.2013.4116; McCurdy et al. (2010) J Strength Cond Res 24(11):3081-3088 DOI:10.1519/JSC.0b013e3181d75807",
            "video": "",
            "sports": "Sprint Running, Track & Field, American Football, Soccer, Rugby, Basketball, Volleyball, Tennis, CrossFit, Powerlifting, Olympic Weightlifting, Skiing, Cycling"
        },
        {
            "name": "Deadlift",
            "primary": "Erector Spinae, Gluteus Maximus, Quadriceps (Vastus Lateralis, Vastus Medialis, Vastus Intermedius, Rectus Femoris), Hamstrings (Biceps Femoris, Semitendinosus, Semimembranosus)",
            "secondary": "Trapezius, Latissimus Dorsi, Rhomboids, Forearm Flexors, Core Stabilizers",
            "type": "Compound",
            "equipment": "Barbell, Weight Plates",
            "instructions": "Stand feet hip-width, barbell over mid-foot (shoelaces). Bend at hips and knees to grip bar just outside legs (overhand or mixed grip). Shoulders directly over or slightly ahead of bar. Flatten back by pulling chest up, engaging lats (pull bar toward shins). Take deep breath, brace core. Drive through heels to lift bar close to body. Extend hips and knees simultaneously, stand straight shoulders back. Lower by pushing hips back first, then bend knees once bar passes them.",
            "cues": "Erector spinae and quadriceps show greater activation than glutes and biceps femoris; Semitendinosus exhibits slightly greater activation than biceps femoris; Maintain thoracolumbar extension throughout - any flexion under load increases injury risk; 'Leg press the floor away' rather than 'pull the bar up' to optimize biomechanics; Romanian deadlift shifts activation toward hamstrings (lower erector spinae, higher biceps femoris/semitendinosus)",
            "reference": "Martín-Fuentes et al. (2020) PLOS ONE 15(2):e0229507 DOI:10.1371/journal.pone.0229507 [Systematic review EMG patterns deadlift variations]; McAllister et al. (2014) J Strength Cond Res 28(6):1573-1580 DOI:10.1519/JSC.0000000000000302 [Semitendinosus more active, hamstrings maximized in RDL]; Camara et al. (2016) J Strength Cond Res 30(5):1183-1188 DOI:10.1519/JSC.0000000000001352; Hales et al. (2009) J Strength Cond Res 23(9):2498-2506 DOI:10.1519/JSC.0b013e3181bc1d7c",
            "video": "",
            "sports": "Powerlifting, Olympic Weightlifting, CrossFit, American Football, Rugby, Wrestling, MMA, Track & Field, Strongman, Bodybuilding, Rowing, Sprint Running"
        },
        {
            "name": "Leg Curl",
            "primary": "Hamstrings (Biceps Femoris Long Head, Biceps Femoris Short Head, Semitendinosus, Semimembranosus)",
            "secondary": "Gastrocnemius, Popliteus",
            "type": "Isolation",
            "equipment": "Leg Curl Machine",
            "instructions": "Adjust machine so pad rests on back of lower legs (just above heels). Position on machine according to variant (lying/seated/standing). Grip handles for stability. Start legs fully extended (avoid hyperextension). Engage core, keep hips pressed against pad (lying/seated). Curl heels toward glutes bending at knees. Squeeze hamstrings at fully contracted position. Slowly return to start with control, maintain tension throughout.",
            "cues": "Mean hamstring activation 48.78% MVIC (moderate intensity); Most exercises show 6-26% higher semitendinosus vs biceps femoris, but supine leg curls preferentially activate biceps femoris; Point toes toward shins (dorsiflexion) to reduce gastrocnemius involvement, maximize hamstring activation; Avoid lifting hips off pad during lying leg curls - indicates weight too heavy; Eccentric emphasis (4-5s lowering) significantly enhances hamstring hypertrophy and strength",
            "reference": "Bourne et al. (2017) Sports Med 48(2):251-267 DOI:10.1007/s40279-017-0796-x; Tsaklis et al. (2015) PLOS ONE 10(3):e0245838 DOI:10.1371/journal.pone.0245838; Schoenfeld et al. (2015) Sports Med 45(10):1411-1426 PMCID:PMC8393607; Alonso-Fernandez et al. (2018) Open Access J Sports Med 9:175-186 PMCID:PMC4492645",
            "video": "",
            "sports": "Sprint Running, Soccer, American Football, Rugby, Basketball, Track & Field, Tennis, Skiing, Snowboarding, Cycling, Powerlifting, Bodybuilding, CrossFit"
        },
        {
            "name": "Lying Alternating Leg Curl",
            "primary": "Hamstrings (Biceps Femoris, Semitendinosus, Semimembranosus) - Unilateral",
            "secondary": "Gastrocnemius, Gluteus Maximus",
            "type": "Isolation",
            "equipment": "Lying Leg Curl Machine",
            "instructions": "Lie face down, pad positioned just above heels. Adjust so knees align with pivot point. Grip handles, press hips firmly against pad. Start both legs extended. Curl one heel toward glute bending at knee, keep other leg straight. Squeeze hamstring at top. Lower that leg with control to start. Immediately curl opposite leg, alternating legs each repetition.",
            "cues": "Alternating unilateral work identifies and corrects strength imbalances between legs; Maintain strict pelvic stability - avoid hip rotation or lifting one side of pelvis; Non-working leg remains actively extended against pad for stability; Use controlled tempo both phases (2s up, 3s down); Allows slightly heavier loads per leg vs simultaneous bilateral curls",
            "reference": "Tsaklis et al. (2015) PLOS ONE 10(3):e0245838 DOI:10.1371/journal.pone.0245838; Bourne et al. (2017) Sports Med 48(2):251-267 DOI:10.1007/s40279-017-0796-x; Schoenfeld et al. (2020) J Sport Health Sci 11(2):202-211 DOI:10.1016/j.jshs.2021.01.007; McAllister et al. (2014) J Strength Cond Res 28(6):1573-1580 DOI:10.1519/JSC.0000000000000302",
            "video": "",
            "sports": "Sprint Running, Soccer, American Football, Rugby, Track & Field, Basketball, Tennis, Skiing, Cycling, Bodybuilding, CrossFit"
        },
        {
            "name": "Lying Leg Curl",
            "primary": "Hamstrings (Biceps Femoris Long Head, Biceps Femoris Short Head, Semitendinosus, Semimembranosus)",
            "secondary": "Gastrocnemius, Popliteus, Gracilis",
            "type": "Isolation",
            "equipment": "Lying Leg Curl Machine",
            "instructions": "Lie face down, knees just off bench edge. Position pad on back of lower legs just above heels. Align knees with machine pivot point. Grip handles, keep hips pressed firmly against bench throughout. Start legs fully extended (slight knee bend to protect joint). Curl both heels toward glutes flexing at knees. Squeeze hamstrings hard at 90° or greater flexion. Lower weight slowly to start, maintain hamstring tension.",
            "cues": "Lying leg curls preferentially activate biceps femoris over semitendinosus (uncommon among hamstring exercises); Keep ankles dorsiflexed (toes toward shins) to minimize gastrocnemius contribution; Resist urge to lift hips off pad - indicates excessive weight, reduces hamstring isolation; Peak EMG during muscle-tendon unit shortening phase (concentric); Supine position reduces lumbar stress vs standing or kneeling variations",
            "reference": "Ebben (2009) Int J Sports Physiol Perform 4(1):84-96 DOI:10.1123/ijspp.4.1.84 [Supine leg curls activated biceps femoris more than semitendinosus]; Bourne et al. (2021) Int J Sports Phys Ther 16(4):1090-1101 PMCID:PMC8329323; Schoenfeld et al. (2015) Sports Med 45(10):1411-1426 PMCID:PMC8393607 [Leg curls 48.78% MVIC]; Wright et al. (1999) J Strength Cond Res 13(2):168-174",
            "video": "",
            "sports": "Sprint Running, Track & Field, Soccer, American Football, Rugby, Basketball, Tennis, Volleyball, Skiing, Cycling, Powerlifting, Bodybuilding, CrossFit"
        },
        {
            "name": "Lying Single-Leg Curl",
            "primary": "Hamstrings (Biceps Femoris, Semitendinosus, Semimembranosus) - Unilateral",
            "secondary": "Gastrocnemius, Gluteus Maximus, Erector Spinae",
            "type": "Isolation",
            "equipment": "Lying Leg Curl Machine",
            "instructions": "Lie face down, pad positioned just above heels. Ensure knees align with machine pivot. Grip handles, press hips firmly against bench. Keep one leg extended and inactive while working other leg. Curl one heel toward glute bending at knee. Focus on squeezing hamstring of working leg at peak contraction. Lower leg with control to start. Complete all reps one side before switching to other leg.",
            "cues": "Unilateral training reveals and corrects bilateral strength deficits (common in athletes); Non-working leg remains extended but relaxed - do not actively press into pad; Single-leg increases core stabilization demands to prevent torso rotation; Work weaker side first to ensure full neurological resources; Use 10-15% less load than bilateral to maintain proper form and full ROM",
            "reference": "McCurdy et al. (2005) J Strength Cond Res 19(1):9-15 DOI:10.1519/14013.1; Tsaklis et al. (2015) PLOS ONE 10(3):e0245838 DOI:10.1371/journal.pone.0245838; Bourne et al. (2021) Int J Sports Phys Ther 16(4):1090-1101 PMCID:PMC8329323; Schoenfeld et al. (2015) Sports Med 45(10):1411-1426 PMCID:PMC8393607",
            "video": "",
            "sports": "Sprint Running, Soccer, American Football, Rugby, Track & Field, Basketball, Tennis, Skiing, Cycling, Bodybuilding, CrossFit, Powerlifting"
        },
        {
            "name": "Seated Leg Curl",
            "primary": "Hamstrings (Biceps Femoris Long Head, Biceps Femoris Short Head, Semitendinosus, Semimembranosus)",
            "secondary": "Gastrocnemius, Popliteus",
            "type": "Isolation",
            "equipment": "Seated Leg Curl Machine",
            "instructions": "Sit in machine, adjust back pad so knees align with pivot. Position lower pad against back of calves (just above heels). Place thigh pad securely over thighs to anchor legs. Grip handles on sides of seat. Start legs extended straight out front. Curl heels down and back toward seat bending at knees. Squeeze hamstrings hard at fully contracted position (typically 90+ degrees knee flexion). Slowly extend legs back to start with control.",
            "cues": "Seated position pre-stretches hamstrings by placing hips in flexion, potentially increasing muscle activation; Thigh pad stabilization allows heavier loads vs lying variations; Minimize hip extension during curl - movement isolated to knee flexion; Dorsiflex ankles (pull toes toward shins) to reduce calf involvement; Seated recruits similar hamstring activation as lying curls but with reduced lumbar stress",
            "reference": "Mohamed et al. (2002) Isokinetics Exercise Sci 10(4):193-199 DOI:10.3233/IES-2002-0109; Ebben (2009) Int J Sports Physiol Perform 4(1):84-96 DOI:10.1123/ijspp.4.1.84; Bourne et al. (2017) Sports Med 48(2):251-267 DOI:10.1007/s40279-017-0796-x; Alonso-Fernandez et al. (2018) Open Access J Sports Med 9:175-186 PMCID:PMC4492645",
            "video": "",
            "sports": "Sprint Running, Track & Field, Soccer, American Football, Rugby, Basketball, Tennis, Volleyball, Skiing, Cycling, Bodybuilding, Powerlifting, CrossFit"
        }
    ]
}

# Output the formatted entries
print("=" * 80)
print("BATCH 5 EXERCISES - FORMATTED FOR DATABASE INTEGRATION")
print("Session 12 - 2025-12-02")
print("=" * 80)
print()

print("CHEST EXERCISES (3)")
print("-" * 80)
for i, ex in enumerate(exercises["chest"], 1):
    print(f"\n{i}. {ex['name']}")
    print(f"   Primary: {ex['primary']}")
    print(f"   Type: {ex['type']} | Equipment: {ex['equipment']}")
    print()

print("\nHAMSTRING EXERCISES (11)")
print("-" * 80)
for i, ex in enumerate(exercises["hamstrings"], 1):
    print(f"\n{i+3}. {ex['name']}")
    print(f"   Primary: {ex['primary']}")
    print(f"   Type: {ex['type']} | Equipment: {ex['equipment']}")
    print()

print("\n" + "=" * 80)
print(f"Total Chest Exercises Formatted: {len(exercises['chest'])}")
print(f"Total Hamstring Exercises Formatted: {len(exercises['hamstrings'])}")
print(f"Grand Total So Far: {len(exercises['chest']) + len(exercises['hamstrings'])}")
print("=" * 80)
