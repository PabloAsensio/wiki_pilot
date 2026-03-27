---
title: "Direct Reading Magnetic Compass (DRC): Turning and Acceleration Errors"
description: "Study direct-reading magnetic compass behavior in flight, including UNOS/ANDS error patterns, pendulous suspension effects, and serviceability checks."
keywords:
    - "compass turns"
    - "points on the compass"
    - "magnetic headings"
    - "magnetic course"
---
# Direct Reading Magnetic Compass (DRC): Turning and Acceleration Errors

The **Direct Reading Compass (DRC)**, often called the "whiskey compass", is a standalone instrument that aligns itself with the Earth's magnetic field.

## Principle and Limitations
The magnet assembly tries to align with the magnetic field lines. However, due to the Earth's **Dip ($Z$ component)**, the assembly tends to tilt downwards towards the pole. To counter this, the center of gravity (CG) of the magnet assembly is deliberately offset (lowered) relative to the pivot point to keep it horizontal.
This **pendulous suspension** creates dynamic errors during flight. The compass is **only accurate in straight, level, unaccelerated flight**.

## Turning Errors (UNOS)
Occur when turning from **North** or **South** headings (worst on N/S, zero on E/W).
*   **Turning through North:** The compass lags (Under-turns) or moves initially in the opposite direction.
*   **Turning through South:** The compass leads (Over-turns).
*   *Mnemonic (Northern Hemisphere):* **UNOS**
    *   **U**ndershoot **N**orth
    *   **O**vershoot **S**outh

## Acceleration Errors (ANDS)
Occur on **East** or **West** headings (worst on E/W, zero on N/S).
*   **Acceleration:** Center of Gravity inertia causes a rotation indicating a turn to the **North**.
*   **Deceleration:** Inertia causes a rotation indicating a turn to the **South**.
*   *Mnemonic (Northern Hemisphere):* **ANDS**
    *   **A**ccelerate **N**orth
    *   **D**ecelerate **S**outh

## Serviceability Checks
Before flight, check:
1.  **Fluid:** No bubbles or discoloration (dampens oscillation).
2.  **Card/Casing:** Intact and readable.
3.  **Indication:** Must match a known heading (Runway or Taxiway) within limits (typically $\pm 10^\circ$).
4.  **Deviation Card:** Must be present and legible.
