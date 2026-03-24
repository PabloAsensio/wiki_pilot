---
title: "Fundamentals of Turbine Engine Operation"
description: "Brayton cycle fundamentals, core components, turbine engine types, and start sequence basics."
---

# Fundamentals of Turbine Engine Operation

A gas turbine engine is a heat engine that uses air as a working fluid to produce thrust. It operates on the **Brayton Cycle**.

## Operation Principle (Brayton Cycle)
Like a piston engine (Otto Cycle), a gas turbine has four phases: Induction, Compression, Combustion, and Exhaust.
*   **Continuous Process**: Unlike the intermittent piston engine, the gas turbine process is **continuous**.
*   **Constant Pressure**: Combustion occurs at a **constant pressure** (volume and temperature increase), whereas in a piston engine, it occurs at constant volume.

## Main Components
Air flows axially from front to back:
1.  **Inlet**: Designed to reduce air velocity (dynamic pressure) and **increase static pressure and temperature** (divergent duct) before the compressor.
2.  **Compressor**: Increases the pressure of the air. Can be axial or centrifugal.
3.  **Combustion Chamber**: Mixes fuel with compressed air and burns it at **constant pressure**.
4.  **Turbine**: Extracts energy from the hot expanding gases to drive the compressor (and fan/propeller).
5.  **Exhaust/Nozzle**: Accelerates exhaust gases to produce thrust (convergent duct increases velocity, decreases pressure).

## Engine Types

### Turbojet / Turbofan
*   **Single Spool**: One shaft connecting compressor and turbine.
*   **Multi-Spool (e.g., Twin Spool)**:
    *   **N1 (Low Pressure)**: Fan + LP Compressor driven by LP Turbine.
    *   **N2 (High Pressure)**: HP Compressor driven by HP Turbine.
    *    shafts rotate mechanically independently.
*   **Bypass Ratio**: Ratio of air bypassing the core to air going through the core (HP compressor).
    *   **Formula**: `Bypass Ratio = (Total Inlet Flow - HP Core Flow) / HP Core Flow`
    *   High bypass engines are more efficient (lower SFC) and quieter.

### Turboprop / Turboshaft (Free Turbine)
*   **Gas Generator**: Core engine (Compressor + Combustion + Compressor-Turbine) creates high-energy gas.
*   **Free Turbine**: A separate turbine (mechanically independent from the core) extracts energy to drive a propeller or rotor via a reduction gearbox.
*   **Control**:
    *   **Power Lever**: Controls fuel flow (Gas Generator/N1 speed).
    *   **Propeller Lever / CSU**: Adjusts blade angle to maintain constant propeller/free-turbine (N2/Np) RPM.

## Performance Concepts

### Thrust
*   **Static Thrust**: When the aircraft is stationary.
    *   Produces **Force**, but **Zero Mechanical Power** (Power = Force x Velocity; if Velocity is 0, Power is 0).
    *   Equal to the product of mass flow and exhaust velocity (plus pressure term).

### Specific Fuel Consumption (SFC)
*   **Turbojet/Turbofan**: Fuel flow per unit of **Thrust**. Unit: `kg/hour/Newton` (or lb/hr/lbf).
*   **Turboprop/Piston**: Fuel flow per unit of **Power**. Unit: `kg/hour/Watt` (or lb/hr/shp).
*   Lower SFC indicates better efficiency.

## Start Sequence
1.  **Start Selected**: Starter rotates HP compressor (N2).
2.  **Ignition ON**: Igniters activated.
3.  **Fuel ON**: Fuel sprayed into combustion chamber.
4.  **Light-up**: Mixture ignites.
5.  **Self-sustaining**: Engine accelerates to idle; starter disengages.
