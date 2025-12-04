# Exercise Database v3.0 - User Guide

**Generated:** 2025-12-04
**Purpose:** Clean, filterable exercise database for Google Sheets with functional group filtering

---

## 📊 What's New in v3.0?

### Key Changes from v2.0

1. **Removed All Session Context**
   - No more "Session 1", "Session 7", "Batch 4a" headers
   - Single, clean table structure
   - No narrative text or session notes

2. **Added Functional Group Column**
   - New `Functional_Groups` column for dropdown filtering
   - Exercises tagged with multiple groups (e.g., "Chest_Pectoralis; Arms_Triceps")
   - Compatible with Google Sheets filter/dropdown features

3. **Clean Structure**
   - **Total Exercises:** 358 exercises
   - **Single Table:** All exercises in one continuous table
   - **CSV Export:** `comprehensive_exercise_database_v3.csv` ready for Google Sheets import

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

## 📥 How to Use in Google Sheets

### Method 1: Direct CSV Import (Recommended)

1. **Upload to Google Drive:**
   - Upload `comprehensive_exercise_database_v3.csv` to your Google Drive

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

**Total:** 358 exercises (some exercises appear in multiple groups)

### Coverage vs Origym CSV

- **Origym CSV:** 324 unique exercises
- **Our Database v3:** 358 exercises
- **Coverage:** 73.8% of Origym exercises
- **Missing Exercises:** 19 high-priority (see `missing_exercises_clean.txt`)

---

## ❌ Missing Exercises from Origym CSV

The following 19 exercises are in the Origym CSV but **NOT** in our research database:

### High Priority - Definitely Missing

1. Ab-Cycle
2. Box Jumps
3. Broard Jumps (likely "Broad Jumps")
4. Clean
5. Clean and Jerk
6. Conditioning Ball Reverse Jack Knife
7. Hang Clean
8. Kettle Bell Swings
9. Kettlebell Row (double)
10. Kettlebell Row (single)
11. Machine-Row
12. Prowler
13. Snatch
14. Squat Jumps
15. Superman
16. Superman-Hold
17. Suspended Reverse Mountain Climbers
18. Suspended Row
19. Thruster

**Note:** These exercises should be researched and added in a future session to achieve 100% Origym coverage.

---

## 🔄 Future Enhancements

### Potential v3.1 Updates

1. **Add Missing 19 Exercises:**
   - Research and add Olympic lifts (Clean, Snatch, Hang Clean)
   - Add plyometric exercises (Box Jumps, Squat Jumps, Broad Jumps)
   - Add conditioning equipment exercises (Prowler, Kettlebell Rows)
   - Add suspension training exercises (Suspended Row, Suspended Mountain Climbers)
   - Research specialized exercises (Ab-Cycle, Conditioning Ball variations)

2. **Enhanced Filtering Columns:**
   - Add `Equipment_Type` split into categories (Barbell, Dumbbell, Cable, Machine, Bodyweight)
   - Add `Movement_Pattern` refinement (Horizontal Push/Pull, Vertical Push/Pull)
   - Add `Training_Goal` tags (Strength, Hypertrophy, Endurance, Power, Stability)

3. **Video Link Integration:**
   - Add ExRx and JEFIT video columns (currently in v2, removed in v3 for simplicity)
   - Add placeholder column for CoachWhitt custom videos

4. **Workout Program Templates:**
   - Create preset workout program sheets using FILTER formulas
   - Example: "Upper Body Push" auto-populates chest, shoulders, triceps exercises

---

## 📋 Column Reference

### v3.0 Column Structure (14 columns)

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

### v3.0 (2025-12-04)
- Created clean table structure (removed all session context)
- Added `Functional_Groups` column with 27 filtering tags
- Exported CSV for Google Sheets compatibility
- Identified 19 missing exercises from Origym CSV

### v2.0 (2025-11-27 to 2025-12-04)
- Expanded from 110 to 409 exercises over 10 sessions
- Maintained 16-column metadata structure
- Added 1,600+ peer-reviewed scientific references

### v1.0 (2025-11-11)
- Initial 110-exercise database
- Comprehensive scientific references
- Brand-aligned structure

---

**Database v3.0 is now ready for Google Sheets import and filtering!** 🎉
