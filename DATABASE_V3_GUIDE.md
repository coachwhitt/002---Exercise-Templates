# Exercise Database v3.1 - User Guide

**Generated:** 2025-12-10
**Purpose:** Clean, filterable exercise database for Google Sheets with enhanced filtering and video link integration

---

## 📊 What's New in v3.1?

### Key Enhancements from v3.0

1. **19 Missing Exercises Added**
   - Added missing exercises from Origym curriculum
   - Includes Olympic lifts (Clean, Snatch, Hang Clean, Clean and Jerk, Thruster)
   - Includes plyometrics (Box Jumps, Broad Jumps, Squat Jumps)
   - Includes suspension/stability exercises (Suspended Rows, Kettlebell variations)
   - **Total Exercises:** 377 exercises (up from 358)

2. **3 Enhanced Filtering Columns Added**
   - **Training_Goal:** Filter by primary training adaptation (Strength, Hypertrophy, Power, Endurance, Stability)
   - **Movement_Pattern:** Filter by movement type (Push_Horizontal, Pull_Vertical, Hinge, Squat, etc.)
   - **Equipment_Type:** Filter by specific equipment (Barbell, Dumbbell, Kettlebell, Machine, etc.)

3. **3 Video Link Columns Added**
   - **ExRx_Video_URL:** Placeholder for ExRx.net video demonstrations
   - **JEFIT_Video_URL:** Placeholder for JEFIT app video links
   - **CoachWhitt_Video_URL:** Placeholder for custom CoachWhitt video content

4. **Database Structure**
   - **Total Exercises:** 377 exercises
   - **Total Columns:** 20 columns (14 original + 3 enhanced filtering + 3 video links)
   - **Single Table:** All exercises in one continuous table
   - **CSV Export:** `comprehensive_exercise_database_v3.1.csv` ready for Google Sheets import

### Changes from v2.0 to v3.0

1. **Removed All Session Context**
   - No more "Session 1", "Session 7", "Batch 4a" headers
   - Single, clean table structure
   - No narrative text or session notes

2. **Added Functional Group Column**
   - New `Functional_Groups` column for dropdown filtering
   - Exercises tagged with multiple groups (e.g., "Chest_Pectoralis; Arms_Triceps")
   - Compatible with Google Sheets filter/dropdown features

---

## 🎯 Functional Group System

The v3 database uses **functional movement groups** similar to the Origym CSV structure. Each exercise is tagged with 1 or more functional groups, allowing you to filter exercises by:

### Primary Muscle Groups (15 tags)

| Tag | Description | Example Exercises |
|-----|-------------|-------------------|
| `Chest_Pectoralis` | Chest exercises | Barbell Bench Press, Push-Ups, Dips |
| `Back_Latissimus_Dorsi` | Lat-focused back exercises | Pull-Ups, Lat Pulldown, Rows |
| `Trapezius_and_Rhomboids` | Upper back exercises | Rows, Face Pulls, Shrugs |
| `Shoulders_Delts_and_Traps` | Shoulder exercises | Overhead Press, Lateral Raises |
| `Arms_Biceps` | Bicep exercises | Curls (all variations) |
| `Arms_Triceps` | Tricep exercises | Extensions, Pushdowns, Dips |
| `Legs_Quadriceps` | Quad-focused leg exercises | Squats, Lunges, Leg Extensions |
| `Legs_Hamstrings` | Hamstring exercises | Deadlifts, Leg Curls, RDLs |
| `Gluteals` | Glute exercises | Hip Thrusts, Glute Bridges, Lunges |
| `Calves_Gastrocnemius` | Standing calf exercises | Standing Calf Raise |
| `Calves_Soleus` | Seated calf exercises | Seated Calf Raise |
| `Forearms_Grip` | Forearm/grip exercises | Wrist Curls, Farmer's Walk |
| `Neck` | Neck exercises | Neck Flexion, Extension |
| `Rotator_Cuff` | Rotator cuff exercises | Internal/External Rotation |

### Core Regions (7 tags)

| Tag | Description | Example Exercises |
|-----|-------------|-------------------|
| `Abdominal_Lower` | Lower ab exercises | Reverse Crunches, Leg Raises |
| `Abdominal_Upper` | Upper ab exercises | Crunches, Sit-Ups |
| `Abdominal_Total` | Full ab exercises | Planks, Ab Wheel |
| `Abdominal_Obliques` | Oblique exercises | Twists, Side Planks, Chops |
| `Lower_Back_Erector_Spinae` | Lower back exercises | Hyperextensions, Supermans |
| `Full_Core` | Total core stability | Planks, Anti-rotation exercises |
| `Total_Core` | Multi-region core | Exercises hitting 2+ core regions |

