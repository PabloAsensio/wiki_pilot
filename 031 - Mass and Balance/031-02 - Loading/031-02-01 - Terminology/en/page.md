---
title: "Mass and Balance Terminology: BEM, DOM, ZFM, TOM, and Fuel Definitions"
description: "Master core mass-and-balance terminology used in loading operations, including BEM/DOM/ZFM/TOM relationships and operational fuel definitions."
keywords:
    - "mass and balance terminology"
    - "bem dom zfm"
    - "traffic load"
    - "block fuel"
---

# Mass and Balance Terminology: BEM, DOM, ZFM, TOM, and Fuel Definitions

## Standard Mass Definitions

*   **Basic Empty Mass (BEM)**: The mass of the aeroplane including:
    *   Airframe, engines, and all fixed equipment.
    *   Unusable fuel and oil.
    *   Hydraulic fluid, fire extinguishers, emergency oxygen, etc.
    *   Does **not** include crew or usable fuel.

*   **Dry Operating Mass (DOM)**: The total mass of the aeroplane ready for a specific type of operation, excluding usable fuel and traffic load.
    *   DOM = BEM + Crew + Crew Baggage + Catering + Potable Water + Lavatory Chemicals.

*   **Operating Mass (OM)**: The DOM plus fuel but without traffic load.
    *   OM = DOM + Fuel Load.

*   **Zero Fuel Mass (ZFM)**: The total mass of the aeroplane including everything *except* usable fuel.
    *   ZFM = DOM + Traffic Load.

## Load Definitions

*   **Useful Load**: The total mass of the items that can be carried in addition to the Basic Empty Mass.
    *   Useful Load = TOM - BEM.
    *   Useful Load = Traffic Load + Fuel Load.

*   **Traffic Load (Payload)**: The total mass of passengers, baggage, and cargo, including any non-revenue load.
    *   Traffic Load = TOM - DOM - Fuel Load.

*   **Fuel Load**: The total mass of usable fuel on board.
    *   **Block Fuel (Ramp Fuel)**: The total fuel on board before starting engines.
    *   **Taxi Fuel**: Fuel consumed during ground operations before take-off.
    *   **Take-off Fuel**: Fuel on board at the start of the take-off run (Block Fuel - Taxi Fuel).
    *   **Trip Fuel**: Fuel required for the flight from take-off to landing.
    *   **Landing Fuel**: Fuel remaining on board at landing (Take-off Fuel - Trip Fuel).

## Relationship Summary

$$
\text{DOM} = \text{BEM} + \text{Crew} + \text{Pantry}
$$
$$
\text{ZFM} = \text{DOM} + \text{Traffic Load}
$$
$$
\text{TOM} = \text{ZFM} + \text{Take-off Fuel}
$$
$$
\text{LM} = \text{TOM} - \text{Trip Fuel}
$$
