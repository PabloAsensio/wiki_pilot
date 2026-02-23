GNSS is a general term encompassing satellite navigation systems that provide autonomous geospatial positioning with global coverage.

## Main Systems
There are four main recognized GNSS systems:
*   **NAVSTAR GPS** (USA): Operational.
*   **GLONASS** (Russia): Operational.
*   **Galileo** (Europe): Operational.
*   **BeiDou** (China): Operational.

### Interoperability
*   **System Level:** GPS and GLONASS are interoperable at the system level. They have different frequencies and reference frames (WGS-84 vs PZ-90), so their signals are not directly compatible, but the receiver can process both solutions independently and combine them.
*   **Signal Level:** Galileo and GPS have certain frequencies that are interoperable at the signal level.

## NAVSTAR GPS

![GPS Satellite Constellation](https://upload.wikimedia.org/wikipedia/commons/d/d3/GPS_satellite_constellation.jpg)

The GPS system consists of three segments:

1.  **Space Segment:**
    *   Nominal constellation of **24 satellites** (technical minimum).
    *   Orbit in **6 orbital planes** at an altitude of approximately **20,200 km**.
    *   Orbital period of 12 hours.
2.  **Control Segment:**
    *   Ground monitoring and control stations.
    *   Maintain constellation health, correct atomic clocks, and update ephemerides.
3.  **User Segment:**
    *   GPS receivers (aircraft, mobile devices, etc.).

### Operating Principle

![GPS Trilateration](https://upload.wikimedia.org/wikipedia/commons/f/ff/Trilateration_with_Three_Circles.png)

The receiver calculates its position via **trilateration** by measuring the time it takes for the signal to travel from the satellite to the receiver (Pseudorange).
*   **3 Satellites:** 2D Position (Latitude, Longitude) + Time (if altitude is known).
*   **4 Satellites:** 3D Position (Latitude, Longitude, Altitude) + Time.

### Frequencies and Services
Satellites transmit in the UHF band (L-Band):
*   **L1 (1575.42 MHz):**
    *   Carries the **C/A** (Coarse Acquisition) code and the **P** (Precision) code.
    *   Provides the **SPS** (Standard Positioning Service) for civil use.
*   **L2 (1227.60 MHz):**
    *   Carries only the **P** code.
    *   Together with L1, provides the **PPS** (Precise Positioning Service) for authorized users (military).
    *   Using two frequencies allows correcting ionospheric errors.

### Navigation Message
Each satellite transmits:
*   **Almanac:** Approximate orbital data for the *entire* constellation.
*   **Ephemeris:** Precise orbital data for the *specific* satellite.
*   **Clock Correction:** Status of the satellite's atomic clock.
*   **Ionospheric Model:** To correct delays in single-frequency receivers.

## System Errors

### Error Sources
1.  **Ionospheric Delay:** This is the **most significant error**. The ionosphere slows down the signal. It is mitigated with mathematical models or dual-frequency receivers.
2.  **Satellite Clock Errors:** Although they use atomic clocks, small drifts exist.
3.  **Ephemeris Errors:** Difference between the actual and expected position of the satellite.
4.  **Multipath:** Reflection of the signal off surfaces (buildings, terrain) before reaching the antenna.
5.  **Receiver Noise:** Internal equipment errors.

### Dilution of Precision (DOP)
Satellite geometry affects the accuracy of the calculated position.
*   **GDOP (Geometric Dilution of Precision):** Measure of geometry quality.
*   **PDOP (Position Dilution of Precision):** Dilution in 3D position.
*   **Low Value = Better Accuracy.**
*   **Ideal Geometry:** One satellite directly overhead (zenith) and three on the horizon separated by 120°.
*   **Poor Geometry:** Satellites clustered very close to each other.

**Total Error = UERE (User Equivalent Range Error) × GDOP**

## Integrity (RAIM)
**RAIM (Receiver Autonomous Integrity Monitoring)** is a technique where the receiver uses "extra" satellites to verify the integrity of the navigation solution.
*   **Fault Detection (FD):** Requires minimum **5 satellites**. Detects if a satellite is failing but cannot identify which one.
*   **Fault Detection and Exclusion (FDE):** Requires minimum **6 satellites**. Detects and excludes the faulty satellite, allowing navigation to continue.
*   If barometric aiding (pressure altitude) is available, one less satellite is required (4 for FD, 5 for FDE).
