---
title: "Level Flight, Range and Endurance"
description: "Optimization of flight for maximum distance (Range) or maximum time (Endurance)."
keywords: ["range", "endurance", "SAR", "specific range", "fuel flow", "maximum range speed"]
---

## Specific Range (SR) vs. Specific Endurance (SE)

Performance planning focuses on efficiency: how much distance or time can be gained per unit of fuel.

![Maximum Endurance and Range](https://upload.wikimedia.org/wikipedia/commons/3/34/Maximum_Endurance_and_Range.jpg)

### Specific Range (SR)
*   **Definition**: Distance flown per unit of fuel.
    $$
    SR = \frac{\text{True Airspeed (TAS)}}{\text{Fuel Flow (FF)}}
    $$
*   **Goal**: Max Range (flying as far as possible).
*   **Aerodynamic Condition**:
    *   **Jet**: Fly at $1.32 V_{MD}$ (approx). Optimized where the ratio $TAS/Drag$ is maximum.
    *   **Prop**: Fly at $V_{MD}$. Optimized where $Drag$ is minimum.

### Specific Endurance (SE)
*   **Definition**: Flight time per unit of fuel.
    $$
    SE = \frac{1}{\text{Fuel Flow}}
    $$
*   **Goal**: Max Endurance (staying airborne as long as possible, e.g., Holding).
*   **Aerodynamic Condition**:
    *   **Jet**: Fly at $V_{MD}$. Minimum Thrust required = Minimum Fuel Flow.
    *   **Prop**: Fly at $V_{mp}$ (Minimum Power Speed). Minimum Power = Minimum Fuel Flow.

## Effect of Variables

### Wind
*   **Range**: Tailwind increases Ground Speed, increasing Range. Headwind decreases Range.
    *   *Pilot Action*: In a headwind, increase speed slightly (Cost Index increases) to penetrate the wind. In a tailwind, decrease speed to stay in the wind longer.
*   **Endurance**: Wind has **no effect** on Endurance (time aloft depends only on fuel flow, not ground distance covered).

### Mass (Weight)
*   **Range**: Higher mass requires higher Lift ($L=W$), creating more Induced Drag. More thrust/fuel is needed. Range decreases.
    *   *Speed*: As weight decreases (fuel burn), the optimum range speed decreases.
*   **Endurance**: Higher mass requires more power/thrust to maintain altitude. Endurance decreases.

### Altitude
*   **Jet Range**: generally increases with altitude due to lower temperature (better engine efficiency) and higher TAS for the same IAS.
*   **Prop Range**: less affected by altitude, limited by engine performance drop-off.
