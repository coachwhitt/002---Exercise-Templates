/**
 * CoachWhitt Programme Card Auto-Generator v2.0
 *
 * INSTRUCTIONS:
 * 1. Create a blank Google Sheet
 * 2. Go to Extensions → Apps Script
 * 3. Delete any default code
 * 4. Paste this entire script
 * 5. Save (Ctrl+S or File → Save)
 * 6. Close Apps Script tab
 * 7. Refresh your Google Sheet
 * 8. A new menu "CoachWhitt" will appear at the top
 * 9. Click CoachWhitt → Generate Programme Card
 * 10. Wait 10-15 seconds for generation to complete
 *
 * The script will create 4 tabs:
 * - Programme Overview
 * - Week 01
 * - Progress Log
 * - RPE Guide
 *
 * All formatting, colors, formulas, and structure will be automatically applied.
 * Includes conditional RPE formatting, progress charts, and session time estimation.
 */

// Brand Colors (per context/04-visual-brand-guide.md)
const DEEP_CHARCOAL = '#1E1F22';
const OFF_WHITE = '#EBE7D9';
const ACCENT_RED = '#F55139';
const LIGHT_BLUE = '#D1E7FF';

// Logo image URL
const LOGO_URL = 'https://coachwhitt.com/images/07-logo-png-transparent.png';

// Font
const FONT_FAMILY = 'Montserrat';
const DEFAULT_FONT_SIZE = 10;

// Add custom menu when sheet opens
function onOpen() {
  const ui = SpreadsheetApp.getUi();
  ui.createMenu('CoachWhitt')
    .addItem('Generate Programme Card', 'generateProgrammeCard')
    .addItem('Generate Blank Template', 'generateBlankTemplate')
    .addToUi();
}

/**
 * Main function - generates complete programme card with sample data
 */
function generateProgrammeCard() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();

  // Delete existing sheets if present
  deleteExistingSheets(ss);

  // Create four new sheets
  const overviewSheet = ss.insertSheet('Programme Overview');
  const week01Sheet = ss.insertSheet('Week 01');
  const progressSheet = ss.insertSheet('Progress Log');
  const rpeSheet = ss.insertSheet('RPE Guide');

  // Generate each tab
  createProgrammeOverview(overviewSheet, true); // true = include sample data
  createWeek01Tab(week01Sheet, true);
  createProgressLog(progressSheet, true);
  createRPEGuide(rpeSheet);

  // Set active sheet to Overview
  ss.setActiveSheet(overviewSheet);

  SpreadsheetApp.getUi().alert('✅ Programme Card generated successfully!\n\nAll 4 tabs created with sample data.\n\nReady to customize for your client.');
}

/**
 * Alternative function - generates blank template without sample data
 */
function generateBlankTemplate() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();

  deleteExistingSheets(ss);

  const overviewSheet = ss.insertSheet('Programme Overview');
  const week01Sheet = ss.insertSheet('Week 01');
  const progressSheet = ss.insertSheet('Progress Log');
  const rpeSheet = ss.insertSheet('RPE Guide');

  createProgrammeOverview(overviewSheet, false); // false = no sample data
  createWeek01Tab(week01Sheet, false);
  createProgressLog(progressSheet, false);
  createRPEGuide(rpeSheet);

  ss.setActiveSheet(overviewSheet);

  SpreadsheetApp.getUi().alert('✅ Blank template generated!\n\nAll 4 tabs created.\n\nFill in client information and exercises.');
}

/**
 * Delete existing programme sheets if present
 */
function deleteExistingSheets(ss) {
  const sheetNames = ['Programme Overview', 'Week 01', 'Progress Log', 'RPE Guide'];
  sheetNames.forEach(name => {
    const sheet = ss.getSheetByName(name);
    if (sheet) {
      ss.deleteSheet(sheet);
    }
  });
}

/**
 * Apply header with logo and tagline (used on all tabs)
 */
function applyHeaderWithLogo(sheet, startRow, maxColumn) {
  // Row: Logo (100px height)
  sheet.getRange(startRow, 1).setFormula(`=image("${LOGO_URL}",4,50,573.4)`);
  sheet.getRange(startRow, 1, 1, maxColumn).merge()
    .setBackground(DEEP_CHARCOAL)
    .setVerticalAlignment('middle')
    .setHorizontalAlignment('center');
  sheet.setRowHeight(startRow, 100);

  // Row: Tagline (40px height) - BOLD on all tabs
  const taglineRow = startRow + 1;
  sheet.getRange(taglineRow, 1, 1, maxColumn).merge()
    .setValue('Train Like an Athlete. Live Like You.')
    .setFontFamily(FONT_FAMILY)
    .setFontSize(12)
    .setFontStyle('italic')
    .setFontWeight('bold')
    .setFontColor(ACCENT_RED)
    .setHorizontalAlignment('center')
    .setVerticalAlignment('middle');
  sheet.setRowHeight(taglineRow, 40);

  // Row: Blank spacer (10px)
  sheet.setRowHeight(startRow + 2, 10);

  return startRow + 3; // Return next usable row
}

/**
 * Create Programme Overview tab
 */
