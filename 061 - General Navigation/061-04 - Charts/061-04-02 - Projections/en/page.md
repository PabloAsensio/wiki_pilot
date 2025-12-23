Navigating the world requires translating a three-dimensional sphere (the Earth) to a two-dimensional flat map. This process is carried out through **projections**, and each one has its own rules and distortions. Below, we explain in a simple way how the main projections used in aviation work, integrating all the essential theoretical and mathematical concepts.

## Fundamental Navigation Concepts

Before studying maps, we must understand how lines and angles behave on the Earth's surface:

*   **Orthodrome (Great Circle):** It is the shortest distance between two points on a sphere. Its direction changes constantly as we cross meridians. In most charts, we seek for these routes to appear as straight lines.
*   **Loxodrome (Rhumb Line):** It is a line that maintains a constant direction, cutting all meridians at the same angle. It is easy to fly (you just follow a fixed heading on the compass), but it is not the shortest route. On polar charts, it is a curve concave toward the pole.
*   **Convergence (Convergency):** It is the angle of inclination between two meridians. On Earth, meridians meet at the poles.
    *   Formula: **Convergence = Change in Longitude × Sine (Mean Latitude)**.
*   **Conversion Angle:** It is the angular difference between the direction of the Orthodrome and the Loxodrome.
    *   Key rule: **Conversion Angle = ½ Convergence**.

***

## 1. Polar Stereographic Projection

This chart is created by imagining a flat plane that touches the Earth at one of the Poles (point of tangency). It is ideal for navigation at high latitudes.

*   **Graticule (Geographic Network):** The **meridians** are straight lines radiating from the pole. The **parallels** are concentric circles whose distance increases when moving away from the pole.
*   **Convergence Factor (n=1):** In this chart, convergence is maximum and identical to polar reality.
    *   **Chart Convergence = Change in Longitude**.
*   **Route Behavior:**
    *   A straight line drawn passing through the pole is a meridian.
    *   **Orthodromes** (great circles) are almost straight near the pole, but technically are slightly concave curves toward the pole.
    *   **Loxodromes** are pronounced curves, always concave toward the projection pole.
*   **Scale:** It is correct only at the Pole. It expands as we move away (proportional to the secant squared of half the co-latitude).

***

## 2. Lambert Conformal Conic Projection

It is the standard chart for aviation at mid-latitudes. A cone is used that "cuts" the Earth, intersecting it at two **Standard Parallels**.

*   **Origin Parallel:** It is the central mathematical latitude of the projection, located halfway between the two standard parallels. Here the chart convergence equals the Earth convergence.
    *   Calculation: *(Standard Parallel 1 + Standard Parallel 2) / 2*.
*   **Cone Constant (n):** It defines how much the cone has been "flattened" (0 is a cylinder, 1 is a plane).
    *   **Cone Constant = Sine (Origin Parallel)**.
*   **Chart Convergence:** It is constant throughout the map.
    *   **Convergence = Change in Longitude × Cone Constant**.
*   **Scale:** It is exact on the standard parallels. It **contracts** (reduces) between them (minimum at the origin parallel) and **expands** (increases) outside them. The scale error is typically kept below **1%**.
*   **Orthomorphic:** Yes, like all navigation charts, it preserves angles and shapes in small areas.

***

## 3. Direct Mercator Projection

It is a cylindrical projection where the cylinder wraps the Earth touching the **Equator** (its origin parallel).

*   **Graticule:** The **meridians** are straight parallel lines uniformly spaced. The **parallels** are straight parallel lines that separate more as they move away from the Equator.
*   **Zero Convergence:** Since the meridians are parallel, they never touch. The chart convergence is zero.
*   **Routes:**
    *   **Loxodromes** are perfect straight lines (its great advantage).
    *   **Orthodromes** are convex curves toward the pole (concave to the Equator).
*   **Variable Scale:** The scale is correct only at the Equator and increases rapidly toward the poles (like the secant of the latitude).
*   **The "ABBA" Formula:** To calculate distances or scales at different latitudes on a Mercator, we use this mathematical relationship:
    *   **Distance A × Cos(Latitude B) = Distance B × Cos(Latitude A)**.

***

## Practical Direction Rules

To solve direction problems between two points (A and B):

1.  **Calculate Convergence:** Depending on the projection (Change in Longitude for Polar; Change in Longitude × Sine of Latitude for Lambert).
2.  **Calculate Conversion Angle:** Divide the convergence by 2.
3.  **Apply the Hemisphere Rule:**
    *   The **Orthodrome** is always closer to the Pole than the Loxodrome.
    *   On a Lambert or Polar chart, the Orthodrome is the straightest line; the Loxodrome curves toward the equator.
    *   **GCT (Great Circle Track) = RLT (Rhumb Line Track) ± Conversion Angle**.
