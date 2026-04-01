---
title: "PET and PSR Calculations"
description: "Critical point and point of no return calculations for flight planning."
keywords: ["PET", "PSR", "Point of Equal Time", "Point of Safe Return", "Critical Point", "ETP"]
---

# PET and PSR Calculations


## Point of Equal Time (PET) / Critical Point (CP)
The point along the track where it takes the **same time** to continue to destination as to return to departure (or proceed to an alternate).
*   Important for Engine Failure or Depressurization scenarios.
*   **Concept**: Since wind affects Ground Speed (GS) differently outbound vs inbound (headwind becomes tailwind), the PET shifts **into the wind**.
*   **Formula**:
    $$
    Distance_{PET} = \frac{D \times GS_{Home}}{GS_{Home} + GS_{Dest}}
    $$
    *   $D$: Total Distance.
    *   $GS_{Home}$: Ground Speed returning.
    *   $GS_{Dest}$: Ground Speed continuing.

## Point of Safe Return (PSR) / Point of No Return (PNR)
The furthest point along the track from which the aircraft can return to the departure airport (or alternate) with the required fuel reserves still intact.
*   Beyond this point, the aircraft **must** proceed to the destination (or another en-route alternate).
*   **Formula**:
    $$
    Time_{PSR} = \frac{Endurance_{Safe} \times GS_{Home}}{GS_{Home} + GS_{Out}}
    $$
    *   $Endurance_{Safe}$: Total usable endurance minus reserves.
    *   $GS_{Out}$: Ground speed outbound.
