---
title: "CG Calculation Methods"
description: "Different methods for determining the Centre of Gravity position."
keywords: ["CG calculation", "mathematical method", "graphical method", "index method"]
---

## Mathematical Method

The most precise method involves calculating the moments of all masses.

1.  **Datum**: A fixed reference line.
2.  **Arm**: Horizontal distance from the datum to the CG of a component.
3.  **Moment**: Mass × Arm.

$$
\text{Total Moment} = \sum (\text{Mass}_i \times \text{Arm}_i)
$$
$$
\text{CG Position} = \frac{\text{Total Moment}}{\text{Total Mass}}
$$

*   Arms behind the datum are positive (+).
*   Arms forward of the datum are negative (-).

## Graphical/Index Method

To simplify pilot workload and reduce calculation errors, manufacturers provide:
*   **Loading Graphs**: Pilot reads an index or moment value from a graph for each load item (fuel, pax, bags).
*   **CG Envelopes**: The total index is plotted against total mass to verify it falls within the safe envelope.

This avoids large moment numbers and complex arithmetic, replacing them with simple addition of index units.

## Electronic Method

Modern aircraft use Flight Management Computers (FMC) or Electronic Flight Bags (EFB) to calculate mass and CG.
*   **Input**: ZFM, Fuel, Pax distribution.
*   **Output**: TOW, LAW, ZFW CG, TOW CG, Trim setting.
*   **Crosscheck**: Pilots must still verify inputs against the load sheet.
