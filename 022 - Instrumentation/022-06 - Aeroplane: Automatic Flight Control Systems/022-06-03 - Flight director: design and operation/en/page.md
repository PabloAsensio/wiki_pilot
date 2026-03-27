---
layout: default
title: "Flight Director Design and Operation: Command Bars, Modes, and Crew Use"
description: "Learn flight-director command logic, crossbar/V-bar interpretation, manual and AP-coupled operation, and safe handling during failures."
keywords:
  - "flight level"
  - "minimum speed"
  - "magnetic headings"
  - "compass turns"
parent: "022-06 - Aeroplane: Automatic Flight Control Systems"
grand_parent: "022 - Instrumentation"
nav_order: 3
---

# Flight Director Design and Operation: Command Bars, Modes, and Crew Use

## Principles

The **Flight Director (FD)** provides visual guidance to the pilot to join and maintain a desired flight path with the optimum attitude. The FD computer calculates the **direction and magnitude** of the control inputs (pitch and roll) required to satisfy the selected flight guidance modes.

- **Information Display**: Presented as command bars on the Attitude Director Indicator (ADI) or Primary Flight Display (PFD).
- **Function**:
  - **Manual signal**: The pilot manually manipulates the controls to center the command bars.
  - **Automatic signal**: When the Autopilot (AP) is engaged, it follows the same commands computed by the FD.

### Command Bars

There are two main types of presentation: "Crossbars" (more common on Airbus/modern systems) and "V-Bars" (often found on Boeing/older systems).

1.  **Vertical Bar (Roll Command)**:
    - Moves left or right.
    - Indicates the necessary correction to the **bank angle** (roll channel) to follow the lateral path (Heading, Nav, Localizer, etc.).
    - To follow: If the bar moves left, the pilot must bank left.
2.  **Horizontal Bar (Pitch Command)**:
    - Moves up or down.
    - Indicates the necessary correction to the **pitch angle** (pitch channel) to follow the vertical profile (Altitude, V/S, Glide Slope, Speed, etc.).
    - To follow: If the bar moves up, the pilot must pull back (pitch up).

> **Note**: The FD indicates *attitude* corrections (pitch and bank), not position relative to the path directly (though following them corrects position).

## Operation and Usage

The modes available for the Flight Director are **identical** to those available for the Autopilot. They are selected on the same panel:
- **MCP (Mode Control Panel)** on Boeing.
- **FCU (Flight Control Unit)** on Airbus.

### Modes of Operation

- **FD Only (Manual Flight)**: The pilot hand-flies the aircraft, strictly following the FD command bars to achieve the desired trajectory. The FD reduces pilot workload by converting complex navigation and performance data into simple pitch and bank targets.
- **FD + AP (Automatic Flight)**: The AP is engaged and servos move the control surfaces to follow the FD's computed commands. The pilot's role becomes **monitoring** that the AP is correctly following the FD indications.
- **Take-off (TO/GA)**:
  - Engaged via TO/GA switches.
  - Initial command: Fixed pitch up (e.g., 10°-15°) and wings level.
  - After liftoff: Pitch commands a target speed (e.g., $V_2 + 20$ kt) and roll maintains track or heading.

### Crew Coordination (Multi-pilot)

- **Pilot Flying (PF)**: Responsible for flying the aircraft (manually or managing the AP) and calling out mode changes.
- **Pilot Monitoring (PM)**: Responsible for monitoring flight parameters, checklists, and communications.
- **SOPs**: Both pilots must monitor the FMA (Flight Mode Annunciator) to confirm that the selected modes on the MCP/FCU are actually engaged or armed.

## Failure and Disengagement

If the FD command bars disappear or a warning flag appears:
- do **not** blindly engage the Autopilot (it uses the same data).
- **Investigate** the cause (check FMA for flags).
- Revert to "raw data" flying (basic attitude and navigation) if necessary.
- If the FD commands are erratic or contradict raw data, the FD should be **disengaged** (switched off) to declutter the display and avoid confusion.

### Indications

- **Centered Bars**: The aircraft is achieving the required pitch and bank to satisfy the active mode.
- **Deviated Bars**: Control input is required in the direction of the bar to return to the path.
