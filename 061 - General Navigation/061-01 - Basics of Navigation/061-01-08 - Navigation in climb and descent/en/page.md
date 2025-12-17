Navigation during climb and descent phases requires specific calculations to determine speed, time, and distance accurately. Unlike level cruise flight, where conditions are relatively constant, climbs and descents involve continuous changes in altitude, which affect **True Airspeed (TAS)** and the effect of wind. Below are the key concepts and rules needed to master these calculations.

## Determining Average Wind and TAS

To solve navigation problems during these phases, pilots do not use the wind or TAS from a single altitude, but rather a representative average. Training standards establish the following empirical rules to calculate average **Ground Speed (GS)**:

* **For climb problems:** Use the TAS and wind (W/V) at an altitude corresponding to **2/3 of the cruising altitude** (or 2/3 of the altitude difference added to the base altitude).
* **For descent problems:** Use the TAS and wind (W/V) at an altitude corresponding to **1/2 of the descent altitude** (or half of the layer to be descended).

For example, if an aircraft climbs from sea level (0 ft) to **FL270** (27,000 ft), the reference altitude for calculations would be 18,000 ft ($27,000 \times 2/3$). If the climb is between 4,000 ft and 8,000 ft, the altitude to use would be 6,667 ft ($4,000 + 2/3 \times 4,000$).

## Calculating Ground Speed

Once the reference altitude is determined, the **Ground Speed (GS)** must be obtained. This generally involves three steps:

1. **Determine the Temperature:** Calculate the standard temperature (ISA) at that altitude and adjust it with the given deviation (for example, ISA +5°C).
2. **Calculate TAS:** Use a flight computer (such as an E6-B or CRP-5) to convert Calibrated Airspeed (CAS) to **True Airspeed (TAS)**, applying compressibility corrections if the speed is high (above 300 kt).
3. **Apply the Wind:** Use the wind direction and speed at the reference altitude to find the effective GS. If exact data for that altitude is not provided, interpolate between the winds given at higher and lower levels.

## Gradients and Rate of Climb/Descent

It is crucial to distinguish between the climb/descent angle and the vertical speed.

* **Climb/Descent Gradient:** The ratio between the change in altitude and the horizontal distance traveled, usually expressed as a percentage (%).

  * Formula:
    $$
    \text{Gradient (\%)} = \frac{\text{Change in Altitude}}{\text{Horizontal Distance}} \times 100
    $$
* **Rate of Climb (ROC) / Rate of Descent (ROD):** The vertical speed, measured in feet per minute (ft/min or fpm).

There is a direct relationship between gradient, ground speed, and vertical rate. A practical rule (based on the 1 in 60 rule) to estimate the required **Rate of Descent** is:

$$
\text{ROD (ft/min)} \approx \text{Gradient (\%)} \times \text{GS (kt)}
$$

Or, for a standard 3-degree glide path:
$$
\text{ROD} \approx 5 \times \text{GS}
$$

For example, with a **GS** of 120 kt on a 3° slope (approximately 5%), the rate would be about 600 fpm.

## Time and Distance Calculations

Finally, to determine how long it will take to reach a given altitude or how much distance will be covered during these maneuvers:

* **Climb/Descent Time:** Divide the total altitude difference by the average **Rate of Climb (ROC)** or **Rate of Descent (ROD)**.

  * $$
    \text{Time} = \frac{\text{Altitude Difference}}{\text{Rate (fpm)}}
    $$
* **Ground Distance:** Multiply the average **Ground Speed (GS)** by the calculated time.

  * $$
    \text{Distance} = \text{GS} \times \text{Time}
    $$

It is essential to remember that altitudes and distances must be in the same units for gradient calculations (usually feet, where 1 Nautical Mile (NM) ≈ 6,080 feet).
