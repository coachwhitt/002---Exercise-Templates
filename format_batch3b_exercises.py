#!/usr/bin/env python3
"""
Format Batch 3b exercises from research file into database table format.
Extracts 10 calf exercises + 9 chest exercises = 19 total.
"""

# CALF EXERCISES (10 total)
calf_exercises = [
    {
        "name": "Barbell Calf Raise",
        "primary": "Gastrocnemius (medial head), Gastrocnemius (lateral head)",
        "secondary": "Soleus, Core stabilizers (erector spinae, rectus abdominis, obliques)",
        "type": "Isolation",
        "equipment": "Barbell, Raised Platform",
        "level": "Intermediate",
        "region": "Lower",
        "movement": "Push",
        "modality": "Free Weight",
        "instructions": "1. Position barbell on upper back in power rack 2. Stand on raised platform with balls of feet, heels hanging off 3. Lower heels below platform for deep stretch 4. Push through balls of feet to maximum height 5. Squeeze calves at peak for 1-2 seconds 6. Lower with control to stretched position 7. Maintain straight knees throughout movement",
        "cues": "1. Keep knees fully extended—any flexion shifts work to soleus 2. Full ROM: minimum 4-inch stretch below, 3+ inches above 3. Vary tempo: explosive concentric for power, slow for hypertrophy 4. Foot variation: toes forward (balanced), outward (medial head), inward (lateral head) 5. Progress to 1.5-2x bodyweight for advanced development",
        "reference": "Nunes JP et al. (2020). Different effects of seated and standing calf raise exercises. J Strength Cond Res 34(12) | Bordoni B & Varacallo M (2023). Gastrocnemius Muscle Anatomy. StatPearls | Gollnick PD et al. (1974). Fiber composition in skeletal muscle. J Appl Physiol 37(2):241-247",
        "sports": "Track & Field, Basketball, Volleyball, Soccer, American Football, Tennis, Boxing, Running"
    },
    {
        "name": "Calf Press",
        "primary": "Gastrocnemius (medial head), Gastrocnemius (lateral head)",
        "secondary": "Soleus, Quadriceps (isometric stabilization)",
        "type": "Isolation",
        "equipment": "Leg Press Machine",
        "level": "Beginner",
        "region": "Lower",
        "movement": "Push",
        "modality": "Machine",
        "instructions": "1. Sit in leg press machine with appropriate weight 2. Place balls of feet on bottom edge of footplate, heels hanging off 3. Extend legs fully, keeping knees straight 4. Release safety locks 5. Flex ankles to let footplate move toward you for stretch 6. Press through balls of feet to extend ankles maximally 7. Hold peak contraction 1-2 seconds, return to stretch",
        "cues": "1. Locked knees—no flexion or quadriceps engagement 2. Machine allows 3-4x bodyweight for advanced hypertrophy 3. Use stretch reflex: pause briefly at bottom then explode 4. Single-leg variation: use 50-60% bilateral weight per leg 5. High frequency: 12-20 sets/week across 3-4 sessions optimal",
        "reference": "Nunes JP et al. (2020). Seated vs standing calf raises. J Strength Cond Res 34(12) | Bordoni B & Varacallo M (2023). Gastrocnemius Muscle Anatomy. StatPearls | Schoenfeld BJ et al. (2015). Volume-equated resistance training. J Strength Cond Res 29(10):2909-2918",
        "sports": "Basketball, Track & Field, Volleyball, Soccer, American Football, Rugby, Cycling, Dancing"
    },
    {
        "name": "Calf Raise - Seated",
        "primary": "Gastrocnemius (medial head - reduced), Gastrocnemius (lateral head - reduced)",
        "secondary": "Soleus (NOTE: Actually PRIMARY due to knee flexion placing gastrocnemius in active insufficiency)",
        "type": "Isolation",
        "equipment": "Bench, Dumbbells or Weight Plates, Raised Platform",
        "level": "Beginner",
        "region": "Lower",
        "movement": "Push",
        "modality": "Free Weight",
        "instructions": "1. Sit on bench with feet flat on floor 2. Place platform under balls of feet 3. Position weights on thighs just above knees 4. Drop heels to floor level for starting stretch 5. Push through balls of feet to lift heels maximally 6. Squeeze calves at peak for 1-2 seconds 7. Lower heels with control, maintain 90° knee angle",
        "cues": "1. 90° knee flexion isolates soleus via gastrocnemius active insufficiency 2. Soleus is Type I slow-twitch: use 15-30 reps, longer TUT vs heavy loads 3. Full ROM: 2-3 inch stretch below, 3+ inches above platform 4. Pause reps: hold 3-5 seconds at top for metabolic stress 5. Program 1:1 ratio standing to seated for balanced triceps surae development",
        "reference": "Nunes JP et al. (2020). Seated vs standing calf raises. J Strength Cond Res 34(12) | Avery DM & Tan JM (2023). Soleus Muscle Anatomy. StatPearls | Remaud A et al. (2009). Knee-flexion angle effects. Gait & Posture 30(2):205-209",
        "sports": "Running, Cycling, Soccer, Basketball, Hiking, Dance, Swimming, Walking/Rucking"
    },
    {
        "name": "Calf Raise - Standing",
        "primary": "Gastrocnemius (medial head), Gastrocnemius (lateral head)",
        "secondary": "Soleus, Core stabilizers (erector spinae, rectus abdominis, obliques)",
        "type": "Isolation",
        "equipment": "Raised Platform or Step (bodyweight or add dumbbells)",
        "level": "Beginner",
        "region": "Lower",
        "movement": "Push",
        "modality": "Bodyweight",
        "instructions": "1. Stand on raised platform with balls of feet, heels hanging off 2. Feet hip-width apart, toes forward or slightly outward 3. Hold wall or support for balance if needed 4. Lower heels below platform level for deep stretch 5. Push through balls of feet to rise onto tiptoes maximally 6. Squeeze calves at top for 1-2 seconds 7. Lower with control to stretched position",
        "cues": "1. Perfect beginner exercise: master form before adding external load 2. Progress to single-leg variation for 2x bodyweight resistance per leg 3. Add dumbbells when 3x15 reps too easy 4. Minimal balance requirement compared to free weight barbell version 5. Daily frequency possible due to bodyweight loading",
        "reference": "Nunes JP et al. (2020). Standing vs seated calf raises. J Strength Cond Res 34(12) | Bordoni B & Varacallo M (2023). Gastrocnemius Muscle Anatomy. StatPearls | Schoenfeld BJ (2010). Muscle hypertrophy mechanisms. J Strength Cond Res 24(10):2857-2872",
        "sports": "Basketball, Track & Field, Volleyball, Soccer, Running, Tennis, Boxing, General Fitness"
    },
    {
        "name": "Dumbbell Calf Raise",
        "primary": "Gastrocnemius (medial head), Gastrocnemius (lateral head)",
        "secondary": "Soleus, Core stabilizers, Grip strength (forearms)",
        "type": "Isolation",
        "equipment": "Dumbbells, Raised Platform",
        "level": "Beginner",
        "region": "Lower",
        "movement": "Push",
        "modality": "Free Weight",
        "instructions": "1. Hold dumbbells at sides with neutral grip 2. Stand on raised platform with balls of feet, heels hanging off 3. Feet hip-width apart, maintain upright posture 4. Lower heels below platform for deep calf stretch 5. Push through balls of feet to rise onto tiptoes 6. Squeeze calves hard at top for 1-2 seconds 7. Lower with control to starting position",
        "cues": "1. Dumbbells easier to balance than barbell but limited by grip strength 2. Use lifting straps if grip fails before calf fatigue 3. Perfect for home gym training without machines 4. Natural arm position reduces core stability demands vs barbell 5. Progress to heavier dumbbells or single-leg variation",
        "reference": "Bordoni B & Varacallo M (2023). Gastrocnemius Muscle Anatomy. StatPearls | Nunes JP et al. (2020). Calf raise variations. J Strength Cond Res 34(12) | Schoenfeld BJ (2010). Hypertrophy mechanisms. J Strength Cond Res 24(10):2857-2872",
        "sports": "Basketball, Track & Field, Soccer, Running, Tennis, Volleyball, General Fitness"
    },
    {
        "name": "Single-Leg Calf Press",
        "primary": "Gastrocnemius (medial head), Gastrocnemius (lateral head)",
        "secondary": "Soleus, Quadriceps (isometric stabilization)",
        "type": "Isolation",
        "equipment": "Leg Press Machine",
        "level": "Intermediate",
        "region": "Lower",
        "movement": "Push",
        "modality": "Machine",
        "instructions": "1. Sit in leg press machine with moderate weight (50-60% bilateral load) 2. Place ball of ONE foot on bottom edge of footplate, heel off 3. Other leg rests on floor or bent up off footplate 4. Extend working leg fully, maintain straight knee 5. Flex ankle to let footplate move toward you for stretch 6. Press through ball of foot to extend ankle maximally 7. Hold peak contraction, return to stretch, repeat, then switch legs",
        "cues": "1. Identifies and corrects bilateral strength imbalances 2. Addresses weaker leg first to prevent favoring stronger side 3. Double volume: perform same reps per leg as bilateral sets 4. Enhanced mind-muscle connection with unilateral focus 5. Targets medial/lateral head imbalances with foot angle variation",
        "reference": "Nunes JP et al. (2020). Calf raise muscle activation. J Strength Cond Res 34(12) | Bordoni B & Varacallo M (2023). Gastrocnemius Anatomy. StatPearls | Schoenfeld BJ et al. (2015). Volume-equated training. J Strength Cond Res 29(10):2909-2918",
        "sports": "Basketball, Track & Field, Soccer, Running, Tennis, Volleyball, American Football"
    },
    {
        "name": "Single-Leg Dumbbell Calf Raise",
        "primary": "Gastrocnemius (medial head), Gastrocnemius (lateral head)",
        "secondary": "Soleus, Core stabilizers (significantly increased for balance), Grip strength",
        "type": "Isolation",
        "equipment": "Dumbbell, Raised Platform",
        "level": "Intermediate",
        "region": "Lower",
        "movement": "Push",
        "modality": "Free Weight",
        "instructions": "1. Hold dumbbell in one hand at side 2. Stand on raised platform on same-side leg, other leg bent behind you 3. Use free hand on wall or support for balance 4. Lower heel below platform for deep stretch 5. Push through ball of foot to rise onto tiptoe 6. Squeeze calf hard at top for 1-2 seconds 7. Lower with control, complete set, then switch legs",
        "cues": "1. Doubles bodyweight resistance vs bilateral bodyweight calf raise 2. Enhanced balance requirement increases core and stabilizer activation 3. Perfect progression from bilateral bodyweight calf raises 4. Hold dumbbell on same side as working leg for natural balance 5. Address weaker leg first, match reps with stronger leg",
        "reference": "Bordoni B & Varacallo M (2023). Gastrocnemius Muscle Anatomy. StatPearls | Nunes JP et al. (2020). Standing calf raises. J Strength Cond Res 34(12) | Schoenfeld BJ (2010). Muscle hypertrophy. J Strength Cond Res 24(10):2857-2872",
        "sports": "Basketball, Running, Track & Field, Soccer, Tennis, Volleyball, Boxing"
    },
    {
        "name": "Smith Machine Calf Raise",
        "primary": "Gastrocnemius (medial head), Gastrocnemius (lateral head)",
        "secondary": "Soleus, Core stabilizers (reduced vs free weight barbell)",
        "type": "Isolation",
        "equipment": "Smith Machine, Raised Platform",
        "level": "Beginner",
        "region": "Lower",
        "movement": "Push",
        "modality": "Machine",
        "instructions": "1. Position Smith machine bar at upper back height 2. Load appropriate weight, stand on platform under bar 3. Position bar across upper back, balls of feet on platform edge 4. Unrack bar and straighten body, heels hanging off platform 5. Lower heels below platform for deep calf stretch 6. Push through balls of feet to rise onto tiptoes maximally 7. Squeeze calves at top, lower with control to stretch",
        "cues": "1. Fixed vertical path reduces balance demands vs free weight barbell 2. Allows focus purely on calf contraction without stabilization 3. Safer for heavy loads—can rerack easily at any point 4. Linear bar path may not suit all body mechanics (slight forward lean natural) 5. Great beginner alternative before progressing to free weight barbell",
        "reference": "Bordoni B & Varacallo M (2023). Gastrocnemius Muscle Anatomy. StatPearls | Nunes JP et al. (2020). Standing calf raises. J Strength Cond Res 34(12) | Schick EE et al. (2010). Smith machine vs free weight. J Strength Cond Res 24(3):779-784",
        "sports": "Basketball, Track & Field, Volleyball, Soccer, American Football, Running, Boxing"
    },
    {
        "name": "Seated Calf Raise",
        "primary": "Soleus",
        "secondary": "Gastrocnemius (medial head - minimal), Gastrocnemius (lateral head - minimal)",
        "type": "Isolation",
        "equipment": "Seated Calf Raise Machine",
        "level": "Beginner",
        "region": "Lower",
        "movement": "Push",
        "modality": "Machine",
        "instructions": "1. Sit in seated calf raise machine, adjust knee pad height 2. Place balls of feet on footplate, heels hanging off 3. Position knee pad across thighs just above knees 4. Release safety lever, allow heels to drop below footplate 5. Push through balls of feet to raise heels maximally 6. Squeeze calves at peak for 1-2 seconds 7. Lower heels with control to stretched position",
        "cues": "1. Primary soleus exercise due to 90° knee flexion (active insufficiency of gastrocnemius) 2. Soleus Type I fibers: use 15-30 reps, longer TUT, moderate loads 3. Machine provides stable progressive overload superior to free weight seated 4. Essential for complete calf development (pair with standing variations) 5. Pause reps: 3-5 second holds at top maximize metabolic stress",
        "reference": "Avery DM & Tan JM (2023). Soleus Muscle Anatomy. StatPearls | Nunes JP et al. (2020). Seated vs standing calf raises. J Strength Cond Res 34(12) | Remaud A et al. (2009). Knee-flexion angle effects. Gait & Posture 30(2):205-209",
        "sports": "Running, Cycling, Soccer, Basketball, Hiking, Swimming, Walking/Rucking, Dance"
    },
    {
        "name": "Seated Single-Leg Calf Raise",
        "primary": "Soleus",
        "secondary": "Gastrocnemius (medial head - minimal), Gastrocnemius (lateral head - minimal)",
        "type": "Isolation",
        "equipment": "Seated Calf Raise Machine",
        "level": "Intermediate",
        "region": "Lower",
        "movement": "Push",
        "modality": "Machine",
        "instructions": "1. Sit in seated calf raise machine with reduced weight (50-60% bilateral) 2. Place ball of ONE foot on footplate, other foot on floor 3. Position knee pad across working leg thigh 4. Release safety, drop heel below footplate for stretch 5. Push through ball of foot to raise heel maximally 6. Hold peak contraction 1-2 seconds 7. Lower with control, complete set, switch legs",
        "cues": "1. Unilateral soleus training identifies left/right imbalances 2. Critical for runners/cyclists to prevent overuse injuries from compensation 3. Enhanced mind-muscle connection with single-leg focus 4. Double volume approach: same reps per leg as bilateral sets 5. Address weaker leg first, match volume with stronger side",
        "reference": "Avery DM & Tan JM (2023). Soleus Muscle Anatomy. StatPearls | Nunes JP et al. (2020). Seated calf raise variations. J Strength Cond Res 34(12) | Remaud A et al. (2009). Soleus activation. Gait & Posture 30(2):205-209",
        "sports": "Running, Cycling, Soccer, Triathlon, Basketball, Hiking, Swimming"
    }
]

