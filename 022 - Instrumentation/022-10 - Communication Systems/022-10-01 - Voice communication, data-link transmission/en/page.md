---
layout: default
title: "Voice Communication and Data-Link Transmission: ACARS, CPDLC, and D-ATIS"
description: "Study aviation communication architecture across voice and datalink systems, including ACARS, CPDLC, D-ATIS, DCL, and VHF/HF/SATCOM media selection."
keywords:
    - "cpdlc"
    - "acars"
    - "flight level"
    - "minimum speed"
parent: "022-10 - Communication Systems"
grand_parent: "022 - Instrumentation"
nav_order: 1
---

# Voice Communication and Data-Link Transmission: ACARS, CPDLC, and D-ATIS

## ACARS (Aircraft Communication Addressing and Reporting System)

**ACARS** is a digital datalink system for transmitting short messages between aircraft and ground stations. Developed by **ARINC** in the late 1970s, it remains the industry standard.

- **Purpose**:
    - **AOC (Airline Operational Control)**: Company messages (schedules, passenger data, maintenance tech logs).
    - **ATC (Air Traffic Control)**: Clearances, requests, weather.
- **Onboard Management**: The **CMU (Communication Management Unit)** manages the routing of messages. It connects to the MCDU (interface), VHF, HF, and SATCOM radios.
- **Terminology**:
    - **Uplink**: Message from Ground $\rightarrow$ Aircraft.
    - **Downlink**: Message from Aircraft $\rightarrow$ Ground.

## Transmission Media

ACARS and other datalink systems use various radio frequencies depending on availability and location.

1.  **VHF (Very High Frequency)**:
    - **Properties**: Line-of-sight operation. Terrestrial range limited by curvature of Earth.
    - **Speed/Quality**: Good quality, moderate speed. Standard for continental/domestic operations.
2.  **SATCOM (Satellite Communication)**:
    - **Properties**: Uses UHF band. Global coverage (except sometimes Polar). **No line-of-sight limitation** with ground stations.
    - **Speed/Quality**: **Highest data rate**, immune to ionospheric interference. High signal quality.
3.  **HF (High Frequency)**:
    - **Properties**: Long range (Oceanic/Remote) due to ionospheric reflection ("skywave").
    - **Speed/Quality**: **Lowest data rate**, poor quality due to static and interference. Used only when VHF/SATCOM are unavailable (e.g., polar regions without Iridium satcom).

## Applications

### CPDLC (Controller-Pilot Data Link Communications)
A text-based method for pilots and controllers to exchange messages (Clearances, Requests, Reports).
- **Benefits**: Reduces frequency congestion, eliminates "hearback/readback" errors, allows complex instructions to be reviewed.
- **Examples**: Oceanic Clearances, Route modifications, Frequency changes.

### D-ATIS (Digital ATIS)
- Receives the ATIS (Automatic Terminal Information Service) text message via datalink.
- Displayed on the MCDU or printed. Eliminates the need to listen and transcribe the audio broadcast.

### DCL (Departure Clearance)
- Obtaining the pre-departure clearance via datalink before engine start.
- Improves efficiency and reduces ramp congestion/workload.
