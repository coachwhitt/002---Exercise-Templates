# Adobe Illustrator Exercise Card Prototype Guide

**Version:** 3.0 (A4 Format, Revised Layout)
**Date:** 12 November 2025
**Updated For:** Adobe Illustrator 30.0
**Purpose:** Step-by-step instructions for creating the first CoachWhitt Exercise Card prototype in Adobe Illustrator. This version revises the vertical spacing for a cleaner layout and unifies the background color for a more professional, cohesive design.

---

## Prerequisites

**Required Software:**
- Adobe Illustrator 30.0 or later (2024+)
- Montserrat font family installed (download from Google Fonts)

**Required Files:**
- CoachWhitt logo: `./context_files/05-logo-main.svg`
- Visual Brand Guide: `./context_files/04-visual-brand-guide.md`
- Example anatomical images: `./example images/` (for style reference)
- Card Specification: `exercise_card_specification.md`
- Visual Mockup: `exercise_card_visual_mockup.md`

---

## Quick Reference: A4 Sizing Specifications

**Canvas:**
- **Size:** 210mm × 297mm (A4 portrait)
- **Resolution:** 300 DPI = 2480 × 3508 pixels
- **Color Mode:** CMYK (print) or RGB (digital-only)
- **Bleed:** 3mm all sides
- **Safe Area:** 8mm margins

**Section Heights (Y-axis from top):**
| Section | Y Start | Height | Y End |
|---------|---------|--------|-------|
| Header | 0mm | 36mm | 36mm |
| Anatomy | 36mm | 74mm | 110mm |
| Equipment | 110mm | 20mm | 130mm |
| Instructions | 130mm | 95mm | 225mm |
| Illustration | 225mm | 50mm | 275mm |
| Tracking | 275mm | 22mm | 297mm |
| Footer | 285mm | 12mm | **297mm** |

**Typography Scale:**
- Exercise Name: **30pt** (Montserrat Bold, can wrap to 2 lines)
- Section Headings: **13pt** (Montserrat Bold)
- Section Labels: **11pt** (Montserrat Bold)
- Body Text: **12pt** (Montserrat Regular)
- Coaching Points: **11pt** (Montserrat Regular)
- Badge Text: **11pt** (Montserrat Semi-Bold)
- Footer Text: **9pt** (Montserrat Regular)

**Key Elements:**
- Logo: **5mm** height (~57mm width based on aspect ratio)
- Exercise Name: **30pt** (text box width 128mm, wraps to 2 lines for long names)
- Movement Badge: 30mm × 7mm (3.5mm radius)
- Anatomical Diagrams: 40mm × 65mm each
- Exercise Illustrations: 40mm × 40mm each
- Tracking Fields: 4 evenly spaced fields
- Red Border: 5mm wide

**Header Layout Strategy:**
- Logo: Top-right corner, 5mm height (~57mm width), 12mm margins
- Exercise name: Left side, 30pt text, 128mm wide text box
- Gap between text and logo: 1mm (tight but functional)
- Long exercise names automatically wrap to 2 lines
- Movement badge: Below exercise name (30mm wide)
- Total header height: 36mm accommodates all elements including wrapped text

**Why A4 vs A5?**
- Better for detailed anatomical diagrams
- Excellent digital viewing (2480 × 3508px)
- Can scale to 71% for A5 print if needed
- More professional layout with proper spacing

---

## Phase 1: Document Setup

### Step 1: Create New Document

1. Open Adobe Illustrator 30.0
2. **File > New** (or Cmd/Ctrl + N)
3. In the New Document dialog:
   - **Name:** `CoachWhitt_Exercise_Card_Template`
   - **Profile:** Print
   - **Units:** Millimeters
   - **Width:** 210 mm (A4)
   - **Height:** 297 mm (A4)
   - **Orientation:** Portrait
   - **Bleed:** 3 mm (all sides)
   - **Color Mode:** CMYK (for print)
   - **Raster Effects:** High (300 PPI)
   - **Resolution:** 300 DPI (results in 2480 × 3508 pixels)
4. Click **Create**

**Note:** A4 size is optimal for:
- Digital viewing (excellent resolution on mobile, tablet, desktop)
- Print flexibility (full-size A4 or scale to 71% for A5)
- Detailed anatomical diagrams with clear muscle visualization
- Professional layout with proper breathing room between sections

### Step 2: Set Up Rulers and Guides

