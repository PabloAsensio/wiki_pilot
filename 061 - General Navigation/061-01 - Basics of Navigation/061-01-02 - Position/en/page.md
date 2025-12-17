In air navigation, **position** is defined by a coordinate system using latitude and longitude. Although we often consider the Earth a perfect sphere to simplify calculations, reality is more complex and requires accurate models like the **WGS 84 ellipsoid** to ensure safety and precision in flight.

## Earth Shape and References

The Earth is not a perfect sphere; due to its rotation, it is slightly flattened at the poles and bulged at the equator. This shape is known as an **oblate spheroid** or ellipsoid.
*   **Sphere**: Assumed for general calculations, where 1 degree of latitude equals **60 NM**.
*   **Ellipsoid (WGS 84)**: Mathematical model used by systems like GPS. Here, the length of 1 degree of latitude varies: it is less at the equator (approx. 59.7 NM) and greater at the poles (approx. 60.3 NM).

## Latitude: Geodetic vs. Geocentric

Latitude is measured as an angle from the Equator (0°) to the Poles (90° N/S). There are two key definitions:
*   **Geocentric Latitude**: The angle measured from the **center of the Earth**.
*   **Geodetic (or Geographic) Latitude**: The angle between the equatorial plane and a line **perpendicular** to the surface of the ellipsoid at the observer's point. This is the latitude used on **navigation charts**.

Because the Earth is not a perfect sphere, these two latitudes only coincide at the Equator and the Poles. The maximum difference occurs near 45° N/S.

To calculate the **Change of Latitude** between two points:
*   If they are in the **same hemisphere**, subtract the angles. For example: 36°42'37'' - 27°48'05'' = **8°54'32''**.
*   If they are in **opposite hemispheres**, add them.

## Longitude and Meridians

**Longitude** is measured as the angle in the equatorial plane between the **Greenwich Meridian** (Prime Meridian) and the meridian of the point in question. Unlike latitude, geocentric and geodetic longitude are identical because they share the same vertex at the center of the Earth.

To calculate the change of longitude:
*   Same hemisphere (East/East or West/West): Subtract.
*   Different hemispheres (East/West): Add. For example, between 45°34'E and 09°18'W, the difference is **54°52'**.

## Navigation Lines: Great Circle and Rhumb Line

On the Earth's surface, we distinguish two main types of paths:
*   **Great Circle**: A line that divides the Earth into two equal halves (passes through the center). It represents the **shortest distance** between two points. The Equator and all meridians are Great Circles.
*   **Rhumb Line**: A line of **constant direction** that intersects all meridians at the same angle. Parallels of latitude are Rhumb Lines (they intersect meridians at 90°).

| Feature | Great Circle | Rhumb Line |
| :--- | :--- | :--- |
| **Definition** | Radius equal to Earth's radius | Cuts meridians at same angle |
| **Main Property** | Shortest distance | Constant direction |
| **Examples** | Equator, Meridians | Parallels, Equator, Meridians |

## Departure and Environmental Effects

**Departure** is the distance in nautical miles (NM) along a parallel of latitude. It is calculated with the formula:
\[ \text{Departure} = \text{Change of Longitude (min)} \times \cos(\text{Latitude}) \]
For example, a change of longitude of 500 NM at a latitude of 17°46' results in a longitude change of approximately **8°45'**.

Finally, it is crucial to consider temperature in vertical navigation (**Baro-VNAV**). Temperatures lower than standard cause the aircraft to fly a lower actual vertical path (shallower angle), which can be dangerous near terrain.