function createProgrammeOverview(sheet, includeSampleData) {
  // Set column widths (A-G, only A-F used, G+ deleted at end)
  sheet.setColumnWidth(1, 200); // A
  sheet.setColumnWidth(2, 150); // B
  sheet.setColumnWidth(3, 150); // C
  sheet.setColumnWidth(4, 150); // D
  sheet.setColumnWidth(5, 150); // E
  sheet.setColumnWidth(6, 150); // F
  sheet.setColumnWidth(7, 100); // G (will be deleted)

  // Apply header with logo (merge to column F only)
  let currentRow = applyHeaderWithLogo(sheet, 1, 6);

  // CLIENT INFORMATION Header
  sheet.getRange(currentRow, 1, 1, 6).merge()
    .setValue('CLIENT INFORMATION')
    .setFontFamily(FONT_FAMILY)
    .setFontSize(12)
    .setFontWeight('bold')
    .setFontColor(OFF_WHITE)
    .setBackground(DEEP_CHARCOAL)
    .setHorizontalAlignment('left')
    .setVerticalAlignment('middle');
  sheet.setRowHeight(currentRow, 30);
  currentRow++;

  // Client details
  const clientName = includeSampleData ? 'Dean Whittingslow' : '';
  const preferredName = includeSampleData ? 'Dean' : '';
  const service = includeSampleData ? 'Performance Plus' : '';
  const startDate = includeSampleData ? '06-Jan-2026' : '';
  const endDate = includeSampleData ? '02-Feb-2026' : '';

  setLabelValue(sheet, currentRow++, 'Client Name:', clientName, false, true); // true = bold value
  setLabelValue(sheet, currentRow++, 'Preferred Name', preferredName);
  setLabelValue(sheet, currentRow++, 'Service:', service, false, false, true); // true = left align value
  setLabelValue(sheet, currentRow++, 'Programme Start Date:', startDate, false, false, true); // true = left align value
  setLabelValue(sheet, currentRow++, 'Programme End Date:', endDate, false, false, true); // true = left align value

  // Blank spacer
  sheet.setRowHeight(currentRow++, 10);

  // PROGRAMME GOALS Header
  sheet.getRange(currentRow, 1, 1, 6).merge()
    .setValue('PROGRAMME GOALS')
    .setFontFamily(FONT_FAMILY)
    .setFontSize(12)
    .setFontWeight('bold')
    .setFontColor(OFF_WHITE)
    .setBackground(DEEP_CHARCOAL)
    .setHorizontalAlignment('left')
    .setVerticalAlignment('middle');
  sheet.setRowHeight(currentRow, 30);
  currentRow++;

  // Goals
  const primaryGoal = includeSampleData ? 'Build strength and muscle mass' : '';
  const secondaryGoal = includeSampleData ? 'Improve conditioning and work capacity' : '';

  setLabelValue(sheet, currentRow++, 'Primary Goal:', primaryGoal, true);
  setLabelValue(sheet, currentRow++, 'Secondary Goal:', secondaryGoal, true);

  // Blank spacer
  sheet.setRowHeight(currentRow++, 10);

  // TRAINING SCHEDULE Header
  sheet.getRange(currentRow, 1, 1, 6).merge()
    .setValue('TRAINING SCHEDULE')
    .setFontFamily(FONT_FAMILY)
    .setFontSize(12)
    .setFontWeight('bold')
    .setFontColor(OFF_WHITE)
    .setBackground(DEEP_CHARCOAL)
    .setHorizontalAlignment('left')
    .setVerticalAlignment('middle');
  sheet.setRowHeight(currentRow, 30);
  currentRow++;

  // Schedule details
  const trainingDays = includeSampleData ? 'Monday, Wednesday, Friday, Saturday' : '';
  const duration = includeSampleData ? '60-75' : '';
  const split = includeSampleData ? 'Upper/Lower/Full Body/Conditioning' : '';

  setLabelValue(sheet, currentRow++, 'Training Days:', trainingDays, true);
  setLabelValue(sheet, currentRow++, 'Session Duration (mins):', duration, true, false, true); // true = left align value
  setLabelValue(sheet, currentRow++, 'Training Split:', split, true);

  // Blank spacer
  sheet.setRowHeight(currentRow++, 10);

  // HOW TO USE THIS PROGRAMME Header
  sheet.getRange(currentRow, 1, 1, 6).merge()
    .setValue('HOW TO USE THIS PROGRAMME:')
    .setFontFamily(FONT_FAMILY)
    .setFontSize(11)
    .setFontWeight('bold')
    .setFontColor(OFF_WHITE)
    .setBackground(DEEP_CHARCOAL)
    .setVerticalAlignment('middle');
  sheet.setRowHeight(currentRow, 25);
  currentRow++;

  // Instructions
  const instructions = [
    '1. Complete exercises in the order shown on the "Week XX" tab',
    '2. Log your completed weights in the designated columns (blue cells)',
    '3. Rest periods are shown for each exercise - stick to them for best results',
    '4. Update your Progress Log weekly (Monday mornings before training)',
    '5. Make sure you let me know how you\'re getting on - good or bad!'
  ];

  instructions.forEach(instruction => {
    sheet.getRange(currentRow, 1, 1, 6).merge()
      .setValue(instruction)
      .setFontFamily(FONT_FAMILY)
      .setFontSize(DEFAULT_FONT_SIZE)
      .setVerticalAlignment('middle');
    sheet.setRowHeight(currentRow, 25);
    currentRow++;
  });

  // Delete columns G onwards and rows 30 onwards
  const maxColumns = sheet.getMaxColumns();
  if (maxColumns > 6) {
    sheet.deleteColumns(7, maxColumns - 6);
  }
  const maxRows = sheet.getMaxRows();
  if (maxRows > 29) {
    sheet.deleteRows(30, maxRows - 29);
  }
}

/**
 * Helper function to set label/value pairs
 */
function setLabelValue(sheet, row, label, value, wideValue = false, boldValue = false, leftAlignValue = false) {
  sheet.getRange(row, 1).setValue(label)
    .setFontFamily(FONT_FAMILY)
    .setFontWeight('bold')
    .setFontSize(DEFAULT_FONT_SIZE);

  if (wideValue) {
    sheet.getRange(row, 2, 1, 5).merge();
    const valueCell = sheet.getRange(row, 2).setValue(value)
      .setFontFamily(FONT_FAMILY)
      .setFontSize(DEFAULT_FONT_SIZE);
    if (boldValue) valueCell.setFontWeight('bold');
    if (leftAlignValue) valueCell.setHorizontalAlignment('left');
  } else {
    sheet.getRange(row, 2, 1, 2).merge();
    const valueCell = sheet.getRange(row, 2).setValue(value)
      .setFontFamily(FONT_FAMILY)
      .setFontSize(DEFAULT_FONT_SIZE);
    if (boldValue) valueCell.setFontWeight('bold');
    if (leftAlignValue) valueCell.setHorizontalAlignment('left');
  }

  sheet.setRowHeight(row, 25);
}