1. **View > Rulers > Show Rulers** (Cmd/Ctrl + R)
2. **View > Guides > Lock Guides** (uncheck for now - or in Illustrator 30.0: **View > Guides > Lock Guides** toggle off)
3. Create safe area guides (8mm margin):
   - Drag horizontal guide from top ruler to **8mm from top edge**
   - Drag horizontal guide to **8mm from bottom edge** (289mm)
   - Drag vertical guide to **8mm from left edge**
   - Drag vertical guide to **8mm from right edge** (202mm)
4. These safe area guides ensure critical text doesn't get cut off during printing

**Tip:** In Illustrator 30.0, you can also use **View > Guides > Create Guides** and enter precise measurements

---

## Phase 2: Color Swatches Setup

### Step 3: Add Brand Colors to Swatches Panel

1. Open **Window > Swatches** (F5)
2. For each brand color, create a new swatch. For a unified, professional look, we will use the primary Deep Charcoal for all background elements.

**Deep Charcoal (Primary Background):**
- Click New Swatch icon (bottom of Swatches panel)
- **Color Mode:** CMYK
- **C:** 85%, **M:** 78%, **Y:** 76%, **K:** 77%
- **Name:** "CW Deep Charcoal"
- **Note:** Apply this color to ALL background sections.
- Click OK

**Off-White (Primary Text):**
- New swatch
- **CMYK:** C6, M5, Y12, K0
- **Name:** "CW Off-White"

**Accent Red:**
- New swatch
- **CMYK:** C0, M78, Y82, K0
- **Name:** "CW Accent Red"

**Muted/Secondary Text:**
- New swatch
- **CMYK:** C25, M23, Y28, K0
- **Name:** "CW Muted/Secondary"

### Step 4: Save Working File

1. **File > Save** (Cmd/Ctrl + S)
2. Name: `CoachWhitt_Card_Template.ai`
3. Location: Your project folder
4. We'll save as a template (.ait) after the prototype is complete

**Note:** In Illustrator 30.0, templates are saved via **File > Save As** and selecting "Adobe Illustrator Template (.ait)" from the format dropdown

---

## Phase 3: Build Card Structure

### Step 5: Create Background Layer

1. Open **Window > Layers** (F7)
2. Double-click Layer 1, rename to "Background"
3. Lock layer after creating background

**Create Full Background:**
1. Select Rectangle Tool (M)
2. Click on artboard
3. **Width:** 210 mm, **Height:** 297 mm
4. Position at X: 0, Y: 0 (use Transform panel: **Window > Transform** or F9)
5. Fill: "CW Deep Charcoal"
6. **Object > Lock > Selection** (Cmd/Ctrl + 2)

### Step 6: Create Section Layers

1. Create new layers (Layer panel menu > New Layer):
   - Layer: "Header"
   - Layer: "Anatomy Section"
   - Layer: "Equipment Section"
   - Layer: "Instructions Section"
   - Layer: "Exercise Illustration"
   - Layer: "Tracking Fields"
   - Layer: "Footer"
   - Layer: "Logo" (top layer)

---

## Phase 4: Build Header Section

### Step 7: Create Header Background

1. Select "Header" layer
2. Rectangle Tool (M)
3. Draw rectangle:
   - **X:** 0, **Y:** 0
   - **Width:** 210 mm, **Height:** 36 mm
4. Fill: "CW Deep Charcoal"

### Step 8: Add Exercise Name Text

1. Select Type Tool (T)
2. **Click and drag** to create a text box in header area
3. Text box dimensions:
   - **Width:** 128mm (leaves 1mm gap + 57mm for logo on right)
   - **Height:** 25mm (allows for 2 lines if needed)
4. Type: "BARBELL BENCH PRESS"
5. **Character Panel** (**Window > Type > Character** or Cmd/Ctrl + T):
   - Font: Montserrat Bold
   - Size: **30pt**
   - Leading: **34pt** (allows comfortable line spacing if wrapping)
   - Tracking: 0
   - Fill: "CW Off-White"
6. **Paragraph Panel** (**Window > Type > Paragraph**):
   - Alignment: Left
7. Position text box:
   - **X:** 12mm from left edge
   - **Y:** 8mm from top edge
8. **Type > Create Outlines** (Cmd/Ctrl + Shift + O) - Do this last after finalizing text

