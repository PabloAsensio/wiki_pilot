# Additional Components and Systems

## Accessory Gearbox
The accessory gearbox drives essential engine and aircraft systems.
*   **Drive Source**: Usually driven by the **HP Compressor shaft** (High speed) via an internal gearbox.
*   **Driven Components**:
    *   **Fuel Pumps** (High Pressure).
    *   **Oil Pumps**.
    *   **Hydraulic Pumps**.
    *   **IDG/CSD** (AC Generator).
*   **Lubrication**: Lubricated by the **engine oil system**.
*   **Shear Neck**: A weak point in the drive shaft designed to break if a component seizes (e.g., a generator jams). This protects the main gearbox and engine from damage, allowing the engine to continue running (minus the failed accessory).

## Ignition System
Gas turbine engines use high-energy ignition systems.
*   **Components**:
    *   **Ignition Exciter/Unit**: Converts low voltage (DC/AC) to high voltage (up to 25,000 V).
    *   **Igniters**: Spark plugs designed for high energy discharge. Two per engine.
*   **Operation**:
    *   **Start**: High energy spark to ignite the mixture.
    *   **Continuous Ignition**: Low energy spark used to prevent flameout. Selected automatically (by FADEC) or manually during:
        *   Take-off / Landing.
        *   Heavy precipitation / Turbulence.
        *   Anti-ice operation.
        *   Stall warning or engine surge.
*   **Ignition Type**: High intensity capacitor discharge system.

## Engine Starting
*   **Sequence**:
    1.  **Rotation**: Starter spins HP compressor (N2).
    2.  **Ignition**: Spark initiated.
    3.  **Fuel**: Fuel introduced.
*   **Starter Types**:
    *   **Electric**: Used on small engines and APUs (battery powered).
    *   **Pneumatic (Air Starter)**: Used on most large turbofans. Powered by high-pressure air from:
        *   **APU** (Auxiliary Power Unit).
        *   **Ground Cart** (GPU/ASU).
        *   **Cross-bleed** (from the other running engine).

## FADEC (Full Authority Digital Engine Control)
A digital computer system that manages all engine functions.
*   **Architecture**:
    *   **Dual Channel**: Two independent ECUs (Electronic Control Units) for redundancy (Active/Standby).
    *   **Power Supply**: Dedicated **Permanent Magnet Alternator (PMA)** on the engine provides independent power.
*   **Redundancy**:
    *   **Single Fault Tolerant**: If one channel fails, the other takes over immediately with no loss of performance.
    *   **Total Failure**: If both channels fail (and no hydromechanical backup exists), the engine shuts down (fuel valve closes).
*   **Functions**:
    *   Fuel metering.
    *   Engine limit protection (Overspeed, Over-temp).
    *   Auto-start.
    *   Thrust Reverser control.
    *   Engine health monitoring.

## Auxiliary Power Unit (APU)
A small gas turbine located in the tail.
*   **Purpose**: Provides **Electrical Power** (AC) and **Pneumatic Air** (for air conditioning and engine starting) on the ground and in flight.
*   **Starting**: Usually started electrically using the **aircraft battery**.
