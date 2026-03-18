Accurate air temperature measurement is crucial for calculating True Airspeed (TAS) and monitoring engine performance.

## Temperature Definitions
*   **Static Air Temperature (SAT) / Outside Air Temperature (OAT):** The temperature of the undisturbed air through which the aircraft is flying.
*   **Total Air Temperature (TAT):** The temperature measured by a probe sensing the airflow. It is always **higher** than SAT due to heating effects.
*   **Ram Rise:** The difference between TAT and SAT ($TAT = SAT + \text{Ram Rise}$).

## Heating Effects
As the aircraft moves through the air, the temperature measured by the probe increases due to two factors:
1.  **Kinetic Heating:** Caused by friction between air molecules and the probe surface.
2.  **Adiabatic Heating:** Caused by the compression of air as it is brought to rest in the probe.

## Measurement and Calculation
*   On modern aircraft with an Air Data Computer (ADC), the **TAT** is the measured value (using a Rosemount probe, for example).
*   There is no direct OAT probe. Instead, the ADC calculates **SAT** (and OAT) internally by subtracting the calculated Ram Rise and accounting for the probe's recovery factor from the measured TAT.
*   **Formula:** $TAT = SAT (1 + 0.2 \times K \times M^2)$, where K is the recovery factor and M is the Mach number.
