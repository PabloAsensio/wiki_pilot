---
title: "Carburettor & Injection Systems"
description: "Principles of carburetors and injection systems, induction icing, mixture control, and priming."
---

# Carburettor & Injection Systems

## Carburetor Principles

*   **Function**: Mixes fuel and air in the correct proportions before delivering it to the cylinders.
*   **Operation**: Based on **Bernoulli's Principle**.
    *   Air accelerates through a **Venturi**, causing a **drop in static pressure and temperature**.
    *   This pressure drop draws fuel from the float chamber into the airstream.
*   **Diffuser**: Maintains a **constant mixture ratio** across a wide range of engine speeds (prevents the mixture from becoming too rich at high airflow).
    *   Uses a "pressure balance duct" to bleed air into the fuel nozzle, reducing suction at high power.
*   **Accelerator Pump**: Prevents a temporary **lean cut** during rapid throttle advance.
    *   Injects a shot of fuel into the venturi when the throttle is opened quickly, matching the rapid increase in airflow.

### Induction Icing

*   **Susceptibility**: Affects **both** carburetors and fuel injection systems (though carburetors are more prone due to fuel vaporization cooling).
*   **Carburetor Icing Factors**:
    *   **Fuel Evaporation**: Absorbs latent heat, cooling the air.
    *   **Venturi/Throttle Effect**: Pressure drop causes temperature drop.
    *   **Result**: Ice forms on the venturi walls and throttle valve, restricting airflow (drop in RPM/Manifold Pressure).
*   **Carburetor Heat**:
    *   **Action**: Supplies hot, unfiltered air to the intake.
    *   **Effect**: Melts ice.
    *   **Side Effects**:
        *   Hot air is **less dense** $\rightarrow$ **Power drops** (~15%) and **Mixture becomes Richer**.
        *   Combustion becomes less efficient (risk of detonation at high power).
    *   **Indication**: Initial drop in RPM (due to hot air), followed by a rise in RPM (as ice melts and airflow is restored).
    *   **Usage**: Use fully ON when icing is suspected. Avoid extended use at high power (takeoff/climb) to prevent detonation and power loss.

### Priming & Starting

*   **Purpose**: To inject extra fuel for starting (enrich the mixture), especially in cold conditions.
*   **Primer Pump**: Forces atomized fuel **directly into the cylinder intake ports** (bypassing the carburetor).
*   **Throttle Pumping**: Uses the accelerator pump to squirt fuel into the carburetor. Less effective and carries a higher risk of **induction fire**.
*   **Induction Fire on Start**:
    *   **Procedure**: **Keep Cranking**. This sucks the flames back into the engine.
    *   If engine starts: Run at moderate RPM to extinguish.
    *   If start fails: Shut down, mixture idle cut-off, fuel selector off, master off, evacuate, extinguish.

### Fuel Injection

*   **Operation**: Fuel is injected continuously into the inlet port (just before the valve).
*   **Advantages**: No venturi restriction (more power), uniform mixture distribution, immune to *refrigeration* icing (though impact icing is still possible).
*   **Components**: Engine-driven pump, fuel/air control unit, manifold valve, injector nozzles.
