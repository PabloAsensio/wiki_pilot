---
title: "Meteorological Observation"
description: "How meteorological observations (METAR, SPECI, automated stations) are gathered and recorded for aviation."
keywords: ["meteorological observation aviation", "METAR SPECI flying", "automated weather stations ATPL", "weather observation networks"]
---

## Visibility

![Automated Airport Weather Station](https://upload.wikimedia.org/wikipedia/commons/2/28/Sydney_Airport_BOM_weather_station.jpg)

### Definition and Reporting
According to **ICAO Annex 3**, visibility for aeronautical purposes is defined as the greater of:
1.  The greatest distance at which a black object of suitable dimensions, situated near the ground, can be seen and recognized when observed against a bright background.
2.  The greatest distance at which lights in the vicinity of approximately **1,000 candelas** can be seen and identified against an unlit background.

**Prevailing Visibility:**
The greatest visibility value, observed in accordance with the definition of "visibility", which is reached within at least half the horizon circle or within at least half of the surface of the aerodrome. These areas could comprise contiguous or non-contiguous sectors.
*   In METAR and SPECI, it is recommended to report the prevailing visibility.
*   When visibility is below **1,500 m**, RVR should also be reported.

### Runway Visual Range (RVR)
**RVR (Runway Visual Range)** is the range over which the pilot of an aircraft on the centre line of a runway can see the runway surface markings or the lights delineating the runway or identifying its centre line.

*   **Measurement:** It is measured using **transmissometers** (or scatterometers) located along the runway (touchdown zone, mid-point, and stop-end). It can also be assessed by human observation by counting visible lights or markings.
*   **Reporting:**
    *   In METAR/SPECI, it is prefixed with "R", followed by the runway and the value (e.g., R18/450).
    *   It is reported in **metres** (although some countries like the USA use feet).
    *   Reporting steps:
        *   25 m (if RVR < 400 m).
        *   50 m (if RVR 400 - 800 m).
        *   100 m (if RVR > 800 m).
*   **Difference:** RVR is usually greater than prevailing visibility and is specific to the runway direction.

## Clouds

### Amount Reporting
Cloud amount is reported in **oktas** (eighths of the sky covered):
*   **FEW:** 1 to 2 oktas.
*   **SCT (Scattered):** 3 to 4 oktas.
*   **BKN (Broken):** 5 to 7 oktas.
*   **OVC (Overcast):** 8 oktas.

### Cloud Ceiling
It is the height above the ground or water of the base of the lowest layer of cloud below 6,000 m (20,000 ft) covering **more than half the sky** (i.e., BKN or OVC).

### Vertical Visibility (VV)
When the sky is obscured and clouds cannot be forecast or seen (e.g., dense fog), vertical visibility is reported instead of cloud amount. It is indicated as "VV" followed by the value in hundreds of feet (e.g., VV002 = 200 ft).

### Measurement
*   **Ceilometer:** An instrument (usually laser-based) used to measure the height of the cloud base.

## Wind

### Measurement and Reporting
*   **Instrument:** **Anemometer**, standardly positioned at **10 metres (33 ft)** above ground level, away from obstructions.
*   **Averages:**
    *   **METAR:** Mean speed and direction over the last **10 minutes**.
    *   **ATIS / ATC:** Mean speed and direction over the last **2 minutes**.
*   **Gusts:** Instantaneous deviations from the mean speed. They are reported in the METAR (with the letter "G") if the maximum speed exceeds the mean by **10 knots or more**. This applies to both increases and decreases (lulls).

## Airborne Weather Radar

### Operating Principle
The radar detects **precipitation drops** (rain, wet snow, wet hail) based on their **reflectivity**.
*   **Does not detect:** Clear Air Turbulence (CAT), clouds without precipitation, fog, or dry ice (dry hail/dry snow have low reflectivity).
*   **Display:**
    *   **Red:** High reflectivity (intense precipitation).
    *   **Yellow:** Medium precipitation.
    *   **Green:** Low reflectivity (light precipitation).
    *   **Magenta:** Often indicates turbulence (in radars with Doppler function).

### Attenuation and Shadows
*   **Attenuation:** Radar energy is absorbed or scattered by intense precipitation, preventing detection of what lies behind.
*   **Shadow:** A black area behind a red echo indicates that the signal has been fully attenuated. **Danger:** A severe storm may be hidden in the shadow.
    *   *Rule:* If there is a shadow, assume severe activity behind it. If there is no storm in front of the dark area, it could be a mountain or a lake (depending on the antenna tilt).

### Turbulence Detection
Some modern radars use the **Doppler effect** to detect the horizontal movement of rain drops, indicating possible turbulence (TURB function). Generally effective only up to 40 NM and requires the presence of precipitation ("wet turbulence").

### Hazardous Shapes
*   **Hooks, Fingers, Arcs:** Indicate severe convective activity, possible rotation (mesocyclone), and risk of **tornadoes** or severe hail.
*   **U-Shape:** Indicates strong vertical currents and severe hail.

## Satellite Imagery

Two main types of images are used to analyze weather:

| Feature | Visible (VIS) | Infrared (IR) |
| :--- | :--- | :--- |
| **Source** | Reflected sunlight. | Thermal radiation (temperature). |
| **Availability** | Day only. | 24 hours (day and night). |
| **Cloud Appearance** | White. | White (if cold/high), Grey (if low/warm). |
| **Land/Sea** | Land grey, Sea black. | Warm land dark, Cold land lighter. |
| **Main Use** | See texture and thickness. | See height of cloud tops. |

**Combined Interpretation:**
*   **Both bright:** High and thick cloud (e.g., CB, convective activity).
*   **Visible bright / IR dark:** Low cloud or fog (temperature similar to surface).
*   **Visible faint / IR bright:** High and thin cloud (e.g., Cirrostratus).

**Volcanic Ash:**
Detected by monitoring visible and infrared images. In IR, ash, as it rises and cools, appears white (similar to cold clouds).

## Other Instruments and Reports

*   **Radiosonde:** An instrument carried by a balloon that measures **pressure, temperature, and relative humidity** as it ascends.
*   **Thermometer:** Measures air temperature. It is placed in a **Stevenson Screen** (at 1.25 - 2 m above ground) to protect it from direct solar radiation and precipitation, allowing air circulation.
*   **Air-reports:**
    *   **Routine:** Position and basic meteorological information.
    *   **Special (ARS):** Issued when hazardous conditions are encountered (e.g., severe turbulence, severe icing, mountain waves, thunderstorms, volcanic ash).
