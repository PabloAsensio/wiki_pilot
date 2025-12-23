Aeronautical charts are fundamental representations for air navigation, acting as a "reduced Earth" on a plane. Their main function is to show the relationship between distances on the map and actual distances on the planet, allowing pilots to plan and execute flights with precision. Below are the key concepts for understanding their operation.

## Chart Scale

The **chart scale** is the relationship between a length measured on the map and the corresponding distance on Earth. It is expressed using the formula:

**Scale = Distance on Chart / Distance on Earth**

To compare scales, a simple rule based on the denominator of the representative fraction is used:
*   **Larger denominator, smaller scale**: Covers more area but with less detail (e.g., 1:2,000,000).
*   **Smaller denominator, larger scale**: Covers less area but with more detail (e.g., 1:500,000).

For example, when calculating the scale at a latitude of 45°N where 6 cm on the map represents 1 degree of longitude, we obtain a scale of approximately **1:1,309,562**. It is crucial to remember to convert all measurements to the same unit (such as centimeters) before performing the calculation.

## Distance Calculation (Departure)

To determine the actual distance between two meridians at a specific latitude, the **departure** formula is used. Because meridians converge toward the poles, the distance between them decreases as latitude increases.

**Departure (NM) = Change in Longitude x 60 x cos(latitude)**

This formula allows calculating the distance in Nautical Miles (NM) that separates two points of different longitude located on the same parallel.

## Cartographic Projections

There are different ways to project the Earth's spherical surface onto a plane, each with its own characteristics.

### Lambert Conformal Conic Projection
In this projection, the scale is exact only on the **standard parallels**. Its main characteristics are:
*   The scale decreases between the standard parallels and increases outside of them.
*   **Chart convergence** is constant and is calculated by multiplying the change in longitude by the sine of the origin parallel (known as the "cone constant").
*   A straight line on this chart approximates a **great circle**, which is ideal for radio navigation.

### Mercator Projection
It is a cylindrical projection where the scale expands as we move away from the Equator.
*   Scale expansion is proportional to the secant of the latitude.
*   To solve scale problems in Mercator, the relationship is used: **Denominator A x cos(Lat B) = Denominator B x cos(Lat A)**.

## Convergence and Orthomorphism

An essential property of navigation charts is **orthomorphism** (or conformality), which guarantees that angles measured on the chart are equal to angles on Earth. This ensures that navigation headings are correct.

*   **Chart Convergence**: Is the angle of inclination between meridians on the map.
*   **Earth Convergence**: Is the actual angle of inclination of meridians on the planet.
*   **Conversion Angle**: Is the angular difference between the great circle (shortest route) and the rhumb line (loxodromic). It is calculated as half the convergence.

## Practical Application: Speed and Time

The correct use of scale allows calculating **Ground Speed (GS)**. If we know the distance on the map and the time it takes to cover it, we first convert the map distance to ground distance using the scale, and then apply the formula:

**GS = Ground Distance / Flight Time**

For example, if we measure 13.8 cm on a chart with a scale where 1 cm equals 3.1 NM, the actual distance is 42.78 NM. If we fly that segment in 15 minutes, our ground speed would be 171 knots.
