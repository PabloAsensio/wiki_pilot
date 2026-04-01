---
title: Radio Navigation: Ground Radar
description: Learn primary and secondary ground radar use in air traffic surveillance.
keywords:
  - ground radar
  - air traffic surveillance
  - radar navigation
---

# Radio Navigation: Ground Radar

## Primary Surveillance Radar (PSR)

The **PSR (Primary Surveillance Radar)** is the most basic type of radar used on the ground for air traffic control.

### Operating Principle
It works by emitting pulses of electromagnetic energy from a rotating antenna and detecting the echoes reflected by objects (aircraft, clouds, terrain).

*   **Information Provided:** It provides only **2D position**:
    *   **Range:** Calculated by measuring the **time** it takes for the pulse to travel back and forth (based on the speed of light). It is a slant range.
    *   **Bearing:** Determined by the **azimuth** of the antenna at the moment the echo is received.
*   **Limitations:**
    *   Does not provide altitude.
    *   Does not identify the aircraft (no codes or registration).
    *   Can be affected by weather (rain, clouds) and terrain (clutter).

## Surface Movement Radar (SMR/ASMR)

The **ASMR (Airport Surface Movement Radar)** or **ASMI (Airfield Surface Movement Indicator)** is a short-range radar designed to monitor traffic on the airport ground.

*   **Function:** To provide controllers with a clear and detailed picture of all aircraft and vehicles on runways and taxiways, especially useful in low visibility conditions.
*   **Characteristics:**
    *   **High Definition:** Requires very high resolution to distinguish close objects.
    *   **High Frequency:** Operates at very high frequencies (SHF or EHF bands) to achieve the necessary resolution with reasonably sized antennas.
    *   **Size Detection:** In older analog systems, high definition allowed estimating aircraft size by the size of the echo on the screen.
*   **Modern Systems:** Integrated with transponder data (multilateration) to tag targets with identification, improving safety and efficiency (A-SMGCS).

## ATS Information Requirements

To provide ATS surveillance service, the minimum required information is:
1.  **Position** (provided by PSR or SSR).
2.  **Map Information** (airspace structure reference).

If SSR (Secondary Radar) is available, it adds:
*   **Mode A:** 2D Position + Identification Code (Squawk).
*   **Mode C:** 3D Position (adds pressure altitude).
*   **Mode S:** Additional data and selective data link.
