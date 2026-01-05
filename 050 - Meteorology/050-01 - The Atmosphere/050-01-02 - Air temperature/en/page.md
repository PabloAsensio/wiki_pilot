## International Standard Atmosphere (ISA)

ICAO defines a standard atmosphere for calibration and comparison:
*   **Mean Sea Level (MSL)**: Temperature **15°C**, Pressure 1013.25 hPa.
*   **Lapse Rate**: Temperature decreases **2°C per 1000 ft** (0.65°C/100m) in the troposphere.
*   **ISA Tropopause**: At **36,090 ft (11 km)**.
*   **Lower Stratosphere**: Constant temperature of **-56.5°C** from the tropopause up to approx. 20 km (65,000 ft).

### Temperature Calculations
To calculate the ISA temperature at a given altitude (in thousands of feet):
$$T_{ISA} = 15 - (2 \times Altitude)$$
*Example at FL240 (24,000 ft):* $15 - (2 \times 24) = 15 - 48 = -33^\circ C$.

**ISA Deviation**: Difference between the actual temperature (OAT) and the ISA temperature.
$$Deviation = T_{Actual} - T_{ISA}$$
*Example: If at FL380 the actual T is -48°C. ISA T is -56.5°C. Deviation = -48 - (-56.5) = ISA +8.5°C.*

## Heat Transfer

1.  **Radiation**:
    *   **Solar (Insolation)**: The sun emits **shortwave** radiation (UV, visible). The atmosphere is almost transparent to it.
    *   **Terrestrial**: The Earth absorbs solar radiation and re-emits it as **longwave (Infrared)** radiation. This is the main heat source for the troposphere (it is heated from below).
    *   **Greenhouse Effect**: Gases like water vapor and CO2 absorb terrestrial longwave radiation, retaining heat.
2.  **Conduction**: Transfer by direct contact. Heats or cools only the layer of air in immediate contact with the surface (a few centimeters). Important for the formation of nocturnal inversions.
3.  **Convection**: Vertical transfer by movement of air masses. Warm air (less dense) rises (thermals).
4.  **Advection**: Horizontal transfer of heat by the wind.

## Diurnal Variation

*   **Day**: The surface heats up by insolation. Maximum temperature is usually in the afternoon (approx. 15:00), when heat received exceeds heat emitted.
*   **Night**: The surface cools by terrestrial radiation. Minimum temperature occurs just after sunrise.
*   **Effect of Clouds**:
    *   **Day**: Reflect solar radiation -> Lower temperatures.
    *   **Night**: Absorb and re-emit terrestrial radiation (blanket effect) -> Higher temperatures (less cooling).
*   **Effect of Wind**: Mixes the air, reducing extreme surface cooling at night (hinders inversions).

## Temperature Inversions

An inversion occurs when the temperature **increases with altitude** in the troposphere. They are very stable layers.

1.  **Radiation Inversion (Nocturnal)**:
    *   Occurs on **clear and calm** nights.
    *   The ground cools rapidly by radiation, cooling the air in contact by conduction.
    *   Common in winter over land. Can cause radiation fog.
2.  **Subsidence Inversion**:
    *   Associated with **High Pressure (Anticyclone)** systems.
    *   Air descends (subsidence) and warms by adiabatic compression.
    *   Creates a warm layer over a colder, stagnant layer near the ground.
    *   Common in winter over continents and in subtropical oceans.
3.  **Valley Inversion**:
    *   Cold air (denser) drains down slopes to the valley floor at night (katabatic wind), displacing warm air upwards.
4.  **Frontal Inversion**:
    *   Warm air rising over a cold air mass (fronts).

## Albedo

It is the reflectivity of a surface (0 to 1).
*   **High Albedo**: Fresh snow (0.80), Thick clouds. Reflect a lot of heat, warm up little.
*   **Low Albedo**: Asphalt, Forests, Dark ocean. Absorb a lot of heat.
