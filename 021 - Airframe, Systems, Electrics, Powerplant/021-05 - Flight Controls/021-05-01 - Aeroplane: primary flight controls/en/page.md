---
title: "Aircraft Primary Flight Controls: Reversible vs Irreversible Systems"
description: "Primary control architectures, artificial feel logic, trim behavior differences, gust-lock considerations, and redundancy principles."
---

# Aircraft Primary Flight Controls: Reversible vs Irreversible Systems

Primary flight controls (elevator, ailerons, and rudder) are responsible for controlling the aircraft's rotation about its three axes. Depending on the aircraft's size and speed, these controls can be manually operated, power-assisted, or fully powered.

## Control System Types

- **Reversible Controls:**
    - **Characteristics:** There is a direct mechanical link effectively transmitting force both ways. A force applied to the cockpit controls moves the control surface, and **aerodynamic loads on the surface move the cockpit controls**.
    - **Feedback:** The pilot naturally feels the aerodynamic load (feedback).
    - **Application:** Found in manual and partially powered systems.
    - **Ground Behavior:** Wind moving the control surface **will cause the cockpit controls to move**.

- **Irreversible Controls:**
    - **Characteristics:** The system is **fully powered** (hydraulic or fly-by-wire). Inputs from the cockpit move valves or sensors that actuate the surface, but **forces on the surface are not transmitted back to the cockpit**.
    - **Feedback:** Contains **no natural feel**.
    - **Ground Behavior:** Wind moving the control surface (e.g., rudder blown to full deflection) **will NOT cause movement of the cockpit controls** (rudder pedals).

## Artificial Feel

Since irreversible systems provide no natural feedback, an **Artificial Feel Unit** is required.
- **Purpose:** To provide the pilot with tactile resistance and centering forces.
- **Function:** The force applied to the cockpit controls should be proportional to the **control deflection** and the **aircraft's speed** (dynamic pressure).

## Trim System Behavior

In fully powered (irreversible) systems with artificial feel, trim operation differs by axis:
- **Elevator Trim:** Trimming typically changes the reference for the feel unit but **does not move the control column** to a new neutral position. The zero-force position remains centered.
- **Aileron and Rudder Trim:** Trimming usually **changes the zero-force position** of the controls. The control wheel or rudder pedals will physically move in the direction of the trim.

## Gust Locks

Gust locks (internal or external) are used to protect control surfaces and linkages from damage caused by wind when the aircraft is parked.
- **Requirement:** Design precautions (such as mechanical interlocks with the throttles) must be in place to **prevent the aircraft from taking off with gust locks engaged**.
- **Relevance:** Particularly important for **reversible** control systems where wind can easily slam surfaces against their stops.

## Redundancy

To ensure safety, flight control systems employ redundancy:
- **Multiple Actuators:** Using more than one actuator (often powered by different hydraulic systems) per control surface.
- **Multiple Surfaces:** Using multiple surfaces for the same function (e.g., using spoilers to assist ailerons for roll control).
