# CoachWhitt Visual Brand Guide

This is the master visual reference for the CoachWhitt brand. All color specifications, logo files, typography, and design guidelines are defined here.

For brand identity, messaging, and personality, refer to `03-brand-outline.md`.

---

## Logo Files & Usage

### Available Logo Files

**`05-logo-main.svg`**
- **Format:** Scalable Vector Graphics (SVG)
- **Usage:** Primary logo for ALL scalable applications
- **Best for:** Web, print, signage, branded merchandise
- **Advantages:** Infinite scalability without quality loss
- **File size:** 3.4 KB

**`06-logo-png-dark-bg.png`**
- **Format:** PNG (raster, high-resolution)
- **Usage:** Logo displayed on dark backgrounds
- **Resolution:** 331 KB
- **Best for:** Dark-themed presentations, mockups with dark backgrounds

**`07-logo-png-transparent.png`**
- **Format:** PNG with transparent background (raster, high-resolution)
- **Usage:** Overlaying on photos, graphics, social media profile images
- **Resolution:** 462 KB
- **Best for:** Social media, photo overlays, mixed/light backgrounds

---

### Logo Usage Guidelines

**Mandatory Rules:**

✓ **Do:**
- Always maintain the aspect ratio when resizing
- Ensure adequate clear space around the logo (minimum: logo height ÷ 2)
- Use `05-logo-main.svg` for all scalable applications
- Use `07-logo-png-transparent.png` for social media and photo overlays
- Provide `05-logo-main.svg` to print vendors for merchandise

✗ **Don't:**
- Never rotate, distort, skew, or apply effects to the logo
- Never alter logo colors (use official brand colors only)
- Never place logo on busy backgrounds where it becomes illegible
- Never recreate or redraw the logo
- Never use low-resolution versions for print

---

### Logo for Specific Applications

| Application | Recommended File | Notes |
|-------------|-----------------|-------|
| **Website** | `05-logo-main.svg` | Scalable, fast loading |
| **Social Media Profile** | `07-logo-png-transparent.png` | Transparent background |
| **Print Materials** | `05-logo-main.svg` | Vector format for quality |
| **Branded Clothing** | `05-logo-main.svg` | Provide to printer with Pantone specs |
| **Email Signature** | `07-logo-png-transparent.png` | PNG for email compatibility |
| **Presentations** | `06-logo-png-dark-bg.png` or `07-logo-png-transparent.png` | Choose based on slide background |
| **Business Cards** | `05-logo-main.svg` | Vector for print quality |

---

## Official Brand Colors

### Primary Colors

#### Deep Charcoal (Primary Background)
- **Hex:** `#1E1F22`
- **RGB:** `rgb(30, 31, 34)`
- **CMYK:** C85 M78 Y76 K77 (approximate)
- **Pantone:** Black 6 C (closest match)
- **Usage:** Primary background color, dark sections, professional applications

#### Off-White (Primary Text)
- **Hex:** `#EBE7D9`
- **RGB:** `rgb(235, 231, 217)`
- **CMYK:** C6 M5 Y12 K0 (approximate)
- **Pantone:** 7527 C or Warm Gray 1 C (closest match)
- **Usage:** Primary text color, headings, body copy, light sections

#### Accent Coral/Red (Brand Highlight)
- **Hex:** `#F55139`
- **RGB:** `rgb(245, 81, 57)`
- **CMYK:** C0 M78 Y82 K0 (approximate)
- **Pantone:** 2028 C or 172 C (closest matches)
- **Usage:** "//" logo motif, CTAs, highlights, links, emphasis elements

---

### Secondary/Supporting Colors

#### Secondary Background
- **Hex:** `#25262A`
- **RGB:** `rgb(37, 38, 42)`
- **Usage:** Card backgrounds, alternate sections

#### Gradient Background
- **Hex:** `#2C2D31`
- **RGB:** `rgb(44, 45, 49)`
- **Usage:** Hero sections, gradient effects

#### Footer Background
- **Hex:** `#15161A`
- **RGB:** `rgb(21, 22, 26)`
- **Usage:** Footer sections, darkest elements

#### Muted/Secondary Text
- **Hex:** `#B8B3A8`
- **RGB:** `rgb(184, 179, 168)`
- **Usage:** Subtitles, captions, less prominent text

#### Accent Hover State
- **Hex:** `#D4441E`
- **RGB:** `rgb(212, 68, 30)`
- **Usage:** Button hover states, interactive elements

---

### Color Usage for Print/Merchandise

When ordering branded clothing or print materials, provide vendors with:

**Primary Colors (Pantone):**
- **Background/Dark Elements:** Pantone Black 6 C
- **Text/Light Elements:** Pantone 7527 C (or Warm Gray 1 C)
- **Accent/Highlights:** Pantone 2028 C (or 172 C)

**Logo File:** Provide `05-logo-main.svg`

**CMYK Values** (if Pantone not available):
- Deep Charcoal: C85 M78 Y76 K77
- Off-White: C6 M5 Y12 K0
- Accent Red: C0 M78 Y82 K0

---

## Typography

### Primary Font: Montserrat

