---
title: Radio Navigation: GNSS Augmentation Systems
description: Understand ground, satellite, and aircraft based augmentation for GNSS accuracy.
keywords:
  - gnss augmentation
  - gbas sbas abaas
  - navigation integrity
---

# Radio Navigation: GNSS Augmentation Systems

Augmentation systems aim to improve the accuracy, integrity, availability, and continuity of the basic GNSS signal to meet civil aviation requirements, especially in critical phases such as approach.

## ABAS (Aircraft-Based Augmentation System)
Aircraft-based systems that use satellite redundancy or onboard sensors.

### RAIM (Receiver Autonomous Integrity Monitoring)
Technique where the GNSS receiver uses additional satellites to verify the consistency of the navigation solution.
*   **Fault Detection (FD):** Requires minimum **5 satellites**. Detects a failure but does not identify the satellite.
*   **Fault Detection and Exclusion (FDE):** Requires minimum **6 satellites**. Detects and excludes the faulty satellite.
*   Using barometric aiding (Baro-aiding) can reduce the number of required satellites by 1.

### AAIM (Aircraft Autonomous Integrity Monitoring)
Uses onboard sensors to verify the GNSS position.
*   **Typical Sensors:** Barometric altimeter, IRS (Inertial Reference System).
*   Allows maintaining integrity even with fewer visible satellites.

## SBAS (Satellite-Based Augmentation System)
Wide-area (continental) coverage systems using geostationary satellites.
*   **Examples:** **EGNOS** (Europe), **WAAS** (USA), MSAS (Japan), GAGAN (India).

### Operation
1.  A network of ground reference stations (with known positions) monitors GNSS signals.
2.  They calculate corrections (clock, ephemeris, ionosphere) and integrity data.
3.  They send this data to a master station, which uploads it to geostationary satellites.
4.  The geostationary satellites retransmit the signal to users on the same **L1** frequency as GPS.

### Benefits
*   **Integrity:** Alerts of failures within **6 seconds** (compared to hours in standard GPS).
*   **Accuracy:** Improves horizontal and vertical accuracy.
*   **Availability:** SBAS satellites act as additional GNSS satellites (ranging source).
*   **Operations:** Enables **LPV** (Localiser Performance with Vertical Guidance) approaches with minimums down to 200 ft (equivalent to CAT I).

## GBAS (Ground-Based Augmentation System)
Local coverage (airport) systems using a ground station. Also known as **LAAS** (Local Area Augmentation System).

### Operation
1.  Reference receivers at the airport (precise known position) measure GNSS satellite errors.
2.  The ground station calculates differential corrections.
3.  It transmits corrections, integrity data, and approach path data to aircraft via a **VHF (VDB - VHF Data Broadcast)** data link.

### Characteristics
*   **Coverage:** Approximately **20-30 km** (or 20 NM) from the station.
    *   +/- 35° up to 15 NM.
    *   +/- 10° between 15 and 20 NM.
*   **GLS (GBAS Landing System):** Enables precision approaches (CAT I, II, III) using GNSS.
*   **FAS Data Block:** Final Approach Segment Data Block that defines the geometric path of the approach (similar to ILS but virtual).
*   **Channel:** Selected via a 5-digit channel code.

### Key Differences
*   **SBAS:** Wide coverage (continental), satellite corrections, LPV approaches (APV).
*   **GBAS:** Local coverage (airport), VHF corrections, GLS approaches (Precision).