# CHEST EXERCISES (9 total)
chest_exercises = [
    {
        "name": "Alternating Dumbbell Bench Press",
        "primary": "Pectoralis Major (sternal head), Pectoralis Major (clavicular head)",
        "secondary": "Anterior Deltoid, Triceps Brachii, Core stabilizers (anti-rotation)",
        "type": "Compound",
        "equipment": "Dumbbells, Flat Bench",
        "level": "Intermediate",
        "region": "Upper",
        "movement": "Push",
        "modality": "Free Weight",
        "instructions": "1. Lie supine on flat bench holding dumbbells at chest level 2. Position feet flat on floor, maintain neutral spine 3. Start with both dumbbells at chest, elbows at 45° 4. Press ONE dumbbell up to full elbow extension 5. Lower that dumbbell while pressing opposite dumbbell up 6. Continue alternating in controlled rhythm 7. Maintain constant core tension to resist rotation",
        "cues": "1. Massive anti-rotation core demand—transverse abdominis and obliques highly active 2. Unilateral loading identifies left/right chest strength imbalances 3. Time under tension doubled per side vs bilateral pressing 4. Breathing: exhale during press, inhale during lowering of each rep 5. Perfect for athletic programs requiring rotational stability",
        "reference": "Solari F & Burns B (2023). Pectoralis Major Anatomy. StatPearls | Fimland MS et al. (2011). Muscle activity in semi-free-weight vs machine exercises. J Strength Cond Res 25(4):1034-1039 | Schoenfeld BJ (2010). Hypertrophy mechanisms. J Strength Cond Res 24(10):2857-2872",
        "sports": "Baseball, American Football, Rugby, Tennis, Golf, Boxing, Wrestling, MMA"
    },
    {
        "name": "Barbell Bench Press",
        "primary": "Pectoralis Major (sternal head), Pectoralis Major (clavicular head)",
        "secondary": "Anterior Deltoid, Triceps Brachii",
        "type": "Compound",
        "equipment": "Barbell, Flat Bench, Power Rack",
        "level": "Beginner",
        "region": "Upper",
        "movement": "Push",
        "modality": "Free Weight",
        "instructions": "1. Lie supine on flat bench, eyes under barbell 2. Grip bar slightly wider than shoulder-width 3. Unrack bar to arms extended position above chest 4. Lower bar to mid-chest with elbows at 45° 5. Touch chest lightly without bouncing 6. Press bar up to full elbow extension 7. Maintain shoulder blade retraction throughout",
        "cues": "1. King of upper body pressing—highest load potential for pec development 2. Bar path: slight arc from mid-chest to above shoulders at lockout 3. Leg drive: push feet into floor to maintain upper back tightness 4. Balanced sternal and clavicular head activation on flat angle 5. Greater triceps activation than dumbbell press due to fixed hand position",
        "reference": "Solari F & Burns B (2023). Pectoralis Major Anatomy. StatPearls | Rodríguez-Ridao D et al. (2020). Bench inclinations and pectoralis EMG. Int J Environ Res Public Health 17(19):7339 | Schick EE et al. (2010). Smith machine vs free weight. J Strength Cond Res 24(3):779-784",
        "sports": "American Football, Rugby, Wrestling, Powerlifting, Strongman, MMA, Boxing"
    },
    {
        "name": "Chest Press (Machine)",
        "primary": "Pectoralis Major (sternal head), Pectoralis Major (clavicular head)",
        "secondary": "Anterior Deltoid, Triceps Brachii",
        "type": "Compound",
        "equipment": "Chest Press Machine",
        "level": "Beginner",
        "region": "Upper",
        "movement": "Push",
        "modality": "Machine",
        "instructions": "1. Adjust seat height so handles align with mid-chest 2. Sit with back flat against pad, feet on floor 3. Grip handles with neutral or pronated grip 4. Press handles forward to full arm extension 5. Pause briefly at full extension 6. Lower with control to starting position 7. Avoid allowing weight stack to touch between reps",
        "cues": "1. Fixed path eliminates stabilizer recruitment—pure pec isolation 2. Safer for high-rep training to failure without spotter 3. Allows higher loads than dumbbells due to stability 4. Perfect for beginners learning pressing mechanics before free weights 5. Use for drop sets and metabolic stress training",
        "reference": "Solari F & Burns B (2023). Pectoralis Major Anatomy. StatPearls | Fimland MS et al. (2011). Machine vs free weight muscle activity. J Strength Cond Res 25(4):1034-1039 | Schick EE et al. (2010). Machine chest press mechanics. J Strength Cond Res 24(3):779-784",
        "sports": "General Fitness, Bodybuilding, Rehabilitation, Beginner Strength Training"
    },
    {
        "name": "Decline Dumbbell Bench Press",
        "primary": "Pectoralis Major (sternal head - emphasized), Pectoralis Major (clavicular head)",
        "secondary": "Anterior Deltoid (reduced vs flat/incline), Triceps Brachii",
        "type": "Compound",
        "equipment": "Dumbbells, Decline Bench",
        "level": "Intermediate",
        "region": "Upper",
        "movement": "Push",
        "modality": "Free Weight",
        "instructions": "1. Secure feet under leg supports on decline bench 2. Lie back on decline (15-30° angle) holding dumbbells 3. Position dumbbells at chest level, elbows at 45° 4. Press dumbbells up to full extension above lower chest 5. Lower with control allowing stretch below chest level 6. Press back up, optionally bring dumbbells together at top 7. Maintain constant tension on pectorals throughout",
        "cues": "1. Maximal sternal (lower) pectoralis major activation due to decline angle 2. Minimal anterior deltoid involvement compared to flat/incline 3. Dumbbells allow greater ROM than barbell (descend below chest) 4. Adduction at top (bringing DBs together) increases pec contraction 5. Enhanced safety vs decline barbell—drop dumbbells if needed",
        "reference": "Solari F & Burns B (2023). Pectoralis Major Anatomy. StatPearls | Rodríguez-Ridao D et al. (2020). Bench angle effects on pectoralis EMG. Int J Environ Res Public Health 17(19):7339 | Lauver JD et al. (2016). Bench angle muscular activation. Eur J Sport Sci 16(3):309-316",
        "sports": "Bodybuilding, American Football, Rugby, Wrestling, Powerlifting, MMA"
    },
    {
        "name": "Decline Smith Machine Bench Press",
        "primary": "Pectoralis Major (sternal head - emphasized), Pectoralis Major (clavicular head)",
        "secondary": "Anterior Deltoid (reduced), Triceps Brachii",
        "type": "Compound",
        "equipment": "Smith Machine, Decline Bench",
        "level": "Beginner",
        "region": "Upper",
        "movement": "Push",
        "modality": "Machine",
        "instructions": "1. Position decline bench under Smith machine bar 2. Secure feet under leg supports 3. Lie back on decline, position bar above lower chest 4. Unrack bar and lower to lower chest with control 5. Press bar up to full extension 6. Rerack at any point using safety hooks 7. Maintain shoulder blade retraction throughout",
        "cues": "1. Fixed vertical path allows focus on lower pec contraction 2. Safer for training to failure without spotter (rerack anytime) 3. Reduced stabilizer demand vs free weight decline press 4. Great for isolating sternal pectoralis major fibers 5. Linear bar path may not suit all individual biomechanics",
        "reference": "Solari F & Burns B (2023). Pectoralis Major Anatomy. StatPearls | Rodríguez-Ridao D et al. (2020). Bench angle effects. Int J Environ Res Public Health 17(19):7339 | Schick EE et al. (2010). Smith machine vs free weight. J Strength Cond Res 24(3):779-784",
        "sports": "Bodybuilding, General Fitness, Powerlifting Assistance, Rehabilitation"
    },
    {
        "name": "Dumbbell Bench Press",
        "primary": "Pectoralis Major (sternal head), Pectoralis Major (clavicular head)",
        "secondary": "Anterior Deltoid, Triceps Brachii, Stabilizer muscles (rotator cuff)",
        "type": "Compound",
        "equipment": "Dumbbells, Flat Bench",
        "level": "Beginner",
        "region": "Upper",
        "movement": "Push",
        "modality": "Free Weight",
        "instructions": "1. Sit on flat bench holding dumbbells on thighs 2. Lie back while bringing dumbbells to chest level 3. Position feet flat on floor, maintain neutral spine 4. Press dumbbells up to full extension above chest 5. Lower with control, allowing elbows to descend below chest level 6. Press back up, optionally bring dumbbells together at top 7. Maintain shoulder blade retraction throughout",
        "cues": "1. Greater pectoralis activation than barbell due to increased ROM 2. Descend dumbbells below chest level for deep stretch 3. Adduction at top (bringing DBs together) maximizes pec contraction 4. Significantly higher anterior deltoid and stabilizer activation vs barbell 5. Independent arm movement identifies left/right strength imbalances",
        "reference": "Solari F & Burns B (2023). Pectoralis Major Anatomy. StatPearls | Fimland MS et al. (2011). Free weight vs machine muscle activity. J Strength Cond Res 25(4):1034-1039 | Rodríguez-Ridao D et al. (2020). Pectoralis EMG analysis. Int J Environ Res Public Health 17(19):7339",
        "sports": "American Football, Rugby, Wrestling, Baseball, MMA, Bodybuilding, General Fitness"
    },
    {
        "name": "Dumbbell Push-Up",
        "primary": "Pectoralis Major (sternal head), Pectoralis Major (clavicular head)",
        "secondary": "Anterior Deltoid, Triceps Brachii, Core stabilizers (rectus abdominis, obliques), Serratus Anterior",
        "type": "Compound",
        "equipment": "Dumbbells (hexagonal preferred)",
        "level": "Intermediate",
        "region": "Upper",
        "movement": "Push",
        "modality": "Bodyweight",
        "instructions": "1. Place two hexagonal dumbbells on floor shoulder-width apart 2. Grip dumbbell handles in push-up position 3. Body in straight plank: shoulders to ankles in line 4. Lower body by bending elbows to 90° 5. Descend slightly deeper than normal push-up (below hand level) 6. Press back up to full elbow extension 7. Maintain rigid core throughout movement",
        "cues": "1. Elevated hand position increases ROM vs floor push-ups 2. Neutral grip (palms facing) reduces shoulder stress vs pronated 3. Enhanced grip strength and forearm activation from holding dumbbells 4. Unstable surface increases core and stabilizer demand 5. Progress to single-arm variations for anti-rotation core work",
        "reference": "Solari F & Burns B (2023). Pectoralis Major Anatomy. StatPearls | Kim YS et al. (2016). Push-up variations muscle activity. J Phys Ther Sci 28(5):1349-1352 | Schoenfeld BJ (2010). Hypertrophy mechanisms. J Strength Cond Res 24(10):2857-2872",
        "sports": "MMA, Wrestling, Gymnastics, Calisthenics, American Football, Rugby, General Fitness"
    },
    {
        "name": "Elevated Push-Up",
        "primary": "Pectoralis Major (clavicular head - emphasized), Pectoralis Major (sternal head)",
        "secondary": "Anterior Deltoid (increased activation), Triceps Brachii, Core stabilizers",
        "type": "Compound",
        "equipment": "Elevated Surface (bench, box, or platform)",
        "level": "Intermediate",
        "region": "Upper",
        "movement": "Push",
        "modality": "Bodyweight",
        "instructions": "1. Place hands on elevated surface (bench/box) shoulder-width apart 2. Walk feet back to create straight plank position 3. Body angle: feet lower than hands (incline position) 4. Lower chest toward elevated surface by bending elbows 5. Descend until chest nearly touches surface 6. Press back up to full elbow extension 7. Maintain rigid core and neutral spine",
        "cues": "1. Incline angle emphasizes clavicular (upper) pectoralis major 2. Higher elevation = greater upper pec/anterior deltoid activation 3. Regression for beginners: higher surface = easier resistance 4. Progress by lowering surface height until reaching floor push-ups 5. Narrow hand position increases pectoralis and triceps activation",
        "reference": "Solari F & Burns B (2023). Pectoralis Major Anatomy. StatPearls | Kim YS et al. (2016). Push-up angle effects. J Phys Ther Sci 28(5):1349-1352 | Rodríguez-Ridao D et al. (2020). Bench angle and pectoralis activation. Int J Environ Res Public Health 17(19):7339",
        "sports": "General Fitness, Bodyweight Training, Rehabilitation, MMA, Wrestling, Gymnastics"
    },
    {
        "name": "Flat Bench Press",
        "primary": "Pectoralis Major (sternal head), Pectoralis Major (clavicular head)",
        "secondary": "Anterior Deltoid, Triceps Brachii",
        "type": "Compound",
        "equipment": "Barbell, Flat Bench, Power Rack",
        "level": "Beginner",
        "region": "Upper",
        "movement": "Push",
        "modality": "Free Weight",
        "instructions": "1. Lie supine on flat bench with eyes under barbell 2. Grip barbell slightly wider than shoulder-width 3. Unrack bar to arms extended above chest 4. Lower bar to mid-chest with controlled tempo 5. Touch chest lightly, maintain tension 6. Press bar up to full extension 7. Rerack safely with spotter or safety pins",
        "cues": "1. Balanced activation of both sternal and clavicular pectoralis heads 2. Retract and depress shoulder blades before unracking 3. Bar path: slight arc from mid-chest to above shoulders 4. Leg drive: push feet into floor for upper back stability 5. Elbow angle: 45° from torso (not 90° flared out)",
        "reference": "Solari F & Burns B (2023). Pectoralis Major Anatomy. StatPearls | Rodríguez-Ridao D et al. (2020). Bench press EMG analysis. Int J Environ Res Public Health 17(19):7339 | Trebs AA et al. (2010). Chest press angle EMG. J Strength Cond Res 24(7):1925-1930",
        "sports": "Powerlifting, American Football, Rugby, Wrestling, Strongman, MMA, General Strength"
    }
]

# Format exercises for database table
def format_exercise_row(ex):
    """Format exercise dict as database table row."""
    return f"| {ex['name']} | {ex['primary']} | {ex['secondary']} | {ex['type']} | {ex['equipment']} | {ex['level']} | {ex['region']} | {ex['movement']} | {ex['modality']} | {ex['instructions']} | {ex['cues']} | {ex['reference']} | {ex['sports']} | [TBD] | [TBD] | [TBD] |"

# Print CALF EXERCISES
print("CALF EXERCISES (10 total):")
print("=" * 80)
for ex in calf_exercises:
    print(format_exercise_row(ex))
    print()

print("\n" + "=" * 80)
print("\nCHEST EXERCISES (9 total):")
print("=" * 80)
for ex in chest_exercises:
    print(format_exercise_row(ex))
    print()
