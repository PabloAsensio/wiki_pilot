---
layout: default
title: "Trim Systems in Flight Control: Auto-Trim, Mach Trim, and Runaway Actions"
description: "Learn trim-system operation in manual and automatic flight, including THS auto-trim logic, Mach trim compensation, and stabilizer-runaway procedures."
keywords:
    - "minimum speed"
    - "flight level"
    - "magnetic headings"
    - "compass turns"
parent: "022-08 - Trims – Yaw Damper – Flight Envelope Protection"
grand_parent: "022 - Instrumentation"
nav_order: 1
---

# Trim Systems in Flight Control: Auto-Trim, Mach Trim, and Runaway Actions

## Purpose and Function

The primary purpose of a trim system is to **relieve the pilot of control forces** required to maintain a desired flight attitude or path.

- **Manual Flight**: The pilot uses trim (mechanical or electrical) to zero out force on the control column.
- **Automatic Flight**: The Autopilot (AP) uses the **Auto-Trim** system to manage long-term pitch control.

## Auto-Trim

In modern jet transport aircraft (conventional), the Elevator controls short-term pitch changes, while the **Trimmable Horizontal Stabilizer (THS)** controls long-term trim.

- **Operation**: The Auto-trim system moves the entire Horizontal Stabilizer to relieve aerodynamic load from the elevator.
- **Goal**: To keep the elevator streamlined (neutral position) with the stabilizer. This ensures full elevator authority is available for maneuvering.
- **Activation**:
    - **Conventional Controls**: Auto-trim is typically active **only when the Autopilot is engaged**.
    - **Fly-By-Wire (FBW)**: Auto-trim is **always active** (in Normal Law), automatically compensating for thrust, speed, and configuration changes (e.g., flaps/gear).
- **Disengagement**: When the AP is disconnected ("Hand-Over"), the aircraft is left in a properly trimmed state, preventing sudden pitch transients.

### Mach Trim

High-speed aircraft experience **Mach Tuck**: a nose-down pitching moment caused by the rearward movement of the Center of Pressure (CP) and shockwaves as Mach number increases.

- **System**: The **Mach Trim** system is an independent automatic function.
- **Action**: It automatically trims the stabilizer **nose-up** to counteract the nose-down tendency.
- **Independence**: It operates regardless of whether the Autopilot is engaged or not.

## Abnormal Operation: Trim Runaway

**Stabilizer Runaway** is a condition where the trim runs continuously uncommanded.

- **Consequences**: Can lead to extreme control forces that the elevator may not be able to overcome (due to the large surface area of the stabilizer vs. elevator).
- **Pilot Actions**:
    1.  Hold control column firmly (counteract motion).
    2.  Disconnect Autopilot and Autothrust.
    3.  Use "Stab Trim Cutout" switches to disable the electric trim motor.
    4.  Trim manually (if mechanical wheel is available).
