---
title: "Ground-Proximity Warning Systems (GPWS/EGPWS): Modes, Terrain Logic, and Escape"
description: "Learn GPWS mode logic, EGPWS forward-looking terrain functions, warning priorities, and immediate pilot escape actions for pull-up alerts."
keywords:
    - "gpws"
    - "egpws"
    - "terrain warning"
    - "minimum speed"
---

# Ground-Proximity Warning Systems (GPWS/EGPWS): Modes, Terrain Logic, and Escape

The **GPWS** (Ground Proximity Warning System) is designed to generate visual and aural warnings when the aircraft's proximity to the terrain poses a safety threat, specifically to prevent **CFIT** (Controlled Flight Into Terrain).

## System Inputs and Operation
The system requires inputs from the **Air Data Computer (ADC)** (barometric altitude, vertical speed, CAS), **Radio Altimeter** (height AGL), **ILS** (glide slope), and aircraft configuration (flaps, landing gear).
*   **Operating Range**: Automatically active between **50 ft** and **2500 ft** Radio Altitude.
*   **Requirement**: Mandatory for turbine-powered aircraft > 5,700 kg or > 9 passengers.

## Modes of Operation
The basic GPWS (non-enhanced) has 7 modes based on distinct conditions:

| Mode | Condition | Aural Alert | Aural Warning |
|---|---|---|---|
| **1** | Excessive Descent Rate | "SINK RATE" | "PULL UP" |
| **2** | Excessive Terrain Closure Rate | "TERRAIN" | "PULL UP" |
| **3** | Altitude Loss after Take-off/Go-around | "DON'T SINK" | - |
| **4** | Unsafe Terrain Clearance (Config) | "TOO LOW GEAR/FLAPS/TERRAIN" | - |
| **5** | Below Glide Slope Deviation | "GLIDE SLOPE" (Soft) | "GLIDE SLOPE" (Loud) |
| **6** | Altitude Callouts / Excessive Bank | "MINIMUMS", "BANK ANGLE" | - |
| **7** | Windshear (Reactive) | "WINDSHEAR" (x3) | Siren + Voice |

*   **Mode 5 Inhibition**: Can be cancelled by the pilot (e.g., for visual approaches or localizer-only approaches) using a specific button ("G/S INHIBIT" or similar).
*   **Mode 7 Priority**: Windshear alerts take priority over all other GPWS modes.

## Enhanced GPWS (EGPWS) / TAWS
Basic GPWS relies on the Radio Altimeter, which looks straight down. It effectively "looks down, not ahead".
*   **Limitation**: A sheer cliff or rapid terrain rise might not be detected in time by Mode 2.
*   **Solution**: **EGPWS** (or TAWS - Terrain Awareness and Warning System) adds a **Forward-Looking Terrain Avoidance (FLTA)** function.
*   **Mechanism**: Uses a worldwide **Terrain Database** matched with the aircraft's position (GPS/FMS) to predict conflicts.

### Terrain Display (EGPWS)
Using the navigation display to show terrain threats:
*   **Red**: Terrain well above aircraft altitude (Warning).
*   **Amber/Yellow**: Terrain near aircraft altitude (Caution).
*   **Green**: Terrain safely below aircraft.
*   **Magenta**: No terrain data available.

## Pilot Response (PULL UP Warning)
If a "PULL UP" or "TERRAIN AHEAD, PULL UP" warning occurs:
1.  **Autopilot**: Disconnect.
2.  **Pitch**: Apply **Maximum Backstick** (Full Aft) / Pitch up to the limit (stick shaker/PLI).
    *   *Note*: In Fly-By-Wire aircraft, full backstick commands max available alpha without stalling (alpha protection).
3.  **Thrust**: Apply Maximum Power (**TOGA**).
4.  **Speedbrakes**: Retract.
5.  **Bank**: Wings Level.
6.  **Configuration**: Do **not** change gear or flap configuration until clear of the obstacle (drag considerations).