**Note:**
- Long exercise names will automatically wrap to 2 lines within the 128mm text box width
- The 36mm header height accommodates wrapped text comfortably
- In Illustrator 30.0, Character/Paragraph settings appear in the Properties panel when text is selected
- Text box leaves exactly 1mm gap before the logo starts at 141mm

### Step 9: Create Movement Type Badge

1. Select Rounded Rectangle Tool (hidden under Rectangle Tool - click and hold Rectangle Tool to reveal)
2. Click on artboard
3. **Height:** 7mm, **Corner Radius:** 3.5mm
4. Fill: "CW Accent Red"
5. **Add Badge Text:**
   1. Type Tool (T)
   2. Type: "COMPOUND MOVEMENT"
   3. Character settings:
      - Font: Montserrat Semi-Bold
      - Size: **11 pt**
      - Fill: "CW Off-White"
   4. Position the text over the rounded rectangle.
   5. **Adjust the width of the rounded rectangle to comfortably fit the "COMPOUND MOVEMENT" text.**
   6. Center text in badge:
      - Select both badge (rounded rectangle) and text
      - **Window > Align** (Shift + F7)
      - Click "Horizontal Align Center"
      - Click "Vertical Align Center"
6. Position the completed badge:
   - **X:** Center horizontally with the logo (logo center is at 169.5mm).
   - **Y:** 21mm from top edge (8mm logo top + 5mm logo height + 8mm gap).

**Illustrator 30.0 Tip:** The Align options are also available in the Properties panel when multiple objects are selected

### Step 10: Add Logo

1. Select "Logo" layer
2. **File > Place** (Shift + Cmd/Ctrl + P)
3. Navigate to: `./context_files/05-logo-main.svg`
4. Click artboard to place
5. Resize to height: **5mm** (maintain aspect ratio - hold Shift while dragging corner)
   - **Width will auto-adjust to ~57mm**
6. Position:
   - **X:** Align to right edge with 12mm margin (right edge at 198mm)
   - **Y:** 8mm from top (aligned with exercise name)
7. **Object > Lock > Selection** (Cmd/Ctrl + 2)

**Illustrator 30.0 Tips:**
- When placing, you'll see a live preview before clicking
- Use **Properties panel** to enter exact height: **5mm** (width auto-adjusts to ~57mm)
- Use **Align panel** (Shift + F7) → "Align to Artboard" → "Align Right" → then nudge left 12mm using Transform panel

**Layout Verification:**
- Available width: 210mm - 12mm (left) - 12mm (right) = **186mm**
- Exercise name text box: Starts at 12mm, width 128mm → ends at 140mm
- Logo: Width 57mm, right edge at 198mm → left edge at 141mm
- **Gap between text and logo: 141mm - 140mm = 1mm** ✓
- This tight but functional layout means long exercise names will wrap to 2 lines

**Logo Sizing Calculation:**
- Logo aspect ratio: ~11.44:1 (width:height)
- At 5mm height → ~57mm width
- Positioned top-right corner of header

---

## Phase 5: Anatomy Section

### Step 11: Create Anatomy Background

1. Select "Anatomy Section" layer
2. Rectangle Tool (M)
3. Draw rectangle:
   - **X:** 0, **Y:** 36 mm (below header)
   - **Width:** 210 mm, **Height:** 74 mm
4. Fill: "CW Deep Charcoal"

### Step 12: Place Anatomical Diagrams (Placeholder)

For the prototype, we'll use placeholder rectangles. Later replace with actual diagrams.

**Front View Placeholder:**
1. Rectangle Tool (M)
2. Draw rectangle:
   - **Width:** 40 mm, **Height:** 65 mm
3. Position: Left side of anatomy section (centered vertically, 20mm from left edge)
4. Fill: 30% gray
5. Stroke: 1pt, "CW Off-White"

**Add "FRONT VIEW" label:**
1. Type Tool (T)
2. Type: "FRONT VIEW"
3. Font: Montserrat Regular, **10pt**, "CW Muted/Secondary"
4. Position: Centered above rectangle (2mm gap from top of section)

**Rear View Placeholder:**
1. Duplicate front view rectangle (Alt/Option + Drag)
2. Position: Right side of anatomy section (20mm from right edge)
3. Change label to: "REAR VIEW"

**Illustrator 30.0 Tip:** Use **Smart Guides** (Cmd/Ctrl + U) to easily align the two diagrams at the same vertical position

### Step 13: Add Muscle Labels

