#!/usr/bin/env python3
"""
Extract and format 19 missing exercises from research files into database v3 format
"""

# Exercise data extracted from batch_supplementary_6_exercises_research.md
batch_1_exercises = [
    {
        "exercise": "Bicycle Crunches",
        "primary_muscles": "Rectus Abdominis, Obliquus Externus Abdominis",
        "secondary_muscles": "Obliquus Internus Abdominis, Transversus Abdominis, Iliopsoas, Rectus Femoris",
        "type": "Isolation",
        "equipment": "Bodyweight",
        "level": "Beginner",
        "body_region": "Core",
        "movement": "Dynamic",
        "modality": "Bodyweight",
        "functional_groups": "Abdominal_Total; Abdominal_Obliques; Full_Core",
        "steps": "1. Lie supine on mat, lower back pressed to floor, hands behind head with elbows wide 2. Lift feet off ground with knees bent at 90°, shins parallel to floor 3. Draw navel toward spine to activate transversus abdominis 4. Lift shoulder blades 2-3 inches off mat 5. Rotate torso bringing right elbow toward left knee while extending right leg straight at 45° 6. Switch sides bringing left elbow toward right knee while extending left leg 7. Continue alternating for prescribed reps, exhaling during each rotation",
        "key_points": "1. Contralateral rotation mechanics maximize oblique recruitment—external oblique on rotating side contracts with opposite internal oblique 2. Maintain anti-extension stabilization via transversus abdominis to prevent lumbar hyperextension 3. Keep scapulae protracted throughout to minimize neck strain and maximize rectus abdominis activation 4. Conscious gluteal contraction before leg lift reduces excessive erector spinae dominance 5. EMG studies show bicycle crunches produce 248% mean rectus abdominis activity relative to traditional crunch baseline",
        "references": "Escamilla RF et al. (2006). Electromyographic analysis of traditional and nontraditional abdominal exercises: implications for rehabilitation and training. Physical Therapy 86(5):656-671; Youdas JW et al. (2008). EMG analysis of Ab-Slide vs abdominal crunch. J Strength Cond Res 22(6):1939-1946; Vispute SS et al. (2011). Effect of abdominal exercise on abdominal fat. J Strength Cond Res 25(9):2559-2564",
        "sports": "American Football, Rugby, Basketball, Soccer, Tennis, Baseball, Golf, MMA, Boxing, Swimming, Track & Field, Ice Hockey"
    },
    {
        "exercise": "Box Jumps",
        "primary_muscles": "Gluteus Maximus, Vastus Lateralis, Vastus Medialis, Vastus Intermedius, Rectus Femoris",
        "secondary_muscles": "Gastrocnemius, Soleus, Biceps Femoris, Semitendinosus, Semimembranosus, Erector Spinae, Rectus Abdominis, Obliques",
        "type": "Compound",
        "equipment": "Plyometric Box",
        "level": "Intermediate",
        "body_region": "Lower",
        "movement": "Explosive",
        "modality": "Bodyweight",
        "functional_groups": "Legs_Quadriceps; Gluteals; Quads_Hamstrings_Glutes; Full_Body_Movements",
        "steps": "1. Select box height allowing hips above knee level (12-18\" for beginners), stand 6-12\" away 2. Assume athletic stance with feet hip to shoulder-width, toes forward, weight through midfoot 3. Initiate rapid quarter-squat (90-100° knee flexion) with arms swinging backward and downward 4. Explosively extend hips, knees, and ankles simultaneously (triple extension) while swinging arms upward 5. Keep body compact during flight with hips flexed and knees drawn toward chest 6. Land softly on box with both feet simultaneously, feet flat, hips above knees 7. Stand fully upright on box then step down one foot at a time (do not jump down)",
        "key_points": "1. Stretch-shortening cycle optimization requires minimizing ground contact time (<0.2 sec) during countermovement 2. Land with decreased knee/hip flexion and increased knee valgus increases ACL loading—cue \"land like a cat\" 3. Optimal power occurs when hip extension slightly precedes knee extension during takeoff (proximal-to-distal sequencing) 4. Box heights 18-24\" produce similar EMG activation to 30-36\" with significantly reduced landing forces 5. Jump height decreases 10-15% after 10-15 reps with landing mechanics deteriorating—limit sets to 5-10 reps",
        "references": "Pechlivanos I et al. (2024). Effects of plyometric training on vertical jump performance. European J Sport Science 24(5):567-576; Markovic G & Mikulic P (2010). Neuro-musculoskeletal adaptations to plyometric training. Sports Med 40(10):859-895; Welling W et al. (2016). Enhanced retention of drop vertical jump landing technique. Human Movement Science 45:84-95",
        "sports": "Basketball, Volleyball, American Football, Track & Field, Soccer, Rugby, Netball, CrossFit, Parkour, Figure Skating, Beach Volleyball"
    },
    {
        "exercise": "Broad Jumps",
        "primary_muscles": "Gluteus Maximus, Vastus Lateralis, Vastus Medialis, Vastus Intermedius, Rectus Femoris",
        "secondary_muscles": "Gastrocnemius, Soleus, Biceps Femoris, Semitendinosus, Semimembranosus, Erector Spinae, Rectus Abdominis, Triceps Brachii, Deltoideus Anterior",
        "type": "Compound",
        "equipment": "Bodyweight",
        "level": "Beginner",
        "body_region": "Lower",
        "movement": "Explosive",
        "modality": "Bodyweight",
        "functional_groups": "Legs_Quadriceps; Gluteals; Quads_Hamstrings_Glutes; Full_Body_Movements",
        "steps": "1. Stand with feet hip to shoulder-width, toes at starting line, weight through midfoot 2. Begin countermovement by flexing hips, knees, ankles to 90-100° knee flexion, arms swinging backward 3. At bottom position, torso leans forward 30-45° with arms extended behind body 4. Explosively extend hips, knees, ankles simultaneously while driving hips forward with 20-30° takeoff angle 5. Coordinate explosive arm swing forward and upward to shoulder height during takeoff 6. During flight, bring knees toward chest while reaching arms forward 7. Extend legs forward before landing, land heels first with 30-40° knee flexion, swing arms backward",
        "key_points": "1. Horizontal force vector optimization requires 20-30° takeoff angle vs vertical plyometrics which use more upright posture 2. Gluteus maximus is primary force producer with activation exceeding 100% MVIC—athletes with greater glute CSA achieve longer distances 3. Arm swing contributes 10-15% of total distance via momentum transfer—triceps brachii and anterior deltoid most influential 4. Greatest muscle activation in gluteus maximus and biceps femoris during push-off phase, particularly with straddle foot position 5. Landing stability requires eccentric quadriceps/hamstring strength and core anti-extension strength to \"stick\" landing",
        "references": "Zhang Y et al. (2023). Effects of muscle strength on standing long jump based on sEMG. Frontiers in Physiology 14:1246776; Wakai M & Linthorne NP (2005). Optimum take-off angle in standing long jump. Human Movement Science 24(1):81-96; Nagano A et al. (2007). Optimal coordination of maximal-effort horizontal and vertical jump motions. J Biomechanics 40(1):67-75",
        "sports": "Track & Field, American Football, Rugby, Basketball, Soccer, Speed Skating, CrossFit, Parkour, Baseball, Tennis, Volleyball"
    },
    {
        "exercise": "Squat Jumps",
        "primary_muscles": "Gluteus Maximus, Vastus Lateralis, Vastus Medialis, Vastus Intermedius, Rectus Femoris",
        "secondary_muscles": "Gastrocnemius, Soleus, Biceps Femoris, Semitendinosus, Semimembranosus, Erector Spinae, Rectus Abdominis, Multifidus",
        "type": "Compound",
        "equipment": "Bodyweight",
        "level": "Beginner",
        "body_region": "Lower",
        "movement": "Explosive",
        "modality": "Bodyweight",
        "functional_groups": "Legs_Quadriceps; Gluteals; Quads_Hamstrings_Glutes; Full_Body_Movements",
        "steps": "1. Stand with feet hip to shoulder-width, lower into static squat position with 90° knee flexion, hands behind head 2. Hold bottom position completely still for 2-3 seconds to eliminate elastic energy contribution 3. Ensure knees track over toes, weight through midfoot, torso upright with neutral spine, hips level with knees 4. While holding static position, take deep breath and brace core for spinal stability 5. From dead-stop, explosively extend hips, knees, ankles simultaneously with maximal effort 6. Achieve maximal vertical displacement with full triple extension at takeoff, body in tall vertical alignment 7. Land with both feet simultaneously, immediately absorb impact via ankle/knee/hip flexion, return to static squat and hold 2-3 sec",
        "key_points": "1. Concentric-only force production eliminates stretch-shortening cycle—squat jump height typically 10-15% lower than countermovement jump 2. Rate of force development in first 100-200ms is primary predictor of squat jump height, more so than maximal strength 3. Squat jumps demonstrate 10-15% higher vastus lateralis EMG activation vs countermovement jumps due to quadriceps dominance 4. 8-week jump squat training improves Fmax by ~18% and RFD100 by ~25%, with 2-4% improvement in 50m sprint times 5. SJ:CMJ ratio below 0.85 suggests poor eccentric utilization or inadequate reactive strength",
        "references": "Cormie P et al. (2011). Developing maximal neuromuscular power: Part 2 - Training considerations. Sports Medicine 41(2):125-146; McBride JM et al. (2002). Effect of heavy- vs light-load jump squats. J Strength Cond Res 16(1):75-82; Komi PV & Gollhofer A (1997). Stretch reflexes role in force enhancement during SSC exercise. J Applied Biomechanics 13(4):451-460",
        "sports": "Basketball, Volleyball, Track & Field, Alpine Skiing, Speed Skating, American Football, Rugby, Soccer, Figure Skating, Gymnastics, MMA"
    },
    {
        "exercise": "Superman",
        "primary_muscles": "Erector Spinae, Gluteus Maximus, Lumbar Multifidus",
        "secondary_muscles": "Biceps Femoris, Semitendinosus, Semimembranosus, Deltoideus Posterior, Trapezius, Rhomboideus Major, Rhomboideus Minor, Teres Major",
        "type": "Isolation",
        "equipment": "Bodyweight",
        "level": "Beginner",
        "body_region": "Core",
        "movement": "Static Hold",
        "modality": "Bodyweight",
        "functional_groups": "Lower_Back_Erector_Spinae; Gluteals; Full_Core",
        "steps": "1. Lie face-down (prone) on mat with body fully extended, legs hip-width apart, arms overhead with palms down 2. Establish neutral spine by gently engaging core, pelvis remains in contact with mat throughout 3. Simultaneously lift chest, shoulders, and arms off mat by 4-6 inches by squeezing shoulder blades together 4. Simultaneously engage glutes and lift both legs off mat by 4-6 inches via hip extension, knees straight 5. Hold top position with arms and legs elevated forming slight arc, pelvis and lower abdomen maintain mat contact 6. Maintain superman position for 10-30 seconds with continuous muscle tension, shallow breathing if hold exceeds 10 sec 7. Slowly lower arms, chest, and legs simultaneously in controlled manner (2-3 sec descent), rest 5-10 sec",
        "key_points": "1. Lumbar multifidus activation increases progressively: upper extremity only < lower extremity only < combined lift (highest, ~80-95% MVIC) 2. Gluteus maximus delayed activation pattern—consciously cue gluteal contraction before leg lift to optimize sequence and reduce erector spinae dominance 3. Abdominal drawing-in maneuver (ADIM) significantly enhances lumbar stability and increases gluteus maximus activity while decreasing compensatory erector spinae hyperactivity 4. Evidence-based progression: upper extremity only → lower extremity only → alternating arm/leg (bird dog) → full superman 5. Focus on \"lengthen, don't crunch\"—lift chest and legs modestly (4-6\") with emphasis on muscle contraction quality, not height achieved",
        "references": "Kim SY & Kang MH (2018). Comparison of lumbar multifidus thickness during graded superman exercises. J Physical Therapy Science 30(9):1166-1169; Park SY & Yoo WG (2013). Effect of ADIM on lumbar lordosis and EMG during prone hip extension. J Physical Therapy Science 25(2):133-135; Lee CW et al. (2014). Effects of PNF and ball exercise on pain and muscle activity in CLBP patients. J Physical Therapy Science 26(1):93-96",
        "sports": "Swimming, Gymnastics, Figure Skating, Diving, CrossFit, Rowing, Cycling, Track & Field, Wrestling, Rugby, American Football, Rock Climbing"
    },
    {
        "exercise": "Superman Hold",
        "primary_muscles": "Erector Spinae, Lumbar Multifidus, Gluteus Maximus",
        "secondary_muscles": "Biceps Femoris, Semitendinosus, Semimembranosus, Deltoideus Posterior, Trapezius, Rhomboideus Major, Rhomboideus Minor, Infraspinatus, Teres Major, Latissimus Dorsi",
        "type": "Isolation",
        "equipment": "Bodyweight",
        "level": "Intermediate",
        "body_region": "Core",
        "movement": "Static Hold",
        "modality": "Bodyweight",
        "functional_groups": "Lower_Back_Erector_Spinae; Gluteals; Full_Core",
        "steps": "1. Lie face-down on mat in fully extended position, legs hip-width, arms overhead with palms down or thumbs up 2. Before lifting, perform full-body tension check: engage glutes, brace core with gentle abdominal drawing-in, retract shoulder blades 3. In one smooth motion, simultaneously lift chest, arms, and legs off mat by 4-6 inches in even, balanced manner 4. Verify position: shoulder blades squeezed together, arms extended overhead with locked elbows, legs straight with feet together, gluteus maximus maximally contracted, pelvis maintains mat contact 5. Establish shallow rhythmic breathing through nose or mouth while maintaining core tension 6. Maintain superman hold for prescribed duration (20-60 sec intermediate; 60-90+ sec advanced) without sagging 7. At completion, slowly lower arms, chest, legs simultaneously over 2-3 sec, rest prone with complete relaxation 30-60 sec",
        "key_points": "1. Moderate-intensity holds (30-40% MVIC) optimize erector spinae muscle stiffness development without excessive fatigue—aim for 45-90 sec holds 2. Systematic reviews show isometric lumbar extension exercises produce significant pain reduction (ES = -0.633, p = 0.004) and disability improvement in chronic low back pain 3. Sustained isometric nature produces greater type I muscle fiber recruitment vs dynamic variations—ideal for endurance adaptations 4. Superman holds develop core stability (resist unwanted movement) rather than core strength (produce movement)—superior for postural control 5. Progressive overload sequence: duration increase (20→30→45→60→90s) → increased sets (2→3→4) → reduced rest (60→45→30s) → instability → external load",
        "references": "Chen Z et al. (2023). Effect of different isometric trunk extension intensities on muscle stiffness. Frontiers in Physiology 14:1337170; Wong AY et al. (2017). Low back pain in older adults: risk factors and management. Spondyloarthritis Research 8:134-145; Youdas JW et al. (2013). EMG during isometric back extension exercises. Physiotherapy Theory Practice 29(3):184-194",
        "sports": "Swimming, Rowing, Cycling, CrossFit, Gymnastics, Figure Skating, Rock Climbing, Wrestling, Track & Field, Triathlon, Nordic Skiing, American Football"
    }
]

