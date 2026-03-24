A gyroscope is a rotating mass that maintains its orientation in space unless acted upon by an external force. This property makes it essential for flight instrumentation (Attitude Indicator, Heading Indicator, Turn Indicator).

## Key Properties
1.  **Rigidity in Space:** The tendency of a spinning mass to maintain its plane of rotation fixed in space.
    *   Depends on: **Mass** (heavier = more rigid), **Radius** (mass at periphery = more rigid), and **Speed** (faster = more rigid).
2.  **Precession:** If a force is applied to the spinning rotor, the reaction occurs **90° later** in the direction of rotation.

## Degrees of Freedom
*   **1 Degree of Freedom:** The gyro can move around only one axis (besides its spin axis). Used in **Turn Indicators**.
*   **2 Degrees of Freedom:** The gyro can move around two axes. Used in **Artificial Horizons** (Pitch/Roll) and **Directional Gyros** (Heading).

## Wander
Wander is any movement of the gyro axis from its intended orientation.
*   **Real Wander:** Physical movement of the axis due to mechanical imperfections (friction, unbalance).
*   **Apparent Wander:** The gyro stays fixed in space, but the Earth rotates beneath it, making it *appear* to move.
    *   **Drift:** Horizontal movement. Max at Poles ($15^\circ/hr \times \sin \text{Lat}$).
    *   **Topple:** Vertical movement.
*   **Transport Wander:** Apparent wander caused by moving the aircraft across the Earth's curved surface (changing longitude).

## Gyro Types by Axis
*   **Vertical Axis Gyro:** Used for **Attitude Indicators** (detects Pitch and Roll).
*   **Horizontal Axis Gyro:** Used for **Directional Gyros** (detects Yaw) and **Turn Indicators** (detects Rate of Yaw).
