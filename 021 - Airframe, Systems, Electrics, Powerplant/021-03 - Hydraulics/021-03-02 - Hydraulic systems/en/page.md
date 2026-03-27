---
title: "Aircraft Hydraulic Systems: Fluids, Pumps, Valves, and Monitoring"
description: "Hydraulic fluid types, pump architectures, accumulator and reservoir functions, valve logic, and pressure monitoring in modern aircraft systems."
---

# Aircraft Hydraulic Systems: Fluids, Pumps, Valves, and Monitoring

Hydraulic systems in modern aircraft are complex networks designed to transmit high forces reliably. This section details the fluids, components, and operational principles that ensure these systems function correctly under all flight conditions.

## Hydraulic Fluids

Hydraulic fluids are the medium for transmitting pressure and energy. Their correct selection and handling are vital.

- **Ideal Properties:**
    - **Low Compressibility:** Allows for instantaneous operation.
    - **High Flash Point / Low Flammability:** Essential for fire safety.
    - **Viscosity:** Must flow easily at low temperatures while maintaining adequate viscosity at high temperatures.
    - **Protection:** Must provide **lubrication** and **anti-corrosion** properties to protect pumps and actuators.
- **Types:**
    - **Mineral-based (e.g., DTD 585):** Typically red. Uses synthetic rubber seals.
    - **Synthetic (e.g., Skydrol):** Typically purple or green. Fire-resistant.
    - **Warning:** Different fluid types **must never be mixed**, as this leads to seal breakdown and leakage. Fluids are also **corrosive to paintwork** and are skin/eye irritants.

## Hydraulic Pumps

Pumps generate the flow of fluid required to pressurize the system.

- **Constant Pressure (Demand) Pump:** Uses a variable swash plate (axial piston) to modulate output volume based on demand, maintaining constant system pressure. This is the standard for modern aircraft.
- **Constant Delivery (Fixed Volume) Pump:** Delivers a fixed volume per turn. It requires an **Automatic Cut-Out Valve (ACOV)** to regulate pressure and return excess fluid to the reservoir (idling) when services are not in use.
- **Hand Pump:** Often used on the ground for specific tasks (e.g., opening cargo doors) when electrical or engine power is unavailable.
- **Ram Air Turbine (RAT):** An emergency pump acting as a last resort. Deployed in flight, it powers vital systems (flight controls) if main power sources fail.

## Accumulators

Accumulators are storage devices containing hydraulic fluid under pressure, separated from a compressed gas (nitrogen) by a piston or diaphragm.

- **Functions:**
    - **Store Energy:** Provides a limited supply of pressurized fluid for emergency operation (e.g., braking) if the pump fails.
    - **Dampen Fluctuations:** Smooths out transient pressure spikes in the system.
    - **Thermal Expansion:** Absorbs fluid expansion in closed systems.
- **Operation:** The gas is pre-charged. As system pressure builds, fluid enters the accumulator and compresses the gas until pressures equalize.

## Reservoirs and Filters

- **Reservoir:** Stores the system's fluid. It is usually **pressurized** (often by pneumatic bleed air) to prevent **cavitation** (formation of air bubbles) at high altitude and ensure a positive feed to the pumps.
    - **Stack Pipe:** A standpipe design ensures that if a leak occurs in the main supply line, a reserve of fluid remains at the bottom of the reservoir specifically for **emergency systems**.
- **Filters:** Remove contaminants. They often feature pop-out indicators to signal an **impending bypass**, warning that the filter is becoming clogged.

## Valves and Control Logic

- **Pressure Relief Valve (PRV):** A safety valve that limits the maximum system pressure by venting excess fluid back to the tank.
- **Non-Return Valve (NRV):** Ensures fluid flows in only one direction (check valve).
- **Selector Valve:** Directs fluid to one side of an actuator or the other. Trapping fluid between a closed selector and a piston can caus a **Hydraulic Lock**.
- **Shuttle Valve:** Automatically selects the higher pressure source, allowing an alternate system to take over (e.g., for brakes) if the primary pressure fails.
- **Fuses:** Safety devices that shut off flow if a sudden high-volume leak (pressure drop) is detected, preventing total system fluid loss.

## System Monitoring

- **Typical Pressure:** Most commercial airliners operate at **3000 psi**.
- **Indications:** A loss of hydraulic pressure typically triggers an **Amber Caution** (Master Caution light + Low Press annunciation), requiring crew awareness.
- **Overheat:** Can be caused by blocked cooling flow, requiring the system to be de-energized.