# Exercise data extracted from batch_supplementary_olympic_lifts_7_exercises_research.md
batch_2_exercises = [
    {
        "exercise": "Clean (Power Clean)",
        "primary_muscles": "Gluteus Maximus, Semitendinosus, Biceps Femoris, Vastus Lateralis, Vastus Medialis, Erector Spinae, Trapezius",
        "secondary_muscles": "Gastrocnemius, Soleus, Deltoids, Rhomboids, Rectus Abdominis, Obliques, Multifidus",
        "type": "Compound",
        "equipment": "Barbell",
        "level": "Advanced",
        "body_region": "Full Body",
        "movement": "Explosive",
        "modality": "Free Weight",
        "functional_groups": "Full_Body_Movements; Quads_Hamstrings_Glutes; Lower_Back_Erector_Spinae; Trapezius_and_Rhomboids",
        "steps": "1. Stand with feet hip-width, toes under barbell, squat down with chest up and grip bar with hook grip slightly wider than shoulders 2. Back straight, hips lower than shoulders, shoulders directly over or slightly in front of bar 3. Initiate lift by driving through heels and extending legs, angle of back remains constant, arms straight, bar close to shins 4. As bar passes knees, rebend knees slightly and bring torso more upright (scoop motion loads hamstrings/glutes) 5. Explosively extend hips, knees, ankles (triple extension) like vertical jump, shrug shoulders and pull body under bar 6. As you drop under bar, rotate elbows forward and around bar quickly, receive bar in front squat position on anterior deltoids, elbows high 7. Drive up from squat to full standing position",
        "key_points": "1. Maximize triple extension—second pull generates majority of bar's upward velocity via violent hip extension 2. Bar trajectory must remain close to body throughout—bar path looping away reduces efficiency and power 3. Elbow speed in catch is critical for successful catch—requires significant shoulder mobility and aggressive action 4. Maintain consistent back angle during first pull—hips rising faster than shoulders turns lift into stiff-legged deadlift 5. Hook grip (thumb wrapped around bar, fingers over thumb) prevents bar slipping during high-velocity second pull",
        "references": "Gidday K et al. (2007). Biomechanical analysis of power clean at 70% vs 90% of 1RM. J Strength Cond Res; Sato K et al. (2017). Muscle activation comparison hang power clean vs hang high pull. J Sports Science Medicine 16(4):569-574; Comfort P et al. (2011). Kinematic and kinetic comparison of power clean and hang power clean. J Strength Cond Res 25(11):2986-2993",
        "sports": "Weightlifting, CrossFit, American Football, Basketball, Track & Field, Rugby, Wrestling, MMA, Volleyball, Soccer, Bobsledding"
    },
    {
        "exercise": "Clean and Jerk",
        "primary_muscles": "Gluteus Maximus, Quadriceps, Erector Spinae, Deltoids, Triceps Brachii, Trapezius",
        "secondary_muscles": "Hamstrings, Gastrocnemius, Soleus, Rectus Abdominis, Obliques, Serratus Anterior, Pectoralis Major",
        "type": "Compound",
        "equipment": "Barbell",
        "level": "Advanced",
        "body_region": "Full Body",
        "movement": "Explosive",
        "modality": "Free Weight",
        "functional_groups": "Full_Body_Movements; Quads_Hamstrings_Glutes; Shoulders_Delts_and_Traps; Arms_Triceps",
        "steps": "1. Perform full Clean movement receiving bar in full deep front squat 2. From bottom of squat, drive through heels to stand to fully erect position with bar resting on anterior deltoids 3. With feet hip-width, initiate jerk with shallow controlled dip by bending knees, torso upright, elbows high 4. Explosively drive upward with legs, extending hips and knees to propel barbell off shoulders 5. As bar leaves shoulders, quickly split legs one forward one backward into lunge position, simultaneously press body under bar locking elbows overhead 6. Once stable, bring front foot halfway back, then back foot to meet it, stand with feet together, bar held overhead 7. Carefully lower bar to shoulders then to floor",
        "key_points": "1. Jerk dip should be shallow and straight down—drive must be vertical and powerful using leg power to create upward momentum 2. Split should be long and stable with front shin vertical and back knee slightly bent for solid base of support 3. During jerk drive, head must move back out of bar path then come forward \"through the window\" once bar clears chin 4. Take deep breath and brace core before clean and again before jerk—intra-abdominal pressure crucial for spinal stability 5. Clean and Jerk is rhythmic lift—transition from clean's recovery to jerk's dip should be seamless but controlled",
        "references": "Gourgoulis V et al. (2009). Three-dimensional kinematic analysis of clean and jerk. J Sports Sciences 22(5):459-469; Campos J et al. (2006). Kinematical analysis of clean and jerk. J Strength Cond Res 20(3):508-513; Hadi G et al. (2012). Three-dimensional kinematic analysis of jerk movement. J Strength Cond Res 26(6):1566-1572",
        "sports": "Weightlifting, CrossFit, Strongman, Olympic Sports, Track & Field, American Football, Rugby, Combat Sports, Gymnastics"
    },
    {
        "exercise": "Hang Clean",
        "primary_muscles": "Gluteus Maximus, Hamstrings, Trapezius, Erector Spinae, Deltoids",
        "secondary_muscles": "Quadriceps, Gastrocnemius, Rhomboids, Rectus Abdominis, Obliques",
        "type": "Compound",
        "equipment": "Barbell",
        "level": "Advanced",
        "body_region": "Full Body",
        "movement": "Explosive",
        "modality": "Free Weight",
        "functional_groups": "Full_Body_Movements; Legs_Hamstrings; Gluteals; Trapezius_and_Rhomboids",
        "steps": "1. Deadlift barbell to standing position, hinge at hips and slightly bend knees to lower bar to \"hang\" position just above knees 2. From hang position, explosively extend hips, knees, ankles (triple extension) in powerful vertical jumping motion 3. As body reaches full extension, shrug shoulders powerfully and use momentum to pull body under bar, arms remain straight 4. Quickly rotate elbows forward and around bar, receive bar in front squat position on anterior deltoids 5. Drive up from squat to full standing position 6. Safely lower bar back to hang position or to floor",
        "key_points": "1. Hang position emphasizes eccentric loading of hamstrings and glutes—feel tension build before initiating explosive pull 2. Power comes from hips not arms—arms act as ropes guiding bar upward only after full hip and leg extension 3. Hang clean forces more pronounced violent hip extension to generate vertical momentum since there's no \"first pull\" from floor 4. Maintain balance over mid-foot—pressure shifts from mid-foot toward ball of foot culminating in \"jump\" 5. Varying hang positions (high-hang/hip, mid-thigh, below knee) targets specific phases and develops power from different joint angles",
        "references": "Sato K et al. (2017). Muscle activation comparison hang power clean vs hang high pull. J Sports Science Medicine 16(4):569-574; Comfort P et al. (2011). Kinematic and kinetic comparison of power clean and hang power clean. J Strength Cond Res 25(11):2986-2993; Hori N et al. (2009). Pulling movement in weightlifting exercises. Strength & Conditioning Journal 31(3):22-29",
        "sports": "CrossFit, American Football, Rugby, Track & Field, Basketball, Volleyball, Wrestling, Bobsledding, Soccer, Tennis"
    },
    {
        "exercise": "Snatch (Power Snatch)",
        "primary_muscles": "Gluteus Maximus, Hamstrings, Quadriceps, Erector Spinae, Deltoids, Trapezius",
        "secondary_muscles": "Gastrocnemius, Rhomboids, Serratus Anterior, Triceps Brachii, Rectus Abdominis, Obliques",
        "type": "Compound",
        "equipment": "Barbell",
        "level": "Advanced",
        "body_region": "Full Body",
        "movement": "Explosive",
        "modality": "Free Weight",
        "functional_groups": "Full_Body_Movements; Quads_Hamstrings_Glutes; Shoulders_Delts_and_Traps",
        "steps": "1. Feet hip-width apart, grip barbell with very wide grip (snatch grip), squat down with straight back, chest up, hips low 2. Drive with legs to lift bar from floor, arms straight, bar close to shins, back angle constant until bar passes knees 3. As bar clears knees, explosively extend hips, knees, ankles, bar makes contact with hip crease propelling it vertically 4. After full extension, shrug shoulders and actively pull body under bar, keep bar close to torso 5. Receive bar overhead with arms locked in partial squat, head \"through the window\" slightly forward of arms 6. Stand up from squat to full upright position with bar held securely overhead",
        "key_points": "1. Ideal snatch grip width allows bar to rest in hip crease when standing tall—crucial for maximizing power transfer during second pull 2. Snatch demands exceptional shoulder and thoracic spine mobility and stability to support weight overhead 3. Speed under bar often described as \"jumping and landing in squat\"—speed of transition from extending upwards to pulling downwards determines success 4. Active shoulders in catch position—shoulders pushed up towards ears creating stable \"bone-on-bone\" support structure 5. Do not cut second pull short—ensure full violent triple extension before initiating pull under bar",
        "references": "Gourgoulis V et al. (2000). Three-dimensional kinematic analysis of snatch. J Sports Sciences 18(8):643-652; Harbili E (2012). Gender-based kinematic and kinetic analysis of snatch lift. J Sports Science Medicine 11(1):162-169; Stone MH et al. (2006). Weightlifting: A brief overview. Strength & Conditioning Journal 28(1):50-66",
        "sports": "Weightlifting, CrossFit, Track & Field, Gymnastics, Diving, American Football, Rugby, Volleyball, Martial Arts"
    },
    {
        "exercise": "Thruster",
        "primary_muscles": "Gluteus Maximus, Quadriceps, Deltoids, Triceps Brachii",
        "secondary_muscles": "Hamstrings, Erector Spinae, Rectus Abdominis, Obliques, Trapezius, Serratus Anterior",
        "type": "Compound",
        "equipment": "Barbell",
        "level": "Intermediate",
        "body_region": "Full Body",
        "movement": "Explosive",
        "modality": "Free Weight",
        "functional_groups": "Full_Body_Movements; Legs_Quadriceps; Shoulders_Delts_and_Traps; Arms_Triceps",
        "steps": "1. Hold barbell in front rack position resting on anterior deltoids with loose fingertip grip, feet shoulder-width 2. Initiate movement by sending hips back and down into full front squat, chest up, back straight, elbows high 3. From bottom of squat, explosively drive upwards through heels 4. As you approach top of squat, use powerful momentum from hip extension to begin pressing barbell overhead 5. Continue press until arms fully locked overhead, head moves slightly back then forward \"through the window\" 6. In controlled manner, lower bar back to front rack position and immediately descend into next squat, movement fluid and continuous",
        "key_points": "1. Key is seamless transfer of energy from lower body to upper body—press initiated by hip drive not as separate movement 2. Develop consistent breathing pattern—typically inhale on way down, exhale forcefully as driving weight overhead 3. Keeping elbows high in front squat crucial for maintaining upright torso and solid \"shelf\" for bar 4. Overhead portion is push press driven by leg momentum—avoid turning into strict press which limits weight 5. For very heavy thrusters or fatigued state, slight re-bend of knees as bar comes off shoulders can help re-accelerate it overhead",
        "references": "Gullett JC et al. (2009). Biomechanical comparison of back and front squats. J Strength Cond Res 23(1):284-292; Contreras B et al. (2016). Comparison of gluteus maximus, biceps femoris, vastus lateralis EMG. J Applied Biomechanics 32(1):16-22; Kroell J & Mike J (2017). Comparison of EMG during barbell overhead press and push press. J Strength Cond Res 31(10):2841-2849",
        "sports": "CrossFit, Functional Fitness, MMA, Wrestling, Rugby, American Football, Basketball, Military Training, Strongman"
    },
    {
        "exercise": "Kettlebell Swings",
        "primary_muscles": "Gluteus Maximus, Hamstrings, Erector Spinae",
        "secondary_muscles": "Latissimus Dorsi, Deltoids, Rectus Abdominis, Obliques, Quadriceps, Forearm Flexors",
        "type": "Compound",
        "equipment": "Kettlebell",
        "level": "Intermediate",
        "body_region": "Full Body",
        "movement": "Explosive",
        "modality": "Free Weight",
        "functional_groups": "Gluteals; Legs_Hamstrings; Lower_Back_Erector_Spinae; Full_Body_Movements",
        "steps": "1. Stand with feet slightly wider than shoulder-width, place kettlebell about a foot in front on floor 2. Hinge at hips keeping back flat and grip kettlebell with both hands, \"hike\" kettlebell back between legs high into groin 3. Explosively drive hips forward, squeeze glutes and straighten legs—hip thrust propels kettlebell forward and up 4. Allow kettlebell to float up to chest height, arms relaxed acting like ropes, do not lift with shoulders 5. As kettlebell descends, let gravity do work, guide it back between legs as you hinge at hips for next rep 6. Exhale sharply at top of swing, inhale as you hinge back",
        "key_points": "1. It's a hinge not a squat—primary movement is horizontal projection of hips (hip hinge), knees bend only to facilitate hinge 2. Sharp exhalation at top (\"tssss\" sound) helps brace core and amplify power production 3. Before hike, \"pack\" shoulders down and back to engage lats—keeps kettlebell connected to body and protects lower back 4. At apex of swing, body forms rigid vertical plank with glutes and abs contracted hard—avoid leaning back or hyper-extending spine 5. Don't fight kettlebell on downswing—let it fall and only hinge hips back at last moment maximizing stretch-shortening cycle",
        "references": "McGill SM & Marshall LW (2012). Kettlebell swing, snatch, and bottoms-up carry: muscle activation and low back loads. J Strength Cond Res 26(1):16-27; van den Tillaar R & Andersen V (2019). Core muscle activation single-arm vs two-arm kettlebell swing. J Human Kinetics 69:137-145; Lake JP & Lauder MA (2012). Kettlebell swing training improves maximal and explosive strength. J Strength Cond Res 26(8):2228-2233",
        "sports": "General Conditioning, MMA, Brazilian Jiu-Jitsu, Wrestling, Track & Field, American Football, Rugby, CrossFit, Fat Loss Programs"
    },
    {
        "exercise": "Prowler Push",
        "primary_muscles": "Quadriceps, Gluteus Maximus, Gastrocnemius, Soleus",
        "secondary_muscles": "Hamstrings, Erector Spinae, Rectus Abdominis, Obliques, Deltoids, Pectoralis Major, Triceps Brachii",
        "type": "Compound",
        "equipment": "Prowler / Sled",
        "level": "Beginner",
        "body_region": "Full Body",
        "movement": "Push",
        "modality": "Other",
        "functional_groups": "Legs_Quadriceps; Gluteals; Quads_Hamstrings_Glutes; Full_Body_Movements",
        "steps": "1. Load prowler with appropriate weight, start light to master form 2. Stand behind prowler and grip vertical push-handles, arms bent or nearly straight, lean body forward at 45° 3. Step forward and drive with legs pushing sled, body forms straight line from head to heels 4. Continue driving sled forward with powerful deliberate steps, focus on pushing ground away behind you 5. Maintain posture with core braced and back flat throughout, avoid letting hips sag or back round",
        "key_points": "1. Body angle dictates focus—more upright posture (high-handle) better for speed/acceleration, lower body angle (low-handle) increases leg load for strength 2. Movement is leg drive not arm push—arms and torso act as rigid structure to transfer force from legs into sled 3. For strength use powerful shorter strides, for speed/conditioning use longer more rapid strides with high knee drive 4. Regardless of weight, push with maximal intent and aggression on every step—excellent for concentric power without eccentric loading 5. Find rhythmic breathing pattern matching stride cadence—heavy slow pushes may breathe between steps, lighter faster pushes more rapid breathing",
        "references": "Wyland JP et al. (2015). Acute effects of heavy- and light-load sled pushes on 20-m sprint performance. J Strength Cond Res 29(12):3426-3431; Strohmeyer T & Cronin J (2011). Effects of resisted sled-push training on sprint kinematics. J Strength Cond Res 25(4):969-979; Kavanaugh AA et al. (2019). Acute effects of heavy resisted sled sprinting on subsequent sprint performance. Int J Sports Physiol Performance 14(4):486-492",
        "sports": "American Football, Rugby, Strongman, Sprinting, Field Hockey, Soccer, General Conditioning, MetCon, Team Sports, Firefighter Training"
    }
]

