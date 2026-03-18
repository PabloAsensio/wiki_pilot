---
title: "Fly-By-Wire (FBW)"
description: "Electronic flight control systems and flight envelope protection."
keywords: ["fly-by-wire", "flight control computer", "protection", "alpha floor", "stick pusher"]
---

## Concept
Replaces mechanical linkages (cables/rods) with electrical signals.
*   Pilot input -> Computer -> Actuator -> Control Surface.
*   Computers can modify inputs to ensure stability and prevent exceeding limits.

## Flight Envelope Protection
FBW systems (like Airbus Laws) prevent the pilot from stalling or overstressing the aircraft.
1.  **High Speed Protection**: Automatically pitches up or reduces thrust to prevent overspeed.
2.  **High Angle of Attack Protection (Alpha Protection)**:
    *   **Alpha Floor**: Automatically applies TO/GA thrust if speed/AoA gets critically dangerous.
    *   **Alpha Max**: Limits the maximum AoA the pilot can command (elevator authority is reduced).
3.  **Bank Angle Protection**: Limits bank angle (e.g., to 67° or 33° depending on mode).
4.  **Load Factor Protection**: Limits G-load (e.g., +2.5g / -1.0g).

## Normal Law vs Direct Law
*   **Normal Law**: Full protections active.
*   **Direct Law**: No protections. Direct stick-to-surface relationship (like a Cessna). happens if multiple computers/sensors fail.
