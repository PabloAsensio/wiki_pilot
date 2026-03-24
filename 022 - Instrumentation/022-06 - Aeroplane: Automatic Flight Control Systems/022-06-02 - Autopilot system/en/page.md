---
title: "Autopilot System & Modes"
description: "Detailed operation of autopilot modes, including synchronization, TO/GA, and interaction with Flight Director."
keywords: ["synchronization", "TO/GA", "CWS", "automation modes", "FMA", "flight envelope"]
---

## Autopilot Engagement & Synchronization

For a smooth transition from manual to automatic flight, the autopilot system uses a **synchronization function**.
*   **Purpose**: Prevents "snatching" or jerking of controls upon engagement.
*   **Mechanism**: Before engagement, the system checks that the aircraft is in trim and matches the autopilot's internal commands with the current position of the control surfaces/servos.
*   **Failure**: If synchronization fails, the autopilot will typically refuse to engage.

## Mixed Modes: TO/GA (Take-Off / Go-Around)

The **Take-Off / Go-Around (TO/GA)** mode is a combined mode involving both Autopilot and Autothrust.
*   **Activation**: Typically activated by a switch on the throttle levers.
*   **Go-Around Function**:
    *   Disconnects Approach modes (like G/S and LOC).
    *   Commands a pitch-up attitude (e.g., for 1000-2000 fpm climb).
    *   Autothrust advances to Go-Around thrust (reduced or full limit).
    *   **Logic**: The go-around mode will command a climb **regardless of the missed approach altitude** selected on the MCP (it demands a positive climb gradient away from the ground).

## Vertical Modes

Vertical modes control the aircraft's pitch/thrust to manage altitude or vertical path.
*   **Vertical Speed (V/S)**: Maintains a specific rate of climb/descent (e.g., 1000 ft/min). Airspeed is controlled by pitch/thrust balance (potential risk of stalling if thrust is insufficient).
*   **Flight Path Angle (FPA)**: Maintains a specific geometric angle of climb/descent relative to the horizon (e.g., -3.0°). Adjusts V/S automatically if groundspeed changes.
*   **Level Change (LVL CHG) / Open Climb/Descent**: Pitch controls airspeed, Thrust is set to Climb/Idle. Used for efficient altitude changes.
*   **Altitude Hold (ALT)**: Captures and maintains a specific barometric altitude.

## Lateral Modes

Lateral modes control roll to manage heading or track.
*   **Heading (HDG) / Track (TRK)**: Follows a pilot-selected Vector.
*   **LNAV (Lateral Navigation)**: Follows the FMS flight plan (great circle route between waypoints).
*   **VOC/LOC**: Intercepts and tracks radio navigation signals.

## Control Wheel Steering (CWS)

**Control Wheel Steering (CWS)** is a hybrid mode available on some aircraft.
*   **Operation**: The pilot maneuvers the aircraft manually using the yoke. When the pilot releases the pressure, the autopilot **holds the existing attitude** (pitch and roll).
*   **Annunciation**: Displays "CWS P" (Pitch) and "CWS R" (Roll) on the FMA.
*   **Distinction**: The autopilot does NOT follow internal commands in this mode; it responds to pilot pressure.

## Flight Mode Annunciator (FMA) awareness

It is critical for pilots to monitor the **Flight Mode Annunciator (FMA)** (top of PFD).
*   **Undesired States**: Failing to notice mode changes can lead to danger. Example: Attempting to capture a Glideslope (G/S) before capturing the Localizer (LOC) can result in a descent into unprotected airspace.
*   **Normal Law**: In Fly-By-Wire aircraft, "Normal Law" provides full flight envelope protection. Reversion to "Direct Law" or "Alternate Law" degrades these protections.

## Power Supply & Backup

*   **ADC Dependency**: The Autopilot relies on the Air Data Computer (ADC). An ADC failure affects all associated systems (AP, FD, Autothrust).
*   **Disconnection**: Disconnecting the AP (e.g., via instinctive cutout) triggers a temporary warning.
