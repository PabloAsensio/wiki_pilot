---
title: "Information for flight planning"
description: "Meteorological information required for pre-flight planning: TAF, AIRMET, SIGMET, and pre-flight briefings."
keywords: ["flight planning meteorology", "TAF AIRMET SIGMET aviation", "pre flight weather briefing ATPL", "pilot weather flight planning"]
---

## Aerodrome Meteorological Reports (METAR and SPECI)

![METAR and TAF Processing Equipment](https://upload.wikimedia.org/wikipedia/commons/9/91/Metar_2010.jpg)

### METAR (Meteorological Aerodrome Report)
It is a routine report of meteorological conditions observed at an aerodrome. It is generally issued every 30 or 60 minutes.

### SPECI (Special Report)
It is a special report issued when significant changes (deterioration or improvement) occur in meteorological conditions between routine reports (e.g., change in wind, visibility, low clouds, or onset/cessation of thunderstorms).

### Basic Decoding
Example: `EGKK 191050Z 09002KT 0200 R08R/0350 VV001 M03/M02 Q1008`

*   **Identifier:** `EGKK` (Gatwick).
*   **Date/Time:** `191050Z` (Day 19 at 10:50 UTC).
*   **Wind:** `09002KT` (090 degrees, 2 knots).
*   **Visibility:** `0200` (200 metres).
*   **RVR:** `R08R/0350` (Runway 08 Right, 350 metres).
    *   Trends: `U` (Increasing), `D` (Decreasing), `N` (No change).
    *   Prefixes: `P` (More than, e.g., P1500), `M` (Less than, e.g., M0050).
*   **Clouds/Vertical Visibility:** `VV001` (Vertical visibility 100 feet - sky obscured).
    *   `FEW`, `SCT`, `BKN`, `OVC`.
    *   `NSC`: No Significant Clouds (no clouds of operational significance, but not CAVOK).
    *   `CAVOK`: Visibility $\ge$ 10 km, no clouds below 5000 ft or MSA, no significant phenomena (CB/TCU).
*   **Temperature/Dew Point:** `M03/M02` (-3°C / -2°C).
*   **QNH:** `Q1008` (1008 hPa).

### Trend Forecast
Added at the end of the METAR and is valid for **2 hours**.
*   **NOSIG:** No significant changes forecast.
*   **BECMG:** Gradual or regular change to new conditions.
*   **TEMPO:** Temporary fluctuations (less than 1 hour each time, and less than half the total period).

## Aerodrome Forecasts (TAF)

The TAF (Terminal Aerodrome Forecast) describes the expected meteorological conditions at an aerodrome during a specific period (usually 9, 24, or 30 hours).

### Change Indicators
*   **BECMG (Becoming):** Permanent change expected within the indicated time period.
*   **TEMPO (Temporary):** Temporary conditions lasting less than one hour.
*   **PROB30 / PROB40:** 30% or 40% probability of a phenomenon occurring (usually used with TEMPO).

## En-route Information (SIGMET and AIRMET)

### SIGMET
Information concerning en-route weather phenomena which may affect the safety of **all aircraft**.
*   **Validity:** Maximum 4 hours (6 hours for Volcanic Ash and Tropical Cyclones).
*   **Phenomena:**
    *   Thunderstorms (TS) (Obscured, Embedded, Frequent, Squall line).
    *   Severe Turbulence (SEV TURB).
    *   Severe Icing (SEV ICE).
    *   Severe Mountain Waves (SEV MTW).
    *   Heavy dust/sand storms.
    *   Volcanic Ash (VA).
    *   Tropical Cyclone (TC).

### AIRMET
Similar to SIGMET but for phenomena affecting the safety of **low-level** flights (generally below FL100 or FL150 in mountainous areas) and which were not included in the area forecast.

## Warnings and Alerts

### Aerodrome Warnings
Concise information on conditions that could adversely affect aircraft **on the ground** (including parked aircraft) and facilities.
*   Examples: Strong wind, hail, snow, frost, ground icing.

### Wind Shear Alert
Warnings about the observed or expected existence of wind shear in the approach or take-off path (between runway level and 500 m / 1600 ft).

### Volcanic Ash and Cyclone Advisories
Issued by **VAAC** (Volcanic Ash Advisory Centres) and **TCAC** (Tropical Cyclone Advisory Centres) to guide meteorological watch offices in issuing SIGMETs.

## Flight Information Services

### ATIS (Automatic Terminal Information Service)
Continuous broadcast (voice or D-ATIS data link) of routine information for arriving or departing aircraft. Contains operational (runway in use) and meteorological (wind, visibility, clouds, temp, QNH) information.

### VOLMET
Broadcast of meteorological information (METAR, SPECI, TAF, SIGMET) for aircraft **in flight**.

## Aircraft Reports (AIREP)

*   **Routine AIREP:** Position and basic meteorological information.
*   **Special AIREP (ARS):** Must be issued when hazardous unforecast or significant conditions are encountered, such as:
    *   Moderate or severe turbulence.
    *   Moderate or severe icing.
    *   Severe mountain waves.
    *   Thunderstorms with or without hail.
    *   Volcanic ash cloud.
