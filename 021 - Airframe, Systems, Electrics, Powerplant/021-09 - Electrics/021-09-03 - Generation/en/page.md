---
title: "Generation"
description: "AC and DC generation, CSD, IDG, TRUs, Inverters, and power distribution."
---

### AC Generation

Large aircraft typically require High Voltage AC power (115/200V, 400Hz, 3-phase).
*   **Brushless AC Generators**: Use a set of **permanent magnets** for initial excitation.
    *   **Exciter Generator**: Mounted on the same shaft.
    *   **Permanent Magnet Generator (PMG)**: Specifically used for initial excitation current and powering the generator control.
*   **Voltage Regulation**: The **Voltage Regulator** controls the output voltage (keeps it constant at varying loads/speeds) by adjusting the **excitation current** to the field coil.
    *   Wired in series with the field coil.
    *   If electrical load increases -> Voltage drops -> Regulator increases excitation current -> Voltage returns to normal.

### Constant Speed Drive (CSD) & IDG

AC generators must spin at a constant speed to maintain a constant **frequency (400Hz)**, despite the engine's varying RPM.
*   **CSD (Constant Speed Drive)**: A hydromechanical unit that converts variable engine speed to constant generator speed.
    *   Monitors/Adjusts: **Output Frequency**.
    *   Has its own independent oil system for lubrication and cooling.
    *   **Faults**: High oil temperature, low oil pressure.
*   **IDG (Integrated Drive Generator)**: Combines the **CSD and the Generator** into one single unit.
    *   **Disconnect**: In case of a fault (e.g., high oil temp, low pressure), the pilot **operates the IDG disconnect switch**.
    *   **Consequence**: The drive shaft is mechanically disconnected. The generator is **unusable for the rest of the flight**.
    *   **Reset**: Can **ONLY** be reconnected on the ground by maintenance with the engine stopped.

### Frequency Wild

*   **Frequency Wild Generators**: Generators where the frequency varies with engine speed (no CSD/IDG).
*   **Application**: Only suitable for **resistive loads** (e.g., anti-icing mats/heaters) because inductance/reactance are frequency-dependent.

### DC Generation & Conversion

*   **TRU (Transformer Rectifier Unit)**:
    *   Combines a Transformer and a Rectifier.
    *   **Function**: Converts **AC** (115V) to **DC** (28V).
    *   Used to power DC buses and charge batteries from the main AC supply.
    *   Often includes a smoothing/filter circuit to minimize output fluctuation.
*   **Inverter**:
    *   **Function**: Converts **DC** (28V) to **AC** (115V, 400Hz).
    *   **Static Inverter**: Solid-state device (no moving parts) used for essential AC loads if main AC fails.
*   **Starter-Generator**:
    *   Combines starter motor and generator functions (common on turbine engines).
    *   Acts as a **starter motor** to spool the engine up to self-sustaining speed.
    *   Switches to become a **DC generator** once the engine is running.

### Protection & Control

*   **GCU (Generator Control Unit)**:
    *   Checks for faults (over-voltage, over-excitation).
    *   Controls the Generator Circuit Breaker (GCB) and Exciter Control Relay.
*   **Split Bus System**: If a generator fails, GCBs/BTBs (Bus Tie Breakers) reconfigure to ensure essential loads are powered.
