In global navigation, it is crucial to understand how lines are drawn on the curved surface of the Earth. The two most important concepts that define these trajectories are the **Rhumb Line** and the **Great Circle** (Orthodrome).

## What is a Rhumb Line?
A **Rhumb Line** (or *Loxodrome*) is a line on the Earth's surface that **crosses all meridians at the same angle**. This means it is a line of **constant direction**. For a pilot or navigator, following a rhumb line is convenient because it allows maintaining a fixed heading on the compass without having to constantly adjust it.

Visually, a rhumb line has a unique geometric characteristic: **it forms a spiral toward the nearest Pole**, unless its direction is true North, South, East, or West.
*   **Special Cases:**
    *   **Parallels of latitude** are rhumb lines because they cross all meridians at 90°.
    *   **Meridians** and the **Equator** are rhumb lines because they maintain a constant direction (North-South or East-West) and are also Great Circles.

## What is an Orthodrome?
A **Great Circle** (or *Orthodrome*) is a circle drawn on the Earth's surface whose center and radius coincide with those of the terrestrial sphere. It is the largest possible intersection that can be obtained on a sphere.
Its key properties are:
*   It represents the **shortest distance** between two points on the Earth's surface.
*   Only one Great Circle exists between two points (unless they are antipodes).
*   Its direction continuously changes with respect to meridians (it is not a constant heading line).

## Relationship between Rhumb Line and Orthodrome

Although the orthodrome offers the shortest route, the direction constantly changes, which is difficult to fly manually. The rhumb line is longer but easier to follow.
The positional relationship between both is fixed:

*   The **Rhumb Line** is always located on the **equatorial** side of the equivalent orthodrome.
*   The **Orthodrome** is always located on the **polar** side (closer to the pole) of the rhumb line.

On a map, the angular difference between the orthodrome track and the rhumb line track is called the **Conversion Angle**, which equals half the **Convergence**.

## Navigation Calculations

To convert between these headings, specific formulas are used:

1.  **Convergence**: Calculated by multiplying the change in longitude by the sine of the mean latitude.
    *   *Formula: Convergence = Change in Longitude × Sine (Mean Latitude)*
2.  **Conversion Angle**: It is half of the convergence.
    *   *Formula: Conversion Angle = ½ Convergence*

**Practical Example:**
If we fly between two points in the northern hemisphere with a mean latitude of 55°N and a change in longitude of 10°:
*   Convergence = 10° × Sin(55°) ≈ 8°.
*   Conversion Angle = 4°.
The rhumb line heading will be the sum (or subtraction, depending on direction) of the initial orthodrome heading and this conversion angle. At the midpoint of the route, the rhumb line heading and the orthodrome heading **have the same direction**.

## Summary of Properties

| Characteristic | Rhumb Line | Great Circle (Orthodrome) |
| :--- | :--- | :--- |
| **Definition** | Line of **constant direction** crossing meridians at the same angle. | Circle with the same center and radius as the Earth. |
| **Advantage** | Easy to navigate (fixed heading). | **Shortest distance** between two points. |
| **Trajectory** | Curves in a spiral toward the pole. | Direct circle around the sphere. |
| **Relationship** | Located toward the **Equator**. | Located toward the **Pole**. |
| **Examples** | Meridians, Equator, Parallels. | Meridians, Equator. |
