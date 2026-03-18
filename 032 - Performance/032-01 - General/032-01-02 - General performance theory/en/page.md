---
title: "General Performance Theory"
description: "Foundational concepts of aerodynamic forces in flight: Thrust, Drag, Lift, and Weight."
keywords: ["performance theory", "forces of flight", "thrust", "drag", "power", "equilibrium"]
---

## The Four Forces

In steady level flight, the four forces acting on the aircraft are in equilibrium:
1.  **Lift (L)** balances **Weight (W)**.
    *   $L = W = m \times g$
2.  **Thrust (T)** balances **Drag (D)**.
    *   $T = D$

## Drag Characteristics

Drag is the resistance the aircraft faces moving through the air. It has two main components:

### 1. Parasite Drag ($D_p$)
*   Caused by friction and form resistance.
*   Increases with the square of speed ($V^2$).
*   Dominant at high speeds.

### 2. Induced Drag ($D_i$)
*   By-product of lift generation (wingtip vortices).
*   Decreases with the square of speed ($1/V^2$).
*   Dominant at low speeds.

### Total Drag Curve
The sum of Parasite and Induced Drag creates a U-shaped curve when plotted against speed.
*   **$V_{MD}$ (Minimum Drag Speed)**: The speed at the bottom of the curve where Total Drag is minimum.
*   At $V_{MD}$, Induced Drag equals Parasite Drag.

## Thrust vs. Power

It is crucial to distinguish between Thrust and Power, especially for different engine types.

*   **Thrust ($T$)**: The force produced by the engine (Newtons or lbs). Important for **Jet** aircraft.
*   **Power ($P$)**: The rate of doing work ($P = T \times V$). Important for **Propeller** aircraft.
    *   **Power Available ($P_A$)**: The power the engine can deliver.
    *   **Power Required ($P_R$)**: The power needed to overcome drag ($P_R = D \times V$).

## Flight Regimes

### Region of Normal Command
*   Speeds higher than $V_{MD}$.
*   To fly faster, you need more thrust/power. Drag increases as speed increases.
*   Stable speed control.

### Region of Reversed Command (Back side of the power curve)
*   Speeds lower than $V_{MD}$.
*   To fly slower, you need **more** thrust/power because induced drag increases rapidly.
*   Unstable speed control (slower speed $\rightarrow$ more drag $\rightarrow$ speed decreases further unless power is added).