/**
 * Create Week 01 tab with 7 days of training
 */
function createWeek01Tab(sheet, includeSampleData) {
  // Set column widths (A-N plus hidden M & N for session estimation)
  sheet.setColumnWidth(1, 40);   // # (row number)
  sheet.setColumnWidth(2, 120);  // Activity Group
  sheet.setColumnWidth(3, 180);  // Exercise
  sheet.setColumnWidth(4, 50);   // Sets
  sheet.setColumnWidth(5, 80);   // Reps/Time
  sheet.setColumnWidth(6, 70);   // Rest (sec)
  sheet.setColumnWidth(7, 90);   // Weight (kg)
  sheet.setColumnWidth(8, 150);  // Coach Notes
  sheet.setColumnWidth(9, 100);  // Video Link
  sheet.setColumnWidth(10, 100); // Actual Weight Completed
  sheet.setColumnWidth(11, 80);  // RPE after activity
  sheet.setColumnWidth(12, 200); // Dean's Notes
  sheet.setColumnWidth(13, 50);  // M - Hidden (blank)
  sheet.setColumnWidth(14, 120); // N - Hidden (Session Time Est.)

  // Hide columns M & N
  sheet.hideColumns(13, 2);

  // Apply header with logo (merge to column N)
  let currentRow = applyHeaderWithLogo(sheet, 1, 14);

  // Hidden helper cell N3: Reference to Programme Overview session duration (B17)
  sheet.getRange(3, 14).setFormula("='Programme Overview'!B17")
    .setFontSize(8)
    .setFontColor('#CCCCCC'); // Light gray text (hidden but readable if needed)

  // WEEK 01 - TRAINING PROGRAMME Header
  sheet.getRange(currentRow, 1, 1, 14).merge()
    .setValue('WEEK 01 - TRAINING PROGRAMME')
    .setFontFamily(FONT_FAMILY)
    .setFontSize(14)
    .setFontWeight('bold')
    .setFontColor(OFF_WHITE)
    .setBackground(DEEP_CHARCOAL)
    .setHorizontalAlignment('center')
    .setVerticalAlignment('middle');
  sheet.setRowHeight(currentRow, 30);
  currentRow++;

  // Blank spacer
  sheet.setRowHeight(currentRow++, 10);

  // Create 7 days of training
  const sampleExercises = includeSampleData ? getSampleExercises() : getBlankExercises();

  for (let day = 1; day <= 7; day++) {
    currentRow = createTrainingDay(sheet, currentRow, day, sampleExercises[day - 1], includeSampleData);
  }

  // Delete columns O onwards and rows 100 onwards
  const maxColumns = sheet.getMaxColumns();
  if (maxColumns > 14) {
    sheet.deleteColumns(15, maxColumns - 14);
  }
  const maxRows = sheet.getMaxRows();
  if (maxRows > 99) {
    sheet.deleteRows(100, maxRows - 99);
  }
}

/**
 * Create a single training day section (10 rows: warmup, 8 exercises, cooldown, stretch)
 */
