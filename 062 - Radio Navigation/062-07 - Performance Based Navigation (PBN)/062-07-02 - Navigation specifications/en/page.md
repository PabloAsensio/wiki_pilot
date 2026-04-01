---
title: "Radio Navigation: Navigation Specifications"
description: "Understand RNAV and RNP navigation specifications and operational requirements."
keywords:
    - "navigation specifications"
    - "rnav rnp"
    - "pbn"
---

# Radio Navigation: Navigation Specifications

Navigation specifications define the performance requirements (accuracy, integrity, etc.) that the aircraft and crew must meet to operate in a defined airspace.

## Specification Types
There are two main types, differentiated by the requirement for on-board monitoring and alerting:

1.  **RNAV (Area Navigation):**
    *   Does **NOT** require on-board performance monitoring and alerting.
    *   Examples: RNAV 10, RNAV 5, RNAV 1.
2.  **RNP (Required Navigation Performance):**
    *   **DOES** require on-board performance monitoring and alerting.
    *   The system alerts the pilot if the required accuracy is not met (ANP > RNP).
    *   Examples: RNP 4, RNP 1, RNP APCH.

## Application by Flight Phase (Summary)

| Specification | Typical Flight Phase | Lateral Accuracy (95%) | Notes |
| :--- | :--- | :--- | :--- |
| **RNAV 10 (RNP 10)** | Oceanic / Remote | 10 NM | Used in NAT HLA. Despite the name "RNP 10", it is an RNAV specification (no alerting). |
| **RNP 4** | Oceanic / Remote | 4 NM | Allows reduced lateral separation (e.g., 30 NM or 50 NM). |
| **RNP 2** | En-route (Continental and Oceanic/Remote) | 2 NM | Versatile for areas with little ground infrastructure. |
| **RNAV 5** | En-route Continental | 5 NM | Used in Europe (B-RNAV). Also for arrivals (STAR) outside 30 NM/MSA. |
| **RNAV 2** | En-route Continental, Departures/Arrivals | 2 NM | Common in the USA. |
| **RNAV 1** | Terminal (Departures/Arrivals) | 1 NM | P-RNAV in Europe. Requires radar coverage or GNSS. |
| **RNP 1** | Terminal (Departures/Arrivals) | 1 NM | Similar to RNAV 1 but with alerting. Used where there is no robust ATS surveillance. |
| **RNP APCH** | Approach (Initial, Intermediate, Final, Missed) | 0.3 NM (Final) | Standard GNSS approaches (LNAV, LNAV/VNAV, LPV). |
| **RNP AR APCH** | Approach (Authorisation Required) | 0.3 - 0.1 NM | For complex terrain. Requires specific authorization and training. |
| **RNP 0.3** | All (except Oceanic and Final Approach) | 0.3 NM | Specific for **helicopters**. |

## Key Points
*   **Operational Approval:** An approval for a stricter specification (e.g., RNP 0.3) does **NOT** imply automatic approval for a less strict one (e.g., RNP 4), as functional requirements may differ.
*   **Designation:** The "X" in RNAV X or RNP X indicates the lateral accuracy in nautical miles that must be maintained 95% of the time.
*   **NAT HLA:** Requires RNP 10 (RNAV 10) or RNP 4.
