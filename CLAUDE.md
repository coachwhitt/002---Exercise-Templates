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

**Phase 1: Exercise Database (IN PROGRESS - SYSTEMATIC BATCH EXPANSION)**
- [x] Initial comprehensive exercise database with 100+ exercises
- [x] Scientific validation and references (peer-reviewed sources)
- [x] Organized by 11 muscle groups
- [x] Modular data structure for automation (16-column JSON structure)
- [x] Batch 1a complete (20 core/abdominal exercises) - Session 7
- [x] Batch 1b complete (20 upper abdominal/back exercises) - Session 7
- [x] Batch 2a complete (20 back rowing exercises) - Session 9
- [x] Batch 2b complete (3 back + 17 biceps exercises) - Session 9
- [x] Batch 3a complete (20 advanced biceps variations) - Session 10
- [x] Batch 3b complete (1 spider curl + 10 calf + 9 chest exercises) - Session 10
- [ ] Batches 4-10 (150 exercises remaining, 6 sessions estimated)
- **Current Status:** 230/380 exercises in database (60.5% coverage of full target)
- **Remaining Work:** 150 exercises (6 more sessions estimated)

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

### Current Phase - Implementation Ready + Database Expansion (Ongoing)

**Phase 1 Continuation: Systematic Database Expansion (ACTIVE)**
- [x] Batch processing workflow established
- [x] Origym.csv progress tracking system implemented
- [x] 40 exercises added in Session 7
- [x] 40 exercises added in Session 9 (Batches 2a & 2b)
- [x] 40 exercises added in Session 10 (Batches 3a & 3b)
- [x] 25-exercise per-session batch size optimization implemented
- [ ] Continue systematic batch processing through Batches 4-10
- [ ] Target: 25 exercises per session for 6 sessions until 380 exercises complete

**Phase 2c: Card Design Implementation (NEXT - AFTER DATABASE EXPANSION PHASE)**
- [ ] Create Adobe Illustrator prototype (1 card)
- [ ] Get design approval from stakeholder
- [ ] Finalize card template

**Phase 2d: Blender Setup & Learning (PARALLEL - AFTER DATABASE EXPANSION PHASE)**
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

### Session 2025-11-28 (Exercise Database Expansion - Session 10)

*   **Phase:** Phase 1 Continuation - Exercise Database Batch Expansion (Batches 3a & 3b)
*   **Accomplishments:**
    - Completed Batch 3a integration: 20 advanced biceps exercises (lying cable, overhead cable, preacher, seated, single-arm variations)
    - Completed Batch 3b integration: 20 exercises (spider curl, 10 calf variations, 9 chest press/push-up variations)
    - Total session expansion: 190 → 230 exercises (40 exercises added)
    - All 40 exercises include 3-4 peer-reviewed scientific references with EMG data
    - Identified and implemented 25-exercise per-session batch size optimization (improved token efficiency from 75% to 55-60%)
    - Created future_session_plan_25_exercise_batches.md detailing Batches 4-10 strategy
    - Maintained consistent 16-column metadata structure across all 230 exercises
*   **Key Decisions:**
    - Batch size reduction: 40-exercise sessions (2x20) → 25-exercise sessions per remaining batches
    - Rationale: Token efficiency (55-60% vs 75%), sustainable quality maintenance, built-in research buffer
    - Expanded database target: 270 → 380 exercises (supplementary beyond base Origym coverage)
    - Timeline adjustment: 6 sessions remaining (Sessions 11-16) vs estimated 5-6 from Session 8
    - Target completion: Mid-January 2026 (vs late December previously)
    - Deferred card design & Blender learning: Continue database expansion through completion before initiating Phase 2c/2d
*   **Next Steps:**
    - Session 11: Extract Batch 4 (25 exercises, Origym.csv Lines 126-150)
    - Session 11: Research Batch 4 using Gemini with exercise_research_prompt.md
    - Session 11: Integrate Batch 4 into comprehensive_exercise_database_v2.md
    - Sessions 12-16: Continue systematic batch processing through Batch 10 (150 remaining exercises)