function createTrainingDay(sheet, startRow, dayNumber, exercises, includeSampleData) {
  let currentRow = startRow;

  // Row 6: Day header (e.g., "DAY 1: LOWER BODY") - CHARCOAL fill with OFF_WHITE text
  sheet.getRange(currentRow, 1, 1, 14).merge()
    .setValue(`DAY ${dayNumber}: LOWER BODY (Squat Focus)`)
    .setFontFamily(FONT_FAMILY)
    .setFontSize(12)
    .setFontWeight('bold')
    .setFontColor(OFF_WHITE)
    .setBackground(DEEP_CHARCOAL)
    .setHorizontalAlignment('left')
    .setVerticalAlignment('middle');
  sheet.setRowHeight(currentRow, 30);
  currentRow++;

  // Row 7: Column headers (45px height) - OFF_WHITE fill with CHARCOAL text
  const headers = ['#', 'Activity Group', 'Exercise', 'Sets', 'Reps / Time (secs)', 'Rest (sec)',
                   'Weight (kg)', 'Coach Notes', 'Video Link (where req.)', 'Actual Weight Completed (kg)',
                   'RPE after activity (see RPE guide)', '', '', 'Session Time Est.'];

  for (let i = 0; i < headers.length; i++) {
    if (i === 11) {
      // L7 - Special formula for client's name + notes
      sheet.getRange(currentRow, i + 1)
        .setFormula(`='Programme Overview'!$B$6&"'s Notes"&CHAR(10)&"Notes for next time / How did the movement feel? etc."`)
        .setFontFamily(FONT_FAMILY)
        .setFontSize(9)
        .setFontWeight('bold')
        .setFontColor(DEEP_CHARCOAL)
        .setBackground(OFF_WHITE)
        .setHorizontalAlignment('center')
        .setVerticalAlignment('middle')
        .setWrapStrategy(SpreadsheetApp.WrapStrategy.WRAP);
    } else {
      sheet.getRange(currentRow, i + 1)
        .setValue(headers[i])
        .setFontFamily(FONT_FAMILY)
        .setFontSize(9)
        .setFontWeight('bold')
        .setFontColor(DEEP_CHARCOAL)
        .setBackground(OFF_WHITE)
        .setHorizontalAlignment('center')
        .setVerticalAlignment('middle')
        .setWrapStrategy(SpreadsheetApp.WrapStrategy.WRAP);
    }
  }
  sheet.setRowHeight(currentRow, 45);

  // M7:N7 - OFF_WHITE fill with DEEP_CHARCOAL text (already set above, this ensures consistency)
  sheet.getRange(currentRow, 13).setBackground(OFF_WHITE).setFontColor(DEEP_CHARCOAL); // M7
  sheet.getRange(currentRow, 14)
    .setValue('Session Time Est. (mins)')
    .setFontFamily(FONT_FAMILY)
    .setFontSize(9)
    .setFontWeight('bold')
    .setBackground(OFF_WHITE)
    .setFontColor(DEEP_CHARCOAL)
    .setHorizontalAlignment('center')
    .setVerticalAlignment('middle')
    .setWrapStrategy(SpreadsheetApp.WrapStrategy.WRAP);

  currentRow++;

  // Exercise rows (10 rows total)
  for (let i = 0; i < 10; i++) {
    const rowNum = currentRow + i;
    const exerciseData = exercises[i];

    // Row number (#)
    sheet.getRange(rowNum, 1)
      .setValue(i + 1)
      .setFontFamily(FONT_FAMILY)
      .setFontSize(DEFAULT_FONT_SIZE)
      .setHorizontalAlignment('center');

    // Activity Group (CV Warmup, Cooldown, Stretch)
    if (i === 0) {
      sheet.getRange(rowNum, 2).setValue('CV Warmup');
    } else if (i === 8) {
      sheet.getRange(rowNum, 2).setValue('Cooldown');
    } else if (i === 9) {
      sheet.getRange(rowNum, 2).setValue('Stretch');
    }

    // Exercise, Sets, Reps, Rest, Weight, Coach Notes
    if (includeSampleData && exerciseData) {
      sheet.getRange(rowNum, 3).setValue(exerciseData.exercise);
      sheet.getRange(rowNum, 4).setValue(exerciseData.sets).setHorizontalAlignment('center');
      sheet.getRange(rowNum, 5).setValue(exerciseData.reps).setHorizontalAlignment('center');
      sheet.getRange(rowNum, 6).setValue(exerciseData.rest).setHorizontalAlignment('center');
      sheet.getRange(rowNum, 7).setValue(exerciseData.weight).setHorizontalAlignment('center');
      sheet.getRange(rowNum, 8).setValue(exerciseData.coachNotes);
    }

    // Apply font to all cells (including hidden columns M & N)
    sheet.getRange(rowNum, 1, 1, 14).setFontFamily(FONT_FAMILY).setFontSize(DEFAULT_FONT_SIZE);

    // Blue cells for client input (columns J, K, L - Actual Weight, RPE, Notes)
    sheet.getRange(rowNum, 10).setBackground(LIGHT_BLUE); // Actual Weight Completed
    sheet.getRange(rowNum, 11).setBackground(LIGHT_BLUE); // RPE after activity
    sheet.getRange(rowNum, 12).setBackground(LIGHT_BLUE); // Dean's Notes

    // Hidden column M - clear fill (no background color)
    sheet.getRange(rowNum, 13).setBackground(null).setFontColor('#000000');

    // Hidden column N - Session Time Estimation formula
    if (i < 10) {
      // Rows 1-10 (all exercises including row 10) - calculate session time, clear fill
      sheet.getRange(rowNum, 14).setFormula(
        `=($D${rowNum}*(IFERROR(RIGHT($E${rowNum},LEN($E${rowNum})-SEARCH("-",$E${rowNum})),$E${rowNum})*10)+$D${rowNum}*$F${rowNum})/60`
      ).setBackground(null).setFontColor('#000000');
    }

    sheet.setRowHeight(rowNum, 25);
  }

  // Row 18 (after all exercises) - SUM formula in N18
  const sumStartRow = currentRow;
  const sumEndRow = currentRow + 9; // N8 to N17 (10 rows)
  const sumRowNumber = currentRow + 10;
  sheet.getRange(sumRowNumber, 14).setFormula(`=SUM(N${sumStartRow}:N${sumEndRow})`)
    .setBackground(null)
    .setFontColor('#000000')
    .setFontFamily(FONT_FAMILY)
    .setFontSize(DEFAULT_FONT_SIZE);
  sheet.setRowHeight(sumRowNumber, 25);

  // Apply session duration conditional formatting to N18 (and N32, N46, etc. per day)
  applySessionDurationConditionalFormatting(sheet, sumRowNumber, 14);

  currentRow += 11; // Move past 10 exercise rows + 1 sum row

  // Apply RPE conditional formatting to column K (RPE after activity)
  const rpeRange = sheet.getRange(startRow + 2, 11, 10, 1); // Column K, 10 rows
  applyRPEConditionalFormatting(rpeRange);

  // Blank spacer after day
  sheet.setRowHeight(currentRow++, 10);

  return currentRow;
}

/**
 * Apply session duration conditional formatting
 * Compares N18 (session time in minutes) to N3 (helper cell with session duration from Overview!B17)
 * Red: >15% below lower limit OR >5% above upper limit
 * Orange: Between mid-range and 5% above upper limit
 * Green: <15% below lower limit up to mid-range
 *
 * N3 contains formula: ='Programme Overview'!B17 (e.g., "60-75" or "60")
 * Handles both single values (60) and ranges (60-75)
 */
