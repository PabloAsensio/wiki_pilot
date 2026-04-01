---
title: "Performance Class A (CS-25): Cruise Theory"
description: "Optimization of cruise flight: speed strategies and fuel planning."
keywords: ["Class A", "cruise", "LRC", "MRC", "cost index", "buffet margin"]
---

# Performance Class A (CS-25): Cruise Theory


## Cruise Strategies

### Maximum Range Cruise (MRC)
*   Speed: Corresponds to $1.32 V_{MD}$ (for jets).
*   Objective: Maximum distance per kg of fuel.
*   Disadvantage: Speed can be slow, sensitive to speed instability.

### Long Range Cruise (LRC)
*   Speed: Typically 4% faster than MRC (99% of max specific range).
*   Objective: Provides 99% of the range of MRC but with significantly better speed stability and higher block speed.
*   Historical standard before Cost Index.

### Cost Index (CI)
*   Modern Flight Management Systems (FMS) optimize speed based on the ratio of **Time Cost** to **Fuel Cost**.
    $$
    CI = \frac{\text{Cost of Time (\$ per hour)}}{\text{Cost of Fuel (\$ per kg)}}
    $$
*   **CI = 0**: Minimizing fuel cost (Max Range). Speed close to MRC.
*   **CI = Max**: Minimizing time (Max Speed). Flying at $V_{MO}/M_{MO}$.

## Buffet Margins

At high altitudes, the speed range is limited:
*   **Low Speed Buffet**: Caused by stall onset (high Angle of Attack). Occurs at $V_{S1g} \times \text{load factor}$.
*   **High Speed Buffet**: Caused by shock waves (Mach effects).
*   **Load Factor**: Turning increases load factor (g), which increases stall speed, bringing the buffets closer.

**Operational Requirement**: A minimum margin of **1.3g** load factor protection to buffet onset is usually required for cruise altitude selection. This ensures the aircraft can bank (turn) without stalling or overspeeding.
