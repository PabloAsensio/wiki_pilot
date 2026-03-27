---
title: "Fly-by-Wire Flight Control Laws: Normal, Alternate, and Direct Modes"
description: "FBW control-law behavior, degradation paths after failures, envelope-protection loss, and trim/autopilot implications across operating modes."
---

# Fly-by-Wire Flight Control Laws: Normal, Alternate, and Direct Modes

Fly-by-wire (FBW) systems replace conventional manual flight controls with an electronic interface. Pilot inputs are converted into electronic signals, processed by flight control computers, and then sent to actuators that move the control surfaces. These systems operate under different "laws" or "modes" depending on the system's health and available data.

## Control Laws and Degradation

FBW systems are designed with redundancy. When failures occur (e.g., loss of sensors or computers), the system degrades to a lower level of automation and protection.

### Normal Law (Airbus) / Normal Mode (Boeing)
This is the standard operating mode with all systems functioning.
- **Functionality:** Provides full three-axis control.
- **Protections:** Full flight envelope protection is active (e.g., stall, overspeed, bank angle, pitch attitude).
- **Features:** Autopilot is available. Systems like maneuver load alleviation and gust suppression are active.
- **Operation:** Computers (e.g., PFCs in Boeing) process pilot inputs with complex control laws to optimize stability and handling.

### Alternate Law (Airbus) / Secondary Mode (Boeing)
Occurs when there are failures (e.g., loss of multiple sensors, computer faults).
- **Functionality:** The system reverts to simplified computations.
- **Protections:**
    - **Airbus (ALT1/ALT2):** Some protections are lost or degraded. For example, **Pitch Attitude Protection is lost**, and Low Energy Protection is replaced by **Low Speed Stability** (audio "STALL" warning introduces instead of automatic recovery). Bank Angle protection may be lost in ALT2.
    - **Boeing:** **Envelope protection**, gust suppression, and **autopilot** are lost.
- **Handling:** The aircraft is still controllable, but handling qualities may change (e.g., elevator and rudder may be more sensitive).

### Direct Law (Airbus) / Direct Mode (Boeing)
The lowest level of computer flight control, usually resulting from multiple critical failures (e.g., loss of all flight control computers or inertial reference units).
- **Functionality:** Pilot control inputs are sent **directly** to the control surface actuators without computer refinement.
- **Protections:** **ALL protections are lost.** The pilot has full unrestricted authority but no safety nets.
- **Autopilot:** **Always lost.**
- **Trim:**
    - **Airbus:** Automatic trim is inoperative; **manual trim** (using the trim wheel) is required.
    - **Boeing:** Manual rudder trim cancel may be inoperative.
- **Characteristics:** Control surface movement is directly proportional to stick/column movement.