function applySessionDurationConditionalFormatting(sheet, row, column) {
  const cell = sheet.getRange(row, column);

  // Red condition 1: More than 15% below lower limit
  // If range: lower = LEFT, if single: use entire value
  const redRule1 = SpreadsheetApp.newConditionalFormatRule()
    .whenFormulaSatisfied(`=N${row}<(VALUE(IF(ISERROR(SEARCH("-",$N$3)),$N$3,LEFT($N$3,SEARCH("-",$N$3)-1)))*0.85)`)
    .setBackground('#E06666')
    .setRanges([cell])
    .build();

  // Red condition 2: More than 5% above upper limit
  // If range: upper = RIGHT, if single: use entire value
  const redRule2 = SpreadsheetApp.newConditionalFormatRule()
    .whenFormulaSatisfied(`=N${row}>(VALUE(IF(ISERROR(SEARCH("-",$N$3)),$N$3,RIGHT($N$3,LEN($N$3)-SEARCH("-",$N$3))))*1.05)`)
    .setBackground('#E06666')
    .setRanges([cell])
    .build();

  // Orange condition: Between mid-range and 5% above upper limit
  // If range: calculate midpoint, if single: use value as both lower and upper
  const orangeRule = SpreadsheetApp.newConditionalFormatRule()
    .whenFormulaSatisfied(`=AND(N${row}>=(VALUE(IF(ISERROR(SEARCH("-",$N$3)),$N$3,LEFT($N$3,SEARCH("-",$N$3)-1)))+VALUE(IF(ISERROR(SEARCH("-",$N$3)),$N$3,RIGHT($N$3,LEN($N$3)-SEARCH("-",$N$3)))))/2,N${row}<=(VALUE(IF(ISERROR(SEARCH("-",$N$3)),$N$3,RIGHT($N$3,LEN($N$3)-SEARCH("-",$N$3))))*1.05))`)
    .setBackground('#F6B26B')
    .setRanges([cell])
    .build();

  // Green condition: Less than 15% below lower limit up to mid-range
  // If range: use lower and midpoint, if single: compare to single value
  const greenRule = SpreadsheetApp.newConditionalFormatRule()
    .whenFormulaSatisfied(`=AND(N${row}>=(VALUE(IF(ISERROR(SEARCH("-",$N$3)),$N$3,LEFT($N$3,SEARCH("-",$N$3)-1)))*0.85),N${row}<(VALUE(IF(ISERROR(SEARCH("-",$N$3)),$N$3,LEFT($N$3,SEARCH("-",$N$3)-1)))+VALUE(IF(ISERROR(SEARCH("-",$N$3)),$N$3,RIGHT($N$3,LEN($N$3)-SEARCH("-",$N$3)))))/2)`)
    .setBackground('#93C47D')
    .setRanges([cell])
    .build();

  const rules = sheet.getConditionalFormatRules();
  rules.push(redRule1, redRule2, orangeRule, greenRule);
  sheet.setConditionalFormatRules(rules);
}

/**
 * Apply RPE conditional formatting (Enhancement 1)
 * Green: 1-4 (easy)
 * Yellow: 5-7 (moderate)
 * Orange: 8-9 (hard)
 * Red: 10 (maximal)
 */
function applyRPEConditionalFormatting(range) {
  const greenRule = SpreadsheetApp.newConditionalFormatRule()
    .whenNumberBetween(1, 4)
    .setBackground('#93C47D') // Green
    .setRanges([range])
    .build();

  const yellowRule = SpreadsheetApp.newConditionalFormatRule()
    .whenNumberBetween(5, 7)
    .setBackground('#FFD966') // Yellow
    .setRanges([range])
    .build();

  const orangeRule = SpreadsheetApp.newConditionalFormatRule()
    .whenNumberBetween(8, 9)
    .setBackground('#F6B26B') // Orange
    .setRanges([range])
    .build();

  const redRule = SpreadsheetApp.newConditionalFormatRule()
    .whenNumberEqualTo(10)
    .setBackground('#E06666') // Red
    .setRanges([range])
    .build();

  const sheet = range.getSheet();
  const rules = sheet.getConditionalFormatRules();
  rules.push(greenRule, yellowRule, orangeRule, redRule);
  sheet.setConditionalFormatRules(rules);
}

/**
 * Sample exercises for testing (7 days)
 */
function getSampleExercises() {
  const day1 = [
    { exercise: 'Rowing Machine', sets: 1, reps: 300, rest: 0, weight: '', coachNotes: '5 min - Light pace, warm up joints' },
    { exercise: 'Barbell Back Squat', sets: 4, reps: '6-8', rest: 180, weight: 100, coachNotes: '3 min rest - Focus on depth and control' },
    { exercise: 'Romanian Deadlift', sets: 3, reps: '10-12', rest: 120, weight: 60, coachNotes: '2 min rest - Feel the hamstring stretch' },
    { exercise: 'Leg Press', sets: 3, reps: '12-15', rest: 90, weight: 120, coachNotes: '90 sec rest - Full ROM, controlled descent' },
    { exercise: 'Walking Lunges', sets: 3, reps: 12, rest: 90, weight: 20, coachNotes: '90 sec rest - 12 reps per leg, knee over toe' },
    { exercise: 'Leg Curl', sets: 3, reps: '12-15', rest: 60, weight: 40, coachNotes: '60 sec rest - Squeeze at the top' },
    { exercise: 'Calf Raises', sets: 4, reps: '15-20', rest: 45, weight: 60, coachNotes: '45 sec rest - Full stretch, full contraction' },
    { exercise: 'Plank Hold', sets: 3, reps: 60, rest: 60, weight: '', coachNotes: '60 sec rest - Maintain neutral spine, 45-60 sec holds' },
    { exercise: 'Light stretching', sets: 1, reps: 300, rest: 0, weight: '', coachNotes: '5 min - Focus on legs and hips' },
    { exercise: 'Full body stretch', sets: 1, reps: 300, rest: 0, weight: '', coachNotes: '5 min - Hold each stretch 30 sec' }
  ];

  // For now, return day1 for all 7 days (can customize later)
  return [day1, day1, day1, day1, day1, day1, day1];
}

/**
 * Blank exercises structure (7 days)
 */
function getBlankExercises() {
  const blankDay = Array(10).fill({ exercise: '', sets: '', reps: '', rest: '', weight: '', coachNotes: '' });
  return [blankDay, blankDay, blankDay, blankDay, blankDay, blankDay, blankDay];
}

