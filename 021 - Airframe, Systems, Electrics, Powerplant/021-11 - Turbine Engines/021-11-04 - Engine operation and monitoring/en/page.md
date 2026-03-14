# Engine Operation and Monitoring

## Engine Control & Monitoring

*   **Vibration Monitoring**: Used to detect mechanical deficiencies in rotating parts (bearings, spools).
    *   **Principle**: Accelerometers (piezo-electric) measure vibration. Signals are **filtered** to isolate relevant frequencies.
*   **Engine Trending**: Comparing actual engine data against expected performance models to **detect anomalies and plan maintenance** before a failure occurs.
*   **FADEC Status**: Designed with redundancy.
    *   One channel active, one standby.
    *   **Single-Fault Tolerant**: Engine operates normally after a single component failure.
    *   **Redundancy check**: Power loss to FADEC = **Engine Shutdown**.

## Monitoring Instruments (Examples)
*   **RPM (N1, N2)**: Primary power indication (especially **N1** and **EPR**).
*   **EGT/TGT**: Exhaust Gas Temperature. Critical for monitoring turbine health (creep limit).
*   **Fuel Flow**: Indicates consumption and health (e.g., leaks).
*   **Oil System**:
    *   **Pressure**: Vital for lubrication. Low pressure often leads to high temperature.
    *   **Temperature**: High temp indicates cooling failure or friction. Higher than normal pressure at start (cold oil) is normal.
    *   **Chip Detector**: Detects metal particles in oil (internal wear).
*   **Fuel Filter Bypass**: Indicates filter blockage; unfiltered fuel is supplied to prevent engine starvation.

## Power Ratings and Idle
*   **Ground Idle**: Low RPM to prevent excessive taxi speed.
*   **Flight Idle**: Higher RPM than ground idle.
    *   **Purpose**: Allows rapid acceleration (spool-up) to full power (e.g., for a **go-around** or reverse thrust).
    *   **Activation**: Logic circuits (Weight-on-wheels, flaps, etc.) switch between ground/flight idle.

## Turboprop Control Ranges
*   **Alpha Range**: Flight range (Flight Idle to Max Power). Propeller governed by CSU (Constant Speed Unit).
*   **Beta Range**: Ground range (Below Flight Idle).
    *   **Control**: Pilot directly controls **blade pitch** via the power lever.
    *   **Ground Idle**: Just enough thrust to taxi.
    *   **Reverse**: Maximum negative thrust for deceleration.

## Engine Start Anomalies
*   **Hung Start**: Engine lights up but fails to accelerate to self-sustaining speed.
    *   **Cause**: Low starter pressure, insufficient fuel flow?
    *   **Action**: Shut down, crank (dry motor) to clear fuel.
*   **Hot Start**: EGT exceeds limits.
    *   **Symptoms**: Low RPM + **Sudden/Rapid EGT rise**.
    *   **Cause**: Excess fuel, tailwind, early starter cut-out.
    *   **Action**: **Abort immediately** (Cut fuel).
*   **Wet Start**: No light-up (ignition failure). Unburnt fuel drains from the combustion chamber.
*   **Tailpipe Fire**: Fire in the exhaust nozzle (internal) due to excess fuel igniting after shutdown or failed start.
    *   **Action**: Cut fuel, **ventilate** (crank) engine.

## Operational Concepts
*   **Spool-up Time**: Time from idle to max thrust. Turbines suffer from "inertia" (slow response). High idle helps reduce this time.
*   **Relight in Flight**:
    *   Uses **windmilling** (airspeed) to rotate the compressor.
    *   Envelope depends on **Altitude** and **Airspeed**.
*   **Continuous Ignition**: Selected when there is a risk of flameout (Turbulence, Heavy Rain, Icing, Approach).