**Font Family:** Montserrat
**Source:** Google Fonts
**License:** Open Font License (free for commercial use)

**CDN Link (for web):**
```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700;900&display=swap" rel="stylesheet">
```

**CSS Declaration:**
```css
font-family: 'Montserrat', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
```

---

### Font Weights

| Weight | Name | Usage |
|--------|------|-------|
| 400 | Regular | Body text, paragraphs |
| 500 | Medium | Navigation links, labels |
| 600 | Semi-Bold | Emphasis text, subheadings |
| 700 | Bold | Headings (H1-H6) |
| 900 | Black | "//" logo motif, special emphasis |

---

### Typography Scale

| Element | Desktop Size | Mobile Size | Weight | Color |
|---------|--------------|-------------|--------|-------|
| **H1** | 2.5rem (40px) | 2rem (32px) | 700 | #EBE7D9 |
| **H2** | 2rem (32px) | 1.75rem (28px) | 700 | #EBE7D9 |
| **H3** | 1.5rem (24px) | 1.25rem (20px) | 700 | #EBE7D9 |
| **H4** | 1.25rem (20px) | 1.125rem (18px) | 700 | #EBE7D9 |
| **Body** | 1rem (16px) | 0.875rem (14px) | 400 | #EBE7D9 |
| **Small** | 0.875rem (14px) | 0.875rem (14px) | 400 | #B8B3A8 |

---

## Visual Elements

### Spacing System

**Base Unit:** 1rem (16px)

**Spacing Scale:**
- **XS:** 0.25rem (4px)
- **S:** 0.5rem (8px)
- **M:** 1rem (16px)
- **L:** 2rem (32px)
- **XL:** 3rem (48px)
- **XXL:** 5rem (80px)

---

### Border Radius

- **Small:** 4px (buttons, small cards)
- **Medium:** 8px (larger cards, containers)
- **Large:** 20px (badges, pills, step numbers)
- **Circle:** 50% (circular icons, avatar images)

---

### Shadows

**Subtle Card Elevation:**
```css
box-shadow: 0 4px 12px rgba(245, 81, 57, 0.2);
```

**Strong Hover Effect:**
```css
box-shadow: 0 8px 24px rgba(245, 81, 57, 0.2);
```

---

## Component Styles

### Buttons

#### Primary Button (Call-to-Action)
- **Background:** `#F55139`
- **Text Color:** `#EBE7D9`
- **Padding:** 0.875rem 2rem
- **Border Radius:** 4px
- **Font Weight:** 600
- **Hover Effect:**
  - Background: `#D4441E`
  - Transform: `translateY(-2px)`
  - Shadow: `0 8px 24px rgba(245, 81, 57, 0.3)`

#### Secondary Button (Outline)
- **Background:** Transparent
- **Text Color:** `#EBE7D9`
- **Border:** 2px solid `#EBE7D9`
- **Padding:** 0.875rem 2rem
- **Hover Effect:**
  - Background: `#EBE7D9`
  - Text Color: `#1E1F22`

#### Accent Outline Button
- **Background:** Transparent
- **Text Color:** `#F55139`
- **Border:** 2px solid `#F55139`
- **Padding:** 0.875rem 2rem
- **Hover Effect:**
  - Background: `#F55139`
  - Text Color: `#EBE7D9`

---

### Cards

#### Standard Card
- **Background:** `#25262A`
- **Border:** 1px solid `rgba(245, 81, 57, 0.2)`
- **Border Radius:** 8px
- **Padding:** 2rem
- **Hover Effect:**
  - Border Color: `#F55139`
  - Transform: `translateY(-4px)`
  - Shadow: `0 8px 24px rgba(245, 81, 57, 0.2)`

#### Accent Card (Left Border Highlight)
- **Background:** `#25262A` or `#1E1F22`
- **Border-Left:** 4px solid `#F55139`
- **Border Radius:** 4px
- **Padding:** 1.5rem - 2rem

---

### Links

- **Default Color:** `#F55139`
- **Hover:** Opacity 0.8
- **Transition:** `all 0.3s ease`
- **Text Decoration:** None (underline on hover optional)

---

### Step Numbers / Circular Badges

- **Background:** `#F55139`
- **Text Color:** `#EBE7D9`
- **Size:** 50px × 50px (or 2.5rem - 3rem)
- **Border Radius:** 50% (circle)
- **Font Weight:** 700
- **Font Size:** 1.25rem - 1.5rem

---

## Brand Visual Expression

### Brand Personality in Design

The visual design should always express the three brand personality pillars:

**Friendly:**
- Rounded corners (not sharp edges)
- Generous whitespace
- Approachable color temperature (warm accent red vs. cold blue)
- Clean, uncluttered layouts

**Encouraging:**
- Uplifting color choices (accent red for motivation)
- Positive visual hierarchy (headings stand out)
- Celebration of achievements (step numbers, progress indicators)
- Visual breathing room (not cramped or overwhelming)

**Candid:**
- Clean, professional aesthetic (no gimmicks)
- Direct visual communication (clear hierarchy)
- Honest representation (authentic photos over stock imagery)
- Technical precision (consistent spacing, alignment)