/**
 * Create Progress Log tab (Enhancement 2: Includes charts)
 */
function createProgressLog(sheet, includeSampleData) {
  // Set column widths
  sheet.setColumnWidth(1, 80);   // Week
  sheet.setColumnWidth(2, 100);  // Date
  sheet.setColumnWidth(3, 100);  // Bodyweight
  sheet.setColumnWidth(4, 80);   // Body Fat %
  sheet.setColumnWidth(5, 80);   // Waist
  sheet.setColumnWidth(6, 80);   // Chest
  sheet.setColumnWidth(7, 80);   // Hips
  sheet.setColumnWidth(8, 80);   // Arms
  sheet.setColumnWidth(9, 80);   // Thighs
  sheet.setColumnWidth(10, 80);  // Energy
  sheet.setColumnWidth(11, 100); // Sleep Quality
  sheet.setColumnWidth(12, 100); // Mood/Motivation
  sheet.setColumnWidth(13, 100); // Confidence
  sheet.setColumnWidth(14, 200); // Notes

  // Apply header with logo (merge to column N for Progress Log)
  let currentRow = applyHeaderWithLogo(sheet, 1, 14);

  // PROGRESS LOG Header (A4)
  sheet.getRange(currentRow, 1, 1, 14).merge()
    .setValue('PROGRESS LOG')
    .setFontFamily(FONT_FAMILY)
    .setFontSize(14)
    .setFontWeight('bold')
    .setFontColor(OFF_WHITE)
    .setBackground(DEEP_CHARCOAL)
    .setHorizontalAlignment('center')
    .setVerticalAlignment('middle');
  sheet.setRowHeight(currentRow, 30);
  currentRow++;

  // Instructions (A5 - make this cell bold)
  sheet.getRange(currentRow, 1, 1, 14).merge()
    .setValue('Complete this log every Monday morning before your first training session')
    .setFontFamily(FONT_FAMILY)
    .setFontSize(9)
    .setFontStyle('italic')
    .setFontWeight('bold')
    .setFontColor(ACCENT_RED)
    .setHorizontalAlignment('center')
    .setVerticalAlignment('middle');
  sheet.setRowHeight(currentRow, 25);
  currentRow++;

  // Blank spacer
  sheet.setRowHeight(currentRow++, 10);

  // Column headers
  const headers = ['Week', 'Date', 'Bodyweight (kg)', 'Body Fat %', 'Waist (cm)', 'Chest (cm)',
                   'Hips (cm)', 'Arms (cm)', 'Thighs (cm)', 'Energy (1-10)', 'Sleep Quality (1-10)',
                   'Mood / Motivation (1-10)', 'Confidence (1-10)', 'Notes'];

  for (let i = 0; i < headers.length; i++) {
    sheet.getRange(currentRow, i + 1)
      .setValue(headers[i])
      .setFontFamily(FONT_FAMILY)
      .setFontSize(9)
      .setFontWeight('bold')
      .setFontColor(OFF_WHITE)
      .setBackground(DEEP_CHARCOAL)
      .setHorizontalAlignment('center')
      .setVerticalAlignment('middle')
      .setWrapStrategy(SpreadsheetApp.WrapStrategy.WRAP);
  }
  sheet.setRowHeight(currentRow, 35);
  currentRow++;

  // Sample data for Weeks 1-4 (all populated)
  if (includeSampleData) {
    const weekData = [
      { week: 'Week 01', date: '06-Jan-2026', weight: 85.5, bodyFat: 18.2, waist: 92, chest: 105, hips: 38, arms: 36, thighs: 60, energy: 7, sleep: 8, mood: 7, confidence: 8, notes: 'Feeling strong, ready to start' },
      { week: 'Week 02', date: '13-Jan-2026', weight: 85.2, bodyFat: 18.0, waist: 91, chest: 105, hips: 38, arms: 36, thighs: 60, energy: 8, sleep: 7, mood: 8, confidence: 8, notes: 'Great progress, energy levels up' },
      { week: 'Week 03', date: '20-Jan-2026', weight: 84.8, bodyFat: 17.8, waist: 90, chest: 106, hips: 39, arms: 37, thighs: 61, energy: 8, sleep: 8, mood: 9, confidence: 9, notes: 'Strength gains noticeable' },
      { week: 'Week 04', date: '27-Jan-2026', weight: 84.5, bodyFat: 17.5, waist: 89, chest: 106, hips: 39, arms: 37, thighs: 61, energy: 9, sleep: 8, mood: 9, confidence: 9, notes: 'Excellent month, hitting all targets' }
    ];

    weekData.forEach(data => {
      sheet.getRange(currentRow, 1).setValue(data.week).setFontWeight('bold');
      sheet.getRange(currentRow, 2).setValue(data.date);
      sheet.getRange(currentRow, 3).setValue(data.weight).setNumberFormat('0.0');
      sheet.getRange(currentRow, 4).setValue(data.bodyFat).setNumberFormat('0.0');
      sheet.getRange(currentRow, 5).setValue(data.waist);
      sheet.getRange(currentRow, 6).setValue(data.chest);
      sheet.getRange(currentRow, 7).setValue(data.hips);
      sheet.getRange(currentRow, 8).setValue(data.arms);
      sheet.getRange(currentRow, 9).setValue(data.thighs);
      sheet.getRange(currentRow, 10).setValue(data.energy);
      sheet.getRange(currentRow, 11).setValue(data.sleep);
      sheet.getRange(currentRow, 12).setValue(data.mood);
      sheet.getRange(currentRow, 13).setValue(data.confidence);
      sheet.getRange(currentRow, 14).setValue(data.notes);
      sheet.getRange(currentRow, 1, 1, 14).setFontFamily(FONT_FAMILY).setFontSize(DEFAULT_FONT_SIZE);
      sheet.setRowHeight(currentRow, 25);
      currentRow++;
    });
  } else {
    // Blank placeholder rows for Week 1-4
    for (let week = 1; week <= 4; week++) {
      sheet.getRange(currentRow, 1).setValue(`Week 0${week}`).setFontWeight('bold');
      sheet.getRange(currentRow, 1, 1, 14).setFontFamily(FONT_FAMILY).setFontSize(DEFAULT_FONT_SIZE);
      sheet.setRowHeight(currentRow, 25);
      currentRow++;
    }
  }

  // Add space before charts
  sheet.setRowHeight(currentRow++, 20);

  // Enhancement 2: Create progress charts
  createProgressCharts(sheet, currentRow);

  // Delete column O onwards and rows 100 onwards (Progress Log only has columns A-N)
  const maxColumns = sheet.getMaxColumns();
  if (maxColumns > 14) {
    sheet.deleteColumns(15, maxColumns - 14);
  }
  const maxRows = sheet.getMaxRows();
  if (maxRows > 99) {
    sheet.deleteRows(100, maxRows - 99);
  }
}

