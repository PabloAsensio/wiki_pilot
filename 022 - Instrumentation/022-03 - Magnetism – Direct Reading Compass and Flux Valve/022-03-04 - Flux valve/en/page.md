---
title: "Flux Valve and Gyro-Magnetic Compass: Slaved and Free Modes"
description: "Learn flux-valve sensing principles and gyro-magnetic compass operation, including slaved correction loops, free mode use, and installation constraints."
keywords:
  - "magnetic headings"
  - "magnetic course"
  - "points on the compass"
  - "compass turns"
---
# Flux Valve and Gyro-Magnetic Compass: Slaved and Free Modes

The **Flux Valve** (or Flux Detector) is a sensor used in remote-reading compass systems to detect the **horizontal component** of the Earth's magnetic field without the moving parts and errors of a direct reading compass.

## Construction and Operation
It consists of three spokes (legs) arranged at 120°, made of soft iron, with excitation and pick-off coils.
*   **Sensing:** It detects the horizontal magnetic field electronically.
*   **Location:** Installed in a location with minimal magnetic interference from the aircraft (e.g., **Wing tip** or **Vertical Stabiliser**).
*   **Advantage:** It "senses rather than seeks". It does not rotate to align with North physically; instead, it outputs an electrical signal representing the magnetic heading.

## Gyro-Magnetic Compass
The Flux Valve is the sensing element of a Gyro-Magnetic Compass (or Remote Indicating Compass).
*   **Principle:** It combines the long-term **accuracy** of the magnetic north reference (Flux Valve) with the short-term **stability** of a gyroscope.
*   **Flux Valve:** Senses magnetic north (Long-term reference).
*   **Gyro:** Provides stability during turns and acceleration (Short-term reference).
*   **Error Detector & Amplifier:** Compares the gyro heading with the flux valve heading and uses a torque motor to "slave" or correct the gyro drift.

## Modes of Operation
1.  **Slaved Mode:** Normal operation. The gyro is automatically corrected to Magnetic North by the Flux Valve signals.
2.  **Free Mode (DG Mode):** Used if the flux valve fails or in regions of extreme magnetic variation/dip (near poles). The gyro works as a standard Directional Gyro (DG) and must be checked/reset manually against a standby compass periodically.
