---
title: "Fuel Quantity Indication: Float and Capacitance Gauging Systems"
description: "Understand fuel-quantity indication in aircraft, from float systems to capacitance probes and densitometry for accurate mass-based fuel management."
keywords:
  - "fuel on board"
  - "air density"
  - "calibrated altitude"
  - "altimeter readings"
---
# Fuel Quantity Indication: Float and Capacitance Gauging Systems

Accurate fuel quantity indication is vital for flight safety and efficiency. Systems aim to determine the **mass** of fuel on board, as this determines the energy available, unlike volume which changes with temperature.

## Verification
After refueling, pilots must verify the fuel load:
*   Ensure **Fuel On Board (FOB)** matches the flight plan.
*   Check that any imbalance is within limits.
*   **Compare planned vs. actual uplift** (in kg or lbs) to identify errors or leaks. Discrepancies outside Aircraft Flight Manual (AFM) limits require maintenance.

## Fuel Gauging Systems

### Float-Type System
This is the most basic system, typically found in smaller aircraft.
*   **Principle:** A mechanical float sits on the fuel surface. As the level changes, it moves a mechanical arm connected to a variable resistor (DC circuit), changing the cockpit indication.
*   **Limitation:** It measures **volume**, not mass. Fuel expands when warm and contracts when cold. At high temperatures, the volume increases, causing the gauge to read higher even though the **mass** remains the same. It is also susceptible to errors during maneuvers and turbulence.

### Capacitance-Type System
Modern aircraft use capacitance systems to measure fuel quantity with greater accuracy.
*   **Principle:** Measures the **capacitance** between two plates (tubes) in the tank. The capacitance depends on the dielectric material between them.
*   **Dielectric:** The system distinguishes between **fuel** (permittivity ~2.0) and **air** (permittivity ~1.0). As fuel replaces air between the plates, capacitance increases (e.g., Full = 210pF vs Empty = 100pF).
*   **Volume to Mass:** A **compensator unit** (or densitometer) located at the bottom of the tank is always immersed in fuel. It measures the fuel's specific properties to account for density changes due to temperature. This allows the system to electronically convert the measured volume into a precise **mass** indication.

## Units and Conversion
*   **Mass:** Kilograms (kg), Pounds (lb). ($1 \text{ kg} \approx 2.2 \text{ lb}$)
*   **Volume:** Liters (L), US Gallons (US Gal).
*   **Conversion:** $1 \text{ US Gal} \approx 3.785 \text{ Liters}$.
*   **Example:** To check uplift, if the gauge requires verifying 272 Liters against a US Gal dispenser: $272 / 3.785 \approx 72 \text{ US Gal}$.
