---
title: "CDU / MCDU Interface"
---

## Overview

The **Control Display Unit (CDU)**, or **Multipurpose Control and Display Unit (MCDU)** on Airbus aircraft, is the primary interface between the flight crew and the Flight Management Computer (FMC).

It allows the crew to:
*   Enter navigation and performance data.
*   Monitor flight progress.
*   Manage automatic flight functions.
*   Send non-FMS commands (e.g., ACARS, Datalink) on modern MCDUs.

## Interface Components

The unit consists of a display screen and a keyboard.

### Display Layout
*   **Title Line:** Displays the name of the current page (e.g., `INIT`, `LEGS`, `PROG`).
*   **Label Lines:** Small text identifying the data field below it.
*   **Data Lines:** The actual values (computed data or pilot entries).
*   **Scratchpad:** The bottom line of the screen.
    *   Displays alphanumeric characters typed by the pilot *before* they are inserted into a data field.
    *   Displays system messages (e.g., `CHECK GW`, `GPS PRIMARY`).

### Controls
*   **Line Select Keys (LSK):** Buttons on the left (1L-6L) and right (1R-6R) of the screen used to:
    *   Move data from the scratchpad to a field.
    *   Select items or prompts (e.g., ` <ACTIVATE> `).
*   **Keyboard:** Alpha-numeric keypad for data entry.
*   **EXEC Key:** The "Execute" button (often illuminated) acts as the "Enter" or "Confirm" key to make a modified flight plan active.

### Data Symbology
*   **Amber Boxes (`[][][]`):** Indicate **Mandatory** data entry required for the FMS to function (e.g., ZFW, Cruise Flight Level).
*   **Blue/Green Dashes (`-----`):** Indicate **Optional** data entry (e.g., Wind data, Temp deviation).

## Pre-Flight Setup Sequence

A standard logical flow is used to initialize the FMS:

1.  **IDENT:** **"Who am I?"**
    *   Start-up identifying Aircraft Model, Engine Rating, and Navigation Database validity.
2.  **POS INIT:** **"Where am I?"**
    *   IRS Alignment.
    *   Entry of Present Position (Latitude/Longitude).
3.  **RTE (Route):** **"Where am I going?"**
    *   Origin and Destination airports.
    *   Route definition (Airways, Waypoints, Procedures).
4.  **PERF INIT:** **"How/When will I get there?"**
    *   **Zero Fuel Weight (ZFW):** Critical mandatory input from the loadsheet to calculate Gross Weight.
    *   **Fuel:** Block Fuel entry for planning (FMS usually reads actual FOB from sensors).
    *   **Cost Index:** Economic strategy.
    *   **Cruising Altitude:** Planned level.

## Operational Redundancy

*   **Dual Configuration:** In a dual FMS installation, data entered on one CDU is typically crosstalked to the other FMC.
*   **Independent Display:** While databases are shared, each pilot can select different pages on their respective CDU (e.g., Pilot A views `LEGS`, Pilot B views `PROG`).
*   **Cross-Side Operation:** In failure cases (e.g., Failure of FMGC 1 and MCDU 2), the remaining MCDU 1 can often communicate with FMGC 2 to maintain control.
