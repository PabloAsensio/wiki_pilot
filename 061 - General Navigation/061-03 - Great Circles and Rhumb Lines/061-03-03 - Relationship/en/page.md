To understand navigation, we must first define the two main trajectories that an aircraft follows:

*   **Great Circle:** Represents the **shortest distance** between two points on the Earth's surface. However, due to meridian convergence, a great circle route constantly changes direction (true heading) as it progresses, except at the Equator or when flying directly north-south along a meridian.
*   **Rhumb Line:** A line that crosses all meridians at the **same angle**, meaning it maintains a constant direction. Although it is easier to fly with a compass, the distance traveled is always greater than that of a great circle (except at the Equator or on north-south headings).

## Key Differences and Curvature
On a polar stereographic projection chart, the Pole is the point of tangency. Here, meridians are straight lines radiating from the pole and parallels are concentric circles.

*   **Curvature:** Rhumb lines appear as curves that are concave toward the pole, while great circles are considered nearly straight lines near the pole, although in reality they are slightly concave toward the pole in projections far from the center.
*   **Latitude:** The higher the latitude (closer to the pole), **the less apparent curvature** of great circles on the chart.

The difference between the great circle route and the rhumb line is most notable when the **Conversion Angle** is greater.

## Convergence and Conversion Angle
The angular difference between these two trajectories is governed by the **Convergence** of meridians.

*   **Convergence:** The angle of inclination between two meridians at a given latitude. It is calculated as:
    \[ \text{Convergence} = \text{Change in Longitude} \times \sin(\text{Mean Latitude}) \]
*   **Conversion Angle (CA):** The angular difference between the great circle direction and the rhumb line. It equals half the convergence.
    \[ \text{Conversion Angle} = \frac{1}{2} \times \text{Convergence} \]

As shown in the following graph, both convergence and conversion angle increase significantly as we move away from the Equator toward the poles.

![Convergence and Conversion Angle vs Latitude](../assets/Convergencia_y_Angulo_de_Conversión_vs_Latitud.png)

Therefore, the discrepancy between flying a great circle or a rhumb line is greater when:
1.  The **Change in Longitude** increases.
2.  The **Mean Latitude** increases.

## Distance Variation
The general rule states that the difference in distance between a great circle route and a rhumb line route **increases** if:
*   The latitude of the route increases.
*   The difference in longitude between points increases.

For example, the distance difference between two points separated by 20° of longitude will be much greater at 60° latitude than at 20° latitude.

## Practical Rule: DIID
To calculate headings and correct the trajectory between a great circle and a rhumb line, the mnemonic rule **D-I-I-D** (Decrease-Increase-Increase-Decrease) is used for the northern hemisphere:

*   **D (Decrease):** When flying **West**, the great circle heading **Decreases**.
*   **I (Increase):** When flying **East**, the great circle heading **Increases**.

| Hemisphere | Direction | Great Circle Heading Behavior |
| :--- | :--- | :--- |
| **North** | West | Decreases (Decrease) |
| **North** | East | Increases (Increase) |
| **South** | West | Increases (Increase) |
| **South** | East | Decreases (Decrease) |

When applying the conversion angle, remember that the Great Circle heading always "pulls" toward the pole compared to the Rhumb Line.
