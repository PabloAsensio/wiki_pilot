---
title: "Piston Engine Ignition Circuits: Magnetos and Impulse Coupling"
description: "Study magneto ignition circuit operation, impulse coupling during start, and grounding logic for safe piston engine handling."
---
# Piston Engine Ignition Circuits: Magnetos and Impulse Coupling

A **magneto** is a self-contained, engine-driven electrical generator designed to supply high voltage to the spark plugs. It does not require an external battery to operate, making it a reliable, independent ignition source for aircraft engines.

## Construction and Operation

The magneto consists of a rotating permanent magnet and two windings:
*   **Primary Winding**: A few turns of **thick** wire (Low Tension).
*   **Secondary Winding**: Many turns of **thin** wire (High Tension).

### Working Principle
1.  As the magnet rotates, it induces current in the primary winding.
2.  A **contact breaker** (cam-operated) interrupts the primary circuit.
3.  This interruption causes a rapid **collapse of the magnetic field**.
4.  The collapsing field induces a very **high voltage** in the secondary winding.
5.  A **distributor** directs this high voltage pulse to the correct spark plug via high-tension leads.

## Impulse Coupling

At low engine speeds (during start), a magneto rotates too slowly to produce a strong spark. An **Impulse Coupling** is used to solve this:
*   **Mechanism**: A spring-loaded clutch between the engine drive and magneto shaft.
*   **Function 1 (Retard)**: It delays the spark to ensure ignition happens after Top Dead Center (preventing kickback/backfire).
*   **Function 2 (Accelerate)**: It winds up the spring and releases it rapidly, spinning the magneto fast enough to generate a strong spark for starting.
*   After the engine starts, centrifugal force disengages the coupling.

## Ignition Switch and Grounding

Reference is often made to the "Mag Check" or "Dead Cut" check.
*   **Switch OFF**: The ignition switch works by **grounding (earthing) the primary circuit**. This stops the high voltage generation.
*   **Switch ON**: The ground connection is broken, allowing the points to control the circuit.
*   **Broken Ground Wire**: If the ground wire breaks, the magneto is **permanently ON** ("Hot"). The engine will not stop when the switch is turned off.
    *   **Danger**: The propeller is live! Moving it could start the engine.
    *   **Action**: If the engine doesn't stop with the key, stop it by cutting the fuel mixture (Idle Cut-Off).
