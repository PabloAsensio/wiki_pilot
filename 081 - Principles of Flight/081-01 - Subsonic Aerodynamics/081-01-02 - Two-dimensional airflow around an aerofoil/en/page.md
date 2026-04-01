---
title: "Airflow around an Aerofoil (2D)"
description: "Definitions of aerofoil geometry and aerodynamic forces in two dimensions."
keywords: ["chord line", "camber", "angle of attack", "center of pressure", "aerodynamic center"]
---

# Airflow around an Aerofoil (2D)


## Geometry
*   **Chord Line**: A straight line connecting the leading edge and the trailing edge.
*   **Mean Camber Line**: A line equidistant from the upper and lower surfaces.
*   **Camber**: The curvature of the aerofoil (distance between chord line and mean camber line).
    *   **Symmetrical Aerofoil**: Camber is zero. Chord line = Mean camber line.
    *   **Positively Cambered**: Produces lift at zero Angle of Attack.
*   **Thickness**: Maximum distance between upper and lower surfaces.
*   **Angle of Attack ($\alpha$)**: The angle between the **Chord Line** and the **Relative Airflow**.
*   **Angle of Incidence**: The angle between the Chord Line and the **Longitudinal Axis** of the aircraft (fixed by design).

## Aerodynamic Forces
*   **Total Aerodynamic Reaction (TAR)**: The resultant force of all pressure and friction forces.
*   **Lift ($L$)**: The component of TAR **perpendicular** to the Relative Airflow.
*   **Drag ($D$)**: The component of TAR **parallel** to the Relative Airflow.

## Significant Points
*   **Center of Pressure (CP)**: The point through which the Lift acts.
    *   Moves forward as Angle of Attack increases (for most subsonic aerofoils) until the stall.
*   **Aerodynamic Center (AC)**: The point where the pitching moment coefficient is constant with changes in Angle of Attack.
    *   Typically located at 25% of the chord (subsonic).