/**
 * Create progress charts for bodyweight and measurements (Enhancement 2)
 * Charts configured to treat row 7 as headers
 * Each chart specifies exact series columns only
 */
function createProgressCharts(sheet, startRow) {
  // Chart 1: Bodyweight & Body Fat Progress
  // Data range: A7:D50, Series: C7:C11 (Bodyweight), D7:D11 (Body Fat %)
  // Bodyweight on left axis (0), Body Fat % on right axis (1)
  const bodyweightChart = sheet.newChart()
    .setChartType(Charts.ChartType.LINE)
    .addRange(sheet.getRange('A7:A11')) // X-axis with header
    .addRange(sheet.getRange('C7:C11')) // Series 1: Bodyweight (kg)
    .addRange(sheet.getRange('D7:D11')) // Series 2: Body Fat %
    .setNumHeaders(1) // Use row 7 as headers
    .setPosition(startRow, 1, 0, 0)
    .setOption('title', 'Bodyweight & Body Fat Progress')
    .setOption('titleTextStyle', { fontName: FONT_FAMILY, fontSize: 12 })
    .setOption('legend', { position: 'bottom', textStyle: { fontName: FONT_FAMILY, fontSize: 10 } })
    .setOption('hAxis', { title: 'Week', titleTextStyle: { fontName: FONT_FAMILY } })
    .setOption('vAxis', { title: 'Bodyweight (kg)', titleTextStyle: { fontName: FONT_FAMILY } })
    .setOption('vAxes', { 1: { title: 'Body Fat %', titleTextStyle: { fontName: FONT_FAMILY } } })
    .setOption('series', { 0: { targetAxisIndex: 0 }, 1: { targetAxisIndex: 1 } })
    .setOption('useFirstColumnAsDomain', true)
    .setOption('width', 500)
    .setOption('height', 300)
    .build();

  sheet.insertChart(bodyweightChart);

  // Chart 2: Body Measurements (cm) - Waist, Chest, Hips, Arms, Thighs
  // Data range: A7:I50, Series: E, F, G, H, I (Waist, Chest, Hips, Arms, Thighs)
  const measurementsChart = sheet.newChart()
    .setChartType(Charts.ChartType.LINE)
    .addRange(sheet.getRange('A7:A11')) // X-axis with header
    .addRange(sheet.getRange('E7:E11')) // Series 1: Waist (cm)
    .addRange(sheet.getRange('F7:F11')) // Series 2: Chest (cm)
    .addRange(sheet.getRange('G7:G11')) // Series 3: Hips (cm)
    .addRange(sheet.getRange('H7:H11')) // Series 4: Arms (cm)
    .addRange(sheet.getRange('I7:I11')) // Series 5: Thighs (cm)
    .setNumHeaders(1) // Use row 7 as headers
    .setPosition(startRow, 8, 0, 0)
    .setOption('title', 'Body Measurements Progress (cm)')
    .setOption('titleTextStyle', { fontName: FONT_FAMILY, fontSize: 12 })
    .setOption('legend', { position: 'bottom', textStyle: { fontName: FONT_FAMILY, fontSize: 10 } })
    .setOption('hAxis', { title: 'Week', titleTextStyle: { fontName: FONT_FAMILY } })
    .setOption('vAxis', { title: 'Measurement (cm)', titleTextStyle: { fontName: FONT_FAMILY } })
    .setOption('useFirstColumnAsDomain', true)
    .setOption('width', 500)
    .setOption('height', 300)
    .build();

  sheet.insertChart(measurementsChart);

  // Chart 3: Subjective Measurements - Energy, Sleep, Mood, Confidence
  // Data range: A7:M50, Series: J, K, L, M
  const subjectiveChart = sheet.newChart()
    .setChartType(Charts.ChartType.LINE)
    .addRange(sheet.getRange('A7:A11')) // X-axis with header
    .addRange(sheet.getRange('J7:J11')) // Series 1: Energy (1-10)
    .addRange(sheet.getRange('K7:K11')) // Series 2: Sleep Quality (1-10)
    .addRange(sheet.getRange('L7:L11')) // Series 3: Mood / Motivation (1-10)
    .addRange(sheet.getRange('M7:M11')) // Series 4: Confidence (1-10)
    .setNumHeaders(1) // Use row 7 as headers
    .setPosition(startRow + 20, 1, 0, 0) // Position below first chart
    .setOption('title', 'Subjective Measurements (1-10 Scale)')
    .setOption('titleTextStyle', { fontName: FONT_FAMILY, fontSize: 12 })
    .setOption('legend', { position: 'bottom', textStyle: { fontName: FONT_FAMILY, fontSize: 10 } })
    .setOption('hAxis', { title: 'Week', titleTextStyle: { fontName: FONT_FAMILY } })
    .setOption('vAxis', { title: 'Score (1-10)', titleTextStyle: { fontName: FONT_FAMILY }, minValue: 0, maxValue: 10 })
    .setOption('useFirstColumnAsDomain', true)
    .setOption('width', 500)
    .setOption('height', 300)
    .build();

  sheet.insertChart(subjectiveChart);
}

