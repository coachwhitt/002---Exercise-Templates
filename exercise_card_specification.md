# CoachWhitt Exercise Card Specification

**Version:** 1.0
**Date:** 11 November 2024
**Purpose:** Define the complete specification for CoachWhitt Exercise Cards for client program generation

---

## Overview

CoachWhitt Exercise Cards are modular, branded training documents that combine anatomical muscle visualization, exercise instructions, and trackable metrics. Each card is designed for integration into personalized client workout programs.

---

## Card Layout Structure

### Physical Specifications

**Print Dimensions:**
- **Size:** A5 (148 × 210 mm / 5.8 × 8.3 inches)
- **Orientation:** Portrait
- **Resolution:** 300 DPI minimum for print
- **Format:** PDF for distribution, source files in vector format

**Digital Dimensions:**
- **Size:** 1748 × 2480 px (A5 at 300 DPI)
- **Format:** PDF (interactive), PNG (static)

---

## Visual Design System

### Brand Compliance

All cards must follow the CoachWhitt Visual Brand Guide (`./context_files/04-visual-brand-guide.md`):

**Colors:**
- Background: `#1E1F22` (Deep Charcoal)
- Text: `#EBE7D9` (Off-White)
- Accent/Highlights: `#F55139` (Accent Red)
- Secondary Text: `#B8B3A8` (Muted)
- Card Background: `#25262A` (Secondary Background)

**Typography:**
- Font Family: Montserrat (Google Fonts)
- Headings: 700 (Bold)
- Body Text: 400 (Regular)
- Labels: 600 (Semi-Bold)

**Visual Elements:**
- Border Radius: 8px for cards
- Spacing: 1rem (16px) base unit
- Logo: `05-logo-main.svg` in top-right corner

---

## Card Content Sections

### 1. Header Section

**Position:** Top of card
**Background:** `#1E1F22` (Deep Charcoal)
**Height:** ~80-100px

