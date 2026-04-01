---
title: "Aerodrome Weather Information and ATIS"
description: "Wind reporting conventions, ATIS structure, and aerodrome weather information for operational communication."
keywords: ["aerodrome weather", "atis", "volmet", "metar", "taf", "true north", "magnetic north"]
---

# Aerodrome Weather Information and ATIS

## Wind Reporting Rules
A crucial distinction exists in how wind direction is reported in aviation:

*   **Written Information (Maps, METAR, TAF)**: Wind direction is referenced to **TRUE North**.
    *   *Rule of thumb*: "If you **read** it, it's **True**."
*   **Spoken Information (ATC, ATIS)**: Wind direction is referenced to **MAGNETIC North**.
    *   *Rule of thumb*: "If you **hear** it, it's **Magnetic**."
    *   *Reason*: Pilots use magnetic compasses/headings for takeoff and landing, so ATC converts the wind to magnetic to align with the runway, which is also numbered magnetically.

## ATIS (Automatic Terminal Information Service)
ATIS is the automatic provision of current, routine information to arriving and departing aircraft.

*   **Voice-ATIS**: Continuous voice broadcast, usually on a discrete **VHF** frequency (or VOR voice channel).
*   **D-ATIS**: Provision of ATIS via data link (e.g., ACARS).

### Content and Codes
ATIS messages follow a specific structure (Aerodrome, Designator, Time, Runway, Weather, etc.).
*   **Example Decoding**: "TWY E3 Southbound CLSD due WIP" $\rightarrow$ Taxiway E3 southbound closed due to Work In Progress.

## VOLMET
**VOLMET** provides meteorological information (METAR, SPECI, TAF, SIGMET) for multiple aerodromes to aircraft in flight.
*   **VHF VOLMET**: Normally continuous broadcasts.
*   **HF VOLMET**: Scheduled broadcasts (used for long-range/oceanic coverage).
*   **D-VOLMET**: Provision via data link.

## Meteorological Codes (METAR/SPECI)
### CAVOK (Ceiling And Visibility OK)
Used when distinct conditions occur simultaneously:
*   **Visibility**: 10 km or more.
*   **Clouds**: No clouds of operational significance (No clouds below 5000 ft or MSA, no CB/TCU).
*   **Weather**: No significant weather phenomena.

### RVR (Runway Visual Range)
Format: `R(Runway)/(Value)(Tendency)`
*   **P**: Plus (Greater than). E.g., `P2000` > 2000m.
*   **M**: Minus (Less than). E.g., `M0150` < 150m.
*   **U**: Upward (Increasing) tendency.
*   **D**: Downward (Decreasing) tendency.
*   **N**: No distinct tendency.
*   **V**: Variable (e.g., `1100V1500`).

### Other Definitions
*   **Ceiling**: The height of the base of the lowest cloud layer covering **more than half the sky** (BKN or OVC).
*   **Wind Shear (WS)**: Reported if affecting takeoff/approach paths options (e.g., `WS TKOF RWY20` or `WS ALL RWY`).

## Air-Reports (AIREP)
### Special Air-Reports (AIREP SPECIAL)
Pilots **must** make a special air-report whenever the following conditions are encountered:
1.  **Moderate or Severe Turbulence**.
2.  **Moderate or Severe Icing**.
3.  **Severe Mountain Wave**.
4.  **Thunderstorms** (with/without hail, obscured, embedded, widespread, or in squall lines).
5.  **Heavy Duststorm/Sandstorm**.
6.  **Volcanic Ash** or Pre-eruption activity.
7.  **Braking Action**: If the braking action encountered is **different** (better or worse) than reported.

### Routine Air-Reports
*   **Link with Data Link (ADS-C)**: Aircraft equipped with ADS-C are **exempt** from making verbal routine meteorological reports (automation handles it).
*   **Reporting Intervals (if required)**:
    *   **En-route**: Every 15 minutes.
    *   **Climb-out**: Every 30 seconds for the first 10 minutes.
