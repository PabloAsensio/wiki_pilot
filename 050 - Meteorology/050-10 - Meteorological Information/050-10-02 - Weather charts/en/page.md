## Significant Weather Charts (SIGWX)

Significant Weather Charts (SIGWX) provide a forecast of significant meteorological phenomena for aviation.

### Front Symbols
*   **Warm Front:** Red semicircles.
*   **Cold Front:** Blue triangles.
*   **Occluded Front:** Alternating semicircles and triangles (purple).
    *   **Cold Occlusion:** The occlusion line follows the cold front line.
*   **Stationary Front:** Semicircles and triangles on opposite sides of the line.

### Significant Phenomena
*   **Fog:** Horizontal lines symbol.
*   **Smoke:** Specific symbol.
*   **Haze:** Infinity symbol (∞).
*   **Tropical Cyclone:** Spiral symbol with two arms.
*   **Volcano:** Trapezoid symbol with smoke/ash.

### Jet Streams
Represented as thick lines with arrows.
*   **Core:** Wind speed at the core is indicated with barbs/flags (e.g., 120 kt).
*   **Altitude:** Flight level of the core is indicated (e.g., FL370).
*   **Depth:** Lower and upper levels between which the wind exceeds 80 kt are indicated (e.g., FL230 - FL440).
*   **Wind Change:** Dashed lines parallel to the Jet indicate areas of Clear Air Turbulence (CAT).

### Tropopause
*   **Height:** Indicated in hundreds of feet inside rectangles (e.g., 350 = FL350).
*   **High/Low Centers:** Enclosed in polygons with an "H" (High) or "L" (Low).
    *   The tropopause is higher at the equator and lower at the poles.
    *   In a Jet Stream, the tropopause is lower on the cold (polar) side and higher on the warm side.

### Clouds and Associated Hazards
On SIGWX charts, the mention of **CB (Cumulonimbus)** automatically implies the presence of:
*   Thunderstorms (TS).
*   Hail (GR).
*   Moderate or Severe Turbulence.
*   Moderate or Severe Icing.

**Coverage:**
*   **ISOL (Isolated):** < 50% of the area (individual).
*   **OCNL (Occasional):** 50-75% of the area (well separated).
*   **FRQ (Frequent):** > 75% of the area (little or no separation).
*   **EMBD (Embedded):** Within other cloud layers.

## Numerical Weather Prediction (NWP)

### 3D Grid System
Meteorological models divide the atmosphere into a three-dimensional grid.
*   **Horizontal Data:** Latitude and Longitude.
*   **Vertical Data:** Height or Pressure.
*   Time is not used as a grid axis itself, but time steps are calculated.

### WAFC (World Area Forecast Centre)
There are two centres (London and Washington) designated to prepare and issue global forecasts.
*   They generate gridded forecasts of wind, temperature, humidity, tropopause, CB, icing, and turbulence.
*   These data are integrated into flight planning systems.

### Pilot Reports
Aircraft data (AIREP/PIREP) can be merged into processing systems to improve **situational awareness** and refine future prediction models.

## Surface Charts

Show pressure at sea level using isobars.
*   **Low Pressure (Cyclone/Depression):** Air rotates counter-clockwise (Northern Hemisphere). Winds converge and ascend -> Bad weather.
*   **High Pressure (Anticyclone):** Air rotates clockwise (Northern Hemisphere). Winds diverge and descend (subsidence) -> Good weather, but possible fog/haze due to inversion.
*   **Col:** Area between two highs and two lows. Calm winds. In summer conducive to air mass thunderstorms; in winter to fog.
*   **Ridge:** Extension of high pressure. Good weather.
*   **Trough:** Extension of low pressure. Bad weather.

## Upper Wind and Temperature Charts

Show wind direction and intensity and temperature at specific flight levels.

### Interpretation
*   **Wind Barbs:**
    *   Short line: 5 kt.
    *   Long line: 10 kt.
    *   Triangle/Flag: 50 kt.
    *   Direction is from where the wind blows (compare with local meridians for True North).
*   **Temperature:** Indicated next to the station or on the grid.
    *   **ISA Deviation Calculation:**
        1.  Calculate Standard ISA Temp: $15 - (2 \times \text{Altitude in thousands of feet})$.
        2.  Compare with Actual Temp (OAT).
        3.  Example at FL180 with OAT -30°C:
            *   ISA FL180 = $15 - (2 \times 18) = 15 - 36 = -21^\circ\text{C}$.
            *   Difference: $-30$ is 9 degrees colder than $-21$.
            *   Deviation: ISA -9°C.
