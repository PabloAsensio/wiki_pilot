---
title: "Radio Altimeter (RA): FMCW Principle, Integration, and Failure Impacts"
description: "Study radio-altimeter operation, FMCW ranging, calibration to touchdown geometry, and integration with autoland, GPWS/TAWS, and TCAS inhibitions."
keywords:
    - "radio altimeter"
    - "altimeter readings"
    - "flight level"
    - "minimum speed"
---

# Radio Altimeter (RA): FMCW Principle, Integration, and Failure Impacts

## Overview

The **Radio Altimeter (RA)**, or Radar Altimeter, is a self-contained onboard system that measures the **True Height** of the aircraft above the terrain immediately below it (Above Ground Level - AGL).

## Operating Principle

*   **Frequency Range:** Operates in the SHF band (4200 MHz - 4400 MHz).
*   **Method:** Transmits a **Frequency Modulated Continuous Wave (FMCW)** downwards.
*   **Calculation:** It measures the frequency difference between the transmitted wave and the received wave reflected from the ground. This difference is proportional to the time delay and thus the height.
*   **Operating Range:** Typically indicates from **0 to 2,500 ft**. Above this altitude, the display is usually blanked.

## Calibration and Residual Height

*   **Antenna Location:** Antennas are located on the underside of the fuselage.
*   **Residual Height:** The vertical distance between the antennas and the lowest part of the landing gear (main wheels).
*   **Indication:** The system is calibrated to indicate **0 feet** when the main wheels touch the ground in the landing attitude.

## System Integration

The Radio Altimeter is a critical sensor that provides data to multiple aircraft systems:

1.  **AFCS (Autopilot & Flight Director):**
    *   Essential for **Autoland** operations (controlling Flare and Rollout).
    *   Disconnects Glideslope signal typically at 50 ft.
2.  **Autothrottle (A/T):**
    *   Triggers the **"RETARD"** mode during landing (reducing thrust to idle at specific heights, e.g., 20-30 ft).
3.  **GPWS / TAWS:**
    *   Primary source of height data to calculate closure rates with terrain.
4.  **TCAS / ACAS:**
    *   Used to **inhibit** certain Resolution Advisories (RAs) near the ground (e.g., "Descend" RAs are inhibited below 1,100 ft AGL).

## Operational Implications of Failure

*   **Autoland Capability:** Loss of an RA typically degrades the Autoland capability (e.g., from Fail-Operational to Fail-Passive or prohibiting Autoland entirely).
*   **False Readings:** A faulty RA indicating a low height (e.g., < 50 ft) during cruise could cause the Autothrottle to erroneously enter **RETARD** mode, reducing thrust to idle.
