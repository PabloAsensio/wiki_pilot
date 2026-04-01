---
title: "Ground Direction Finding (DF) in Aviation"
description: "Understand ground direction finding principles and applications in air navigation."
keywords:
    - "ground direction finding"
    - "df navigation"
    - "radio aids"
---

# Ground Direction Finding (DF) in Aviation

**VDF** (VHF Direction Finding) is a system that allows a ground station to determine the direction from which a VHF radio signal transmitted by an aircraft is coming.

## Operating Principles

*   **Aircraft Equipment:** Only requires a **standard VHF radio**. No additional equipment is needed.
*   **Ground Equipment:** Uses a special directional antenna, commonly an **Adcock Antenna** (an array of vertical dipoles). The system measures the phase difference of the incoming signal at the different dipoles to calculate the direction.
*   **Frequency:** Operates in the VHF band (118-137 MHz), the same used for voice communications.
*   **Range:** Using VHF waves, the range is **Line-of-Sight**. It depends on the height of the aircraft and the station, as well as transmission power and terrain obstacles.

## Provided Information

The controller or ground station operator can provide the pilot with the following bearings:

*   **QDM:** Magnetic Heading **to** the station (Magnetic Heading to steer). It is the heading the pilot must fly to go directly to the station (in zero wind).
*   **QDR:** Magnetic Bearing **from** the station (Magnetic Bearing from). It is the magnetic radial the aircraft is on relative to the station.
*   **QUJ:** True Bearing **to** the station.
*   **QTE:** True Bearing **from** the station.

**Important Note:** Bearings provided by VDF **do not correct for wind drift**. The pilot is responsible for calculating and applying the necessary drift correction.

## Accuracy and Classification

ICAO classifies VDF stations according to their accuracy:

| Class | Accuracy |
| :--- | :--- |
| **Class A** | $\pm 2^\circ$ |
| **Class B** | $\pm 5^\circ$ |
| **Class C** | $\pm 10^\circ$ |
| **Class D** | Worse than Class C |

Accuracy can be affected by reflections from buildings, uneven terrain (site errors), and multipath propagation.

## Position Determination

*   **Triangulation:** Using two or more geographically separated VDF stations, an aircraft's position can be determined by finding the point where the lines of position (QTE) intersect.
*   **Auto-triangulation:** Modern systems, such as those used on emergency frequencies (121.5 MHz), can automatically triangulate the position of a transmitting aircraft and display it instantly on the controller's screen.
