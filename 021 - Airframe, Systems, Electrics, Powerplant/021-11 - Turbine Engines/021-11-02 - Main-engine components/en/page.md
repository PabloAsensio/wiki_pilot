# Main Engine Components

The core components of a gas turbine engine are designed to process air through the Brayton cycle: Intake, Compression, Combustion, Expansion (Turbine), and Exhaust.

## Compressor Section
The compressor increases the pressure of the air mass flow to supply the combustion chamber.
*   **Types**:
    *   **Centrifugal**: Accelerates air radially. Robust, simpler, max pressure ratio ~4.5:1 per stage.
    *   **Axial**: Air flows parallel to the axis. Made of alternating rows of **Rotors** and **Stators**.
        *   **Rotor**: Spins reduces volume, adds kinetic energy (Velocity increases, Pressure increases).
        *   **Stator**: Stationary vanes. Converges kinetic energy into pressure energy (Velocity decreases, Pressure increases). Also straightens airflow.
*   **Overall Effect**: Through the compressor, **Pressure and Temperature increase**, while **Axial Velocity decreases**.
*   **Compressor Stall/Surge**: Can occur if airflow is disrupted (e.g., mismatched RPM and airflow).
    *   **Symptoms**: High EGT, Vibration, loss of thrust, "banging" noise (surge).
    *   **Prevention**:
        *   **Variable Inlet Guide Vanes (VIGVs)**: Before the 1st stage, adjust air angle.
        *   **Variable Stator Vanes (VSVs)**: Between stages.
        *   **Bleed Valves**: Release pressure to prevent backflow.

## Diffuser
Located between the compressor exit and the combustion chamber.
*   **Function**: A divergent duct that **decreases air velocity** and **increases static pressure**.
*   **Purpose**: Slows air to a speed compatible with flame propagation speeds, ensuring the **flame burns continuously** and isn't extinguished.

## Combustion Chamber
Mixes compressed air with fuel and burns it.
*   **Process**: Constant pressure combustion.
*   **Fuel Nozzles**: Atomize fuel into a spray with axial and tangential velocity components.
*   **Drain Valves**: Located at the bottom to remove unburnt fuel after a failed start (wet start).

## Turbine Section
Extracts energy from hot gases to drive the compressor and accessories.
*   **Types**:
    *   **Impulse Turbine**:
        *   **Nozzle Guide Vanes (NGV)**: Convergent duct -> Velocity Increases, Pressure Decreases.
        *   **Rotor Blades**: Bucket shape -> Velocity Decreases, **Pressure Constant**.
    *   **Reaction Turbine**:
        *   **NGV**: Directs air (Pressure constant).
        *   **Rotor Blades**: Convergent shape -> Velocity Increases, **Pressure Decreases** (creating reaction force).
*   **Limitations**: The turbine is the **most stressed** component (Heat + Centrifugal force).
    *   **Creep**: Blades stretch over time due to stress/heat. Limits engine life and max temperature (TGT/EGT).
    *   **Active Clearance Control**: Cools the casing to maintain optimal tip clearance.

## Exhaust Section
Directs gases out of the engine to produce thrust.
*   **Jet Pipe**: Conducts gas.
*   **Exhaust Cone**: Smooths flow leaving the turbine.
*   **Propelling Nozzle**: Usually **convergent**.
    *   **Function**: Increases exhaust gas **velocity** and decreases pressure to maximize momentum and thrust.

## Foreign Object Damage (FOD)
Ingestion of debris.
*   **Indications**: High Vibration, High EGT, fluctuating RPM or parameters.
