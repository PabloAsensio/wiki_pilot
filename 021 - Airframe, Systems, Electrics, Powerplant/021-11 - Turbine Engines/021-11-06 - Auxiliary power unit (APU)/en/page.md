---
title: "Auxiliary Power Unit (APU): Functions, Control, and Protection"
description: "Learn APU fundamentals, including electrical and pneumatic outputs, startup sequence, cockpit controls, and automatic shutdown protections."
---
# Auxiliary Power Unit (APU): Functions, Control, and Protection

## Purpose and Function
The APU is a small self-contained gas turbine engine, typically located in the tail cone of the aircraft.

*   **Primary Outputs**:
    1.  **Electrical Power**: Drives a generator (typically 115V AC, 400Hz) to supply aircraft systems on the ground or in flight (backup).
    2.  **Pneumatic Power (Bleed Air)**: Supplies high-pressure air for:
        *   **Main Engine Starting**.
        *   **Air Conditioning** (Environmental Control System).
        *   Wing Anti-icing (in some aircraft, though rare).
*   **Benefits**: Makes the aircraft independent of ground support equipment (GPU / Air Start Unit).

## Operation
*   **Fuel Source**: Draws fuel from the aircraft's main tanks (e.g., Left Main Tank).
*   **Starting**:
    *   Usually started electrically via the **Aircraft Battery** or **Ground Power**.
    *   **Envelope**: Must be certified for starting and operation at altitude.
*   **Combustion**: Operates at constant speed (governed) to maintain generator frequency (400Hz).

## Controls and Indication
*   **Master Switch**:
    *   Energizes the electronic control box (ECB/FADEC).
    *   Opens the **Air Intake Flap** (to ingest air).
    *   Opens the **Fuel Isolation Valve**.
*   **Start Button**:
    *   Energizes the **starter motor**.
    *   Activates ignition systems.
    *   Initiates automatic accelerating sequence.

## Automatic Shutdown Protection
The APU is capable of protecting itself by shutting down automatically (especially on the ground) for conditions such as:
*   **Overspeed** (Critical protection).
*   **Low Oil Pressure**.
*   **High Oil Temperature**.
*   **EGT Overtemperature** (Exhaust Gas Temperature).
*   **Fire**.
*   **reverse flow**, **Underspeed**, etc.

*Note: In flight, some protective shutdowns (like high oil temp) may be inhibited to prioritize electrical power availability in an emergency.*
