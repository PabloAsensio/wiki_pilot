---
title: "Aircraft Tachometers: Mechanical, Electrical, and Electronic RPM Sensing"
description: "Learn tachometer architectures in aviation, including eddy-current mechanical indicators, tacho-generator systems, and pulse-based electronic RPM measurement."
keywords:
    - "rpm"
    - "engine speed"
    - "flight level"
    - "minimum speed"
---
# Aircraft Tachometers: Mechanical, Electrical, and Electronic RPM Sensing

Tachometers measure the rotational speed of the engine, expressed in Revolutions Per Minute (RPM).

## Types of Tachometers

### 1. Mechanical Tachometer
Used on older piston aircraft.
*   **Principle:** A flexible driveshaft connects the engine gearbox to the instrument. Inside, a rotating permanent magnet induces **eddy currents** in an aluminum drag cup, creating a magnetic field that rotates the cup and moves the pointer against a spring.
*   **Features:** Self-powered (no electricity needed). Limited by driveshaft length (max ~2m).

### 2. Electrical Tachometer
Used on some jet aircraft (e.g., for High Pressure compressor speed).
*   **Principle:** A three-phase AC **tacho-generator** on the engine gearbox sends a signal to a synchronous motor in the indicator. This motor spins a magnet/drag cup assembly similar to the mechanical type.
*   **Features:** Self-powered signal. AC frequency varies with RPM.

### 3. Electronic Tachometer
Used on modern gas turbines (multi-spool) and EFIS systems.
*   **Principle:** Uses a **speed probe** (coil + magnet) or induction probe.
    *   **Pulse Counting:** The probe is placed near the engine fan blades or a notched "phonic wheel". As metal passes the probe, it disturbs the **magnetic field**, generating electrical pulses.
    *   **Calculation:** The pulse rate is directly proportional to the spool speed.
*   **Features:** Requires an external power supply. precise.

*Note: While all utilize magnetism, electronic systems use it to generate pulses for counting, whereas mechanical/electrical types use it to create torque (drag) to move a pointer.*
