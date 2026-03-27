---
title: "AHRS and Solid-State Gyros: MEMS Sensors and Attitude/Heading Computation"
description: "Study AHRS architecture with MEMS gyros, accelerometers, and magnetometers, plus RLG principles for high-accuracy attitude and heading reference."
keywords:
    - "magnetic headings"
    - "magnetic course"
    - "points on the compass"
    - "compass turns"
---
# AHRS and Solid-State Gyros: MEMS Sensors and Attitude/Heading Computation

Modern aircraft use solid-state technology to replace mechanical spinning gyroscopes, increasing reliability and accuracy.

## AHRS (Attitude and Heading Reference System)
A single unit that computes aircraft attitude (Pitch/Roll) and Heading (Yaw). It typically replaces the separate Attitude Indicator and Directional Gyro.
*   **Components:**
    *   **MEMS Gyroscopes (Rate Sensors):** Measure angular **rate** (not position) around 3 axes.
    *   **Accelerometers:** Measure acceleration (gravity) to determine the vertical (Pitch/Roll reference).
    *   **Magnetometers:** Measure the magnetic field to determine Heading (Yaw reference, like a Flux Valve).
*   **Integration:** A computer integrates the rate data to calculate attitude and uses gravity/magnetic data to correct for drift.

## Ring Laser Gyro (RLG)
Used in high-end Inertial Reference Systems (IRS/INS).
*   **Principle:** Uses two counter-rotating laser beams in a triangular path.
*   **Sagnac Effect:** When the unit rotates, one beam has a shorter path and the other a longer path, creating a frequency shift.
*   **Features:** No moving parts, extremely accurate, measure angular rate directly.

## Advantages over Mechanical Gyros
*   **Reliability:** No moving parts (Solid-state).
*   **Maintenance:** Significantly reduced.
*   **Startup:** Faster alignment.
*   **Output:** Digital data easily fed to Glass Cockpit displays (PFD/ND).
