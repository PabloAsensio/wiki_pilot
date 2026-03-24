---
title: Electronic Flight Bag (EFB)
---

An **EFB** is an electronic system used by the flight crew to perform tasks previously done with paper documents and tools.

### Functionality
*   **Documentation**: Digital storage of Flight Crew Operating Manuals (FCOM), MEL, etc.
*   **Navigation**: Aeronautical Charts (Enroute, Approach Plates), Moving Maps.
*   **Performance**: Calculation of Take-off/Landing speeds and limits.
*   **Mass & Balance**: Loadsheet calculations.
*   *Note*: The EFB is **distinct** from the FMS (Flight Management System) and aircraft alerting systems (ECAM/EICAS). It does **not** typically handle ACARS/CPDLC or display system warnings directly.

### Hardware Classifications
1.  **Portable EFB (PED)**:
    *   Not part of the certified aircraft configuration.
    *   Can be used inside/outside the aircraft.
    *   Reference material only; crosscheck required.
    *   **Mounting**: Must be removable **without tools**.
2.  **Installed EFB**:
    *   Certified as part of the aircraft avionics.
    *   Included in the **MEL** (Minimum Equipment List) if failed.
    *   Integrated into the flight deck (screens, power, data).

### Software Classifications (Applications)
*   **Type A**: Malfunction/Misuse has **no safety effect**.
    *   *Examples*: HTML/PDF viewers for general manuals, non-interactive documents.
*   **Type B**: Malfunction/Misuse has a **minor safety effect**.
    *   *Examples*: Performance calculation apps, Electronic Charts (Zoom/Pan), interactive Checklists.
    *   *Constraint*: Must not replace a system required by airworthiness regulations (e.g., cannot replace the PFD/ND).

### Operational Issues
*   **Data Entry Error**: "Garbage In, Garbage Out". If a pilot enters incorrect weight/weather data, the EFB outputs **incorrect speeds/limits**.
*   **Failure**: Loss of an EFB (especially in a "paperless" cockpit) implies loss of access to charts, manuals, and performance data. Redundancy (2nd EFB or paper backup) is required.