### Combination Groups (5 tags)

| Tag | Description | Example Exercises |
|-----|-------------|-------------------|
| `Quads_Hamstrings_Glutes` | Compound leg exercises | Squats, Lunges, Deadlifts |
| `Hamstrings_and_Quadriceps` | Balanced leg work | Bulgarian Split Squats |
| `Chest_and_Back` | Push-pull combos | (Rare in single exercises) |
| `Deltoids_and_Lats` | Shoulder + back | Overhead movements with lat involvement |
| `Full_Body_Movements` | 2+ body regions | Compound exercises hitting multiple areas |

---

## 🎯 Enhanced Filtering Columns (v3.1 New)

### Training_Goal Column

Filter exercises by primary training adaptation goal:

| Value | Description | Example Exercises |
|-------|-------------|-------------------|
| **Strength** | Maximal force production, heavy loads | Barbell Bench Press, Back Squat, Deadlift |
| **Hypertrophy** | Muscle size/growth, moderate loads | Dumbbell Press, Cable Flyes, Bicep Curls |
| **Power** | Explosive force production | Clean, Snatch, Box Jumps, Kettlebell Swings |
| **Endurance** | Sustained muscular effort | High-rep bodyweight exercises |
| **Stability** | Core stabilization, anti-rotation | Planks, Superman Holds, Mountain Climbers |
| **Mobility** | Range of motion, flexibility | Dynamic stretches, mobility drills |

### Movement_Pattern Column

Filter exercises by fundamental human movement patterns (can have multiple values):

| Value | Description | Example Exercises |
|-------|-------------|-------------------|
| **Push_Horizontal** | Horizontal pressing | Bench Press, Push-Ups, Dips |
| **Push_Vertical** | Overhead pressing | Overhead Press, Arnold Press, Thruster |
| **Pull_Horizontal** | Horizontal pulling | Barbell Row, Seated Cable Row, Face Pulls |
| **Pull_Vertical** | Vertical pulling | Pull-Ups, Chin-Ups, Lat Pulldown |
| **Squat** | Knee-dominant lower body | Back Squat, Front Squat, Leg Press |
| **Hinge** | Hip-dominant lower body | Deadlift, RDL, Hip Thrust, Kettlebell Swing |
| **Lunge** | Single-leg knee-dominant | Lunges, Split Squats, Step-Ups |
| **Rotation** | Rotational movements | Cable Chops, Russian Twists, Bicycle Crunches |
| **Anti-Rotation** | Resisting rotation | Pallof Press, Single-Arm Rows, Planks |
| **Isolation** | Single-joint movements | Curls, Extensions, Lateral Raises |
| **Isometric** | Static holds | Planks, Wall Sits, Superman Hold |

### Equipment_Type Column

Filter exercises by specific equipment needed (can have multiple values):

| Value | Description |
|-------|-------------|
| **Barbell** | Standard barbell exercises |
| **Dumbbell** | Dumbbell exercises |
| **Kettlebell** | Kettlebell exercises |
| **Machine** | Selectorized or plate-loaded machines |
| **Cable** | Cable machine exercises |
| **Bodyweight** | No equipment needed |
| **Suspension_Trainer** | TRX, rings, suspension systems |
| **Resistance_Band** | Resistance band exercises |
| **Stability_Ball** | Swiss ball, exercise ball |
| **Plyometric_Box** | Box jumps, step-ups |
| **Sled** | Prowler, sleds |
| **Bench** | Requires bench (flat, incline, decline) |
| **Pull-Up_Bar** | Requires pull-up bar |

**Note:** Exercises may have multiple equipment types (e.g., "Barbell; Bench" for Barbell Bench Press)

---

## 🎥 Video Link Columns (v3.1 New)

Three placeholder columns for future video integration:

1. **ExRx_Video_URL** - Links to ExRx.net exercise demonstrations
2. **JEFIT_Video_URL** - Links to JEFIT app video library
3. **CoachWhitt_Video_URL** - Links to custom CoachWhitt instructional videos

These columns are currently empty and ready for future video URL population.

---

## 📥 How to Use in Google Sheets

### Method 1: Direct CSV Import (Recommended)

1. **Upload to Google Drive:**
   - Upload `comprehensive_exercise_database_v3.1.csv` to your Google Drive

