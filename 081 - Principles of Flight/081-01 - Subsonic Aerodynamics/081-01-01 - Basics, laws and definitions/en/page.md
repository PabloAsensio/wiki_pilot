---
title: "Aerodynamics: Basics & Definitions"
description: "Fundamental laws of aerodynamics including Bernoulli's Principle and the Continuity Equation."
keywords: ["Bernoulli", "continuity equation", "static pressure", "dynamic pressure", "IAS", "TAS", "CAS"]
---

# Aerodynamics: Basics & Definitions


## The Atmosphere
*   **Composition**: 78% Nitrogen, 21% Oxygen, 1% Other (Argon, CO2).
*   **ISA (International Standard Atmosphere)**: Used for calibration and comparison.
    *   Temperature: 15°C (288.15 K) at Mean Sea Level (MSL). Lapse rate -1.98°C/1000 ft up to 11km (Tropopause).
    *   Pressure: 1013.25 hPa (29.92 inHg) at MSL.
    *   Density: 1.225 kg/m³ at MSL.

## Continuity Equation
For a steady flow of an incompressible fluid (subsonic flow is treated as incompressible):
$$ A_1 V_1 = A_2 V_2 $$
*   **$A$**: Area.
*   **$V$**: Velocity.
*   If the cross-sectional area of a tube **decreases**, the velocity of the fluid **increases**.

## Bernoulli's Principle
Subject to the flow being steady, incompressible, and inviscid (no friction). The sum of static pressure and dynamic pressure is constant along a streamline.
$$ P_{static} + \frac{1}{2}\rho V^2 = Constant $$
$$ P_{static} + P_{dynamic} = P_{total} $$
*   As velocity ($V$) **increases** (due to converging tube), dynamic pressure **increases**, and static pressure ($P_{static}$) **decreases**.
*   This explains lift generation: air accelerating over the curved upper surface of a wing has lower static pressure than the air below.

## Airspeeds
*   **IAS (Indicated Airspeed)**: Read from the instrument. Driven by dynamic pressure ($q = \frac{1}{2}\rho V^2$).
*   **CAS (Calibrated Airspeed)**: IAS corrected for instrument and position error.
*   **EAS (Equivalent Airspeed)**: CAS corrected for compressibility (significant > 300kt / Mach 0.6).
*   **TAS (True Airspeed)**: The actual speed of the aircraft through the air mass. Corrected for density error.
    *   $TAS = EAS \times \frac{1}{\sqrt{\sigma}}$ (where $\sigma$ is relative density).
    *   At constant IAS, TAS **increases** with altitude (approx 2% per 1,000 ft).
