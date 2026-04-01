---
title: "Antennas"
description: "Understand antenna types, patterns, and practical use in aircraft radio navigation."
keywords:
    - "aviation antennas"
    - "antenna radiation patterns"
    - "radio navigation"
---

# Antennas

Antennas are devices that allow the transition between a guided electric current and an electromagnetic wave in free space.

## Basic Principles

*   **Transmission:** Electric current is converted into electromagnetic waves.
*   **Reception:** Electromagnetic waves induce an electric current in the antenna.
*   **Reciprocity:** The characteristics of an antenna (gain, radiation pattern) are identical for both transmitting and receiving.

## Polarization

Polarization is defined by the orientation of the **electric field (E)** of the wave with respect to the direction of propagation.

*   **Linear:** The electric field oscillates in a single plane (Vertical or Horizontal). For optimal reception, the receiving antenna must have the same polarization as the transmitting one.
*   **Circular:** The electric field rotates as the wave advances. Used in **weather radars** to reduce rain "clutter" (echoes), as water droplets reverse the direction of rotation when reflecting the signal.
*   **Elliptical:** A general combination of the above.

## Types of Antennas

1.  **Dipole:** The most basic form. Used in VOR and VHF communications.
2.  **Loop Antenna:** Used in older **ADF** receivers. It is directional and detects the source of the signal by seeking the "null" (minimum signal).
3.  **Parabolic Antenna:** Uses a curved reflector to focus energy into a narrow beam. High directivity and gain. Used in older radars.
4.  **Slotted Planar Array:** Flat antenna with slots, used in **modern weather radars**. It is more efficient, lighter, and aerodynamic than the parabolic, producing a beam with fewer side lobes.
5.  **Helical Antenna:** Can be directional or omnidirectional. Often used for circular polarization.
6.  **Adcock Antenna:** Array of vertical dipoles used in **VDF** (VHF Direction Finding) ground stations to determine the direction of an aircraft.

## Location and Shadowing

The location of antennas on the aircraft is critical to avoid signal blocking by the aircraft's own structure (wings, fuselage, empennage).

*   **Communications and Ground Navigation Antennas (VOR, DME, ADF):** Generally located on the **bottom** of the fuselage to have line of sight with ground stations.
*   **Satellite Antennas (GNSS/GPS):** Must be located on the **top** of the fuselage to have a direct view of the sky and satellites.
*   **Glide Slope Antenna:** Generally located in the **nose** of the aircraft or behind the radome.

**Note:** During turns, the wing can block the signal between the antenna and the ground station/satellite, causing temporary signal loss.

## Weather Radar

Airborne weather radars typically operate in the **X-Band** (8-12 GHz), with a wavelength of approx. **3 cm**. They require highly directional antennas (narrow beam) to accurately locate storms.