2. **Open with Google Sheets:**
   - Right-click → Open with → Google Sheets

3. **Create Filter Views:**
   - Select header row (Row 1)
   - Click **Data** → **Create a filter**
   - Click filter icon on `Functional_Groups` column
   - Type or select functional group (e.g., "Chest_Pectoralis")

4. **Use Dropdown Menus:**
   - Click filter dropdown on any column
   - Search or select values
   - Multiple filters can be applied simultaneously

### Method 2: Origym-Style Dropdown System

To replicate the Origym CSV dropdown system:

1. **Create a Functional Groups Sheet:**
   - Create new sheet named "Groups"
   - Column A: Functional group names (Chest_Pectoralis, Arms_Biceps, etc.)
   - Columns B-Z: List exercises for each group (one per column)

2. **Create Lookup Formula:**
   ```
   =FILTER('Database v3'!A:N, ISNUMBER(SEARCH(B1, 'Database v3'!J:J)))
   ```
   Where:
   - `B1` = Selected functional group
   - `'Database v3'!J:J` = Functional_Groups column
   - Returns all exercises matching the selected group

3. **Create Dropdown in Row 1:**
   - Data → Data validation
   - Criteria: List from range (your functional group list)
   - Users select group, exercises populate automatically

### Method 3: Multiple Tag Filtering

Since exercises can have multiple tags (e.g., "Chest_Pectoralis; Arms_Triceps"):

1. **Use SEARCH or REGEXMATCH:**
   ```
   =FILTER(A2:N, REGEXMATCH(J:J, "Chest_Pectoralis"))
   ```

2. **Combine Multiple Groups:**
   ```
   =FILTER(A2:N, REGEXMATCH(J:J, "Chest_Pectoralis|Arms_Triceps"))
   ```
   Returns exercises tagged with EITHER chest OR triceps

---

## 📈 Database Statistics

### Exercise Distribution

| Functional Group | Exercise Count |
|------------------|----------------|
| Back_Latissimus_Dorsi | 126 exercises |
| Arms_Biceps | 70 exercises |
| Full_Core | 63 exercises |
| Gluteals | 57 exercises |
| Legs_Quadriceps | 55 exercises |
| Chest_Pectoralis | 51 exercises |
| Quads_Hamstrings_Glutes | 51 exercises |
| Arms_Triceps | 48 exercises |
| Full_Body_Movements | 47 exercises |
| Abdominal_Obliques | 39 exercises |
| Trapezius_and_Rhomboids | 34 exercises |
| Total_Core | 33 exercises |
| Shoulders_Delts_and_Traps | 24 exercises |
| Forearms_Grip | 23 exercises |
| Legs_Hamstrings | 21 exercises |
| Abdominal_Total | 20 exercises |
| Calves_Gastrocnemius | 16 exercises |
| Abdominal_Upper | 15 exercises |
| Neck | 15 exercises |
| Lower_Back_Erector_Spinae | 8 exercises |
| Calves_Soleus | 8 exercises |
| Abdominal_Lower | 7 exercises |
| Rotator_Cuff | 4 exercises |
| Deltoids_and_Lats | 3 exercises |
| Hamstrings_and_Quadriceps | 2 exercises |
| Chest_and_Back | 1 exercise |

**Total:** 377 exercises (some exercises appear in multiple groups)

### v3.1 Coverage vs Origym CSV

- **Origym CSV:** 324 unique exercises
- **Our Database v3.1:** 377 exercises
- **Coverage:** 98.7% of Origym exercises ✅
- **Status:** All 19 high-priority missing exercises added in v3.1

### v3.1 New Exercises Added

The following 19 exercises were added from the Origym curriculum:

**Core & Plyometric (6 exercises):**
1. Bicycle Crunches
2. Box Jumps
3. Broad Jumps
4. Squat Jumps
5. Superman
6. Superman Hold

**Olympic Lifts & Conditioning (7 exercises):**
7. Clean (Power Clean)
8. Clean and Jerk
9. Hang Clean
10. Snatch (Power Snatch)
11. Thruster
12. Kettlebell Swings
13. Prowler Push

**Kettlebell, Suspension & Machine (6 exercises):**
14. Kettlebell Row (Double Arm)
15. Kettlebell Row (Single Arm)
16. Machine Row
17. Suspended Row
18. Suspended Reverse Mountain Climbers
19. Conditioning Ball Reverse Jack Knife

---

## 🔄 Future Enhancements

### Potential v3.2 Updates

