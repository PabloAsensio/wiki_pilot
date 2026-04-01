---
title: Radio Navigation: NDB and ADF in Aviation
description: Learn how non directional beacon systems and ADF work in aviation navigation and their practical limitations.
keywords:
    - adf ndb
    - ndb in aviation
    - non directional beacon
    - automatic direction finding
    - radio navigation
---

# Radio Navigation: NDB and ADF in Aviation

The **NDB** is a ground-based radio aid that transmits an omnidirectional signal. The **ADF** is the airborne instrument that receives this signal and determines the direction to the station.

## Operating Principles

*   **Frequencies:** Operates in the Low Frequency (LF) and Medium Frequency (MF) bands, typically between **190 kHz and 1750 kHz**.
*   **Modulation:**
    *   **N0N:** Unmodulated carrier (basic signal).
    *   **A1A:** Morse code identification by carrier interruption (requires activating the **BFO** - Beat Frequency Oscillator on the ADF to be audible).
    *   **A2A:** Amplitude modulated identification (directly audible, does not require BFO).
*   **ADF Antennas:** Uses two antennas:
    *   **Loop Antenna:** Determines direction but with 180° ambiguity.
    *   **Sense Antenna:** Resolves the ambiguity to indicate if the station is in front or behind.

## Instruments and Indications

![ADF Indicator](https://upload.wikimedia.org/wikipedia/commons/9/9a/Automatic_direction_finder_with_fixed_azimuth_and_magnetic_compass.png)

*   **RBI (Relative Bearing Indicator):** Displays the **Relative Bearing (RB)**, which is the angle between the aircraft's nose and the station. The card is fixed (North is always up).
    *   Formula: $QDM = Magnetic Heading (MH) + Relative Bearing (RB)$.
*   **RMI (Radio Magnetic Indicator):** Combines a directional gyro with the ADF needle. The card rotates automatically to show the aircraft's magnetic heading at the top.
    *   **Needle Head:** Indicates **QDM** (Magnetic Heading TO the station).
    *   **Needle Tail:** Indicates **QDR** (Magnetic Bearing FROM the station).
*   **Accuracy:** Typical ADF accuracy during the day is **$\pm 5^\circ$**.

## ADF System Errors

The ADF is susceptible to numerous errors due to LF/MF wave propagation:

1.  **Night Effect:** At night, the ionosphere's D layer disappears, allowing sky waves to interfere with ground waves. This causes fading and needle oscillation. It is worse at sunrise and sunset.
2.  **Mountain Effect:** **Diffraction** and reflection of waves in mountainous terrain cause erroneous readings.
3.  **Coastal Refraction:** Waves speed up over water, bending towards the coast when crossing the coastline at an oblique angle.
4.  **Thunderstorm Effect:** Lightning (static discharges) emits powerful signals in LF/MF. The ADF needle may momentarily point towards the center of the storm (Cumulonimbus).
5.  **Quadrantal Error:** Deviation caused by signal refraction on the aircraft's metal fuselage.
6.  **Dip Error:** When turning, the loop antenna tilts, causing reading errors.

## Operational Use

*   **Homing:** Flying keeping the ADF needle on the nose (RB 0°). If there is a crosswind, the aircraft will fly a curved path.
*   **Tracking:** Flying a heading corrected for wind to maintain a straight path to or from the station (maintaining a constant QDM or QDR).
*   **NDB Approaches:** Considered non-precision approaches. The pilot must remain within **$\pm 5^\circ$** of the published approach course to be considered "established".
*   **Failure:** Unlike VOR or ILS, the NDB **has no failure flag**. The pilot must continuously monitor the Morse code identification; if it ceases, the station has failed.

## Locator Beacons

These are **low power** NDBs (10-25 NM range) used in terminal approaches, often located at the ILS Outer Marker (forming a LOM - Locator Outer Marker).