# Exercise data extracted from batch_supplementary_kettlebell_suspension_6_exercises_research.md
batch_3_exercises = [
    {
        "exercise": "Kettlebell Row (Double Arm)",
        "primary_muscles": "Latissimus Dorsi, Rhomboids, Trapezius",
        "secondary_muscles": "Biceps Brachii, Erector Spinae, Hamstrings, Gluteus Maximus, Posterior Deltoids, Forearm Flexors",
        "type": "Compound",
        "equipment": "Two Kettlebells",
        "level": "Intermediate",
        "body_region": "Upper",
        "movement": "Pull",
        "modality": "Free Weight",
        "functional_groups": "Back_Latissimus_Dorsi; Trapezius_and_Rhomboids; Forearms_Grip",
        "steps": "1. Place two kettlebells on floor in front, stand with feet shoulder-width 2. Hinge at hips keeping back straight and chest up until torso nearly parallel to floor, bend knees slightly 3. Grasp kettlebells with neutral grip (palms facing), arms fully extended 4. Engage core and pull shoulder blades down and back 5. Drive elbows up and back, pull kettlebells toward lower ribcage, squeeze back muscles at top 6. In controlled manner, lower kettlebells back to starting position 7. Ensure spine remains neutral throughout exercise",
        "key_points": "1. At peak contraction, actively squeeze shoulder blades together (scapular retraction) to maximize rhomboid and mid-trap engagement 2. Incorporate 1-2 second pause at peak contraction to increase time under tension and enhance mind-muscle connection 3. Bilateral row with heavy loads places high demand on erector spinae to resist spinal flexion—focus on maintaining rigid neutral spine 4. Drive elbows towards ceiling keeping them close to body—emphasizes latissimus dorsi over upper traps and biceps 5. Control descent of kettlebells—slow controlled eccentric phase (3-4 sec) enhances muscle damage and stimulates hypertrophy",
        "references": "Saeterbakken A et al. (2015). Effect of bi- and unilateral rowing exercises on core muscle activation. Int J Sports Med 36(11):901-905; Fenwick CM et al. (2009). Comparison of rowing exercises: trunk muscle activation and lumbar spine motion. J Strength Cond Res 23(5):1408-1417; Lehman GJ (2005). Trunk and hip muscle recruitment patterns during rowing exercises. Dynamic Medicine 4(1):6",
        "sports": "Rowing, Wrestling, Judo, Brazilian Jiu-Jitsu, MMA, Rock Climbing, American Football, Rugby, Strongman, General Strength"
    },
    {
        "exercise": "Kettlebell Row (Single Arm)",
        "primary_muscles": "Latissimus Dorsi, Rhomboids, Trapezius, Obliques",
        "secondary_muscles": "Biceps Brachii, Erector Spinae, Hamstrings, Gluteus Maximus, Posterior Deltoids, Quadratus Lumborum",
        "type": "Compound",
        "equipment": "Kettlebell",
        "level": "Intermediate",
        "body_region": "Upper",
        "movement": "Pull",
        "modality": "Free Weight",
        "functional_groups": "Back_Latissimus_Dorsi; Trapezius_and_Rhomboids; Full_Core",
        "steps": "1. Place kettlebell on floor next to bench, place left knee and left hand firmly on bench, back flat and parallel to floor 2. Right foot planted firmly on floor to side 3. Reach down and grasp kettlebell with right hand using neutral grip, arm fully extended 4. Engage core to prevent torso rotation 5. Drive right elbow up and back, pull kettlebell toward hip, focus on initiating pull with back muscles not arm 6. At top squeeze back and lat muscles 7. Slowly lower kettlebell without letting torso rotate, complete all reps before switching",
        "key_points": "1. Primary challenge is resisting rotational pull on torso—actively engage contralateral obliques to keep hips and shoulders square to floor 2. Unilateral row allows greater range of motion and deeper stretch in lat—allow shoulder blade to protract at bottom for full stretch before retracting 3. For advanced athletic variation, perform row from hip hinge stance without bench support requiring significantly more core, glute, hamstring engagement 4. Initiate pull by retracting scapula before any elbow flexion occurs—ensures latissimus dorsi and rhomboids are prime movers 5. Instead of pulling straight up, think about pulling kettlebell in slight \"J\" or arc-like path back toward hip to maximize lat activation",
        "references": "Saeterbakken A et al. (2015). Effect of bi- and unilateral rowing on core activation. Int J Sports Med 36(11):901-905; Heinecke ML et al. (2010). EMG analysis of unilateral bent-over row and biceps curl. Int J Exercise Science 2(2):Article 46; Brown SH & McGill SM (2008). How inherent stiffness of human torso influences spine loading. Clinical Biomechanics 23(1):1-8",
        "sports": "Tennis, Baseball, Golf, Combat Sports, Swimming, Kayaking, Archery, General Fitness, Postural Correction, Bodybuilding"
    },
    {
        "exercise": "Machine Row",
        "primary_muscles": "Latissimus Dorsi, Rhomboids, Trapezius",
        "secondary_muscles": "Biceps Brachii, Posterior Deltoids, Erector Spinae",
        "type": "Compound",
        "equipment": "Seated Row Machine",
        "level": "Beginner",
        "body_region": "Upper",
        "movement": "Pull",
        "modality": "Machine",
        "functional_groups": "Back_Latissimus_Dorsi; Trapezius_and_Rhomboids",
        "steps": "1. Adjust seat height so chest is firmly against chest pad and arms parallel to floor when reaching for handles 2. Grasp handles with neutral grip (palms facing in), sit tall with back straight and chest up 3. Extend arms fully without rounding shoulders or back, feel slight stretch in back muscles 4. Keeping torso stationary, pull handles towards abdomen, focus on driving elbows back and squeezing shoulder blades together 5. Pause for moment at peak contraction squeezing back muscles hard 6. Slowly and with control, return handles to starting position allowing shoulder blades to protract forward 7. Do not use lower back to rock back and forth—movement isolated to arms and back",
        "key_points": "1. Grip variation for muscle emphasis: wide pronated grip increases upper trapezius/posterior deltoid activation, narrow supinated grip increases biceps/lower lat involvement 2. To better isolate lats, think about \"pulling with elbows\" rather than hands—imagine hands are just hooks 3. Exaggerate scapular movement allowing full protraction at start (shoulder blades gliding forward) and full retraction at end (squeezing together) 4. Utilize tempo training (e.g., 3-1-2-1: 3-sec eccentric, 1-sec pause at stretch, 2-sec concentric, 1-sec pause at peak) to eliminate momentum 5. Internal verbal cues like \"squeeze the shoulder blades\" significantly increase trapezius activation",
        "references": "Muyor JM et al. (2023). Influence of shoulder abduction angle and grip on muscle activation during seated cable row. Sports Biomechanics; Snyder BJ & Leech JR (2009). Voluntary increase in latissimus dorsi activity during lat pull-down. J Strength Cond Res 23(8):2321-2326; Fenwick CM et al. (2009). Comparison of rowing exercises: trunk activation and lumbar spine motion. J Strength Cond Res 23(5):1408-1417",
        "sports": "Bodybuilding, General Health, Physical Therapy, Postural Correction, Beginner Strength Programs, Powerlifting, Swimming, Archery, Rock Climbing"
    },
    {
        "exercise": "Suspended Row",
        "primary_muscles": "Latissimus Dorsi, Rhomboids, Trapezius",
        "secondary_muscles": "Biceps Brachii, Posterior Deltoids, Erector Spinae, Rectus Abdominis, Obliques, Gluteus Maximus",
        "type": "Compound",
        "equipment": "Suspension Trainer",
        "level": "Beginner",
        "body_region": "Upper",
        "movement": "Pull",
        "modality": "Bodyweight",
        "functional_groups": "Back_Latissimus_Dorsi; Trapezius_and_Rhomboids; Full_Core",
        "steps": "1. Secure suspension trainer to high anchor point, adjust straps so handles at chest height 2. Grab handles and lean back until arms fully extended, walk feet forward to increase difficulty (more horizontal = harder) 3. Body forms straight rigid plank from head to heels, engage core and glutes 4. Initiate movement by retracting shoulder blades, then drive elbows back to pull chest towards handles 5. At top squeeze back muscles 6. Lower body back to starting position with control, do not let hips sag 7. Keep core and glutes engaged throughout entire set",
        "key_points": "1. Inherent instability of suspension trainer forces greater activation of stabilizer muscles in shoulder girdle and core vs fixed-equipment rows 2. Primary progression is by decreasing body angle relative to floor—walking feet further forward makes exercise significantly harder 3. Single-leg variation lifting one leg dramatically increases demand on core and hip stability challenging anti-rotation and anti-extension 4. Start with pronated grip and rotate to neutral or supinated at peak contraction to increase biceps involvement and provide unique stimulus 5. To achieve highest difficulty, place feet on elevated surface making body parallel to floor at start",
        "references": "Youdas JW et al. (2018). Comparison of muscle activation traditional vs suspension-device inverted row. J Sport Rehabilitation 27(6):564-570; Calatayud J et al. (2014). Muscle activation during push-ups with suspension training systems. J Sports Science Medicine 13(3):502-510; Snarr RL & Esco MR (2013). EMG comparison of traditional, suspension device, and towel pull-up. J Human Kinetics 39:203-213",
        "sports": "Rock Climbing, Swimming, Gymnastics, Calisthenics, Obstacle Course Racing, General Fitness, Functional Training, Travel Fitness, Postural Correction"
    },
    {
        "exercise": "Suspended Reverse Mountain Climbers",
        "primary_muscles": "Rectus Abdominis, Obliques",
        "secondary_muscles": "Transverse Abdominis, Hip Flexors, Serratus Anterior, Deltoids, Triceps Brachii",
        "type": "Compound",
        "equipment": "Suspension Trainer",
        "level": "Advanced",
        "body_region": "Core",
        "movement": "Dynamic",
        "modality": "Bodyweight",
        "functional_groups": "Abdominal_Total; Abdominal_Obliques; Full_Core",
        "steps": "1. Adjust suspension straps to mid-calf height, sit facing away from anchor and place feet into handles 2. Roll over into plank position with hands directly under shoulders and feet suspended in straps 3. Form straight rigid line from head to suspended heels, brace core and engage glutes 4. While keeping torso still, slowly bring RIGHT knee towards LEFT elbow (reverse and cross-body component) 5. Extend right leg back to starting plank position with control 6. Now bring LEFT knee towards RIGHT elbow 7. Continue alternating legs in slow controlled \"climbing\" motion without letting hips sag or rotate",
        "key_points": "1. Main goal is maintaining neutral spine—core works overtime to prevent lower back arching (anti-extension) and hips twisting (anti-rotation) 2. This is not cardio exercise—perform movement slowly to maximize time under tension for abdominal wall and force greater stabilizer engagement 3. Actively push ground away to keep shoulders stable and scapulae protracted engaging serratus anterior and preventing winging 4. Focus on feeling contraction in lower abs and obliques as you drive knee across body 5. Maintain consistent hip height—common error is hips piking up or sagging down, neutral plank-like position is key",
        "references": "Byrne JM et al. (2014). Effect of suspension training-based core program on high school rowers. J Strength Cond Res 28(11):3041-3047; Calatayud J et al. (2014). Muscle activation during push-ups with suspension training systems. J Sports Science Medicine 13(3):502-510; Snarr RL et al. (2016). EMG comparison of suspension-based and traditional crunch exercises. J Human Kinetics 53:21-29",
        "sports": "Gymnastics, Diving, Climbing, Martial Arts, Dance, Wrestling, Advanced Yoga, Functional Fitness, Core Specialization"
    },
    {
        "exercise": "Conditioning Ball Reverse Jack Knife",
        "primary_muscles": "Rectus Abdominis, Transverse Abdominis, Hip Flexors",
        "secondary_muscles": "Obliques, Serratus Anterior, Quadriceps, Deltoids, Triceps Brachii",
        "type": "Compound",
        "equipment": "Stability Ball",
        "level": "Intermediate",
        "body_region": "Core",
        "movement": "Dynamic",
        "modality": "Bodyweight",
        "functional_groups": "Abdominal_Total; Abdominal_Lower; Full_Core",
        "steps": "1. Start in push-up position with hands on floor shoulder-width apart 2. Place tops of feet and shins on stability ball 3. Body forms straight line from head to heels in plank position, brace core, arms straight 4. Keeping back flat, engage lower abs to pull knees towards chest allowing ball to roll forward 5. With control, extend legs back to starting plank position 6. For advanced pike variation: from plank position, engage abs to lift hips high towards ceiling keeping legs as straight as possible, ball rolls towards feet 7. Slowly lower hips back down to starting plank position",
        "key_points": "1. Pike vs knee tuck: knee tuck (jack knife) primarily targets lower rectus abdominis and hip flexors, pike (straight legs, hips high) increases demand on entire rectus abdominis and requires greater shoulder stability and hamstring flexibility 2. Perform movement slowly and deliberately—avoid using momentum to swing hips or knees, work comes from conscious abdominal contraction 3. Lowering phase (extending back to plank) just as important as concentric phase—control return to plank to maximize muscle engagement and prevent lower back strain 4. Keep shoulders pushed away from ears and directly over wrists—don't let them collapse or shift too far forward or back 5. In knee tuck focus on keeping back flat, in pike spine will naturally flex but movement driven from abs lifting hips not from rounding back",
        "references": "Escamilla RF et al. (2010). Core muscle activation during Swiss ball and traditional abdominal exercises. J Orthopaedic Sports Physical Therapy 40(5):265-276; Stevens VK et al. (2007). EMG activity of trunk and hip muscles during stabilization exercises on and off Swiss ball. J Electromyography Kinesiology 17(1):77-83; Vera-Garcia FJ et al. (2000). Abdominal muscle response during curl-ups on stable and labile surfaces. Physical Therapy 80(6):564-569",
        "sports": "Gymnastics, Diving, Swimming, Dance, Acrobatics, Calisthenics, Advanced Core Training, CrossFit, Surfing, Snowboarding"
    }
]

