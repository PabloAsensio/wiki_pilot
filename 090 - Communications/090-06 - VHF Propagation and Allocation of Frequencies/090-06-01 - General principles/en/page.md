---
title: "VHF Propagation and Frequency Allocation: General Principles"
description: "Radio spectrum basics, VHF airband allocation, and operational communication/navigation frequency use."
keywords: ["vhf propagation", "frequency allocation", "airband", "nav frequencies", "com frequencies", "icao communications"]
---

# VHF Propagation and Frequency Allocation: General Principles

## Frequency Bands
The radio spectrum is divided into specific bands based on frequency. Aviation uses several of these:

| Band | Name | Frequency Range | Aviation Use |
| :--- | :--- | :--- | :--- |
| **VLF** | Very Low Frequency | 3 – 30 kHz | Long range nav |
| **LF** | Low Frequency | 30 – 300 kHz | **NDB** |
| **MF** | Medium Frequency | 300 – 3,000 kHz | **NDB**, Commercial AM Radio |
| **HF** | High Frequency | 3 – 30 MHz | **Long Range Comms** (Oceanic) |
| **VHF** | **Very High Frequency** | **30 – 300 MHz** | **Standard Comms & Nav** |
| **UHF** | Ultra High Frequency | 300 – 3,000 MHz | Military, ILS Glideslope, DME |
| **SHF** | Super High Frequency | 3 – 30 GHz | Radar, Radalt |
| **EHF** | Extremely High Frequency | 30 – 300 GHz | - |

## The Airband (VHF)
The "Airband" is the VHF spectrum allocated for civil aviation, ranging from **108.000 MHz to 137.000 MHz**.

### Allocation
1.  **Navigation (NAV)**: **108.000 – 117.975 MHz**.
    *   Used for: **VOR**, **ILS** (Localizer), **ATIS** (sometimes on VOR voice).
    *   *Note*: Frequencies like 116.30 MHz are NAV frequencies and cannot be selected on a standard COM radio for voice transmission.
2.  **Communication (COM)**: **118.000 – 136.975 MHz**.
    *   Used for: **ATC**, **Air-to-Air**, **Operations**.
    *   *Note*: **121.500 MHz** is the International Air Distress frequency.

### Channel Spacing (8.33 kHz)
Traditionally, channels were separated by **25 kHz**. To combat frequency congestion in Europe, channels were subdivided into **8.33 kHz** spacing.
*   This creates 2 extra channels for every 25 kHz block.
*   Mandatory carriage of 8.33 kHz capable radios is required in the ICAO European region (e.g., above FL195).

## VHF Propagation Characteristics
VHF radio waves propagate as **Space Waves** (Direct Waves).

### Line of Sight
*   Transmission is "quasi-optical" or **Line of Sight**.
*   The waves travel in a straight line and do **not** bounce off the ionosphere (unlike HF).
*   **Range** is limited by the curvature of the Earth and terrain/obstacles.

### Range Calculation
The theoretical maximum range depends on the height of the transmitter ($h_{TX}$) and the receiver ($h_{RX}$).
$$ Range (NM) \approx 1.23 \times (\sqrt{h_{TX}} + \sqrt{h_{RX}}) $$
*(Where heights are in feet)*.
*   **Conclusion**: Climbing to a higher altitude significantly increases VHF range and reception.

### Factors Affecting Reception
1.  **Altitude**: Higher is better.
2.  **Obstacles**: Mountains/terrain block signals (Shadowing).
3.  **Atmospheric Ducting**: Under certain conditions (Temperature Inversion), VHF signals can be trapped in a duct and travel **further** than the normal line of sight.
4.  **Attenuation**: Signal strength weakens with distance due to atmospheric absorption.
