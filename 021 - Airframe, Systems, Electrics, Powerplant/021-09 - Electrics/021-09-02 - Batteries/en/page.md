---
title: "Aircraft Electrical Batteries and Thermal Runaway Protection"
description: "Aircraft battery types, properties, hazards (thermal runaway), and charging methods."
---

# Aircraft Electrical Batteries and Thermal Runaway Protection

## Battery Basics

Batteries convert chemical energy into electrical energy.

*   **Capacity**: Measured in **Ampere-hours (Ah)**. Represents the amount of charge a fully charged battery can supply.
    *   Example: A 5 Ah battery can supply 5A for 1 hour, or 2.5A for 2 hours.
    *   Capacity depends on the physical size of the battery plates (not voltage).
    *   **Series Connection**: Voltage doubles, capacity remains the same.
    *   **Parallel Connection**: Capacity doubles, voltage remains the same.

### Condition Check

*   **On-Load Check**: A test applied to give a better indication of battery condition using the aircraft's voltmeter.
    *   Requires applying a load (e.g., lights, pitot heat) for a specific time (10-20 seconds).
    *   Voltage must remain steady and not fall below a specific value.
    *   Involves comparing on-load and off-load voltages.

### Battery Types

#### Lead-Acid Batteries
*   **Composition**: Anode (Lead Peroxide), Cathode (Spongy Lead), Electrolyte (Water and Sulphuric Acid).
*   **Voltage**: 2V per cell on load, **2.2V off load**.
*   **Characteristics**:
    *   Good energy storage but heavy.
    *   Lower energy density.
    *   Discharge rate decreases with lower temperature (internal resistance increases).
*   **Hazards**: Overcharging boils electrolyte, damaging plates.

#### Nickel-Cadmium (NiCd) Batteries
*   **Composition**: Plates of Nickel Oxide and Cadmium, Electrolyte (Potassium Hydroxide).
*   **Voltage**: ~1.2V per cell (remains relatively constant during discharge).
*   **Characteristics**:
    *   Low internal resistance.
    *   Wide operating temperature range.
    *   **Thermal Runaway Risk**: High.
    *   **Venting**: Required.

#### Lithium-Ion (Li-ion) / Lithium-Polymer (LiPo)
*   **Characteristics**: High energy density.
*   **Hazards**: Extremely susceptible to **Thermal Runaway**.
*   **Wear**: Performance degrades over time; internal resistance increases, causing worse performance under load.

### Thermal Runaway

A rapid, unstoppable chain reaction where an increase in temperature changes internal resistance, causing more heat generation, which further increases temperature (positive feedback loop).

*   **Causes**:
    *   **Internal Short Circuit**: Dendrite formation, compressive shock/impact (physical damage), deformation.
    *   **External Short Circuit**.
    *   **Overcharging**: Beyond maximum voltage.
    *   **Overheating**: During charging or due to high currents.
*   **Process**: Electrolyte decomposition (exothermic reaction) -> Rapid temp rise -> Release of stored energy -> Fire/Explosion.
*   **Risk**: Li-ion fires burn at thousands of degrees and are very difficult to extinguish. Fire can spread to neighboring cells.
*   **Protection/Containment**:
    *   **Metal Boxes**: Li-ion batteries are often housed in vented boxes made of galvanized/stainless steel with fire insulation to contain thermal runaway.
    *   **Venting**: Allows dissipation of heat and release of flammable gases.

### Operations and Charging

*   **Charging Method**: Most aircraft use **Constant Voltage Charging**.
    *   Generator voltage exceeds battery voltage (e.g., 28V generator for a 24V battery).
*   **Ammeter**: Connected in series. A positive reading (e.g., +24A) indicates the battery is **charging**.
*   **Loss of Generated Power**: If all generators fail, the remaining electrical power from the battery is **time-limited** (typically 30 minutes for essential systems).
*   **Dangerous Goods**: Spare lithium batteries are restricted/forbidden in cargo due to fire risk.
