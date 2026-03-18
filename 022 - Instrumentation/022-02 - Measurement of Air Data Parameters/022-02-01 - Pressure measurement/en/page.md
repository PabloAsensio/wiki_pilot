The measurement of pressure is fundamental to flight instrumentation. The **Pitot-Static System** provides the raw pressure data needed to determine airspeed, altitude, and vertical speed.

## Principles of Pressure
*   **Static Pressure ($P_s$):** The atmospheric pressure surrounding the aircraft. It acts on all surfaces and decreases with altitude.
*   **Total (Pitot) Pressure ($P_t$):** The sum of static pressure and dynamic pressure created by the aircraft's forward motion.
*   **Dynamic Pressure ($q$):** The pressure determined by airflow velocity and density ($q = 1/2 \rho V^2$).
    *   Relationship: **$P_t = P_s + q$**

## System Components
1.  **Static Ports:** Vents located on the fuselage (often paired to cancel sideslip errors) where airflow is undisturbed. They supply the **Altimeter**, **VSI**, and **ASI**.
2.  **Pitot Tube:** An open-ended tube facing the relative airflow. It measures **Total Pressure** and supplies ONLY the **ASI** (and Machmeter/ADC).

## Blockages and Errors
*   **Static Blockage:**
    *   **Altimeter:** Freezes at the altitude where blockage occurred.
    *   **VSI:** Indicates zero.
    *   **ASI:** Behave like an altimeter in reverse (Under-reads in Climb / Over-reads in Descent).
    *   **cockpit static vent:** If used as an alternate source, the lower pressure in the cockpit (due to aerodynamic suction) causes the Altimeter and Airspeed to **over-read** and the VSI to indicate a momentary climb.
*   **Pitot Blockage:**
    *   **ASI:** Acts like an altimeter (Over-reads in Climb / Under-reads in Descent).
