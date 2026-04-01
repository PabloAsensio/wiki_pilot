---
title: "Performance Based Navigation Operations"
description: "Review PBN operational procedures, constraints, and implementation in flight ops."
keywords:
    - "pbn operations"
    - "rnp operations"
    - "navigation operations"
---

# Performance Based Navigation Operations

PBN operations are based on the navigation system's ability to maintain a defined accuracy and, in the case of RNP, to monitor and alert on performance.

## Navigation System Errors
The total system accuracy is defined as **TSE (Total System Error)**. TSE is the geometric sum of three independent error components:

1.  **PDE (Path Definition Error):**
    *   Occurs when the path defined in the RNAV system does not correspond to the desired path over the ground.
    *   Considered **negligible** if the navigation database is intact and up to date (valid AIRAC cycle).
2.  **FTE (Flight Technical Error):**
    *   Related to the crew's or autopilot's ability to follow the defined path.
    *   Includes CDI centering errors.
    *   Managed through crew procedures or the use of the autopilot.
3.  **NSE (Navigation System Error):**
    *   The difference between the aircraft's estimated position and its actual position.
    *   Depends on the accuracy of the sensors (GNSS, DME/DME, IRS).

**TSE = PDE + FTE + NSE**

## Monitoring and Alerting (RNP)
In RNP specifications, the system must monitor performance:
*   **ANP (Actual Navigation Performance)** or **EPE (Estimated Position Error):** A statistical estimate of the current position error (TSE or NSE depending on context, but functionally represents position uncertainty).
*   **RNP (Required Navigation Performance):** The allowed error limit for the operation (e.g., 1.0 NM).
*   **Alert:** If **ANP > RNP**, the system alerts the crew (e.g., "NAV ACCUR DOWNGRAD"). This indicates that the position uncertainty exceeds the allowed limit.

## Operational Procedures
*   **Database:** Must be updated to the current **AIRAC** cycle (every 28 days).
*   **Deviation:** During an approach, if the deviation exceeds **half-scale** deflection, a missed approach must be initiated.
*   **Loss of Integrity/Accuracy:** If an integrity alert (e.g., RAIM, LOI) is received or if ANP exceeds RNP before the FAF, the approach must be discontinued.
*   **Communication Failure:** Not an immediate cause for a missed approach in an RNP approach (standard communication failure procedures are followed).