**Primary Muscles:**
1. Type Tool (T)
2. Type: "PRIMARY MUSCLES:"
3. Font: Montserrat Bold, **11pt**, "CW Off-White"
4. Position: In center area between diagrams, or below diagrams

**Muscle List:**
1. Type Tool (T)
2. Type: "• Pectoralis Major"
3. Font: Montserrat Regular, **12pt**, "CW Off-White"
4. Position: Below "PRIMARY MUSCLES:" label (2mm gap)
5. Line height (Leading): **20pt**
6. Duplicate for additional muscles

**Secondary Muscles:**
1. Repeat above process
2. Label: "SECONDARY MUSCLES:"
3. Label color: "CW Muted/Secondary" (not Off-White)
4. List muscles: "• Anterior Deltoid • Triceps Brachii"
5. List color: "CW Muted/Secondary" (lighter than primary)

---

## Phase 6: Equipment Section

### Step 14: Equipment Details

1. Select "Equipment Section" layer
2. Rectangle Tool (M)
3. Draw rectangle:
   - **X:** 0, **Y:** 110 mm
   - **Width:** 210 mm, **Height:** 20 mm
4. Fill: "CW Deep Charcoal"

**Add Label:**
1. Type Tool (T)
2. Type: "EQUIPMENT"
3. Font: Montserrat Bold, **11pt**, "CW Muted/Secondary"
4. Position: 12mm from left, centered vertically in the section

**Add Equipment List:**
1. Type Tool (T)
2. Type: "Barbell, Flat Bench"
3. Font: Montserrat Regular, **12pt**, "CW Off-White"
4. Position: To the right of the label, centered vertically

---

## Phase 7: Instructions Section

### Step 15: Create Instructions Background with Red Border

1. Select "Instructions Section" layer
2. Rectangle Tool (M)
3. Draw rectangle:
   - **X:** 0, **Y:** 130 mm
   - **Width:** 210 mm, **Height:** 95 mm
4. Fill: "CW Deep Charcoal"

**Add Left Border Accent:**
1. Rectangle Tool (M)
2. Draw thin rectangle:
   - **X:** 0, **Y:** 130 mm
   - **Width:** 5 mm, **Height:** 95 mm
3. Fill: "CW Accent Red"
4. No stroke

### Step 16: Add "HOW TO PERFORM" Instructions

**Heading:**
1. Type Tool (T)
2. Type: "HOW TO PERFORM"
3. Font: Montserrat Bold, **13pt**, "CW Off-White"
4. Position: 15mm from left (after red border), 8mm from top of section

**Instructions List:**
1. Type Tool (T) - Click and drag to create text box
2. Create text box:
   - Start: 15mm from left (10mm after red border)
   - Width: 180mm (leaves 15mm margin on right)
   - Position: 4mm below heading
3. Type numbered instructions:
   ```
   1. Lie flat on bench with eyes directly under the bar
   2. Grip the bar slightly wider than shoulder width
   3. Unrack the bar with straight arms
   4. Lower the bar with control to mid-chest
   5. Press the bar back up to starting position
   ```
4. **Paragraph Panel** (**Window > Type > Paragraph** or Cmd/Ctrl + Alt + T):
   - Font: Montserrat Regular, **12pt**
   - Leading: **20pt** (line height)
   - Fill: "CW Off-White"
   - Left indent: 6mm (for hanging indent)
   - First line indent: -6mm (creates number outdent)

**Illustrator 30.0 Note:** Paragraph settings are also accessible in the Properties panel when text is selected

### Step 17: Add Coaching Points

**Heading:**
1. Type Tool (T)
2. Type: "COACHING POINTS"
3. Font: Montserrat Bold, **13pt**, **"CW Accent Red"** (note: red, not white)
4. Position: Below instructions (6mm gap)

**Bullet List:**
1. Create text box (same width as instructions: 180mm)
2. Type bulleted points:
   ```
   • Maintain scapular retraction throughout
   • Initiate the press with leg drive
   • Bar path should be slightly diagonal
   ```
3. Font: Montserrat Regular, **11pt**, "CW Off-White"
4. Leading: **19pt**
5. Position: 4mm below heading

---

## Phase 8: Exercise Illustration Section

### Step 18: Illustration Placeholder

1. Select "Exercise Illustration" layer
2. Rectangle Tool (M)
3. Draw rectangle:
   - **X:** 0, **Y:** 225 mm
   - **Width:** 210 mm, **Height:** 50 mm
