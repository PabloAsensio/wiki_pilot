---
title: Radio Navigation: PBN Concept (ICAO Doc 9613)
description: Study the PBN concept and core framework defined in ICAO Doc 9613.
keywords:
  - pbn concept
  - icao doc 9613
  - performance based navigation
---

# Radio Navigation: PBN Concept (ICAO Doc 9613)

The PBN (Performance-Based Navigation) concept specifies that aircraft RNAV system performance requirements be defined in terms of accuracy, integrity, availability, continuity, and functionality, needed for the proposed operations in the context of a particular airspace concept.

## PBN Components
PBN is based on three main components:
1.  **NAVAID Infrastructure:** Can be ground-based (VOR, DME) or space-based (GNSS).
2.  **Navigation Specification:** Defines performance requirements (e.g., RNAV 1, RNP 4).
3.  **Navigation Application:** The use of a specification and the infrastructure for specific routes or procedures.

## Performance Factors
*   **Accuracy:** The difference between the estimated position and the actual position. Often expressed as the lateral error allowed 95% of the time (e.g., RNP 1 = 1 NM).
    *   **TSE (Total System Error):** Sum of PDE (Path Definition Error), FTE (Flight Technical Error), and NSE (Navigation System Error).
*   **Integrity:** The confidence in the correctness of the information and the ability to alert of failures within a reasonable time.
*   **Continuity:** The capability of the system to perform its function without unscheduled interruptions during the operation.
*   **Availability:** The percentage of time the system is usable.
*   **Functionality:** The required functions of the system (e.g., RF legs, Baro-VNAV).

## PBN Scope
*   **Oceanic, En-route, and Terminal Phases:** PBN is limited to operations with **linear** lateral performance requirements.
*   **Approach Phase:** PBN accommodates operations with both **linear** (LNAV) and **angular** (LPV, similar to ILS) lateral guidance.

## PBN Benefits
*   Reduces the need to maintain specific routes and procedures for each sensor.
*   Avoids the development of specific operations for each new technology.
*   Allows for more efficient use of airspace (more direct routes, fuel savings).
*   Facilitates the operational approval process.

## Difference between Raw and Computed Data
*   **Raw Data:** Conventional navigation based on direct indications from ground aids (VOR, NDB).
*   **Computed Data:** PBN navigation where the system calculates position by integrating multiple sensors (GNSS, IRS, DME/DME) and validates data consistency.
