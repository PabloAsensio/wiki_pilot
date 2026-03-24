Fuel flowmeters provide pilots and onboard computers with real-time data on engine performance and fuel consumption.

## Principles of Measurement
Fuel flowmeters measure the quantity of fuel delivered to the engines per unit of time. There are two main methods of measurement:
*   **Volumetric:** Outputs volume per unit of time (e.g., US gal/h, Liters/h). Susceptible to density errors from temperature changes.
*   **Gravimetric:** Outputs **mass** per unit of time (e.g., **kg/h**, lb/h). This is the standard for Commercial Air Transport as it provides a more consistent and accurate measure of energy content.

## Total Fuel Consumption (Fuel Used)
To determine the total fuel consumed during a flight, the system uses **integration**.
*   **Process:** A computer mathematically integrates the rate of fuel consumption (flow) over time.
    *   $\text{Total Consumption} = \int (\text{Fuel Flow}) dt$
*   **Function:** This calculation accounts for all variables affecting consumption (altitude changes, speed, weather).
*   **Utility:** The calculated "Fuel Used" is compared alongside the "Fuel On Board" (FOB) from the tank sensors. This cross-check allows the crew and the Flight Management System (FMS) to:
    1.  Verify accurate fuel burning.
    2.  **Detect leaks** (if Fuel Used + Remaining does not equal Initial FOB).
    3.  Predict fuel at destination accurately.

An **Integrated Flowmeter** is an instrument that displays both the instantaneous Fuel Flow and the Total Fuel Used.
