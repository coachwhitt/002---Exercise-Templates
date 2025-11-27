# CoachWhitt Exercise Templates

A comprehensive, scientifically-grounded exercise database and branded exercise card system for CoachWhitt personal training and elite sports coaching.

## Project Status

**Current Phase:** Database Enhancement & Implementation Ready (Phase 2c/2d)
**Completion:** 21.6% (80 of 370 planned exercises documented)
**Last Updated:** 2025-11-27

## What This Project Is

This repository contains the foundational systems for creating professional, scientifically-backed exercise content for CoachWhitt:

1. **Exercise Database** - Comprehensive exercise library with 80+ exercises (with plans for 370+ total)
2. **Card Design System** - Professional A4 exercise cards with anatomical diagrams, coaching cues, and scientific backing
3. **Blender Workflow** - Custom 3D anatomical diagram generation pipeline using Blender + Z-Anatomy
4. **Brand Integration** - CoachWhitt visual standards, typography, and "3 Cs" framework applied throughout

## Key Features

- **Scientific Backing** - All exercises include peer-reviewed research citations
- **Comprehensive Metadata** - 15 columns of exercise data per exercise (muscle groups, equipment, level, movement patterns, coaching cues, video links)
- **Multi-Level Design** - Content suitable for beginners, intermediate, and advanced athletes
- **Video-Ready** - Integrated links to ExRx, JEFIT, and placeholder for custom CoachWhitt videos
- **Production-Ready CSV** - All data exportable to Google Sheets and integration systems

## Quick Stats

| Metric | Status |
|--------|--------|
| Exercises Completed | 80/370 (21.6%) |
| Muscle Groups Covered | 8 major groups |
| Scientific References | 80 peer-reviewed citations |
| Video Links | Session 1 complete, Sessions 2-5 pending |
| Card Design | Specifications complete, implementation ready |
| Blender Documentation | Complete (4 comprehensive guides) |

## What's Inside

### Core Files

- **`comprehensive_exercise_database_v2.md`** - Main exercise database with 80 documented exercises
- **`exercise_database_complete_v2.csv`** - CSV export for Google Sheets and automation
- **`adobe_illustrator_prototype_guide.md`** - Complete A4 card design specifications (v2.0)
- **`exercise_card_specification.md`** - Card layout, structure, and design system
- **`programme_card_template.gs`** - Google Apps Script for automated workout generation

### Documentation

- **Session Summaries:**
  - `002 - session-summary-2025-11-27.md` - Current session overview
  - `SESSION1_SUMMARY.md` - CHEST exercises (10) and data structure corrections
  - `SESSIONS_2-5_SUMMARY.md` - BACK, SHOULDERS, ARMS, LEGS, CORE (70 exercises)

- **Context Files:** (`./context_files/`)
  - `00-README.md` - Navigation guide for brand materials
  - `01-universal-principles.md` - The "3 Cs" framework (Candid & Credible, Caring & Compassionate, Champion & Celebratory)
  - `02-coachwhitt-framework.md` - Social media strategy and content pillars
  - `03-brand-outline.md` - Company mission, target audience, USP
  - `04-visual-brand-guide.md` - Complete visual specifications, colors, typography

### Research & Reference

- **`research_prompt.md`** - Master specification for exercise database structure
- **`RESEARCH_Anatomical_Diagram_Sourcing.md`** - Analysis of diagram sourcing methods (selected: Blender + Z-Anatomy)
- **`origym/`** - Professional fitness certification materials (Levels 2, 3, 4)
- **`example images/`** - Reference images for anatomical highlighting and video styles

## Current Progress

### Completed Phases

**Phase 1: Exercise Database Foundation (COMPLETED)**
- Comprehensive exercise database with 100+ exercises
- Scientific validation and references
- Organized by muscle group
- Modular data structure for automation

**Phase 2a: Card Design Specifications (COMPLETED)**
- Card layout structure and design system
- JSON data structures
- Visual mockups with exact measurements
- Adobe Illustrator implementation guide (60+ pages)

**Phase 2b: Anatomical Diagram Research (COMPLETED)**
- Analysis of 15+ sourcing methods
- Decision: Custom Blender 3D + Z-Anatomy
- Complete Blender workflow documentation (~55,000 words)

**Phase 2c/2d: Database Enhancement & Implementation (IN PROGRESS)**
- Session 1-5: Enhanced database structure (80 exercises completed, 21.6%)
- Video link research (Session 1 complete, Sessions 2-5 pending)
- CSV export system ready for integration

