---
title: "General, Definitions, Basic Applications"
description: "Basic electrical concepts, units, Ohm's law, circuit protection, static electricity, and logic gates."
---

### Basic Units and Definitions

The fundamental units in electrical systems are:

*   **Current ($I$)**: The flow of electric charge (electrons) through a conductor. Measured in **Amperes (A)**.
*   **Voltage ($V$)**: The potential difference between two points. Measured in **Volts (V)**.
*   **Resistance ($R$)**: The opposition to the flow of current. Measured in **Ohms ($\Omega$)**.
*   **Power ($P$)**: The rate of doing work or transferring energy. Measured in **Watts (W)**.
    *   $P = V \times I$
    *   Also defined as Energy Transferred / Time (Joules per second).
*   **Frequency ($f$)**: The number of cycles per unit time for alternating current. Measured in **Hertz (Hz)**.
*   **Work**: Measured in **Joules (J)**.

### Ohm's Law

Ohm's law states that the current passing through a conductor between two points is proportional to the voltage across the two points.

$$V = I \times R$$

*   Voltage is proportional to Current.
*   If voltage increases (with constant resistance), current increases.

### Circuit Protection

Devices are installed to protect circuits from **overcurrent**, which is a situation where current exceeds the safety rating of the conductor, potentially attempting to generate excessive heat and causing an **electrical fire**.

#### Fuses
A fuse is a thermal protection device containing a strip that melts ("blows") when current exceeds a specific value.
*   **Function**: Protects cables and components.
*   **Replacement**: Must be replaced with a fuse of the *correct amperage, voltage, and type* (fast or slow blow).
*   **Incorrect Rating**: Installing a higher-rated fuse allows overcurrent to persist, creating a severe fire risk. In a healthy system, an incorrect fuse causes no immediate issue, but offers no protection during a fault.
*   **Current Limiters**: High-amperage fuses (often for TRU outputs) designed to withstand short-term overloads but break on sustained faults.

#### Circuit Breakers (CB)
A resettable device that combines the function of a fuse and a switch.
*   **Thermal CB**: Relies on a bi-metallic strip heating up and bending to trip the massive latch. Suitable for small, prolonged overcurrents.
*   **Magnetic CB**: Uses an electromagnet to trip immediately upon high current surge. Best for fast response.
*   **Resetting Rules**:
    *   If a CB trips, it may be reset **once** after a cooling period (if necessary).
    *   If it trips a second time, it should **not** be reset again (indicates a permanent fault).
    *   Repeated resetting damages the system and increases fire risk.
    *   In flight, a tripped CB is usually only reset if the system is essential for safety.

### Static Electricity and Bonding

Friction between the aircraft skin and air particles generates static electricity.

*   **Bonding**: The connection of all aircraft metal components with flexible wire strips.
    *   **Purpose**: Ensures **equal electrical potential** across the aircraft (zero voltage difference).
    *   **Prevents**: Sparks between components (fire hazard) and electrical noise.
    *   It also provides a return path for current (earth return).
*   **Static Wicks**: Conductive rods on trailing edges.
    *   **Purpose**: Dissipate static charge back into the atmosphere.
    *   **Failure**: Missing wicks can cause radio interference (static noise on comms) and loss of communication.

### AC Power Standards

Modern large aircraft typically use Alternating Current (AC) generators.
*   **Standard Values**: **115/200 Volts**, **3-phase**, **400 Hz**.
*   **Frequency**: 400 cycles per second. High frequency allows for lighter generators and transformers (efficient for aerospace).

### Logic Gates

Logic circuits allow complex decision-making in systems.

*   **AND Gate**: Output is 1 only if **ALL** inputs are 1.
*   **OR Gate**: Output is 1 if **ANY** input is 1.
*   **NOT Gate**: Inverts the input (1 becomes 0).
*   **NAND Gate**: AND followed by NOT.
*   **NOR Gate**: OR followed by NOT.

### Electromagnetic Interference (EMI)

Current flowing through a wire creates a magnetic field that can induce unwanted signals in nearby wires (crosstalk/interference).

*   **Shielding/Screening**: A conductive braid (mesh) wrapped around the wire.
*   **Function**: Blocks EMI from entering or leaving the wire.
*   **Result**: Prevents interference with other systems (e.g., radios).

### Capacitors and Inductors (General)

*   **Capacitor**: Stores energy in an electric field. In AC circuits, current leads voltage. High frequency reduces capacitive reactance (current increases).
*   **Lorentz Force**: Force exerted on a charged particle moving perpendicular to a magnetic field.
