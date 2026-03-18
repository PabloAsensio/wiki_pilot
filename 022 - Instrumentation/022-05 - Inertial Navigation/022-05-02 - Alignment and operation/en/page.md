---
title: "Alignment and Operation"
description: "Procedures for alignment, operating modes (NAV, ATT), and performance monitoring of INS/IRS."
keywords: ["alignment", "NAV mode", "ATT mode", "drift", "gyrocompassing", "local vertical"]
---

## Alignment Process

The Inertial Reference System (IRS) must be aligned on the ground before flight to establish a navigation baseline. This process is critical for accurate operation.

### Requirements
*   **Stationary Aircraft**: The aircraft must not move during alignment. Movement disturbs the sensing of gravity and Earth's rotation.
*   **Position Entry**: The pilot must enter the current position (Latitude and Longitude) via the FMS CDU or ISDU.

### Phases of Alignment
1.  **Levelling (Determination of Local Vertical)**:
    *   Accelerometers sense the gravity vector.
    *   The system establishes the **Local Vertical** (down) and creates a horizontal plane (mathematically in IRS, mechanically in INS).
2.  **Gyrocompassing (Alignment to True North)**:
    *   The system detects the Earth's rotation (rate approx 15°/hour).
    *   Since the Earth rotates about the True North axis, the system can determine the direction of **True North** by measuring the horizontal component of Earth's rotation.
    *   **Latitude Calculation**: By measuring the magnitude of Earth's rotation vector, the system can estimate its own **Latitude**. It compares this calculated latitude with the pilot's entry to check for gross errors.
    *   **Longitude**: The system **cannot** determine Longitude; it relies entirely on the pilot's input.

### Alignment Time
*   **Duration**: Typically **10 minutes** at mid-latitudes.
*   **High Latitudes**: Alignment takes longer as latitude increases (Earth's rotational velocity vector is more vertical, making the horizontal component harder to detect).
*   **Limit**: Alignment is generally impossible above **82° Latitude** (Polar regions) due to insufficient horizontal Earth rate.

## Operating Modes (MSU - Mode Selector Unit)

The mode selector typically has the following positions:

1.  **OFF**: System is unpowered.
2.  **ALIGN**: Initiates the alignment and levelling process. Used for quick realignment or when full shut-down is not desired.
3.  **NAV**: Normal operating mode for flight. Provides all data (Attitude, Heading, Position, Speed).
4.  **ATT (Attitude)**: Reversionary mode.
    *   Used if the Navigation mode fails or alignment is lost in flight.
    *   Provides **Attitude** (Pitch/Roll) and **Heading** only.
    *   **Heading Entry**: In ATT mode, heading is not essentially reliable and often needs to be entered/updated manually periodically (e.g., every 15 mins) or synchronized.
    *   **Navigation Lost**: Position and groundspeed data are not available.

## Performance Monitoring (Drift)

Errors in inertial systems accumulate over time (Drift). Pilots check the accuracy of the system after the flight.

### Post-Flight Check
*   **Condition**: Aircraft parked and stationary.
*   **Residual Groundspeed**: The Groundspeed (GS) readout should ideally be **zero**. A high residual groundspeed indicates excessive error/drift.
*   **Position Drift**: Comparing the calculated position with the known gate coordinates.
    *   The drift is measured in **NM/hour**.
    *   Calculation: `Total Position Error (NM) / Flight Time (Hours)`.
    *   Limits vary by unit, but typically drift should be low (e.g., < 2 NM/hr for INS, significantly better for IRS).

## Key Points & Warnings
*   **Moving Aircraft**: If the aircraft moves during alignment, the process restarts or fails.
*   **Latitude Mismatch**: If the entered latitude differs significantly from the sensed latitude, the system will reject the alignment (flashing align light).
*   **Longitude Error**: Entering the wrong longitude is not detected by the system (as it cannot sense longitude) but shifts the entire navigation map, resulting in a position error for the whole flight.
*   **In-flight Realignment**: Not possible for calibration of position/north. Only Attitude (ATT) mode can be engaged if NAV is lost.