# Combine all exercises
all_exercises = batch_1_exercises + batch_2_exercises + batch_3_exercises

# Generate markdown table rows
def format_exercise_row(ex):
    """Format a single exercise as a markdown table row"""
    return f"| {ex['exercise']} | {ex['primary_muscles']} | {ex['secondary_muscles']} | {ex['type']} | {ex['equipment']} | {ex['level']} | {ex['body_region']} | {ex['movement']} | {ex['modality']} | {ex['functional_groups']} | {ex['steps']} | {ex['key_points']} | {ex['references']} | {ex['sports']} |"

# Write output file
output_file = "19_missing_exercises_formatted.md"
with open(output_file, 'w', encoding='utf-8') as f:
    f.write("# 19 Missing Exercises - Formatted for Database v3 Integration\n\n")
    f.write("**Source Files:**\n")
    f.write("- batch_supplementary_6_exercises_research.md (6 exercises)\n")
    f.write("- batch_supplementary_olympic_lifts_7_exercises_research.md (7 exercises)\n")
    f.write("- batch_supplementary_kettlebell_suspension_6_exercises_research.md (6 exercises)\n\n")
    f.write("**Total:** 19 exercises\n\n")
    f.write("---\n\n")
    f.write("## Database Table Format (14 Columns)\n\n")
    f.write("| Exercise | Primary Muscles | Secondary Muscles | Type | Equipment | Level | Body Region | Movement | Modality | Functional Groups | Steps for Beginners | Advanced Key Points | Scientific Reference | Sports Tags |\n")
    f.write("|----------|----------------|-------------------|------|-----------|-------|-------------|----------|----------|-------------------|---------------------|---------------------|---------------------|-------------|\n")

    for exercise in all_exercises:
        f.write(format_exercise_row(exercise) + "\n")

    f.write("\n---\n\n")
    f.write(f"**Total Exercises:** {len(all_exercises)}\n")
    f.write("**Status:** Ready for integration into comprehensive_exercise_database_v3.md\n")

print(f"✅ Successfully formatted {len(all_exercises)} exercises")
print(f"📝 Output file: {output_file}")
print("\n📊 Exercise Breakdown:")
print(f"  - Batch 1 (Core/Plyometrics): {len(batch_1_exercises)} exercises")
print(f"  - Batch 2 (Olympic Lifts): {len(batch_2_exercises)} exercises")
print(f"  - Batch 3 (Kettlebell/Suspension): {len(batch_3_exercises)} exercises")
print(f"  - Total: {len(all_exercises)} exercises")
