## World Area Forecast Centres (WAFC)

**WAFCs (World Area Forecast Centres)** are meteorological centres designated to prepare and issue significant and upper-air forecasts in digital form on a global basis.
*   **Responsibilities:** Prepare gridded forecasts of:
    *   Upper wind and temperature.
    *   Humidity.
    *   Geopotential altitude.
    *   Tropopause (level and temperature).
    *   Maximum wind (direction, speed, and level).
    *   Cumulonimbus clouds (CB).
    *   Icing and Turbulence.

## Tropical Cyclone Advisory (TC Advisory)

Message issued by a TCAC (Tropical Cyclone Advisory Centre) with information on the position, movement, and intensity of a tropical cyclone.

**Code Structure:**
1.  **TC ADVISORY:** Message identification.
2.  **DTG:** Date and time of issue (YYYYMMDD/HHMMZ).
3.  **TCAC:** Name of the centre (e.g., MIAMI).
4.  **TC:** Name of the cyclone (e.g., DORIAN).
5.  **NR:** Advisory number (e.g., 2013/4).
6.  **OBS PSN:** Observed position of the centre (Lat/Long).
7.  **MOV:** Direction and speed of movement (e.g., NW 18 KT).
    *   `SLW` (Slow): < 3 kt.
    *   `STNR` (Stationary): < 1 kt.
8.  **INTST CHANGE:** Intensity change (e.g., `INTSF` = Intensifying, `WKN` = Weakening, `NC` = No Change).
9.  **C:** Atmospheric pressure at the centre (hPa).
10. **MAX WIND:** Maximum surface wind (10 min average).
11. **FCST PSN / MAX WIND:** Forecasts at +6, +12, +18, +24 hours.
12. **NXT MSG EXP:** Date/time of the next message.

## Flight Information Services (ATIS and D-ATIS)

*   **ATIS (Automatic Terminal Information Service):** Continuous broadcast of routine information for arriving and departing aircraft.
*   **D-ATIS (Data Link ATIS):** Digital version of ATIS transmitted via data link (ACARS).
    *   **Advantage:** Allows pilots to obtain meteorological and operational information for the destination airport well before being within VHF radio range (e.g., via SATCOM).

## Meteorological Phenomena Abbreviations

It is crucial to know the ICAO Annex 3 abbreviations to interpret METAR, TAF, and SIGMET:

*   **Precipitation:**
    *   **PL:** Ice Pellets.
    *   **GR:** Hail ($\ge$ 5mm).
    *   **GS:** Small Hail / Snow Pellets (< 5mm).
    *   **SG:** Snow Grains.
    *   **IC:** Ice Crystals (not reported as precipitation in METAR, but as obscuration if visibility < 5000m).
*   **Other Phenomena:**
    *   **SQ:** Squall (Sudden increase in wind of at least 16 kt, reaching 22 kt or more, lasting at least 1 minute).
    *   **PO:** Dust/Sand Whirls.
    *   **FC:** Funnel Cloud (Tornado or Waterspout).
    *   **SS:** Sandstorm.
    *   **DS:** Duststorm.

## Runway State Group

In the METAR, information about the state of the runway can be added if there are contaminants (snow, ice, etc.).
Format: **RDrDr/ErCrereRBrBr** (e.g., `88/425035`)

*   **DrDr:** Runway designator (`88` = All runways).
*   **Er:** Type of deposit (`4` = Dry snow).
*   **Cr:** Extent (`2` = 11% to 25%).
*   **ereR:** Depth (`50` = 50 mm).
*   **BrBr:** Friction coefficient / Braking action (`35` = 0.35 / Medium-Good).

## Aerodrome Warnings and Wind Shear

*   **Aerodrome Warnings:** Warn of hazardous conditions on the ground (strong wind, frost, etc.).
*   **Wind Shear Alerts:** Warn of wind shear on approach or take-off.
    *   Can be based on aircraft reports (e.g., "Microburst reported by A320 on final approach").

## SIGMET

Information issued by a **Meteorological Watch Office (MWO)** concerning the occurrence or expected occurrence of en-route weather phenomena which may affect the safety of aircraft operations (e.g., Severe Turbulence, Severe Icing, Volcanic Ash, etc.).
