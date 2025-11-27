# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

---

## Project Overview

This is the **CoachWhitt Exercise Templates** project - a content development repository for creating a comprehensive, scientifically-grounded exercise database and branded exercise card system for the CoachWhitt personal training business.

**Business Context:** CoachWhitt is a personal training and elite sports coaching business based in Worksop, UK, led by Dean Whittingslow (Team GB Women's American Flag Football coach, 2023 European Champions).

---

## Repository Structure

### Key Directories

**`./origym/`**
- Primary reference material: Professional fitness certification course content (Levels 2, 3, and 4)
- Contains PDFs covering anatomy, exercise physiology, nutrition, biomechanics, and training methodologies
- **IMPORTANT:** This is the foundational knowledge base and must be reviewed first before using external sources

**`./context_files/`**
- Complete CoachWhitt brand reference materials
- Essential documents:
  - `00-README.md` - Navigation guide for all brand materials
  - `01-universal-principles.md` - The "3 Cs" content framework (Candid & Credible, Caring & Compassionate, Champion & Celebratory)
  - `02-coachwhitt-framework.md` - Social media strategy, content pillars, marketing principles
  - `03-brand-outline.md` - Company mission, target audience, USP, brand story
  - `04-visual-brand-guide.md` - Complete visual specifications (colors, typography, logo usage, design system)
  - Logo files (SVG and PNG formats)

**`./example images/`**
- Reference images showing anatomical muscle highlighting styles
- Examples of male/female anatomy visualization for exercise cards
- Style guide for future video asset generation

### Key Files

**`exercise_research_prompt.md`**
- Master specification document for the exercise database project
- Defines data structure, required fields, research methodology, and output format
- Reference this for understanding project requirements and deliverables

**`comprehensive_exercise_database.md`**
- Generated exercise database with 100+ scientifically-validated exercises
- Organized by muscle group with complete metadata for each exercise
- Includes scientific references, equipment requirements, instructions, and sports tags

---

## Research and Content Development Protocol

### Data Source Hierarchy

1. **PRIMARY:** Always review `./origym/` course materials first
2. **SECONDARY:** Use reputable scientific literature and peer-reviewed sources after Origym review
3. **VALIDATION:** Cross-reference with EMG studies, biomechanical research, and meta-analyses

### Exercise Database Requirements

Each exercise must include:
- Exercise name
- Primary and secondary muscles worked
- Type (Compound/Isolation)
- Equipment needed
- Step-by-step beginner instructions
- 3-5 advanced coaching cues
- Scientific reference with DOI/URL
- Applicable sports tags

**Coverage Requirements:**
- Minimum 8 exercises per muscle group
- Mix of equipment types: bodyweight, free weights, machines, cables (at least 2 of each)
- All major muscle groups: Chest, Back, Shoulders, Arms, Legs, Glutes, Core, Calves, Forearms, Neck

---

## Brand Voice and Content Creation

### The "3 Cs" Framework (CRITICAL)

All content must embody:

1. **Candid & Credible**
   - Honest, direct communication
   - Evidence-based information
   - No fluff or false promises

2. **Caring & Compassionate**
   - Supportive and encouraging tone
   - Understanding of client challenges
   - Non-judgmental approach

3. **Champion & Celebratory**
   - Celebrate client wins
   - Positive reinforcement
   - Focus on progress and achievement

### Target Audience

- **Beginners:** Need approachable guidance and foundational knowledge
- **Experienced Athletes:** Want technical precision and performance optimization
- **Career Professionals & Parents:** Need practical solutions that fit busy lifestyles

### Brand Personality

**Friendly, Encouraging, Candid**
- Avoid corporate jargon
- Use conversational but professional tone
- Show the human side of coaching

---

## Visual Brand Standards

### Colors

**Primary Palette:**
- Deep Charcoal: `#1E1F22` (backgrounds)
- Off-White: `#EBE7D9` (text)
- Accent Red: `#F55139` (CTAs, highlights)

For complete color specifications (RGB, CMYK, Pantone), typography, and design system, refer to `./context_files/04-visual-brand-guide.md`.

### Logo Usage

- Primary: Use `05-logo-main.svg` (90% of applications)
- PNG variants available for specific use cases
- Never modify logo colors or proportions

### Typography

- Primary font: **Montserrat** (Google Fonts)
- Full specifications in visual brand guide

---

## Project State - Current Workflow Phase

### Completed Phases

**Phase 1: Exercise Database (COMPLETED)**
- [x] Comprehensive exercise database with 100+ exercises
- [x] Scientific validation and references
- [x] Organized by 11 muscle groups
- [x] Modular data structure for automation

**Phase 2a: Exercise Card Design Specifications (COMPLETED)**
- [x] Card layout structure and design system
- [x] JSON data structure and schemas
- [x] Visual mockups with exact measurements
- [x] Adobe Illustrator implementation guide (60+ pages)
- [x] Brand compliance documentation

**Phase 2b: Anatomical Diagram Sourcing Research (COMPLETED)**
- [x] Analysis of 15+ sourcing methods
- [x] Cost-benefit analysis ($0-$100,000)
- [x] Decision: Custom Blender 3D + Z-Anatomy
- [x] Complete Blender workflow documentation (4 guides, ~55,000 words)

### Current Phase - Implementation Ready (Weeks 1-2)

**Phase 2c: Card Design Implementation (NEXT - IMMEDIATE)**
- [ ] Create Adobe Illustrator prototype (1 card)
- [ ] Get design approval from stakeholder
- [ ] Finalize card template

**Phase 2d: Blender Setup & Learning (PARALLEL - WEEKS 1-4)**
- [ ] Install Blender and Z-Anatomy
- [ ] Complete Blender fundamentals (Donut Tutorial)
- [ ] Create first 5 practice renders
- [ ] Refine workflow based on learning

### Future Development Phases

**Phase 2e: Template Finalization (Weeks 3-4)**
- Adobe Illustrator master template
- Blender reusable setup file
- JSON database conversion tools

**Phase 2f: Production Phase 1 (Weeks 5-8)**
- First 150+ exercise renders in Blender
- First 50+ exercise cards in Illustrator
- Quality refinement and process optimization

**Phase 2g: Production Phase 2 (Weeks 9-12)**
- Remaining 250+ exercise renders
- Remaining 50+ exercise cards
- Final quality assurance

### Phase 3: Video Assets (TBD)
- Short instructional videos per exercise
- Dynamic muscle highlighting during movement
- Male and female versions
- Style reference: Files in `./example images/` (101/102 prefix)

### Phase 4: Program Generation System (TBD)
- Automated workout plan creation from exercise database
- Multi-week session planning
- Session documents with goals and exercise cards
- File format: `Client Name - Week # - Session # - Exercise Name`

---

## Working with Gemini Research

When using Gemini for research tasks:

```bash
gemini -p @exercise_research_prompt.md
```

This command references the master research prompt for structured data gathering.

---

## Brand Story Context

Dean Whittingslow (CoachWhitt) coached Team GB Women's American Flag Football team to:
- European Silver Medal (2019)
- European Gold Medal (2023)
- World #4 ranking (2023)

This elite coaching background differentiates CoachWhitt from general personal trainers and informs the "Champion & Celebratory" brand pillar.

---

## Important Notes

- **No emojis** unless explicitly requested (professional tone without corporate stiffness)
- **Evidence-based approach:** Always cite scientific sources for exercise recommendations
- **Modular design:** Content must be reusable across multiple client programs
- **Accessibility:** All materials should be beginner-friendly while offering depth for advanced users
- **Brand consistency:** Every output must align with the 3 Cs framework and visual brand standards

---

## Session Notes & Key Decisions

### Session 2025-11-11 Morning (Documentation & Specification Phase)

**Major Accomplishments:**
1. Completed 100+ exercise database with full scientific backing
2. Created complete card design specification system (7 documents)
3. Researched and decided on anatomical diagram sourcing method
4. Generated 4 comprehensive Blender workflow guides (~55,000 words)
5. Prepared project for implementation phase

**Key Decisions Made:**
1. **Anatomical Diagrams:** Blender + Z-Anatomy (custom 3D, zero cost vs $5K-$25K alternatives)
2. **Card Content Scope:** Separated client-facing items from database-only items (sports tags, references database-only)
3. **Card Format:** A5 portrait (148mm × 210mm) at 300 DPI for print quality [LATER REVISED]
4. **Data Architecture:** JSON-based modular structure for future automation
5. **Learning Path:** Dual-track approach (card design + Blender learning can run parallel)

---

### Session 2025-11-11 Afternoon (Specification Correction & Optimization Phase)

**Major Accomplishment:**
- Identified critical sizing errors in Adobe Illustrator guide (v1.0)
- Resolved format and sizing issues through comprehensive revision
- Delivered tested, validated specifications ready for implementation

**Critical Issues Fixed:**
1. **Logo Size Problem:** Original 15mm height would create 206mm width—impossible to fit
2. **Layout Cramping:** A5 format inadequate for anatomical diagram detail
3. **Text Overlap:** Exercise name and logo would overlap in header section

**Solution Implemented:**
1. **Format Change:** A5 (148mm × 210mm) → A4 (210mm × 297mm)
   - Provides 42% more area for anatomical detail
   - Better for professional exercise reference materials
   - Digital viewing improved (2480 × 3508px at 300 DPI)
   - Can scale to 71% for A5 if future pocket cards needed

2. **Logo Sizing Fixed:** 15mm → 5mm height
   - 5mm height = ~57mm width (calculated from aspect ratio)
   - Header layout: Exercise name (128mm text box) + 1mm gap + Logo (57mm)
   - Tested and verified to fit without overlap

3. **Complete Recalculation:** All section heights and typography adjusted for A4
   - All heights now sum to exactly 297mm
   - Anatomy section increased to 82mm (supports detailed diagrams)
   - Typography scale optimized for larger format
   - Professional spacing and hierarchy maintained

4. **Software Update:** Updated for Adobe Illustrator 30.0 (current version)
   - Added keyboard shortcuts throughout
   - Updated Properties panel references
   - Updated PDF export workflow

**Files Modified This Session:**
- `adobe_illustrator_prototype_guide.md` (v1.0 → v2.0, complete revision)

**Sessions Summary Files:**
- `002 - session-summary.md` (morning session - documentation phase)
- `003 - session-summary.md` (afternoon session - specification correction)

**Total Documentation:** ~65,000 words, 13 files (12 + this session's revision)

**Immediate Next Steps (Week 1):**
1. Follow revised `adobe_illustrator_prototype_guide.md` (v2.0) for Adobe Illustrator prototype
2. Start Blender learning in parallel (install + Donut Tutorial)
3. Both tracks can proceed simultaneously

**Timeline to Completion:** 12 weeks from 2025-11-11 (estimated completion: 2026-02-02)

**Critical Change:** Card format changed from A5 to A4, but no timeline impact. This actually improves quality and prevents implementation errors.

**For Next Session:**
- Read: `003 - session-summary.md` for complete specification correction context
- Reference: Revised `adobe_illustrator_prototype_guide.md` (v2.0) is now accurate and tested
- Action: Begin Adobe Illustrator prototype using Phase 1 (Document Setup) from revised guide
- Alt: Start Blender learning in parallel using `blender_quick_start_checklist.md`

---

## GitHub Sync Configuration

- **GitHub Repository:** https://github.com/coachwhitt/002---Exercise-Templates
- **GitHub Branch:** main

---

**CoachWhitt** | Train Like an Athlete. Live Like You.