4. Fill: "CW Deep Charcoal"

**Add Placeholder Images:**
1. Create two squares (side-by-side)
2. Each: **40mm × 40mm**
3. Fill: 30% gray, Stroke: 1pt "CW Off-White"
4. Add labels above each:
   - "START POSITION" and "END POSITION"
   - Font: Montserrat Regular, **10pt**, "CW Muted/Secondary"
5. Space evenly with **10mm gap** between them
6. Center the group (both boxes and labels) horizontally and vertically within the illustration section

---

## Phase 9: Tracking Fields Section

### Step 19: Create Tracking Background

1. Select "Tracking Fields" layer
2. Rectangle Tool (M)
3. Draw rectangle:
   - **X:** 0, **Y:** 275 mm
   - **Width:** 210 mm, **Height:** 22 mm
4. Fill: "CW Deep Charcoal"
5. Add subtle top border:
   - Draw thin rectangle at top edge
   - **Width:** 210mm, **Height:** 0.5mm
   - Fill: "CW Accent Red" at 20% opacity

### Step 20: Add Field Labels and Boxes

**Labels:**
1. Type Tool (T)
2. Create four labels in a single row: "SETS", "REPS", "WEIGHT / TIME", "REST"
3. Font: Montserrat Bold, **10pt**, "CW Muted/Secondary"
4. Position the row of labels so it is centered vertically in the top half of the section.
5. Use the **Align panel** to distribute the labels evenly horizontally across the artboard (from margin to margin).

**Input Boxes:**
1. Rounded Rectangle Tool
2. For each label, create an input box below it:
   - **Height:** 10mm
   - **Corner Radius:** 2mm
3. **Width:** Adjust the width of each box to be appropriate for its content (e.g., "WEIGHT / TIME" will need more width than "SETS").
4. Fill: "CW Deep Charcoal"
5. Stroke: 0.5pt, "CW Muted/Secondary" at 50% opacity
6. Position each box directly below its corresponding label.
7. Use the **Align panel** to ensure the boxes are distributed evenly, matching the label distribution.

**Illustrator 30.0 Tip:** Select all boxes, then use **Align To Selection > Distribute Horizontal Centers** to create even spacing.

---

## Phase 10: Footer Section

### Step 21: Create Footer

1. Select "Footer" layer
2. Rectangle Tool (M)
3. Draw rectangle:
   - **X:** 0, **Y:** 285 mm
   - **Width:** 210 mm, **Height:** 12 mm
4. Fill: "CW Deep Charcoal"

**Verification:** Total height = 36 + 74 + 20 + 95 + 50 + 22 + 12 = **297mm** ✓ (perfect A4)

**Add Tagline:**
1. Type Tool (T)
2. Type: "Train Like an Athlete. Live Like You."
3. Font: Montserrat Regular, **9pt**, "CW Muted/Secondary"
4. Position: Centered vertically and horizontally in footer

**Add Page Number (optional):**
1. Type Tool (T)
2. Type: "[1]"
3. Font: Montserrat Regular, **9pt**, "CW Muted/Secondary"
4. Position: Right-aligned, 12mm from right edge

---

## Phase 11: Final Touches

### Step 22: Review and Adjust

1. **View > Guides > Hide Guides** (Cmd/Ctrl + ;) - toggle to check alignment without guide clutter
2. **View > Fit Artboard in Window** (Cmd/Ctrl + 0) - see full card at once
3. Check all text is legible at actual size
4. Verify color accuracy:
   - **View > Proof Setup > Working CMYK**
   - **View > Proof Colors** (Cmd/Ctrl + Y) to toggle soft proof
5. Adjust spacing if needed using arrow keys (hold Shift for 10x movement)

**Illustrator 30.0 Features:**
- Use **View > Preview on Device** to see how it looks on mobile/tablet
- Use **View > Trim View** (Alt/Option + Cmd/Ctrl + 0) to preview without bleed area

### Step 23: Create Character Styles (Optional but Recommended)

1. **Window > Type > Character Styles**
2. Select exercise name text
3. Click "New Style" in Character Styles panel
4. Name: "Exercise Name"
5. Repeat for:
   - "Section Label"
   - "Body Text"
   - "Coaching Point"
   - "Footer Text"

This makes it easy to apply consistent styling later.

### Step 24: Save Versions

**Save Working File:**
1. **File > Save** (Cmd/Ctrl + S)
2. Name: `CoachWhitt_Barbell_Bench_Press_WORKING.ai`
3. Keep all layers editable