1. **Populate Video Link Columns:**
   - Add ExRx.net video URLs for all applicable exercises
   - Add JEFIT video URLs where available
   - Create custom CoachWhitt instructional videos

2. **Workout Program Templates:**
   - Create preset workout program sheets using FILTER formulas
   - Example: "Upper Body Push" auto-populates chest, shoulders, triceps exercises
   - Add program generation based on Training_Goal and Movement_Pattern filters

3. **Additional Exercises:**
   - Consider adding sport-specific variations
   - Add rehabilitation/prehab exercises
   - Expand neck, rotator cuff, and forearm sections

---

## 📋 Column Reference

### v3.1 Column Structure (20 columns)

| Column # | Column Name | Description |
|----------|-------------|-------------|
| 1 | Exercise | Exercise name |
| 2 | Primary_Muscles | Primary muscles worked (Latin names) |
| 3 | Secondary_Muscles | Secondary muscles worked |
| 4 | Type | Compound or Isolation |
| 5 | Equipment | Required equipment |
| 6 | Level | Beginner, Intermediate, or Advanced |
| 7 | Body_Region | Upper, Lower, or Core |
| 8 | Movement | Push, Pull, or Static |
| 9 | Modality | Free Weight, Cables, Fixed Resistance, Bodyweight, Machine |
| **10** | **Functional_Groups** | **Semicolon-separated list of functional groups** |
| 11 | Steps_for_Beginners | Step-by-step instructions |
| 12 | Advanced_Key_Points | 5 advanced coaching cues |
| 13 | Scientific_Reference | Peer-reviewed references with DOI/URLs |
| 14 | Sports_Tags | Applicable sports (10-12 per exercise) |
| **15** | **Training_Goal** | **Primary training adaptation (Strength, Hypertrophy, Power, etc.)** ✨ |
| **16** | **Movement_Pattern** | **Movement type(s) (Push_Horizontal, Hinge, etc.)** ✨ |
| **17** | **Equipment_Type** | **Specific equipment needed (Barbell, Dumbbell, etc.)** ✨ |
| **18** | **ExRx_Video_URL** | **ExRx.net video demonstration link (placeholder)** 🎥 |
| **19** | **JEFIT_Video_URL** | **JEFIT app video link (placeholder)** 🎥 |
| **20** | **CoachWhitt_Video_URL** | **Custom CoachWhitt video link (placeholder)** 🎥 |

**✨ = New in v3.1 | 🎥 = Video links (placeholders)**

---

## 🚀 Quick Start Example

### Google Sheets Filter Example

**Goal:** Find all chest exercises suitable for beginners using dumbbells

**Steps:**
1. Open `comprehensive_exercise_database_v3.csv` in Google Sheets
2. Data → Create a filter
3. Click filter on `Functional_Groups` → Type "Chest_Pectoralis" → OK
4. Click filter on `Level` → Select "Beginner" → OK
5. Click filter on `Equipment` → Search "Dumbbell" → OK

**Result:** Returns exercises like:
- Dumbbell Flyes
- Dumbbell Bench Press
- (Other beginner-friendly dumbbell chest exercises)

---

## 📞 Support & Questions

For questions about the database structure or filtering system:

1. Check `CLAUDE.md` for project context
2. Review `Exercise data.csv` for Origym reference structure
3. Check `missing_exercises_list.txt` for exercises not yet researched

---

## 📝 Version History

### v3.1 (2025-12-10)
- **Added 19 missing exercises** from Origym curriculum (358 → 377 exercises)
- **Added 3 enhanced filtering columns:** Training_Goal, Movement_Pattern, Equipment_Type
- **Added 3 video link columns:** ExRx_Video_URL, JEFIT_Video_URL, CoachWhitt_Video_URL
- **Total columns:** 20 (14 original + 3 enhanced + 3 video links)
- **Coverage:** 98.7% of Origym exercises ✅

### v3.0 (2025-12-04)
- Created clean table structure (removed all session context)
- Added `Functional_Groups` column with 27 filtering tags
- Exported CSV for Google Sheets compatibility
- Total: 358 exercises, 14 columns

### v2.0 (2025-11-27 to 2025-12-04)
- Expanded from 110 to 409 exercises over 10 sessions
- Maintained 16-column metadata structure
- Added 1,600+ peer-reviewed scientific references

### v1.0 (2025-11-11)
- Initial 110-exercise database
- Comprehensive scientific references
- Brand-aligned structure

---

**Database v3.1 is now ready for Google Sheets import and filtering!** 🎉
