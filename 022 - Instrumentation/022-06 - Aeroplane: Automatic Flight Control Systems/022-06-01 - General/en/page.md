---
title: "AFCS General Principles: Autopilot Loops, Modes, and Crew Monitoring"
description: "Overview of automatic flight-control architecture, inner and outer control loops, mode logic, and PF/PM monitoring responsibilities."
keywords:
  - "flight level"
  - "minimum speed"
  - "magnetic headings"
  - "compass turns"
---

# AFCS General Principles: Autopilot Loops, Modes, and Crew Monitoring

## Automatic Flight Control System (AFCS) Overview

The **Automatic Flight Control System (AFCS)** reduces pilot workload, enhances flight accuracy, and minimizes stress on the flight controls. It typically consists of:
*   **Autopilot Flight Director System (AFDS)**: Controls pitch and roll to follow a path or hold parameters (e.g., altitude).
*   **Autothrust (A/T)**: Manages engine thrust to control speed or rate of climb/descent.

### Pilot Roles
In multi-pilot aircraft, roles are defined to ensure safety:
*   **Pilot Flying (PF)**: Focuses on "flying the aircraft" (controlling attitude, speed, path) and managing the AFCS.
*   **Pilot Monitoring (PM)**: Monitors flight parameters, calls out deviations, handles ATC communications, and manages checklists/systems.

## Control Loops

Autopilots use **closed-loop control systems** to maintain stability and follow paths.

### Loop Types
1.  **Inner Loop (Stability)**: Senses displacement (e.g., from a rate gyro) and corrects it to stabilize the aircraft around its Center of Gravity (CG). Fast reaction.
2.  **Outer Loop (Guidance)**: Takes commands from the Mode Control Panel (MCP) or Flight Management Computer (FMC) to guide the aircraft's path (e.g., altitude hold, heading intercept).

### Feedback Mechanism
A closed loop compares the **actual** state (feedback) with the **desired** state (input).
*   **Example**: The system commands an elevator movement. A feedback sensor measures the **actual position** of the elevator and compares it to the commanded position to ensure accuracy.
*   **Oscillations**: If the system is too sensitive or overcompensates, it can cause **self-induced oscillations** (instability).

## Modes of Operation

### Basic (Stabilization) Modes
Operate via the inner loops to maintain aircraft attitude.
*   **Attitude Hold**: Maintains Pitch and Bank angle.
*   **Wings Level**: Keeps wings level.

### Guidance Modes
Operate via the outer loops to navigate in 3D space.
*   **Vertical**: Altitude Hold (ALT), Vertical Speed (V/S), Glideslope (G/S), VNAV.
*   **Lateral**: Heading (HDG), Track (TRK), LNAV, Localizer (VOR/LOC).

## Disengagement and Safety

### Manual Intervention
The crew must be ready to disconnect the autopilot if it behaves abnormally (e.g., large pitch oscillations near the ground).
*   **Disengage Methods**: Pressing the instinctive cut-out button on the control column/sidestick, pushing the stick/column beyond a threshold, or using the MCP/FCU pushbutton.
*   **Warnings**: Disconnection triggers audio/visual warnings.

### Envelope Protection
Modern systems (especially Fly-By-Wire) include protections to prevent the aircraft from exceeding safe limits (Stall, Overspeed, Excessive Bank).
*   **Command Speed Limiting**: Prevents exceeding VMO/MMO or stall speeds.
*   **Mode Reversion**: If a limit is approached (e.g., stall speed), the AFCS may automatically revert modes (e.g., to level change) to protect the aircraft.
