---
title: "Empty Mass and CG Data"
description: "Extracting reference BEM and CG data from documentation for everyday calculations."
keywords: ["BEM extraction", "CG reference", "index", "load sheet"]
---

## Starting Point for Calculations

For daily flight preparation, the pilot does not re-weigh the aircraft. Instead, they extract the **Basic Empty Mass (BEM)** and **Basic Empty CG** directly from the aircraft's current weighing report or the **Mass and Balance Manual**.

### Documentation Data

The entry in the manual will typically show:
*   **Serial Number/Registration**: Confirming the data is for the specific aircraft.
*   **Date of Weighing**: When the data was established.
*   **Basic Empty Mass**: Value in kg or lbs.
*   **Centre of Gravity**: Arm (distance from datum) or **Index**.

### Index Units (IU)

To simplify calculations and avoid large moment numbers, manuals often convert moments into **Index Units**.
*   **Index Formula**:
    $$
    \text{Index} = \frac{\text{Mass} \times (\text{Arm} - \text{Ref})}{\text{Constant C}} + \text{Constant K}
    $$
    *   This scales the numbers down to a more manageable size (e.g., 0-100 scale).

When using an Index system, the pilot:
1.  Starts with the **Basic Index** (corresponding to the BEM).
2.  Adds the **Index change** for each load item (crew, passengers, fuel) based on charts or tables.
3.  Calculates the **Final Total Index**.
4.  Checks if the Final Index is within the allowable Envelope.
