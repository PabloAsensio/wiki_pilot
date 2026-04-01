---
title: "Stall Warning Systems (SWS): Detection Margins, Inputs, and Alerts"
description: "Study SWS operation from CS-25 warning margins to AoA-driven logic, tactile/aural/visual cues, and typical sensor-failure implications."
keywords:
  - "stall warning"
  - "angle of attack"
  - "minimum speed"
  - "flight level"
---

# Stall Warning Systems (SWS): Detection Margins, Inputs, and Alerts

## Overview

The **Stall Warning System (SWS)** is a critical safety system designed to alert the flight crew of an impending stall condition. Its primary function is to provide a clear and distinctive warning with sufficient margin to allow the pilot to take preventative action before the stall actually occurs.

## Regulations (CS-25)

For large transport aeroplanes, regulations (CS-25.207) dictate specific performance criteria for the SWS:

*   **Margin:** The warning must begin at a speed exceeding the stall speed by not less than **5 knots** or **5% CAS** (whichever is greater).
*   **Conditions:** The warning must be effective in both straight and turning flight, and with landing gear and flaps in any normal position.
*   **Duration:** The warning must continue until the angle of attack is reduced to approximately that at which the warning was initiated.

## SWS Operation

### Light Aircraft
*   **Sensor:** Typically a **Moving Vane** (Flapper Switch) located on the wing leading edge.
*   **Mechanism:** As the Angle of Attack (AoA) increases, the stagnation point moves downwards, causing airflow to lift the vane. This closes a micro-switch.
*   **Alert:** Aural buzzer or flashing light in the cockpit.
*   **Icing:** The vane is often electrically heated to prevent ice accumulation.

### Large Transport Aircraft
Modern aircraft use a more sophisticated system driven by digital computers.

#### Inputs
To calculate the correct stall threshold, the SWS computers require several inputs:
1.  **Angle of Attack (Alpha):** The primary input, measured by Alpha Probes on the fuselage.
2.  **Configuration:** **Flap and Slat position** (high lift devices change the stalling AoA).
3.  **Airspeed (CAS):** To ensure the 5% / 5 kt margin is met.
4.  **Air/Ground Logic:** To inhibit the system while on the ground.
5.  **Thrust:** (On some systems).

#### Warning Types
*   **Tactile (Haptic):** **Stick Shaker**. An eccentric weight motor vibrates the control column to simulate pre-stall aerodynamic buffet.
*   **Aural:** Distinctive sounds (e.g., "Cricket" sound, continuous horn) or synthetic voice (**"STALL, STALL"**).
*   **Visual:** **Red** Master Warning light or specific PFD indications.

## Failure Scenarios
*   **Frozen Alpha Probe:** If the AoA sensor becomes frozen (e.g., due to icing) at a specific value, the computer may fail to detect an increasing angle of attack, resulting in **no stall warning** being triggered.

## Distinction from Protection
It is important to distinguish between **Warning** and **Protection**:
*   **Stall Warning (Stick Shaker):** Alerts the pilot *before* the stall.
*   **Stall Protection (Stick Pusher):** Physically pushes the control column forward to *prevent* the stall if the pilot ignores the warning (discussed in the next section).
