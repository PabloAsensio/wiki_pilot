---
title: "Distribution"
description: "Bus bars, split vs. parallel bus systems, DC/AC conversion, and failure scenarios."
---

### Bus Bars

*   **Definition**: Thick copper bars that act as a central distribution point for electrical power.
*   **Function**: Simplifies wiring (lighter than individual wires to each consumer). Collects power from sources and distributes it to consumers.
*   **Consumers**: Connected in **parallel** (isolating one doesn't affect others).
*   **Protection**: Protected by circuit breakers.
    *   **Short Circuit on Bus Bar**: If a bus bar faults (short circuit), its protection isolates it. **All consumers on that bus lose power for the rest of the flight.**

### Distribution Systems

#### Split Bus System
*   **Normal Operation**: Each generator feeds its **own dedicated** AC bus bar. Source are **isolated** (never paralleled).
*   **Typical Setup**: Modern twin-engine aircraft.
*   **Generator Failure**:
    1.  Failed generator GCB (Generator Circuit Breaker) opens.
    2.  BTB (Bus Tie Breaker) closes.
    3.  **Result**: The remaining working generator feeds **BOTH** bus bars. (Or APU takes over the failed side).
    4.  Load shedding may occur due to single source capacity.

#### Parallel Bus System
*   **Normal Operation**: All generators feed into a common distribution network (synchronizing bus).
*   **Requirement**: Generators must be **paralleled** (Synchronized).
*   **Conditions for Paralleling**:
    *   Equal **Voltage**.
    *   Equal **Frequency**.
    *   Equal **Phase Sequence**.
*   **Generator Failure**: Failed generator GCB opens. The remaining generators continue to feed all buses (load is shared among remaining sources).

### Types of Buses

*   **AC BUS**: Main distribution for AC loads.
*   **DC BUS**: Main distribution for DC loads (fed by TRUs).
*   **ESSENTIAL BUS**: Powers critical systems. Can be fed by emergency sources (e.g., batteries/inverter) if main power fails.
*   **HOT BATTERY BUS (Direct Bus)**:
    *   **Directly** connected to the battery.
    *   **Always** powered (even when aircraft is unpowered).
    *   Powers vital items (e.g., fire extinguishers, clocks).

### Power Conversion

*   **TRU (Transformer Rectifier Unit)**:
    *   **AC $\rightarrow$ DC**.
    *   Lowers voltage (115V $\rightarrow$ 28V).
*   **Inverter (Static Inverter)**:
    *   **DC $\rightarrow$ AC**.
    *   Used to power *Essential AC* loads from batteries in an emergency (Total AC failure).
*   **Battery Charging**: Batteries (DC) are charged by the DC Bus (fed by TRUs).

### Contactors & Reconfiguration (Logic)

*   **External Power**: Can feed main buses on the ground via External Power Contactors.
*   **APU**: Can feed main buses (replaces main generators).
*   **Cross-Tie (X-TIE)**: Allows one side's DC bus to feed the other side's DC bus (if a TRU fails).
*   **Emergency Configuration**:
    *   Loss of all generators $\rightarrow$ Batteries feed **DC ESS BUS** $\rightarrow$ Static Inverter feeds **AC ESS BUS**.

### Protection Systems

Electrical systems monitor and protect against:
*   Over-voltage
*   Under-voltage
*   Over-current
*   Over-speed (IDG/CSD)
*   Under-frequency
