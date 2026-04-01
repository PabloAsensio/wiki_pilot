---
title: "Radio Navigation: RNAV and RNP Requirements for RNP Approaches"
description: "Study required navigation performance, RNP approach requirements, and key RNAV/RNP specification criteria."
keywords:
    - "required navigation performance"
    - "rnp approach requirements"
    - "rnp 1 requirements"
    - "rnp 10 requirements"
    - "rnav requirements"
---

# Radio Navigation: RNAV and RNP Requirements for RNP Approaches

ICAO identifies several navigation specifications within the PBN concept, divided into RNAV and RNP families. The fundamental difference is that **RNP specifications require on-board performance monitoring and alerting**, while RNAV specifications do not.

## RNP Specifications

The ICAO PBN Manual identifies seven navigation specifications under the RNP family:

1.  **RNP 4:** For oceanic and remote continental navigation applications.
2.  **RNP 2:** For remote oceanic and continental en-route applications.
3.  **RNP 1:** For arrivals, departures, and initial, intermediate, and missed approach phases.
4.  **Advanced RNP (A-RNP):** For navigation in all phases of flight.
5.  **RNP APCH:** For navigation applications during the approach phase.
6.  **RNP AR APCH** (Authorisation Required): For navigation applications during the approach phase that require specific authorization.
7.  **RNP 0.3:** Specific for helicopter operations in various phases.

### RNP APCH (RNP Approach)

It is the main specification for GNSS approaches. It allows approaches down to 3 different minima:

*   **LNAV (Lateral Navigation):** 2D approach (non-precision). Provides lateral guidance only. Similar to a VOR/DME approach.
*   **LNAV/VNAV (Lateral/Vertical Navigation):** 3D approach (APV - Approach with Vertical Guidance). Uses **Baro-VNAV** (barometric altimetry) or SBAS for vertical guidance.
*   **LPV (Localizer Performance with Vertical guidance):** High precision 3D approach. Uses **SBAS** (such as EGNOS or WAAS) for lateral and vertical guidance. Requires a **FAS Data Block** (Final Approach Segment) that geometrically defines the path.

#### Baro-VNAV Considerations
In LNAV/VNAV approaches based on Baro-VNAV, vertical guidance depends on barometric altitude.
*   **Temperature Effect:** Altimeters are calibrated for the standard atmosphere (ISA). At temperatures **lower than standard**, the true altitude is **lower** than indicated. This can dangerously reduce obstacle clearance margins.
*   **Limitations:** Most RNP approaches have a published minimum temperature (e.g., "Uncompensated Baro-VNAV not authorized below -8°C").
*   **QNH Setting:** Having the correct QNH is critical. An incorrect QNH will shift the entire vertical path.

### RNP AR APCH (RNP Authorisation Required)
Used for complex approaches (e.g., difficult terrain, curved paths on final).
*   Requires **specific authorization** from the state for the operation, covering aircraft equipment, crew training, and operator procedures.
*   Allows RNP values less than 0.3 NM (down to RNP 0.1) and RF (Radius to Fix) legs in the final segment.

## RNAV Specifications

*   **RNAV 10 (designated as RNP 10):** For oceanic and remote areas. Requires a lateral accuracy of ±10 NM for 95% of the time. Typically requires **two independent Long Range Navigation Systems (LRNS)** (e.g., INS, IRS/FMS, or GNSS).
*   **RNAV 5:** For continental en-route phase (B-RNAV in Europe). It is the only specification that **allows manual waypoint entry** by the pilot, although database use is recommended.
*   **RNAV 1 and RNAV 2:** For en-route, arrival (STAR), and departure (SID) phases.

## Common Operational Requirements

### Navigation Database
*   **Retrieval by Name:** For **RNAV 1, RNAV 2, RNP 1, RNP 2, and RNP APCH**, procedures (SID, STAR, Approaches) must be retrieved from the on-board navigation database by their **procedure name** and must conform to the published chart.
*   **Manual Entry Ban:** Manually creating waypoints (latitude/longitude or rho/theta) is not allowed for RNAV 1/2 or RNP procedures (except RNAV 5).
*   **Modifications:** Modifying the route by inserting or deleting specific waypoints in response to ATC clearances (e.g., "Direct to") is allowed, but altering the path definition between the FAF and the MAPt on an approach is not.

### Approach Terminology (ICAO/EASA)
ICAO is transitioning from "Precision/Non-Precision" to **2D** (lateral only) and **3D** (lateral and vertical) approach operations.
*   **Type A:** Minima (MDH/DH) ≥ 250 ft.
*   **Type B:** Minima (DH) < 250 ft. (Only possible with 3D guidance).
*   An RNP APCH approach to **LPV** minima (down to 200 ft) is considered a Type B 3D operation, operationally equivalent to an ILS CAT I.