*   **Files Created:**
    - 010 - session-summary-2025-11-28.md (this session's comprehensive summary)
    - future_session_plan_25_exercise_batches.md (strategic planning for Batches 4-10)
    - batch_3a_exercises.txt, batch_3b_exercises.txt (reference lists)
    - format_batch3b_exercises.py (utility script)
*   **Files Modified:**
    - comprehensive_exercise_database_v2.md (190 → 230 exercises, 40 exercises added)
    - Origym.csv (100/275 COMPLETE, 175 PENDING - updated from 60/275)

### Session 2025-11-28 (Exercise Database Expansion - Session 8)

*   **Phase:** Phase 1 Continuation - Exercise Database Batch Expansion
*   **Accomplishments:**
    - Completed Batch 1a and 1b integration (40 exercises total: 110 → 150 database total)
    - Batch 1a: 20 core/abdominal exercises added and integrated
    - Batch 1b: 20 upper abdominal/back exercises added and integrated
    - Batch 2a: 20 back rowing exercises comprehensively researched (~5,800 words, ready for database integration next session)
    - Established sustainable batch processing workflow and Origym.csv progress tracking system
    - All 40 exercises maintain full 16-column metadata structure with 3-4 peer-reviewed scientific references
    - Created comprehensive session summary documentation (008 - session-summary-2025-11-28.md)
*   **Key Decisions:**
    - Batch processing strategy: 20-exercise research batches + 20-exercise integration batches = 40/session target
    - Deferred Batch 2a database integration to Session 9 to manage token budget (75% usage this session)
    - Established Origym.csv as single source of truth for 270-exercise systematic expansion
    - Research quality standard: 3-4 peer-reviewed references per exercise maintained
    - Timeline: 6-7 more sessions to complete 270-exercise database (estimated December 2025)
*   **Next Steps:**
    - Session 9: Add Batch 2a (20 rowing exercises) to comprehensive_exercise_database_v2.md
    - Session 9: Research Batch 2b (3 back + 17 biceps exercises)
    - Session 9: Add Batch 2b if time permits, mark all COMPLETE in Origym.csv
    - Sessions 10+: Continue systematic batch processing for Batches 3-7 (estimated 6-7 sessions)
*   **Files Created:**
    - 008 - session-summary-2025-11-28.md (this session's comprehensive summary)
    - back_rowing_exercises_research.md (Batch 2a: 5,800+ words, 20 exercises)
    - batch_1a_exercises.txt, batch_1b_exercises.txt, batch_2a_exercises.txt, batch_2b_exercises.txt (reference lists)
    - Python utility scripts for batch processing automation
*   **Files Modified:**
    - comprehensive_exercise_database_v2.md (110 → 150 exercises, ~1,800 lines added)
    - exercise_database_complete_v2.csv (149 exercises, regenerated)
    - Origym.csv (40/270 marked COMPLETE, 230 PENDING)
    - README.md (updated project status and navigation)
    - CLAUDE.md (this file - updated session notes and current focus)

### Session 2025-11-27 (Exercise Database Expansion - Batch 1a, 1b, and Batch 2a Research)

*   **Phase:** Phase 1 Continuation - Exercise Database Expansion
*   **Accomplishments:**
    - Added 40 exercises to comprehensive database (110 → 150 total)
    - Batch 1a complete: 20 core/abdominal exercises added and integrated
    - Batch 1b complete: 20 upper abdominal/back exercises added and integrated
    - Batch 2a complete: 20 back rowing exercises comprehensively researched (~5,800 words)
    - Established batch processing workflow and Origym.csv progress tracking system
    - All exercises maintain full 16-column metadata structure with scientific references
*   **Key Decisions:**
    - Batch processing strategy: 20-exercise batches for manageable research and quality consistency
    - Deferred Batch 2a database integration to next session to manage token usage
    - Established Origym.csv as primary progress tracking for 270-exercise Origym course coverage
    - Gemini research agent for comprehensive scientific backing with 3-4 peer-reviewed references per exercise
    - Target: 40 exercises per session for 6-7 more sessions to complete database expansion
*   **Next Steps:**
    - Add Batch 2a (20 rowing exercises) to comprehensive_exercise_database_v2.md
    - Research Batch 2b (3 back + 17 biceps exercises)
    - Extract and prepare Batch 3 from Origym.csv
    - Continue systematic batch processing through remaining 230 exercises
*   **Files Created:**
    - 007 - session-summary-2025-11-27.md
    - back_rowing_exercises_research.md (5,800+ words, 20 exercises)
    - batch_1a_exercises.txt, batch_1b_exercises.txt, batch_2a_exercises.txt, batch_2b_exercises.txt
    - Python utility scripts for batch processing
*   **Files Modified:**
    - comprehensive_exercise_database_v2.md (110 → 150 exercises)
    - exercise_database_complete_v2.csv (updated with 40 new exercises)
    - Origym.csv (40 exercises marked COMPLETE, 230 pending)

---

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

## Current Focus

### Primary Objective
Expand the comprehensive exercise database from 230 to 380 exercises through systematic batch research and integration from the Origym Professional Fitness Certification course materials, targeting 25 exercises per session for completion by mid-January 2026.

### Current Status (Session 10 - 2025-11-28)
- **Phase:** Phase 1 Continuation - Exercise Database Batch Expansion
- **Progress:** 230/380 exercises in database (60.5% coverage of full target)
- **Origym.csv Progress:** 100/275 COMPLETE (36.4%), 175 PENDING (63.6%)
- **Batch Status:**
  - Batch 1a: COMPLETE - 20 core/abdominal exercises (Session 7)
  - Batch 1b: COMPLETE - 20 upper abdominal/back exercises (Session 7)
  - Batch 2a: COMPLETE - 20 back rowing exercises (Session 9)
  - Batch 2b: COMPLETE - 3 back + 17 biceps exercises (Session 9)
  - Batch 3a: COMPLETE - 20 advanced biceps variations (Session 10)
  - Batch 3b: COMPLETE - 1 spider curl + 10 calf + 9 chest exercises (Session 10)
  - Batches 4-10: PENDING - 150 remaining exercises (6 sessions estimated)

### Immediate Action Items (Session 11)
1. **Priority 1:** Extract Batch 4 (25 exercises, Origym.csv Lines 126-150)
2. **Priority 2:** Research Batch 4 using Gemini research agent with exercise_research_prompt.md
3. **Priority 3:** Integrate Batch 4 into comprehensive_exercise_database_v2.md
4. **Priority 4:** Mark Batch 4 exercises COMPLETE in Origym.csv

### Workflow System
- **Batch Processing:** 25 exercises per session (optimized for 55-60% token efficiency)
- **Progress Tracking:** Origym.csv primary source (100/275 COMPLETE, 175 PENDING)
- **Research Agent:** Gemini with exercise_research_prompt.md for comprehensive scientific backing
- **Database Format:** 16-column structure (name, muscles, type, equipment, instructions, cues, reference, video URL, sports tags)
- **Quality Standards:** 3-4 peer-reviewed scientific references per exercise, specific Latin muscle names, 5+ sport application tags

### Completion Timeline
- **Current pace:** 25 exercises per session
- **Remaining exercises:** 150 (from 380 total target)
- **Estimated sessions to completion:** 6 more sessions (Sessions 11-16)
- **Target completion:** Mid-January 2026

### Token Budget Management
- Session 10 usage: 110-115K/200K tokens (55-60%)
- Strategy: 25-exercise batch per session for sustainable quality and token efficiency
- Improved efficiency: Reduced from 40-exercise to 25-exercise sessions
- Built-in buffer: 85-90K tokens available per session for additional research iterations

### Parallel Track (Post-Database Expansion)
After database expansion completes (estimated mid-January 2026):
- **Phase 2c:** Adobe Illustrator card design implementation (with Blender anatomy renders)
- **Phase 2d:** Blender 3D setup and learning (parallel with card design)
- **Phase 2e:** Template finalization and automation tools
- **Estimated timeline:** 4-8 weeks for phases 2c-2e (January-February 2026)
- **Phase 3 & 4:** Video assets and program generation (post-templates, March+ 2026)

### Status:
- **Infrastructure:** 60.5% complete (230/380 exercises)
- **Content:** Phase 1 systematic expansion in progress
- **Execution:** Card design and Blender phases deferred to January 2026
- **Timeline:** On track for mid-January completion

---

## GitHub Sync Configuration

- **GitHub Repository:** https://github.com/coachwhitt/002---Exercise-Templates
- **GitHub Branch:** main

---

**CoachWhitt** | Train Like an Athlete. Live Like You.
