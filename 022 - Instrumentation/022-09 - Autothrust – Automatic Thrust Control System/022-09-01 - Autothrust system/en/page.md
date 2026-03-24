---
layout: default
title: "022-09-01 - Autothrust system"
parent: "022-09 - Autothrust – Automatic Thrust Control System"
grand_parent: "022 - Instrumentation"
nav_order: 1
---

# Autothrust System (A/THR)

## Purpose and Principles

The **Autothrust** (Airbus) or **Autothrottle** (Boeing) system automates the control of engine power. It sets the required trust to satisfy the current flight phase demands, reducing pilot workload and optimizing fuel efficiency.

- **Primary Control Parameters**:
    - **N1**: Rotational speed of the low-pressure compressor (Fan). Used on most high-bypass turbofans (e.g., CFM56).
    - **EPR (Engine Pressure Ratio)**: Ratio of turbine discharge pressure to compressor inlet pressure. Used on some engines (e.g., Rolls-Royce, some PW).

## Modes of Operation

The system operates in two fundamental distinct modes, depending on how the Autopilot (AP) is controlling the aircraft's pitch.

### 1. SPEED Mode (Speed Control)
- **Function**: The A/THR varies engine thrust to maintain a selected **Target Speed** (IAS or Mach).
- **Usage**: Used when the aircraft's trajectory (vertical path) is fixed by the AP.
    - **Level Flight**: AP holds Altitude (`ALT HOLD`) $\rightarrow$ A/THR holds Speed (`SPEED`).
    - **Vertical Speed Climb/Descent**: AP holds a specific Rate of Climb/Descent (`V/S`) $\rightarrow$ A/THR adjusts thrust to maintain Speed (`SPEED`).
    - **Approach**: AP follows Glide Slope (`G/S`) $\rightarrow$ A/THR holds Speed (`SPEED`).

### 2. THRUST Mode (Thrust Control)
- **Function**: The A/THR sets a **Fixed Thrust Rating** (e.g., Maximum Climb, Idle, Take-off). The AP controls the speed by adjusting the aircraft's pitch ("Speed on Pitch").
- **Usage**: Used during large altitude changes to maximize efficiency.
    - **Climb (Level Change / Open Climb)**: A/THR sets **Climb Thrust** (`N1`, `THR CLB`) $\rightarrow$ AP pitches up/down to maintain Speed.
    - **Descent (Level Change / Open Descent)**: A/THR sets **Idle Thrust** (`IDLE`, `THR IDLE`) $\rightarrow$ AP pitches down to maintain Speed.
    - **Take-off / Go-Around**: A/THR sets **TO/GA** power $\rightarrow$ Pilot/AP flies a pitch attitude to maintain $V_2$ or target speed.

## System Design Variants

### Moving Thrust Levers (e.g., Boeing)
- The thrust levers are driven by a servo motor and **physically move** to match the thrust commanded by the computer.
- **Advantage**: Tactile feedback; the pilot "feels" what the engines are doing.

### Static Thrust Levers (e.g., Airbus FBW)
- The thrust levers remain in a fixed **detent** (e.g., CL - Climb) during automatic operation.
- The computer varies the engine power virtually ("Fly-By-Wire" logic).
- **Indication**: The pilot must look at the **FMA (Flight Mode Annunciator)** and engine instruments to know the thrust output. To disconnect, levers must be matched to the current thrust indication (or moved to Idle).

## Protections

- **Alpha Floor (Airbus)**: If the Angle of Attack increases dangerously, the A/THR automatically commands **TO/GA** thrust, even if the system was off.
- **Limit Protection**: The system prevents the engines from exceeding the redline ($N_1$ or EGT limits) and ensures safe operation limits are respected.
- **Speed Protection**: Prevents selecting speeds below $V_{LS}$ (Lowest Selectable Speed) or above $V_{max}$.
