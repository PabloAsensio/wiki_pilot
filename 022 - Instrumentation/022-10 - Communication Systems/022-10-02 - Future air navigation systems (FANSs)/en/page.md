---
layout: default
title: "022-10-02 - Future air navigation systems (FANSs)"
parent: "022-10 - Communication Systems"
grand_parent: "022 - Instrumentation"
nav_order: 2
---

# Future Air Navigation Systems (FANS)

## Concept and Objectives

**FANS** is a system architecture developed by ICAO to improve communication, navigation, and surveillance (CNS) for air traffic management.

- **Main Objective**: To handle increased air traffic safely and efficiently, particularly in oceanic and remote areas where radar coverage and direct radio contact are limited.
- **Key Shift**: Moving from voice communication to digital **Data Link**.

## Core Applications (FANS 1/A)

FANS 1/A is the avionics package typically installed on commercial aircraft (Boeing/Airbus) to support these functions.

### 1. ATS Facility Notification (AFN)
Also known as the **"Log On"**. Before using FANS services, the aircraft must identify itself to the Air Traffic Services Unit (ATSU).
- **Process**: The pilot allows the aircraft system to send a "Log On" message (usually via the MCDU).
- **Data Transmitted**:
    - Aircraft Callsign.
    - **Data Link Capabilities** (what the plane can do).
    - Flight Plan information.
- **Result**: Establishes the electronic handshake required for CPDLC and ADS-C.

### 2. CPDLC (Controller-Pilot Data Link Communications)
A two-way data-link system allowing the exchange of text messages between the pilot and the air traffic controller.
- **Usage**: Non-urgent clearance requests, frequency changes, and reporting.
- **Advantages**:
    - **Reduced Frequency Congestion**: Frees up voice channels for critical comms.
    - **Clarity**: Eliminates accents, static, and readback/hearback errors.
    - **Efficiency**: Allows complex clearances (e.g., "Climb to reach FL350 by 1230Z") to be reviewed and printed.

### 3. ADS-C (Automatic Dependent Surveillance - Contract)
A surveillance technique where the aircraft automatically transmits position data derived from its onboard navigation systems (GPS/FMS) to the ATC center.
- **"Contract"**: The reporting rate is controlled by the ground station (ATC), not the pilot.
    - **Periodic Contract**: Send position every X minutes/seconds.
    - **Event Contract**: Send position if altitude/heading changes or a waypoint is passed.
    - **Demand Contract**: Send position immediately upon request.
- **Emergency Mode**: If a MAYDAY is triggered, the system switches to a high-rate reporting contract.

> **Note**: Do not confuse ADS-C (Point-to-Point contract with ATC via Satcom/VHF) with **ADS-B** (Broadcast to everyone via 1090MHz ES). FANS primarily uses ADS-C.
