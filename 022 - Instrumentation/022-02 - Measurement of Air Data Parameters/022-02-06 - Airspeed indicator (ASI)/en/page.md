---
title: "Airspeed Indicator (ASI): IAS, CAS, TAS, and Pitot-Static Errors"
description: "Understand ASI operation, color-code ranges, IAS/CAS/TAS relationships, and classic pitot-static blockage effects used in ATPL Instrumentation."
keywords:
    - "calibrated altitude"
    - "air density"
    - "low air density"
    - "what is the air density"
---
# Airspeed Indicator (ASI): IAS, CAS, TAS, and Pitot-Static Errors

The **Airspeed Indicator (ASI)** measures the speed of the aircraft through the air by comparing total pressure and static pressure.

## Principle
*   **Formula:** $\text{Dynamic Pressure} (q) = \text{Total Pressure} (P_t) - \text{Static Pressure} (P_s)$.
*   **Mechanism:** Pitot pressure ($P_t$) is fed to the capsule; static pressure ($P_s$) is fed to the case. The expansion of the capsule represents dynamic pressure ($1/2 \rho V^2$), which is calibrated to airspeed.

## Airspeed Definitions
1.  **IAS (Indicated):** The direct reading from the dial.
2.  **CAS (Calibrated):** IAS corrected for **Instrument** and **Position** errors.
3.  **EAS (Equivalent):** CAS corrected for **Compressibility** error (significant > 300 kts / Mach 0.4).
4.  **TAS (True):** EAS corrected for **Density** error (Altitude/Temperature). TAS is the actual speed through the air.
    *   *Rule of Thumb:* TAS increases with altitude for a constant IAS. ($TAS \approx EAS \times \sqrt{\rho_0 / \rho}$).

## Blockages (PUDSOD)
Errors depend on which port is blocked and the phase of flight:
*   **P**itot Blocked:
    *   **U**nder-reads in **D**escent (and over-reads in climb). Acts like an altimeter.
*   **S**tatic Blocked:
    *   **O**ver-reads in **D**escent (and under-reads in climb).

## Color Coding
*   **White Arc:** Flap operating range ($V_{SO}$ to $V_{FE}$).
*   **Green Arc:** Normal operating range ($V_{S1}$ to $V_{NO}$).
*   **Yellow Arc:** Caution range ($V_{NO}$ to $V_{NE}$).
*   **Red Line:** Never Exceed speed ($V_{NE}$).
*   **Blue Line:** Best single-engine rate of climb ($V_{YSE}$) on light twins.

## Unreliable Airspeed
Recognized by mismatched ASI readings, IAS disagree alerts, or abnormal pitch/power relationships. Pilots must cross-check with **Ground Speed** (GNSS/INS) and pitch/power tables.
