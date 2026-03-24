**Introduction**
The pressurization and air conditioning systems maintain a comfortable and safe environment for passengers and crew. This involves regulating cabin pressure and temperature using air supplied by the engines or APU.

## Air Conditioning (Air Cycle Machine)

Commonly referred to as **"Air Conditioning Packs"** or a **"Bootstrap System"**, the Air Cycle Machine (ACM) cools the hot bleed air for cabin use.

- **Operation Cycle:**
    1.  **Primary Heat Exchanger:** High-pressure bleed air is pre-cooled using ram air.
    2.  **Compressor:** The air is compressed (heating it up again).
    3.  **Secondary Heat Exchanger:** Removes heat from the compressed air using ram air.
    4.  **Turbine:** The air expands through the turbine, which **drives the compressor** and significantly **cools the air**.
    5.  **Water Separator:** Removes excess moisture.
    6.  **Humidifier:** May add moisture back for comfort before entering the cabin.
- **Cooling Medium:** The heat exchangers use **ram air**. On the ground or during slow flight, a **ground cooling fan** draws air through the ram air ducts to ensure heat exchange.
- **Main Function:** While both pressure and temperature drop through the ACM, its primary purpose is to **cool the bleed air**.

## Pressurization Control

Pressurization is achieved by supplying a constant mass of air into the cabin and regulating the amount of air allowed to escape.

- **Outflow Valves:** These are the primary control devices.
    - **Closing** the valves reduces outflow, **increasing cabin pressure** (lowering cabin altitude).
    - **Opening** the valves increases outflow, **decreasing cabin pressure** (raising cabin altitude).
- **Modes of Control:**
    - **Automatic:** An electronic controller signals **AC motors** to position the valves. Theoretically, the cabin pressure decreases more slowly than atmospheric pressure during climb to maintain the schedule.
    - **Manual:** The pilot uses a separate circuit with a **DC motor** to position the valves.
    - **Ditching:** Closes all valves to prevent water entry during a water landing.
    - **Pre-Pressurization:** The system slightly pressurizes the cabin **on the ground** to prevent a pressure "bump" at rotation/liftoff.

## Safety and Malfunctions

- **Safety Valve (Positive Pressure Relief):** Opens if cabin pressure gets too high relative to outside (Max differential + ~0.25 psi).
- **Inward Relief Valve (Negative Pressure Relief):** Opens if outside pressure is higher than inside (e.g., during rapid descent), preventing fuselage damage from compression.
- **Malfunction Scenarios:**
    - **Outflow Valve stuck CLOSED:** Pressure increases until the **safety valve** opens.
    - **Outflow Valve stuck OPEN at cruise:**
        - **Cabin Rate of Climb:** Increases.
        - **Cabin Altitude:** Increases (cabin decompresses).
        - **Differential Pressure:** Decreases (eventually to 0).

## Instrumentation

- **Cabin Altimeter:** Indicates cabin pressure as an equivalent altitude.
- **Cabin Vertical Speed Indicator:** Indicates rate of change of cabin altitude.
- **Differential Pressure Gauge:** Shows the difference between internal and external pressure.
- **Warnings:** Visual and aural warnings trigger if cabin altitude exceeds **10,000 ft**.
