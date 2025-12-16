# Enhanced Filtering Columns Taxonomy

This document defines the values and rules for the 3 new filtering columns being added to database v3.1.

---

## Column 1: Training_Goal

**Purpose:** Allows filtering by primary training adaptation goal.

**Values:** (Single value per exercise)

1. **Strength** - Maximal force production, low-rep heavy loads (1-6 reps)
2. **Hypertrophy** - Muscle size/growth, moderate reps (6-12 reps)
3. **Power** - Explosive force production, rapid acceleration
4. **Endurance** - Sustained muscular or cardiovascular effort, high reps (15+ reps)
5. **Stability** - Core stabilization, anti-rotation, anti-extension
6. **Mobility** - Range of motion, flexibility, dynamic stretching

**Assignment Rules:**
- Olympic lifts (Clean, Snatch, etc.) → **Power**
- Plyometrics (Box Jumps, Broad Jumps, etc.) → **Power**
- Compound barbell exercises (Bench Press, Squat, Deadlift) → **Strength**
- Isolation exercises (Bicep Curls, Leg Extensions) → **Hypertrophy**
- Planks, holds, anti-rotation exercises → **Stability**
- High-rep bodyweight or light resistance → **Endurance**

---

## Column 2: Movement_Pattern

**Purpose:** Categorizes exercises by fundamental human movement patterns (can be multiple values separated by semicolons).

**Values:** (Multiple values allowed, separated by semicolons)

1. **Push_Vertical** - Overhead pressing movements
2. **Push_Horizontal** - Horizontal pressing (bench press, push-ups)
3. **Pull_Vertical** - Vertical pulling (pull-ups, lat pulldowns)
4. **Pull_Horizontal** - Horizontal pulling (rows)
5. **Squat** - Knee-dominant lower body (squats, leg press)
6. **Hinge** - Hip-dominant lower body (deadlifts, hip thrusts, kettlebell swings)
7. **Lunge** - Single-leg knee-dominant (lunges, split squats)
8. **Carry** - Loaded carries (farmer's walks, suitcase carries)
9. **Rotation** - Rotational movements (cable chops, Russian twists)
10. **Anti-Rotation** - Resisting rotation (Pallof press, single-arm rows)
11. **Isolation** - Single-joint movements (curls, extensions, raises)
12. **Isometric** - Static holds (planks, wall sits, Superman hold)

**Assignment Rules:**
- Bench Press → **Push_Horizontal**
- Overhead Press → **Push_Vertical**
- Barbell Row → **Pull_Horizontal; Hinge**
- Pull-Up → **Pull_Vertical**
- Deadlift → **Hinge**
- Back Squat → **Squat**
- Single-Arm Row → **Pull_Horizontal; Anti-Rotation**
- Bicycle Crunches → **Rotation**
- Plank → **Isometric; Anti-Rotation**

---

## Column 3: Equipment_Type

**Purpose:** Filters exercises by specific equipment needed (can be multiple values separated by semicolons).

**Values:** (Multiple values allowed, separated by semicolons)

1. **Barbell**
2. **Dumbbell**
3. **Kettlebell**
4. **Machine**
5. **Cable**
6. **Bodyweight**
7. **Suspension_Trainer** (TRX, rings)
8. **Resistance_Band**
9. **Medicine_Ball**
10. **Stability_Ball** (Swiss ball)
11. **Plyometric_Box**
12. **Sled** (Prowler, sleds)
13. **Landmine**
14. **EZ_Bar**
15. **Trap_Bar**
16. **Smith_Machine**
17. **Bench** (flat, incline, decline)
18. **Pull-Up_Bar**

**Assignment Rules:**
- Match directly from existing "Equipment" column
- If "Equipment" column says "Barbell" → **Barbell**
- If "Equipment" column says "Bodyweight" → **Bodyweight**
- If exercise requires bench + barbell → **Barbell; Bench**
- If exercise requires dumbbell + bench → **Dumbbell; Bench**
- Suspension exercises → **Suspension_Trainer**
- TRX/Rings → **Suspension_Trainer**

---

## Implementation Notes

1. **Training_Goal** is a single value (most dominant training effect)
2. **Movement_Pattern** can have 1-3 values (e.g., "Pull_Horizontal; Hinge; Anti-Rotation")
3. **Equipment_Type** can have 1-3 values (e.g., "Barbell; Bench")
4. Multiple values are separated by semicolons `;` with a space after (e.g., "Value1; Value2; Value3")
5. These columns appear after the existing 14 columns, before video link columns

---

## Column Order in Database v3.1 (20 columns total)

1. Exercise
2. Primary Muscles
3. Secondary Muscles
4. Type
5. Equipment
6. Level
7. Body Region
8. Movement
9. Modality
10. Functional Groups
11. Steps for Beginners
12. Advanced Key Points
13. Scientific Reference
14. Sports Tags
15. **Training_Goal** (NEW)
16. **Movement_Pattern** (NEW)
17. **Equipment_Type** (NEW)
18. ExRx_Video_URL (to be added)
19. JEFIT_Video_URL (to be added)
20. CoachWhitt_Video_URL (to be added)

---

**Status:** Taxonomy defined, ready for Python script implementation.
