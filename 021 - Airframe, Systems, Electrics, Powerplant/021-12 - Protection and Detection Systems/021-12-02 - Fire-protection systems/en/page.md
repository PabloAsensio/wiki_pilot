---
title: "Aircraft Fire Protection Systems: Detection, Extinguishing, and Procedures"
description: "Understand aircraft fire protection systems, including detection loop technologies, extinguishing logic, and standard operational procedures."
---
# Aircraft Fire Protection Systems: Detection, Extinguishing, and Procedures

## Fire Detection Systems
Engine and APU compartments use **thermal/heat detection** (not smoke detection due to high airflow).

### 1. Gaseous Loop (Pneumatic)
*   **Principle**: Gas Laws (Pressure $\propto$ Temperature).
*   **Component**: Stainless steel tube filled with inert gas and a gas-absorbing material.
*   **Operation**:
    *   Fire conditions heat the tube.
    *   Gas expands, **pressure increases**.
    *   At a predetermined pressure, a **pressure switch** closes to trigger the alarm.
*   **Fault Monitoring**:
    *   If the tube leaks, pressure drops.
    *   A **low-pressure switch** detects this and triggers a **Fault** alert (inhibits false fire warnings).

### 2. Continuous Loop (Electrical)
*   **Principle**: Thermistor material properties (Resistance/Capacitance change with heat).
*   **Component**: A central wire embedded in thermistor material inside a conductive tube.
*   **Operation**:
    *   As temperature rises, the **resistance decreases** (Negative Temperature Coefficient) or capacitance increases.
    *   Current flows between the center wire and the tube (ground).
    *   When current exceeds a threshold, the alarm triggers.
*   **Reset**: The system resets automatically when the temperature drops (fire extinguished).
*   **Redundancy (Dual Loop)**:
    *   Modern aircraft use two parallel loops (A and B).
    *   **AND Logic**: Both loops must detect fire to trigger the warning (minimizes false alarms).
    *   **Fault**: If one loop is faulty (e.g., short to ground), the system may revert to "Single Loop" operation or indicate a fault. A condition of **low resistance AND low capacitance** typically indicates a fault/short.

## Fire Extinguishing
*   **Mechanism**: High-rate discharge bottles (spheres) containing extinguishing agent (Halon replacement).
*   **Activation**: **Electrically fired cartridges (Squibs)** break a frangible disc to release the agent.
*   **Regulations (CS 25.1195)**:
    *   Engines must have **two separate discharges** available.
    *   Configuration: Typically 2 bottles shared between engines, or 2 dedicated bottles per engine.
        *   *Cross-feed*: Bottle 1 can be discharged into Engine 1 OR Engine 2.

## Operational Procedure
1.  **Detection**:
    *   **Aural**: Continuous bell/chime or voice ("Engine Fire").
    *   **Visual**: Master Warning (Red) + Fire Handle Light (Red).
2.  **Isolation (Pulling the Fire Handle)**:
    *   **Arms** the squibs (explosive cartridges).
    *   **Closes Fuel** Shut-off Valve (LP Valve).
    *   **Closes Hydraulic** Shut-off Valve.
    *   **Closes Bleed Air** Valve.
    *   **Trips Generator** (Field Relay/Breaker).
    *   **Disables Thrust Reverser**.
3.  **Extinguishing (Rotating the Handle)**:
    *   Pilot rotates handle Left (Bottle 1) or Right (Bottle 2).
    *   Agent is discharged into the compartment.

## Fire Test
*   Simulates a fire condition (e.g., by heating a test element or electrically simulating low resistance).
*   **Success**: All lights illuminate + Aural warning.
*   **Failure**: No indication or specific "Loop Fault" light (if checks continuity).
