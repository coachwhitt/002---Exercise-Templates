# Research Prompt for Gemini
## Topic: Comprehensive List of Weight Lifting Exercises

### Objective
Research and generate a **comprehensive, structured, and scientifically grounded list of weight lifting exercises** that cover **all major and minor muscle groups** of the human body.

This information will form the foundation of a modular exercise knowledge base, designed for use in dynamic workout plan generation and branded presentation materials for **CoachWhitt**.

---

## Data Sources and Research Hierarchy

1. **Primary Source:**  
   Review all course content located in `./origym` and its subfolders.  
   → This content forms the **foundational knowledge base** and must be reviewed thoroughly before referencing any external data.

2. **Secondary Sources:**  
   After the Origym data has been fully processed, use reputable scientific literature and peer-reviewed white papers to validate and expand exercise details, along with other exercises to fill out the knowledge base options.  
   - Each exercise should include at least one supporting scientific reference (citation or paper link).  
   - Sources must have credible biomechanical or physiological authority.

---

## Exercise Coverage and Structure

For **each muscle group**, include at least **eight distinct exercises**, with at least 2 each for bodyweight, free weight, machine weight and cable/resistance.  
Ensure all major and minor muscle groups are represented (Chest, Back, Shoulders, Arms, Legs, Glutes, Core, Calves, Forearms, Neck, etc.).

Include **a variety of exercise types**:
- Free weights (dumbbells, barbells, kettlebells)
- Bodyweight movements
- Machine-based exercises
- Cable or resistance band movements (optional but recommended for completeness)

---

## Required Data Fields for Each Exercise

For every exercise, provide structured data with the following fields:

1. **Exercise Name**  
2. **Primary Muscles Worked**  
3. **Secondary Muscles Worked** (if applicable)  
4. **Type of Movement** — specify *Compound* or *Isolation*.  
5. **Equipment Needed** — e.g., barbell, dumbbell, bench, cable machine, etc.  
6. **Step-by-Step Instructions (Beginner Focus)** —  
   Clear, safe, biomechanically sound guidance for execution and posture.  
7. **Key Points for Advanced Users** —  
   3–5 performance cues for maximizing muscle engagement, control, and load efficiency.  
8. **Scientific Reference(s)** —  
   Include citation(s) or DOI/URL of white papers supporting the exercise’s efficacy or biomechanical validity.
9. **Applicable Sports Tags** —  
   List relevant sports or athletic movements this exercise supports (e.g., “Golf”, “Running”, “Football”, “Rugby”). 

---

## Output Format

Organize exercises by **muscle group** using consistent Markdown tables.

### Example Format

### Chest
| Exercise | Primary Muscles | Secondary Muscles | Type | Equipment | Steps for Beginners | Key Points for Advanced Users | Scientific Reference |
|-----------|----------------|-------------------|-------|------------|---------------------|--------------------------------|----------------------|
| Barbell Bench Press | Pectoralis Major | Triceps, Anterior Deltoids | Compound | Barbell, Bench | 1. Lie on the bench... | - Maintain scapular retraction... | [Smith et al., 2019 – Journal of Strength & Conditioning] |

---

## Functional Goals of the Dataset

The resulting dataset will serve as the **core knowledge base** for a modular exercise selection system used to generate customized training sessions.  
Each exercise must be designed for integration into automated program generation workflows, allowing flexibility and weekly variation.

---

## Future Development – Exercise Card System (CoachWhitt)

After the research dataset is completed, the next step is to design a **CoachWhitt Exercise Card** template.  
Reference all background and branding assets in `./context_files/`.

Each card should include:

1. Exercise Name  
2. Front and rear body diagrams showing active muscles  
   - **Primary muscles:** Highlighted prominently  
   - **Secondary muscles:** Muted highlight  
   - Include both **male and female versions**, stored separately for interchangeable use  
3. Text labels for primary/secondary muscles beside the diagrams  
4. Type of movement (compound/isolation)  
5. Equipment required  
6. Step-by-step beginner guide  
7. Key coaching points for advanced users  
8. Image of the exercise (matching the anatomical style)  
9. Placeholder fields for sets, reps, weight/time — editable per client program  

---

### Video Assets
For each exercise, generate **short instructional videos** showing motion and dynamically highlighting engaged muscles (primary vs secondary).  
- Follow the style of example files beginning `101 / 102` in `./example_images`.  
- Both male and female versions must be produced separately.

---

## Workflow and Output Requirements

1. **Client Program Workflow**
   - Trainer inputs client data (age, weight, fitness level, goals etc).
   - Exercises are selected from the research dataset to form multi-week sessions.
   - Each session auto-generates exercise cards and plan documents.

2. **Session File Format**
   - `Client Name - Week # - Session # - Exercise Name`
   - Cards grouped per session into printable (PDF) or digital scrollable documents.

3. **Session Summary Document**
   - Lists exercise names, sets, reps, weights/times.
   - Includes short-, medium-, and long-term goals.
   - States how the session plan aligns with the client’s objectives.
   - Includes a placeholder for session goals (e.g., “achieve PB”, “complete all sets”).

---

## Development and Review Phases

1. **Exercise Table Review** – Verify completeness and structure.  
2. **Template Card Layout Review** – Evaluate visual consistency and branding alignment.  
3. **Anatomical Muscle Group Mapping Review** – Confirm visual and data accuracy.  
4. **Video Animation Review** – Verify timing, muscle highlighting, and form accuracy (can occur post-launch).  
5. **Bulk Generation Phase** – Once one card is approved, apply template to all exercises.

---

## Deliverables Summary

- ✅ Fully populated Markdown tables by muscle group  
- ✅ Verified scientific references  
- ✅ Modular data suitable for program automation  
- ✅ CoachWhitt-branded exercise card design templates  
- ✅ Consistent, branded visual assets (images and videos)

---

**End of Prompt**