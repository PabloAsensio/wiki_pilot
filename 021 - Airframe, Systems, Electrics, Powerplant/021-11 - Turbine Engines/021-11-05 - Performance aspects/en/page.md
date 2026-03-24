# Performance Aspects

## Thrust and Pressure
*   **Air Acceleration**: As the engine accelerates the air, **dynamic pressure increases** and static pressure decreases (Bernoulli's principle).
*   **Specific Thrust**: Defined as Net Thrust per unit of Air Mass Flow.
    *   If intake airflow increases (due to higher speed/density) while net thrust remains constant, **specific thrust decreases**.

## Flat-Rated Engines
Turbine engines are often "flat-rated" to provide consistent performance across a range of temperatures and to protect the engine components.

*   **Flat-Rated Range (Cold/Standard OAT)**:
    *   Occurs when Outside Air Temperature (OAT) is **below** the "flat-rated temperature" (typically around ISA +15°C).
    *   Thrust is limited by **internal pressure limits** (Maximum Mass Flow / Structural limit).
    *   The engine produces a **constant maximum thrust** regardless of the OAT dropping further.
*   **Temperature Limited Range (Hot OAT)**:
    *   Occurs when OAT is **above** the flat-rated temperature.
    *   Thrust is limited by **EGT/TGT** (Exhaust/Turbine Gas Temperature) to prevent melting or creep of turbine blades.
    *   As OAT increases, **maximum available thrust decreases**.

## Reduced Thrust Take-off (Flex / Assumed Temp)
Used to extend engine life by using less than maximum thrust when takeoff performance allows (light weight, long runway).

*   **Principle**: The FADEC/Computer is "tricked" into thinking the outside air is hotter than it actually is.
*   **Method**:
    *   The pilot enters an **Assumed Temperature** (or Flex Temp) into the FMS.
    *   This assumed temperature is **higher** than the actual OAT.
    *   Since the engine is "temperature limited" at high OATs, the computer calculates a **lower N1/EPR limit**.
    *   **Result**: The engine produces less thrust, running cooler (lower EGT), reducing wear.

## Thrust Indication: EPR
*   **EPR (Engine Pressure Ratio)**: A primary thrust parameter on many jet engines (others use N1).
*   **Definition**: The ratio of **Low-Pressure Turbine Exhaust Pressure** ($P_{exit}$) to **Compressor Inlet Pressure** ($P_{inlet}$).
    *   $$EPR = \frac{\text{Total Pressure at Turbine Exit}}{\text{Total Pressure at Compressor Inlet}}$$
*   **Sensors**: Can be electromechanical bellows or digital transducers.
