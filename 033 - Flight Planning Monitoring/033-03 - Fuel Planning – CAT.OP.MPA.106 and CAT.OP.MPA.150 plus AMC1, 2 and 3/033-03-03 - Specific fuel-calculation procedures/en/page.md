---
title: "Fuel Calculation Procedures"
description: "How to calculate specific fuel segments using performance tables."
keywords: ["fuel flow", "integrated range", "nam", "ngm", "specific gravity"]
---

## Specific Gravity (SG) / Density

Fuel is sold by volume (liters/gallons) but calculated by mass (kg/lbs) for performance.
*   **Formula**: $Mass = Volume \times Density$
*   **Jet A1 Density**: Typically around **0.8 kg/L** (varies with temperature).
*   Hot fuel is less dense (more volume for same weight).
*   Cold fuel is more dense (less volume for same weight).

## Fuel Flow Calculation

### Integrated Range
For long flights, fuel consumption reduces aircraft weight, which in turn reduces fuel consumption.
*   **Calculation**: Done step-by-step (typically hourly) or using accumulated tables (Flight Planning Tables).
*   **Nautical Air Miles (NAM)**: Distance flown through the air mass.
    *   $NAM = TAS \times Time$
    *   $Fuel = NAM \times (Fuel Flow / TAS)$
*   **Nautical Ground Miles (NGM)**: Distance over ground (corrected for wind).
    *   $NGM = GS \times Time$

### Holding Fuel
Calculated at "Holding Speed" usually at **1,500 ft** above destination elevation (for Final Reserve) or at cruise altitude (for Contingency holding).
*   Holding speed is usually lower than cruise speed ($V_{MD}$ usually for max endurance) to minimize flow.

## Computer Flight Plans (CFP)
Modern systems automate these calculations, providing a log with:
*   **Zone Fuel**: Fuel for each leg.
*   **Min Fuel**: Regulatory minimum.
*   **Take-off Fuel**: Actual fuel on board at T/O.
*   **Burn-off**: Expected consumption.
