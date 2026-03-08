---
title: "International Standard Atmosphere (ISA)"
description: "Reference guide on the International Standard Atmosphere (ISA), including standard temperature, pressure, and lapse rate for aviation studies."
keywords: ["isa meteorology", "international standard atmosphere ISA aviation", "ISA values ATPL meteorology", "standard temperature and pressure flying"]
---

The International Standard Atmosphere (ISA) is a hypothetical atmospheric model used as a reference for air navigation and aircraft design.

## Standard Values

![Standard Atmosphere Model (ISA)](https://upload.wikimedia.org/wikipedia/commons/9/9d/Comparison_US_standard_atmosphere_1962.svg)

*   **Mean Sea Level (MSL)**:
    *   Temperature: **+15°C**
    *   Pressure: **1013.25 hPa**
    *   Density: **1.225 kg/m³**
*   **Troposphere**:
    *   Lapse Rate: Temperature decreases at a rate of **2°C per 1000 ft** (or 0.65°C per 100 m).
*   **Tropopause**:
    *   Altitude: **36,090 ft** (11 km).
    *   Temperature: **-56.5°C**.
*   **Lower Stratosphere**:
    *   From the tropopause up to approx. 20 km (65,000 ft), the temperature remains constant (**Isothermal**) at **-56.5°C**.

## ISA Temperature Calculations

To calculate the standard temperature at a given altitude (in the troposphere):

$$T_{ISA} = 15 - (2 \times \frac{Altitude}{1000})$$

**Examples:**
*   At **18,000 ft**: $15 - (2 \times 18) = 15 - 36 = \mathbf{-21^\circ C}$.
*   At **20,000 ft**: $15 - (2 \times 20) = 15 - 40 = \mathbf{-25^\circ C}$.
*   At **30,000 ft**: $15 - (2 \times 30) = 15 - 60 = \mathbf{-45^\circ C}$.

If the actual temperature is different from ISA, it is expressed as a deviation (e.g., ISA +10, ISA -5).
*   If at 18,000 ft the actual temperature is -35°C (ISA being -21°C), the deviation is ISA -14°C.
*   *Note: If the temperature is colder than ISA, the air density will be higher than standard.*

## Pressure Levels and Flight Levels

Relationship between Flight Levels (FL) and pressure in hPa:

| Flight Level (FL) | Pressure (hPa) |
| :--- | :--- |
| FL050 | 850 |
| FL100 | 700 |
| FL140 | 600 |
| FL180 | 500 |
| **FL240** | **400** |
| FL300 | 300 |
| FL340 | 250 |
| **FL390** | **200** |
| FL450 | 150 |

## Lapse Rates

![Adiabatic Lapse Rates (DALR and SALR)](https://upload.wikimedia.org/wikipedia/commons/d/d4/Adiabatic_lapse_rate.svg)

1.  **ELR (Environmental Lapse Rate)**: It is the actual temperature change with height at a given time and place. The ISA average is 2°C/1000 ft.
2.  **DALR (Dry Adiabatic Lapse Rate)**: Cooling rate of an **unsaturated** air parcel that rises. Constant value: **3°C/1000 ft**.
3.  **SALR (Saturated Adiabatic Lapse Rate)**: Cooling rate of a **saturated** air parcel (100% humidity). Variable value (approx. **1.8°C/1000 ft**). It is lower than the DALR because the condensation of water vapor releases **latent heat**, which warms the parcel and reduces its cooling rate.
