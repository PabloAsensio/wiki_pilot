---
title: "Mass Limits Calculations"
description: "Determining the maximum permissible traffic load based on mass limits."
keywords: ["mass limits", "traffic load calculation", "MTOM", "MLM", "MZFM", "regulated take-off mass"]
---

## Determining Maximum Traffic Load

To find the maximum traffic load allowed for a flight, we must calculate the load permitted by each of the three main limits:
1.  **Maximum Take-Off Mass (MTOM)** Limit.
2.  **Maximum Landing Mass (MLM)** Limit.
3.  **Maximum Zero Fuel Mass (MZFM)** Limit.

The *lowest* of the three resulting traffic loads is the limiting factor.

### 1. MTOM Limit
$$
\text{Max Traffic Load (MTOM)} = \text{MTOM} - \text{DOM} - \text{Take-off Fuel}
$$

### 2. MLM Limit
Since the aircraft burns trip fuel, it can take off heavier than the landing limit.
$$
\text{Max Take-off Mass allowed by MLM} = \text{MLM} + \text{Trip Fuel}
$$
$$
\text{Max Traffic Load (MLM)} = (\text{MLM} + \text{Trip Fuel}) - \text{DOM} - \text{Take-off Fuel}
$$
*Alternatively:* Max Traffic Load = MLM - DOM - Reserve Fuel (Landing Fuel).

### 3. MZFM Limit
$$
\text{Max Traffic Load (MZFM)} = \text{MZFM} - \text{DOM}
$$
*Note: Fuel is not part of ZFM.*

## Example Calculation

Given:
*   DOM: 35,000 kg
*   MTOM: 65,000 kg
*   MLM: 55,000 kg
*   MZFM: 52,000 kg
*   Trip Fuel: 8,000 kg
*   Take-off Fuel: 15,000 kg

Calculate Max Traffic Load:

1.  **Based on MTOM**:
    $$65,000 - 35,000 - 15,000 = 15,000 \text{ kg}$$
2.  **Based on MLM**:
    *   Max mass at take-off allowed by landing limit: $55,000 + 8,000 = 63,000 \text{ kg}$
    *   Traffic Load: $63,000 - 35,000 - 15,000 = 13,000 \text{ kg}$
3.  **Based on MZFM**:
    $$52,000 - 35,000 = 17,000 \text{ kg}$$

**Result**: The lowest value is **13,000 kg** (limited by Landing Mass).
