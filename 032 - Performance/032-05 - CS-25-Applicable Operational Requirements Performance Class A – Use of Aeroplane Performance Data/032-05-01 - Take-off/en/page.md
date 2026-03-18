---
title: "Class A Take-Off Data"
description: "Using performance charts and tables for Class A take-off calculations."
keywords: ["Class A", "take-off charts", "RTOW", "Regulated Take-Off Weight", "V-speeds", "line-up allowance"]
---

## Regulated Take-Off Weight (RTOW)

The maximum weight for take-off is the lowest of:
1.  **Field Limit**: Defined by runway length (TODR, ASDR) and slope.
2.  **Obstacle Limit**: Defined by the net flight path clearing obstacles.
3.  **Tyre Speed Limit**: Maximum ground speed for tyres.
4.  **Brake Energy Limit**: Maximum energy brakes can absorb during RTO.
5.  **Structural Limit**: Maximum Take-Off Mass (MTOM) defined by the manufacturer.
6.  **Climb Limit**: Ability to meet the 2.4% WAT (Weight, Altitude, Temperature) climb gradient in the 2nd segment.

## Line-Up Allowance

Performance calculations assume the take-off starts at the beginning of the runway. However, aircraft need space to line up.
*   **Adjustment**: A "Line-Up Allowance" (LUA) distance must be subtracted from the TORA/ASDA to account for the runway length consumed during line-up.
*   **Values**: vary by aircraft size and line-up angle (90° vs 180° turn). E.g., 90° entry might use less runway than a 180° turn on the runway.

## Simplified Take-Off Analysis
Charts usually provide corrections for:
*   **Wind**: Headwind increases RTOW, Tailwind decreases it significantly.
*   **Pressure Altitude**: Higher altitude $\rightarrow$ lower engine thrust $\rightarrow$ lower RTOW.
*   **Temperature**: Higher temperature $\rightarrow$ lower thrust $\rightarrow$ lower RTOW.
*   **Slope**: Downslope assists acceleration (higher RTOW), upslope hinders.
*   **Runway Surface**: Wet/Contaminated reduces screen height to 15 ft (for wet) and degrades stopping performance.

## V-Speed Determination
Once the actual Take-Of Weight (TOW) is known (and confirmed $\le$ RTOW), the V-speeds ($V_1, V_R, V_2$) are extracted from the tables/FMS based on:
1.  Actual Weight.
2.  Flap Setting.
3.  Pressure Altitude & Temperature.
4.  Runway Condition (Wet runway often requires a lower $V_1$ to improve stopping capability).