**Elements:**
- **Logo:** CoachWhitt logo (top-right, 40-50px height)
- **Exercise Name:** H2 (32px, Bold, #EBE7D9)
- **Movement Type Badge:** Small pill badge (Compound/Isolation)
  - Background: `#F55139`
  - Text: `#EBE7D9`, 12px, Semi-Bold
  - Border Radius: 20px

**Layout:**
```
┌─────────────────────────────────────────┐
│  BARBELL BENCH PRESS      [LOGO]       │
│  [COMPOUND]                             │
└─────────────────────────────────────────┘
```

---

### 2. Anatomical Diagram Section

**Position:** Upper-middle of card
**Background:** `#25262A` (Secondary Background)
**Height:** ~400-500px

**Elements:**
- **Two anatomical diagrams:** Side-by-side (front and rear views)
- **Muscle highlighting:**
  - Primary muscles: Full opacity `#F55139` (Accent Red)
  - Secondary muscles: 50% opacity `#F55139`
- **Muscle labels:** Beside diagrams
  - Primary label: Bold, `#EBE7D9`
  - Secondary label: Regular, `#B8B3A8`

**Anatomical Style:**
- 3D-rendered muscular anatomy (reference: `./example images/`)
- Clean, professional medical illustration style
- Separate male and female versions available
- Muscles highlighted in brand accent red

**Layout:**
```
┌──────────────────────────────────────────┐
│  [Front View]      [Rear View]           │
│   Diagram with     Diagram with          │
│   highlighted      highlighted            │
│   muscles          muscles                │
│                                           │
│  PRIMARY MUSCLES:                         │
│  • Pectoralis Major                       │
│  • Anterior Deltoid                       │
│                                           │
│  SECONDARY MUSCLES:                       │
│  • Triceps Brachii                        │
└──────────────────────────────────────────┘
```

---

### 3. Exercise Details Section

**Position:** Middle of card
**Background:** `#1E1F22` (Primary Background)
**Padding:** 1.5rem (24px)

**Elements:**

#### Equipment Required
- **Label:** "EQUIPMENT" (12px, Semi-Bold, `#B8B3A8`)
- **Value:** 14px, Regular, `#EBE7D9`
- **Icon:** Small equipment icon (optional)

**Layout:**
```
┌──────────────────────────────────────────┐
│  EQUIPMENT                                │
│  Barbell, Flat Bench                      │
└──────────────────────────────────────────┘
```

**Note:** Sports tags and scientific references are stored in the database for trainer reference and exercise selection but are NOT displayed on client-facing cards.

---

### 4. Instructions Section

**Position:** Lower-middle of card
**Background:** `#25262A` with left border accent
**Border-Left:** 4px solid `#F55139`
**Padding:** 1.5rem (24px)

#### Beginner Instructions
- **Heading:** "HOW TO PERFORM" (14px, Bold, `#EBE7D9`)
- **Steps:** Numbered list (14px, Regular, `#EBE7D9`, line-height: 1.6)
- **Format:**
  ```
  1. Step one description
  2. Step two description
  3. Step three description
  ```

#### Advanced Coaching Points
- **Heading:** "COACHING POINTS" (14px, Bold, `#F55139`)
- **Points:** Bulleted list (13px, Regular, `#EBE7D9`, line-height: 1.6)
- **Format:**
  ```
  • Coaching cue one
  • Coaching cue two
  • Coaching cue three
  ```

**Layout:**
```
┌│─────────────────────────────────────────┐
││  HOW TO PERFORM                          │
││  1. Lie flat on bench, eyes under bar    │
││  2. Grip bar slightly wider than...      │
││  3. Unrack and lower to mid-chest        │
││  4. Press to lockout                     │
││  5. Maintain 5-point contact             │
││                                           │
││  COACHING POINTS                          │
││  • Retract scapulae throughout           │
││  • Leg drive initiates press             │
││  • Bar path slightly diagonal            │
└│─────────────────────────────────────────┘
```

---

### 5. Exercise Image/Illustration

**Position:** Lower section
**Size:** ~300 × 200px (landscape orientation)
**Style:** Match anatomical diagram style

**Content:**
- Side-view illustration of exercise being performed
- Same 3D-rendered style as anatomical diagrams
- Equipment visible
- Key positioning highlighted
- Can show 2 phases (start/end position) side-by-side

---

### 6. Tracking Section (Editable Fields)

**Position:** Bottom of card
**Background:** `#1E1F22` with subtle border
**Border-Top:** 1px solid `rgba(245, 81, 57, 0.2)`
**Padding:** 1.5rem (24px)

**Elements:**
- **Field Labels:** "SETS", "REPS", "WEIGHT/TIME", "REST" (12px, Bold, `#B8B3A8`)
- **Input Fields:** Empty boxes with light border for handwritten/typed values
- **Field Styling:**
  - Border: 1px solid `#B8B3A8`
  - Background: `#25262A`
  - Height: 40px
  - Border Radius: 4px

**Layout:**
```
┌──────────────────────────────────────────┐
│  SETS       REPS      WEIGHT/TIME   REST │
│  [___]      [___]     [___]         [___]│
│                                           │
│  NOTES:                                   │
│  [_____________________________________]  │
└──────────────────────────────────────────┘
```

---

### 7. Footer Section

**Position:** Bottom of card
**Background:** `#15161A` (Footer Background)
**Height:** ~50px
**Padding:** 1rem (16px)

**Elements:**
- **Tagline:** "Train Like an Athlete. Live Like You." (10px, `#B8B3A8`)
- **Page Number:** Right-aligned (for multi-page programs)

**Layout:**
```
┌──────────────────────────────────────────┐
│  Train Like an Athlete. Live Like You. [1]│
└──────────────────────────────────────────┘
```

---

## Data Structure for Generation

### JSON Schema

```json
{
  "exerciseId": "string",
  "exerciseName": "string",
  "primaryMuscles": ["string"],
  "secondaryMuscles": ["string"],
  "movementType": "Compound|Isolation",
  "equipment": ["string"],
  "instructionsBeginners": ["string"],
  "coachingPoints": ["string"],
  "anatomicalDiagrams": {
    "maleFront": "path/to/image",
    "maleRear": "path/to/image",
    "femaleFront": "path/to/image",
    "femaleRear": "path/to/image"
  },
  "exerciseIllustration": "path/to/image",
  "gender": "male|female"
}
```

**Database-Only Fields (Not Used in Card Generation):**
- `scientificReference`: Stored for trainer reference and exercise validation
- `scientificReferenceDOI`: Research paper identifier
- `sportsTags`: Used for sport-specific program creation and exercise filtering
- `muscleGroup`: Database categorization
- `difficulty`: Exercise difficulty level for program planning

---

## File Naming Convention

### Individual Exercise Cards

**Format:** `{ExerciseName}_{Gender}_Card.pdf`

**Examples:**
- `Barbell_Bench_Press_Male_Card.pdf`
- `Barbell_Bench_Press_Female_Card.pdf`
- `Dumbbell_Lateral_Raise_Male_Card.pdf`

### Client Program Files

**Format:** `{ClientName}_Week{#}_Session{#}_Exercises.pdf`

**Examples:**
- `John_Smith_Week1_Session1_Exercises.pdf`
- `Jane_Doe_Week2_Session3_Exercises.pdf`

---

## Responsive Variations

### Digital Scrollable Version

For mobile/tablet viewing:
- Single-column layout
- Sections stack vertically
- Larger tap targets for input fields
- Optimized for 375px - 768px width

### Print-Optimized Version

For physical printouts:
- Ensure 300 DPI resolution
- CMYK color conversion (use Pantone equivalents)
- Bleed area: 3mm on all sides
- Crop marks included

---

## Accessibility Considerations

**Color Contrast:**
- All text meets WCAG AA standards (4.5:1 minimum)
- Off-White on Deep Charcoal: ✓ Passes
- Accent Red used for non-critical text only

**Typography:**
- Minimum body text: 13px (print), 14px (digital)
- Line height: 1.6 for readability
- Clear hierarchy with size and weight variations

**Alternative Formats:**
- Text-based version available for screen readers
- High-contrast version option for visual impairments

---

## Generation Workflow

### Phase 1: Data Preparation
1. Extract exercise data from `comprehensive_exercise_database.md`
2. Structure data in JSON format
3. Validate all required fields present

### Phase 2: Asset Creation
1. Generate/source anatomical diagrams (male and female)
2. Highlight appropriate muscles in brand accent red
3. Create exercise illustration images
4. Ensure all images match style guide

### Phase 3: Card Assembly
1. Apply CoachWhitt brand template
2. Populate all content sections
3. Generate both male and female versions
4. Export to PDF (300 DPI)

### Phase 4: Program Integration
1. Trainer selects exercises for client program
2. Cards compiled into session document
3. Add session summary page (goals, notes)
4. Generate final PDF with proper naming

---

## Quality Control Checklist

Before finalizing any exercise card:

- ✓ Brand colors match specification exactly
- ✓ Montserrat font used throughout
- ✓ Logo present and properly sized
- ✓ Anatomical diagrams show correct muscles
- ✓ Primary muscles highlighted at full opacity
- ✓ Secondary muscles at 50% opacity
- ✓ All text is legible at print size
- ✓ Instructions are clear and sequential
- ✓ Coaching points are informative
- ✓ Equipment list is accurate
- ✓ Tracking fields are editable
- ✓ File named correctly
- ✓ Both gender versions created

---

## Example Use Cases

### Use Case 1: Single Client Session
**Scenario:** Trainer creates Week 1, Session 1 for new client

**Process:**
1. Select 6-8 exercises from database
2. Generate individual cards (appropriate gender)
3. Compile into session PDF
4. Add session summary page with:
   - Client name and date
   - Session goals
   - Exercise order
   - Total session time estimate
5. Deliver PDF to client (digital or print)

### Use Case 2: Multi-Week Program
**Scenario:** 12-week training program with 3 sessions/week

**Process:**
1. Plan exercise progression over 12 weeks
2. Generate all exercise cards needed (avoiding duplicates)
3. Compile into weekly packets
4. Each week = separate PDF with 3 session documents
5. Create master program document with:
   - Program overview
   - Weekly goals
   - Exercise library index
   - Progress tracking sheets

### Use Case 3: Exercise Library Reference
**Scenario:** Complete library of all available exercises

**Process:**
1. Generate cards for all 100+ exercises
2. Organize by muscle group
3. Create searchable PDF with bookmarks
4. Include muscle group index
5. Available for trainers to reference

---

## Future Enhancements

### Phase 2: Interactive Features
- QR codes linking to video demonstrations
- Clickable links to technique articles
- Embedded video players (digital version)

### Phase 3: Dynamic Content
- Real-time progress tracking integration
- Auto-populate weights from previous sessions
- Client performance analytics

### Phase 4: Mobile App Integration
- Exercise card viewer in dedicated app
- Video overlays on anatomical diagrams
- Form check feature using phone camera

---

## Template Files Structure

```
/exercise_card_templates/
├── base_template.svg           # Master template (editable)
├── male_anatomy_library/       # All male anatomical diagrams
│   ├── chest_front.svg
│   ├── chest_rear.svg
│   └── ...
├── female_anatomy_library/     # All female anatomical diagrams
│   ├── chest_front.svg
│   ├── chest_rear.svg
│   └── ...
├── exercise_illustrations/     # Exercise position images
│   ├── barbell_bench_press.svg
│   └── ...
├── generated_cards/            # Output folder for PDFs
│   ├── male/
│   └── female/
└── client_programs/            # Compiled client programs
    ├── {ClientName}/
    └── ...
```

---

## Technical Implementation Notes

### Recommended Tools

**Design Phase:**
- Adobe Illustrator or Figma for template creation
- Anatomical diagram sourcing: Shutterstock, custom 3D rendering
- Color management: Pantone matching system

**Generation Phase:**
- Python with ReportLab or WeasyPrint for PDF generation
- Jinja2 for template rendering
- Pillow for image processing

**Automation:**
- Script to batch-generate cards from database
- Template variables for dynamic content
- Validation checks for data completeness

---

## Version History

**Version 1.1** (11 November 2024)
- Removed sports tags from client-facing cards (database-only field)
- Removed scientific references from client-facing cards (database-only field)
- Updated footer to only include tagline and page number
- Clarified data structure fields used for cards vs. database reference

**Version 1.0** (11 November 2024)
- Initial specification document
- Complete layout structure defined
- Brand compliance standards established
- Data structure schema created

---

## Contact

**Project Owner:** Dean Whittingslow (CoachWhitt)
**Website:** https://coachwhitt.com
**Email:** info@coachwhitt.com

For questions about exercise card specifications, refer to this document first. For visual brand elements, reference `04-visual-brand-guide.md`.

---

**CoachWhitt** | Train Like an Athlete. Live Like You.