**Save as Template:**
1. **File > Save As**
2. Format: Adobe Illustrator Template (.ait)
3. Name: `CoachWhitt_Exercise_Card_Template.ait`

**Export PDF (Print Quality):**
1. **File > Export > Export As** (Cmd/Ctrl + E in Illustrator 30.0)
2. Format: Adobe PDF (pdf)
3. Name: `CoachWhitt_Barbell_Bench_Press_A4_Prototype.pdf`
4. In the **Export Adobe PDF** dialog:
   - **Adobe PDF Preset:** [High Quality Print] or [Press Quality]
   - **Compatibility:** Acrobat 6 (PDF 1.5) or later
5. **General tab:**
   - ☑ Preserve Illustrator Editing Capabilities (for future edits)
   - ☑ Embed Page Thumbnails
   - ☑ Optimize for Fast Web View (recommended for digital use)
6. **Marks and Bleeds tab:**
   - ☑ Use Document Bleed Settings (includes the 3mm bleed)
   - ☐ All Printer's Marks (uncheck unless printing professionally)
   - ☑ Trim Marks (optional - useful for print verification)
7. **Output tab:**
   - Color Conversion: **Convert to Destination (Preserve Numbers)**
   - Destination: **Coated FOGRA39 (ISO 12647-2:2004)** (standard European print)
   - Profile Inclusion Policy: **Include Destination Profile**
8. Click **Export PDF**

**For Digital-Only PDF (smaller file size):**
1. Use preset: **Smallest File Size**
2. Resolution: 150 PPI (sufficient for screens)
3. Uncheck "Preserve Illustrator Editing Capabilities"

**For A5 Print Version:**
1. **File > Save As** a copy first
2. **Object > Transform > Scale**
3. Scale: **71%** (uniform scaling)
4. This converts A4 to A5 proportionally
5. Change artboard size to 148mm × 210mm
6. Export as PDF

---

## Phase 12: Review and Iterate

### Step 25: Print Test

1. Print PDF on **A4 paper at 100% scale**
2. Check:
   - Text legibility (all text should be clearly readable)
   - Color accuracy (compare to brand guide - note: screen colors differ from print)
   - Spacing and alignment (use ruler to verify margins)
   - Overall visual balance and hierarchy
3. **Optional:** Print scaled version at 71% on A5 paper to test smaller format
4. View PDF on mobile device to test digital legibility

### Step 26: Get Feedback

1. Review with stakeholders
2. Note requested changes:
   - Color adjustments
   - Text sizing
   - Layout modifications
3. Iterate design based on feedback

### Step 27: Finalize Prototype

Once approved:
1. Make final adjustments
2. **Convert all text to outlines** (Type > Create Outlines)
   - **IMPORTANT:** Save a copy with editable text first!
3. Export final PDF as per Step 24
4. Document any custom specifications

---

## Tips and Troubleshooting

### Alignment Tips

1. Use **Align Panel** (Shift + F7) frequently
2. **Smart Guides** (Cmd/Ctrl + U) help with positioning
3. **Snap to Grid** (View > Snap to Grid) for precise placement
4. Use **Transform Panel** for exact numerical positioning

### Working with Colors

1. If colors look different on screen vs. print:
   - **View > Proof Setup > Working CMYK**
   - **View > Proof Colors** (Cmd/Ctrl + Y)
2. For spot colors (Pantone):
   - Window > Swatch Libraries > Color Books > Pantone+ CMYK Coated
   - Find Pantone 2028 C for accent red

### Text Formatting

1. For consistent spacing, use:
   - **Type > Area Type Options**
   - Set consistent insets (5mm recommended)
2. For multiple text boxes with same styling:
   - Use Character Styles and Paragraph Styles
   - Apply globally with one click

### Layer Management

1. Name all layers descriptively
2. Lock completed layers
3. Hide layers when working on others (click eye icon)
4. Use layer colors for visual organization

### File Size Management

1. **Embed images** instead of linking (for portability)
2. **File > Document Setup > Transparency:**
   - Choose "High Resolution" for print
3. Before final export:
   - **File > Clean Up** (remove unused swatches, etc.)

---

## Next Steps After Prototype Approval

### 1. Create Template Variations

- Male version template
- Female version template
- Templates for different muscle groups
- Templates for different exercise illustration layouts

### 2. Batch Production Workflow

