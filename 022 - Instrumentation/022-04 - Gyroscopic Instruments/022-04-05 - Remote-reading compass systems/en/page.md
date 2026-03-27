---
title: "Remote-Reading Compass Systems: Slaved Correction and Free Mode"
description: "Understand remote-reading compass architecture, including flux-valve slaving loops, FEAT correction chain, and DG-style operation in free mode."
keywords:
    - "magnetic headings"
    - "magnetic course"
    - "points on the compass"
    - "compass turns"
---
# Remote-Reading Compass Systems: Slaved Correction and Free Mode

A **Remote Indicating Compass** (often called a Gyro-Magnetic Compass) combines a Directional Gyro with a Flux Valve to provide a stable, magnetically-referenced heading without manual resetting.

## System Components (FEAT)
The loop works as follows:
1.  **F**lux Valve: Senses the Earth's magnetic field error.
2.  **E**rror Detector: Compares Flux Valve heading vs. Gyro heading.
3.  **A**mplifier: Amplifies the error signal.
4.  **T**orque Motor: Precesses the gyro to align it with magnetic north.

## Modes of Operation
1.  **Slaved Mode:** The normal operating mode. The Flux Valve continuously corrects the Gyro (slowly, to avoid chasing temporary magnetic errors). The gyro is "tied" to Magnetic North.
2.  **Free Mode (DG):** The slaving is disconnected. The instrument acts like a standard **Directional Gyro**.
    *   Used in **Polar Regions** (where magnetic field is unreliable/weak).
    *   Used if the Flux Valve fails.
    *   Requires manual synchronization.

## Advantages
*   Eliminates the need for manual resetting (in Slaved mode).
*   Reduces the effect of deviation (Flux valve is in the wingtip/tail).
*   Provides heading data to other systems (Autopilot, RMI, Radar).