---

## Photography & Imagery Guidelines

### Style Direction

**Do:**
- Use authentic photos of Dean coaching, training, or with Team GB
- Natural lighting preferred over harsh gym lighting
- Show real coaching moments (not posed fitness model shots)
- Include variety: age, gender, ability levels
- Warm color tones (not cold/clinical)
- Action shots that tell a story

**Don't:**
- Avoid generic stock photos (especially obvious fitness models)
- No overly polished/commercial aesthetic
- No intimidating "gym bro" imagery
- No cold, clinical lighting
- No staged or fake-looking scenarios

---

### Image Specifications

**File Formats:**
- Web: JPG (compressed, <500KB per image)
- Print: High-res JPG or PNG (300 DPI minimum)
- Graphics/Icons: SVG preferred, PNG fallback

**Aspect Ratios:**
- Hero/Banner images: 16:9 or 3:2
- Portrait/Headshots: 1:1 (square) or 3:4
- Social Media: Follow platform guidelines (Instagram: 1:1, 4:5; LinkedIn: 1.91:1)

**Processing:**
- Compress all web images using TinyPNG.com or similar
- Target: <500KB per image, <2MB total page weight
- Color profile: sRGB for web consistency

---

## Social Media Templates

### Instagram Post Dimensions
- **Feed Post:** 1080 × 1080 px (square) or 1080 × 1350 px (portrait)
- **Story:** 1080 × 1920 px (9:16)
- **Reel Cover:** 1080 × 1920 px (9:16)

### LinkedIn Post Dimensions
- **Single Image:** 1200 × 628 px (1.91:1)
- **Article Cover:** 1200 × 627 px

### Facebook Post Dimensions
- **Feed Post:** 1200 × 630 px
- **Cover Photo:** 820 × 312 px

### Design Elements for Social Media
- Use brand colors for text overlays
- Montserrat font for all text
- Logo placement: Bottom right or top left (consistent)
- Tagline inclusion: "Train Like an Athlete. Live Like You."
- Accent red for highlights/CTAs

---

## Design Do's & Don'ts

### ✓ Do's

- Use official brand colors consistently
- Maintain Montserrat font throughout all materials
- Keep layouts clean and uncluttered
- Use generous whitespace
- Maintain consistent spacing and alignment
- Use the "//" motif in accent red for brand recognition
- Prioritize readability (sufficient contrast)
- Use `05-logo-main.svg` for all scalable applications

### ✗ Don'ts

- Don't alter logo colors or proportions
- Don't use colors outside the brand palette
- Don't mix fonts — stick to Montserrat family only
- Don't overcomplicate designs
- Don't use overly aggressive or intimidating visuals
- Don't lose the balance between "elite" and "approachable"
- Don't use low-resolution logos for print
- Don't place logo on busy backgrounds

---

## Accessibility Guidelines

**Color Contrast:**
- Ensure text meets WCAG AA standards (4.5:1 for normal text, 3:1 for large text)
- Off-White (#EBE7D9) on Deep Charcoal (#1E1F22): ✓ Passes
- Accent Red (#F55139) on Deep Charcoal (#1E1F22): ✓ Passes for large text
- Never use Muted Text (#B8B3A8) for critical information

**Typography:**
- Minimum body text size: 16px (1rem) desktop, 14px (0.875rem) mobile
- Line height: 1.6 for body text, 1.2 for headings
- Maintain adequate spacing for readability

---

## Quick Reference Card

### Core Brand Elements

| Element | Specification |
|---------|--------------|
| **Primary Logo** | `05-logo-main.svg` |
| **Primary Background** | #1E1F22 (Deep Charcoal) |
| **Primary Text** | #EBE7D9 (Off-White) |
| **Accent/CTA** | #F55139 (Coral Red) |
| **Primary Font** | Montserrat (Google Fonts) |
| **Tagline** | "Train Like an Athlete. Live Like You." |

### For Print Vendors

| Element | Specification |
|---------|--------------|
| **Logo File** | `05-logo-main.svg` |
| **Background Pantone** | Black 6 C |
| **Accent Pantone** | 2028 C or 172 C |
| **CMYK Accent** | C0 M78 Y82 K0 |

### For Developers

```css
/* Brand Colors */
--color-bg-primary: #1E1F22;
--color-text-primary: #EBE7D9;
--color-accent: #F55139;
--color-accent-hover: #D4441E;

/* Typography */
font-family: 'Montserrat', sans-serif;
```

---

## Version History

**Version 1.1** (10 November 2024)
- Removed old folder references (/logo/, /website/)
- Updated all file references to context folder naming
- Consolidated all visual specs into single source of truth
- Added print/merchandise specifications
- Added accessibility guidelines
- Added quick reference card

**Version 1.0** (8 November 2024)
- Initial brand guide creation
- Official brand colors documented

---

## Contact

**Brand Owner:** Dean Whittingslow (CoachWhitt)
**Website:** https://coachwhitt.com
**Email:** info@coachwhitt.com

For questions about visual brand usage, refer to this document first. If clarification is needed, contact the brand owner.

---

**Last Updated:** 10 November 2024
