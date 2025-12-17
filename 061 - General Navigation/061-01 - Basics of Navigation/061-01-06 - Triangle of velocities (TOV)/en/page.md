Navigating an aircraft is very different from driving a car. While a car grips the road firmly, an aircraft moves within an air mass that is itself moving over the Earth. To understand where the aircraft is actually going and at what speed, pilots use a fundamental concept called the **Triangle of Velocities**.

Below, we explain in a simple way how these forces work and how pilots calculate them to reach their destination accurately.

## The Three Fundamental Vectors

To solve any navigation problem, we must visualize three forces or **vectors** interacting with each other. A vector is simply an arrow that indicates a direction and a magnitude (speed).

1. **Air Vector:** Represents the movement of the aircraft through the air. It is made up of:

   * **True Heading (TH):** The direction the nose of the aircraft is pointing.
   * **True Airspeed (TAS):** The actual speed of the aircraft relative to the surrounding air.

2. **Wind Vector (W/V):** Represents the movement of the air mass over the Earth. It is defined by its direction (where it is coming from) and its speed (intensity in knots).

3. **Ground Vector:** This is the final result—what the aircraft actually does on the map. It is made up of:

   * **True Track (TT):** The actual line the aircraft traces over the ground.
   * **Ground Speed (GS):** The speed at which the aircraft moves over the terrain.

### Vector Addition

The physical principle behind this is **vector addition**. Imagine walking forward on a moving walkway that is drifting sideways. Your final movement is a diagonal. In aviation, to add these vectors, we place the tail of the **Wind Vector** at the head (tip) of the **Air Vector**; the resulting vector, from the start to the end, is the **Ground Vector**.

## Practical Navigation Concepts

### Drift and Correction

When the wind blows from the side, it pushes the aircraft off its desired route.

* **Drift:** The angular difference between where the aircraft is pointing (Heading) and where it is actually going (Track). If the wind comes from the right, it will push us to the left, creating a left drift.
* **Wind Correction Angle (WCA):** To counteract drift, the pilot must “point” the aircraft into the wind. If the wind pushes you 10° to the left, you must turn 10° to the right to compensate.

### Wind Components

The wind rarely blows directly head-on or directly from behind; it usually comes at an angle. Pilots divide this wind into two effects:

* **Headwind/Tailwind:** Affects the speed at which you move over the ground (Ground Speed).
* **Crosswind (XWC):** Responsible for pushing the aircraft sideways (Drift) and is critical during landing.

## Calculation Tools

### The Flight Computer (CRP-5 / E6-B)

Pilots use a circular mechanical calculator to solve this triangle. There is a golden rule for plotting the wind on the disk depending on which data you have:

* If you know the **Heading**, plot the wind **DOWNWARD** from the center of the disk.
* If you know the **Track**, plot the wind **UPWARD** from the center.

### Mental Calculation (MDR – Mental Dead Reckoning)

In flight, there is sometimes no time to use the computer. There are quick mental math techniques:

* **Clock Code Rule for Crosswind:**
  Used to estimate how much crosswind we have based on the wind angle:

  * **15°** difference: Equivalent to 1/4 of the wind strength (25%).
  * **30°** difference: Equivalent to half the strength (50%).
  * **45°** difference: Equivalent to 3/4 of the strength (75%).
  * **60°** or more: Considered to be 100% effective.

* **1 in 60 Rule for Drift:**
  To estimate how many degrees the wind will push us off course, the formula is:
  \[ \text{Angle} = \frac{\text{Crosswind} \times 60}{\text{TAS}} \]
  This quickly tells us how many degrees we must turn to maintain the route.

## Preparing the Data

Before calculating, the data must be consistent:

1. **From CAS to TAS:** The airspeed indicator in the cockpit (Calibrated Airspeed – CAS) is not perfect. It must be corrected for altitude and temperature to obtain **True Airspeed (TAS)**. Sometimes this involves first converting a Mach Number to TAS.
2. **Magnetic vs. True:** Charts and meteorological data use different references. Wind is usually given with respect to **True North**, while compasses use **Magnetic North**. It is vital to correctly apply **Magnetic Variation** (adding or subtracting depending on whether it is East or West) before mixing the data.