/**
 * Create RPE Guide tab
 */
function createRPEGuide(sheet) {
  // Set column widths (A = emoji, B = description)
  sheet.setColumnWidth(1, 80);  // Column A for emoji
  sheet.setColumnWidth(2, 720); // Column B for description

  // Apply header with logo (merge to columns A-B for RPE Guide)
  let currentRow = applyHeaderWithLogo(sheet, 1, 2);

  // RPE GUIDE Header
  sheet.getRange(currentRow, 1, 1, 2).merge()
    .setValue('RATING OF PERCEIVED EXERTION (RPE) GUIDE')
    .setFontFamily(FONT_FAMILY)
    .setFontSize(14)
    .setFontWeight('bold')
    .setFontColor(OFF_WHITE)
    .setBackground(DEEP_CHARCOAL)
    .setHorizontalAlignment('center')
    .setVerticalAlignment('middle');
  sheet.setRowHeight(currentRow, 30);
  currentRow++;

  // Blank spacer
  sheet.setRowHeight(currentRow++, 10);

  // Instructions
  sheet.getRange(currentRow, 1, 1, 2).merge()
    .setValue('Use this guide to rate how hard each exercise feels after completing your set. Log your RPE in the blue "RPE after activity" column.')
    .setFontFamily(FONT_FAMILY)
    .setFontSize(DEFAULT_FONT_SIZE)
    .setWrapStrategy(SpreadsheetApp.WrapStrategy.WRAP)
    .setVerticalAlignment('top');
  sheet.setRowHeight(currentRow, 40);
  currentRow++;

  // Blank spacer
  sheet.setRowHeight(currentRow++, 10);

  // RPE Scale (10 rows with emoji faces)
  const rpeData = [
    { rpe: 10, emoji: '😵', description: 'I am dead!!!', color: '#E06666', textColor: '#FFFFFF' },
    { rpe: 9, emoji: '🥵', description: 'I am probably going to die!', color: '#E06666', textColor: '#FFFFFF' },
    { rpe: 8, emoji: '😤', description: 'I can grunt in response to your questions and can only keep this pace for a short time period.', color: '#F6B26B', textColor: '#000000' },
    { rpe: 7, emoji: '😓', description: 'I can still talk but I don\'t really want to and I am sweating like a pig!', color: '#F6B26B', textColor: '#000000' },
    { rpe: 6, emoji: '😅', description: 'I can still talk but I am slightly breathless and definitely sweating.', color: '#FFD966', textColor: '#000000' },
    { rpe: 5, emoji: '🙂', description: 'I\'m just above comfortable, I am sweating more and can talk easily.', color: '#FFD966', textColor: '#000000' },
    { rpe: 4, emoji: '😊', description: 'I\'m sweating a little, but I feel good and I can carry on a conversation comfortably.', color: '#93C47D', textColor: '#000000' },
    { rpe: 3, emoji: '😌', description: 'I am still comfortable, but I\'m breathing a bit harder.', color: '#93C47D', textColor: '#000000' },
    { rpe: 2, emoji: '😎', description: 'I\'m comfortable and I can maintain this pace all day long.', color: '#93C47D', textColor: '#000000' },
    { rpe: 1, emoji: '😴', description: 'I\'m watching TV and eating bon bons.', color: '#93C47D', textColor: '#000000' }
  ];

  rpeData.forEach(item => {
    // Column A: Emoji (30pt, centered)
    sheet.getRange(currentRow, 1)
      .setValue(item.emoji)
      .setFontSize(30)
      .setBackground(item.color)
      .setHorizontalAlignment('center')
      .setVerticalAlignment('middle');

    // Column B: Description text
    sheet.getRange(currentRow, 2)
      .setValue(`RPE ${item.rpe}: ${item.description}`)
      .setFontFamily(FONT_FAMILY)
      .setFontSize(DEFAULT_FONT_SIZE)
      .setFontWeight('bold')
      .setBackground(item.color)
      .setFontColor(item.textColor)
      .setVerticalAlignment('middle')
      .setWrapStrategy(SpreadsheetApp.WrapStrategy.WRAP);

    sheet.setRowHeight(currentRow, 40);
    currentRow++;
  });

  // Blank spacer
  sheet.setRowHeight(currentRow++, 10);

  // Additional guidance
  sheet.getRange(currentRow, 1, 1, 2).merge()
    .setValue('💡 TIP: Aim for RPE 6-8 for most strength exercises. RPE 8-9 is appropriate for your heaviest compound lifts (squats, deadlifts). RPE 10 should be rare and used strategically.')
    .setFontFamily(FONT_FAMILY)
    .setFontSize(DEFAULT_FONT_SIZE)
    .setWrapStrategy(SpreadsheetApp.WrapStrategy.WRAP)
    .setVerticalAlignment('top')
    .setBackground('#FFF9E6'); // Light yellow background
  sheet.setRowHeight(currentRow, 50);
  currentRow++;

  // Delete excess columns and rows (RPE Guide only needs columns A & B)
  const maxColumns = sheet.getMaxColumns();
  if (maxColumns > 2) {
    sheet.deleteColumns(3, maxColumns - 2);
  }
  const maxRows = sheet.getMaxRows();
  if (maxRows > currentRow) {
    sheet.deleteRows(currentRow + 1, maxRows - currentRow);
  }
}

/**
 * Helper function to convert column number to letter
 */
function columnToLetter(column) {
  let temp, letter = '';
  while (column > 0) {
    temp = (column - 1) % 26;
    letter = String.fromCharCode(temp + 65) + letter;
    column = (column - temp - 1) / 26;
  }
  return letter;
}
