The **Air Data Computer (ADC)** is a digital computer that processes inputs from various sensors to calculate accurate flight parameters for flight instruments and systems (EFIS, FMS, AFCS, Transponder, etc.).

## Inputs
The ADC receives raw data from:
1.  **Total Pressure ($P_t$):** From Pitot tubes.
2.  **Static Pressure ($P_s$):** From Static ports.
3.  **Total Air Temperature (TAT):** From temperature probes (e.g., Rosemount).
4.  **Angle of Attack (AoA):** From alpha vanes/probes.

## Outputs
Based on these inputs, the ADC computes:
*   **Altitude:** Pressure Altitude, Baro-corrected Altitude.
*   **Speed:** IAS, CAS, **TAS**, Mach Number.
    *   *Note:* The ADC is essential for calculating **TAS**, as it compensates for position, compressibility, and **density** errors using the SAT derived from TAT input. ($TAS = f(CAS, P_s, SAT)$).
*   **Temperature:** **SAT** (Static Air Temperature) is calculated from TAT and Mach number.
*   **Warnings:** Overspeed (VMO/MMO), Stall warnings.

## Redundancy
Modern aircraft typically possess two independent ADCs (ADC 1 and ADC 2) fed by independent sensors.
*   **Failure:** Switching facilities allow instruments to be fed from the alternate ADC if one fails.
*   **Standby:** Standby instruments (ASI, Altimeter) usually usually have their own direct pitot/static sources, separate from the ADC system.

## Key Calculation
The ADC calculates **Static Air Temperature (SAT)**, which cannot be measured directly in flight. It uses the measured **TAT** and the Mach number to derive SAT, which is then used to compute **True Airspeed (TAS)**.
