---
title: "Weighing Procedure"
description: "Procedures for determining aircraft mass and CG position by weighing."
keywords: ["weighing procedure", "scales", "weighing points", "leveling", "datum"]
---

## Weighing Requirements

Weighing establishes the **Basic Empty Mass (BEM)** and the **CG position** of the empty aircraft.

### Aircraft Preparation
Before weighing, the aircraft must be in a specific configuration:
*   **Clean**: Removing dirt, ice, and snow.
*   **Fluids**: Draining usable fuel (unusable fuel remains and is part of BEM). Oil and hydraulic fluids at operating levels.
*   **Equipment**: All fixed equipment installed (seats, galleys, avionics).
*   **Leveling**: The aircraft must be leveled longitudinally and laterally using leveling points defined by the manufacturer.

### Weighing Method
The aircraft is placed on scales at the **jacking points** or under the **wheels**.
*   **Reaction Forces**: The scales measure the reaction force ($R$) at each point (Nose/Tail wheel, Main wheels).
    *   $R_L, R_R$: Left and Right Main Wheel reactions.
    *   $R_N$ or $R_T$: Nose or Tail Wheel reaction.

$$
\text{Total Mass} = R_L + R_R + R_N
$$

## Calculation of CG Position

The position of the CG is calculated using the Principle of Moments.
1.  **Define Datum**: Usually the nose, firewall, or a specific frame forward of the nose.
2.  **Measure Arms**: Distance from the Datum to the weighing points ($d_L, d_R, d_N$).
3.  **Sum of Moments**: Calculate the moment for each reaction ($Force \times Distance$).
    *   $\text{Moment} = \text{Reaction} \times \text{Arm}$
4.  **Find CG Arm**:
    $$
    \text{CG Arm} = \frac{\text{Total Moment}}{\text{Total Mass}}
    $$

*Note: Distances aft of the datum are positive (+), forward are negative (-).*