### Next Phases

**Phase 2e: Template Finalization (Planned)**
- Adobe Illustrator master template refinement
- Blender reusable setup file
- Automation tools for batch processing

**Phase 2f/2g: Production (Planned)**
- 150+ exercise anatomical renders in Blender
- 50+ exercise cards in Adobe Illustrator
- Quality assurance and optimization

**Phase 3: Video Assets (Planned)**
- Short instructional videos per exercise
- Dynamic muscle highlighting during movement
- Male and female versions

**Phase 4: Program Generation (Planned)**
- Automated workout plan creation
- Multi-week session planning
- Client delivery documents

## Using This Project

### For Exercise Database Access

1. Review `comprehensive_exercise_database_v2.md` for exercise details
2. Import `exercise_database_complete_v2.csv` into Google Sheets
3. Use with `programme_card_template.gs` for workout generation

### For Card Design

1. Read `adobe_illustrator_prototype_guide.md` (v2.0)
2. Follow Phase 1 (Document Setup) for initial Adobe Illustrator configuration
3. Reference `exercise_card_specification.md` for layout details

### For Anatomical Diagrams

1. Review Blender workflow guides in documentation
2. Install Blender and Z-Anatomy add-on
3. Follow provided rendering pipeline

### For Brand Compliance

1. Review `context_files/04-visual-brand-guide.md` for visual standards
2. Follow "3 Cs" framework from `context_files/01-universal-principles.md`
3. Use approved colors: Deep Charcoal (#1E1F22), Off-White (#EBE7D9), Accent Red (#F55139)

## Known Issues

### Character Encoding (Priority: Medium)
- Degree symbols displaying as "Â°" in some fields
- Will be resolved in next session
- Does not affect data accuracy, only display

### Video Links (Priority: Medium)
- Sessions 1: Video links populated
- Sessions 2-5: Marked as [TBD] for manual population
- User to verify accuracy before client use

## Next Session Priorities

1. **Fix Character Encoding** - Replace "Â°" with "°" in database files (5 minutes)
2. **User Review** - Validate all 80 exercises for accuracy
3. **Video Link Population** - Manually populate ExRx and JEFIT URLs for Sessions 2-5
4. **Continue Database** - Add remaining 290 exercises (CALVES, FOREARMS, NECK, Origym variations)
5. **Adobe Card Prototype** - Begin card design implementation (can run in parallel)

## Project Details

- **Business:** CoachWhitt Personal Training & Elite Sports Coaching
- **Location:** Worksop, UK
- **Director:** Dean Whittingslow (Team GB Women's American Flag Football Coach, 2023 European Champions)
- **Brand Pillars:** Candid & Credible, Caring & Compassionate, Champion & Celebratory

## Navigation

```
002 - Exercise Templates/
├── README.md (this file)
├── CLAUDE.md (AI context and workflow)
├── AGENTS.md (synchronized AI context)
├── GEMINI.md (synchronized AI context)
│
├── comprehensive_exercise_database_v2.md (Main: 80 exercises)
├── exercise_database_complete_v2.csv (Export: Google Sheets ready)
│
├── SESSION1_SUMMARY.md (Session 1: CHEST - 10 exercises)
├── SESSIONS_2-5_SUMMARY.md (Sessions 2-5: 70 exercises)
├── 002 - session-summary-2025-11-27.md (This session overview)
├── NEXT_SESSION_NOTES.md (Known issues and action items)
│
├── adobe_illustrator_prototype_guide.md (Card design specs v2.0)
├── exercise_card_specification.md (Card structure details)
├── exercise_card_visual_mockup.md (Visual reference)
├── programme_card_template.gs (Google Apps Script)
│
├── context_files/ (Brand materials and guidelines)
│   ├── 00-README.md
│   ├── 01-universal-principles.md
│   ├── 02-coachwhitt-framework.md
│   ├── 03-brand-outline.md
│   ├── 04-visual-brand-guide.md
│   └── [Logo files]
│
├── origym/ (Professional certification materials)
├── example images/ (Design references)
└── [Other supporting files]
```

## Contact & Support

For questions about this project or CoachWhitt services:
- Website: [CoachWhitt]
- Coach: Dean Whittingslow

---

**CoachWhitt** | Train Like an Athlete. Live Like You.

*Project Status: Phase 2c/2d In Progress | Last Updated: 2025-11-27*

