---
title: "Flight Data Recorder (FDR): Mandatory Parameters, Event Marks, and Use"
description: "Study FDR recording requirements, mandatory flight-parameter capture, automatic start/stop logic, and event-mark usage for investigation workflows."
keywords:
    - "fdr"
    - "flight data recorder"
    - "flight level"
    - "minimum speed"
---

# Flight Data Recorder (FDR): Mandatory Parameters, Event Marks, and Use

The **FDR** records technical flight parameters to assist in accident analysis and troubleshooting. It is typically housed in a crash-survivable container (shockproof, fireproof, orange colored) fitted with an **Underwater Locating Device (ULD)**.

## Recording Requirement
The type and number of parameters recorded are determined by:
1.  **Recording Capacity** of the system.
2.  **Applicable Operational Requirements** (Regulations).

## Mandatory Parameters
Common parameters include (but are not limited to):
*   Time / Relative Time Count.
*   Pressure Altitude and Airspeed.
*   Attitude (Pitch and Roll).
*   Heading.
*   Normal Acceleration (Vertical G).
*   Thrust/Power on each engine and Lever positions.
*   Configuration (Flaps, Slats, Spoilers, Gear).
*   Autopilot/Flight Director modes.

## Operation
*   **Automatic Activation**:
    *   **Start**: Prior to the airplane being capable of moving under its own power (often on engine start or power-up).
    *   **Stop**: After the airplane is incapable of moving under its own power (engine shutdown).
*   **Event Button**: A button in the cockpit that allows the crew to place a **Time Mark** in the data stream. This highlights a specific event (e.g., a temporary system failure or turbulence) to aid investigators in locating the relevant data later.
