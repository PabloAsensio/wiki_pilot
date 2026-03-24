---
layout: default
title: "022-08-03 - Flight-envelope protection (FEP)"
parent: "022-08 - Trims – Yaw Damper – Flight Envelope Protection"
grand_parent: "022 - Instrumentation"
nav_order: 3
---

# Flight-Envelope Protection (FEP)

## Concept and Purpose

**Flight Envelope Protection (FEP)** systems serve to monitoring and restricting the aircraft's flight parameters to ensure they remain within safe structural and aerodynamic limits.

- **Objective**: To allow the pilot to use the full capabilities of the aircraft without fear of entering an unsafe state (stall, overstress, overspeed).
- **Implementation**:
    - **Conventional Aircraft**: Often limited to warnings (Stick Shaker) or simple mechanical interventions (Stick Pusher). Corrective action relies heavily on the pilot.
    - **Fly-By-Wire (FBW) Aircraft**: The Flight Control Computers (FCC) process pilot inputs and actively prevent the control surfaces from moving in a way that would exceed limits. This is known as **"Hard Protection"**.

## Key Protections

1.  **Stall Protection (High Angle of Attack)**
    - **Warning**: Stick Shaker (vibrates column to simulate pre-stall buffet).
    - **Prevention (Conventional)**: Stick Pusher (mechanically pushes nose down).
    - **Prevention (FBW)**:
        - **Alpha Prot**: System actively commands nose down to prevent AoA increasing.
        - **Alpha Floor**: Autothrust automatically commands TO/GA (Take-off/Go-around) power if AoA is critical.
        - **Alpha Max**: The aircraft cannot exceed maximum AoA even with full back stick.

2.  **Overspeed Protection (High Speed)**
    - Prevents exceedance of $V_{MO}$ (Maximum Operating Velocity) or $M_{MO}$ (Maximum Operating Mach).
    - **Action**:
        - Inhibits nose-down trim.
        - Commands a pitch-up maneuver to trade speed for altitude.
        - Reduces thrust (if A/THR engaged).
    - **Override**: In emergency descent scenarios, pilots may need to override "soft" protections, but "hard" protections typically remain to prevent structural damage.

3.  **Attitude Protection (Pitch and Bank)**
    - **Pitch Limits**: Prevents excessive nose-up (stall risk) or nose-down (dive risk) attitudes (e.g., +30° / -15°).
    - **Bank Limits**: Prevents excessive banking (spiral dive risk), typically limited to 67° in FBW normal law. If the stick is released, the aircraft returns to a standard bank angle (e.g., 33°).

4.  **Load Factor Protection (G-Load)**
    - Prevents overstressing the airframe.
    - Limits commanded G-force (e.g., Clean configuration: +2.5g to -1.0g).

## Soft vs. Hard Protection

- **Soft Protection**: Returns the aircraft to the safe envelope or warns the pilot, but **can be overridden** by applying more force to the controls.
- **Hard Protection**: **Cannot be overridden** by the pilot in Normal Law. The computer strictly limits control surface deflection to stay within the envelope.

> **Note**: In the event of system failures (sensor loss, computer failure), FBW systems may revert to **Alternate Law** or **Direct Law**, where some or all protections are lost, leaving only basic stability or direct control.