1. Keep master template (.ait)
2. For each exercise:
   - Open template
   - Replace text content
   - Replace anatomical diagrams
   - Replace exercise illustration
   - Save as new file
   - Export PDF

### 3. Automation Considerations

For generating 100+ cards, consider:
- **Adobe Illustrator Scripting** (JavaScript):
  - Automate text replacement from JSON data
  - Batch export PDFs
- **Variable Data / Data Merge**:
  - Link Illustrator to CSV/JSON file
  - Auto-generate multiple variations
- **Python + Illustrator Scripting**:
  - Full automation pipeline
  - Integrate with exercise database

### 4. Asset Library Creation

Before bulk production:
1. Create all anatomical diagrams (male/female, all muscle groups)
2. Create all exercise illustrations
3. Organize in folder structure:
   ```
   /anatomy_assets/
     /male/
       chest_front.svg
       chest_rear.svg
     /female/
       chest_front.svg
       chest_rear.svg
   /exercise_illustrations/
     barbell_bench_press.svg
   ```
4. Maintain consistent naming conventions

---

## Checklist: Prototype Completion

Before considering the prototype complete:

**Document Setup:**
- [ ] Artboard size: 210mm × 297mm (A4)
- [ ] Resolution: 300 DPI (2480 × 3508 pixels)
- [ ] Color mode: CMYK
- [ ] Bleed: 3mm on all sides
- [ ] Safe area: 8mm margins from edges

**Brand Compliance:**
- [ ] All section backgrounds use the unified "CW Deep Charcoal" color.
- [ ] All brand colors match specification exactly (Deep Charcoal, Off-White, Accent Red).
- [ ] Montserrat font used throughout (no fallback fonts).
- [ ] Logo present and sized at 5mm height (~57mm width).
- [ ] Logo positioned correctly (top-right, right edge at 198mm, 8mm from top).

**Layout & Content:**
- [ ] All section heights total 297mm exactly.
- [ ] Header: 36mm (exercise name 30pt in 128mm text box + movement badge + logo 5mm).
- [ ] Anatomy: 74mm (diagrams 40mm × 65mm each).
- [ ] Equipment: 20mm.
- [ ] Instructions: 95mm (with 5mm red border).
- [ ] Illustration: 50mm (placeholders 40mm × 40mm).
- [ ] Tracking: 22mm (4 evenly spaced fields, including "WEIGHT / TIME").
- [ ] Footer: 12mm (tagline centered).

**Text Legibility:**
- [ ] All text is legible at actual size (both screen and print).
- [ ] Line heights (leading) provide good readability.
- [ ] Coaching points in Accent Red are clearly visible.
- [ ] Muted/Secondary text is distinguishable but not distracting.

**Quality Checks:**
- [ ] Red accent border on left side of instructions section.
- [ ] Tracking fields are properly labeled and distributed evenly.
- [ ] Footer contains tagline only (no scientific reference).
- [ ] PDF exports at 300 DPI without errors.
- [ ] Print test on A4 paper completed successfully.
- [ ] Digital preview on mobile/tablet looks good.
- [ ] Stakeholder feedback incorporated.

**File Management:**
- [ ] Working file saved as .ai with editable text.
- [ ] Template saved as .ait.
- [ ] PDF exported with proper naming convention.

---

## Resources

**CoachWhitt Brand Resources:**
- Visual Brand Guide: `./context_files/04-visual-brand-guide.md`
- Logo: `./context_files/05-logo-main.svg`
- Visual Mockup: `exercise_card_visual_mockup.md`
- Card Specification: `exercise_card_specification.md`

**External Resources:**
- Montserrat Font: https://fonts.google.com/specimen/Montserrat
- Adobe Illustrator Tutorials: https://helpx.adobe.com/illustrator/tutorials.html
- CMYK Color Conversion: https://www.pantone.com/color-finder

**Anatomical Diagram Sources:**
- Shutterstock (search: "anatomy muscle illustration")
- Custom 3D rendering services
- Medical illustration stock libraries

---

## Contact

**Questions about this guide:**
- Refer to exercise card specification for layout details
- Refer to visual brand guide for color/typography questions
- Review visual mockup for exact measurements

**Project Owner:** Dean Whittingslow (CoachWhitt)
**Website:** https://coachwhitt.com
**Email:** info@coachwhitt.com

---

**CoachWhitt** | Train Like an Athlete. Live Like You.
