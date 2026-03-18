---
title: "Take-off Configuration Warning (TOCW)"
---

## Overview

The **Take-off Configuration Warning (TOCW)** system is a critical safety mechanism designed to prevent an aircraft from attempting a takeoff in an unsafe configuration.

## Regulations (CS 25.703)

Regulations mandate that large transport aircraft must be equipped with a system that provides an **aural warning** automatically during the **initial portion of the takeoff roll**.

*   **Timing:** The alert must trigger when **throttles are advanced** (applied takeoff power) while on the ground.
*   **Indication:** The minimum requirement is an **Aural** alert (e.g., Siren, Horn, or Voice "CONFIG FLAPS"). Many aircraft also provide visual alerts (Red Master Warning + Message).

## Trigger Conditions

The system activates if any of the following parameters are not in the approved takeoff position:

1.  **Flaps / Slats:** Not within the approved takeoff range (or not set).
2.  **Longitudinal Trim (Stabilizer):** Not in the green band (Takeoff Range).
3.  **Spoilers / Speed Brakes:** Deployed or not in the safe takeoff position.
4.  **Parking Brake:** Set or not released.
5.  **Flight Controls:** Control locks engaged (if applicable).
6.  **Doors:** Essential external doors not closed and locked (on some types).

## Operational Use

*   **Test Function:** Modern aircraft (like the Airbus A320) include a `T.O CONFIG` pushbutton. Pressing this simulates the application of takeoff power to check if the current configuration is valid. If it is, a specific message (e.g., **"TO CONFIG NORMAL"**) is displayed.
*   **Inhibition:** The warning is typically inhibited after a certain speed ($V_1$ or $V_R$) to effectively prioritize alerts and avoid distraction during the critical rotation phase.
