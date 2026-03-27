---
title: "Altimeter Fundamentals: Static Pressure, Subscale Settings, and Errors"
description: "Master altimeter operation from static-pressure sensing to QNH/QFE/STD settings, including lag, blockage behavior, and ISA-related indication errors."
keywords:
    - "altimeter altitude"
    - "altimeter reading"
    - "altimeter readings"
    - "altimeter pressure"
    - "calibrated altitude"
---
# Altimeter Fundamentals: Static Pressure, Subscale Settings, and Errors

The altimeter is essentially a calibrated barometer that measures **static pressure** and displays it as altitude based on the International Standard Atmosphere (ISA).

## Principle of Operation
*   **Sensor:** Contains essentially evacuated **aneroid capsules** (vacuum inside).
*   **Mechanism:** Static pressure is fed into the instrument case surrounding the capsules.
    *   **Climb:** Pressure decreases $\rightarrow$ Capsules expand.
    *   **Descent:** Pressure increases $\rightarrow$ Capsules compress.
*   **Linkage:** This expansion/compression is magnified by mechanical linkages to rotate the pointers.

## Types of Altimeters
*   **Sensitive Altimeter:** Uses multiple capsules for accuracy and range (tens, hundreds, thousands of feet).
*   **Servo-Altimeter:** Uses an electrical motor to drive the display.
    *   **Advantages:** Eliminates **lag error**, greater accuracy at high altitudes, enables digital outputs.
    *   **Disadvantage:** Relies on electrical power (flags appear on failure).

## Errors and Checks
*   **ISA Deviation:** Indicates true altitude *only* in ISA standard conditions.
*   **Blockage:** If the static port is blocked, the altimeter **freezes** at the altitude where the blockage occurred.
*   **Lag Error:** Mechanical altimeters have a slight delay during rapid altitude changes.
*   **GPS Altitude:** Geometric altitude derived from satellites. It is independent of pressure/temperature errors and useful for **gross error checking** of barometric altimeters, though it references a mathematical model (ellipsoid) rather than MSL.

## Subscale Settings
*   **QNH:** Indicates Altitude above Mean Sea Level (MSL).
*   **QFE:** Indicates Height above a specific reference datum (like an airfield).
*   **STD (1013.25 hPa):** Indicates Pressure Altitude (Flight Levels).
