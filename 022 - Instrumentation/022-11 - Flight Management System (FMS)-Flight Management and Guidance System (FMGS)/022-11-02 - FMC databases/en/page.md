---
title: "FMC Databases"
---

## Overview

The Flight Management Computer (FMC) relies on two primary databases to perform its functions: the **Navigation Database** and the **Performance Database**. Additionally, a temporary storage area allows pilots to define custom waypoints.

## Navigation Database (NDB)

The Navigation Database is a digital repository containing aeronautical information essential for lateral navigation and flight planning.

### Content
*   **Airports & Runways:** Locations, elevations, lengths.
*   **Navaids:** VORs, NDBs, DMEs, and their frequencies.
*   **Intersections/Waypoints:** Coordinates and identifiers.
*   **Airways:** Enroute structure.
*   **Procedures:** SIDs (Departures), STARs (Arrivals), and Approaches (ILS, RNAV, etc.).
*   **Company Routes:** Pre-defined routes used by the airline.
*   **Magnetic Variation:** Data to convert True North to Magnetic North.

### Updates & Validity (AIRAC)
*   The database follows the **AIRAC cycle** (Aeronautical Information Regulation and Control) and is updated every **28 days**.
*   The FMC typically holds **two cycles**:
    *   **Active:** The current valid database.
    *   **Standby/Second:** The adjacent cycle (previous or next).
*   **Read-Only:** The core data is **read-only** to ensure integrity. Pilots cannot modify or delete standard waypoints or procedures.
*   **Pilot Action:** Pilots verify the validity dates during pre-flight checks on the `IDENT` page. Changing the active database typically **deletes the active flight plan**.
*   *Note:* Terrain and obstacle data are usually stored in the **EGPWS** database, not the FMS Navigation Database.

## Performance Database

The Performance Database contains static data specific to the aircraft's **airframe** and **engine model**.

### Content
*   **Engine Model:** Thrust characteristics, fuel flow parameters at various power settings and altitudes.
*   **Aerodynamic Model:** Drag polars (clean and configured), lift characteristics.
*   **Speed Limits:** VMO/MMO, flap signaling speeds.
*   **Optimization Data:** Optimum altitudes, maximum altitudes, and recommended cruise speeds (ECON).

### Purpose
The FMC uses this data to calculate:
*   **Thrust Targets:** N1 or EPR settings for Takeoff, Climb, Cruise, and Go-Around.
*   **Predictions:** Fuel consumption, Estimated Time of Arrival (ETA), and Top of Descent (TOD) points.
*   **Speeds:** V1, VR, V2, and Green Dot (best lift-to-drag) speeds.

### Maintenance Factors
While pilots cannot alter the core model, maintenance personnel can enter **Drag Factors** or **Fuel Flow Factors** to account for airframe aging and engine degradation, ensuring predictions remain accurate.

## User-Defined Waypoints

Since pilots cannot modify the main database, the FMS provides a **Supplemental** or **Temporary** database for pilot-created waypoints. These are erased when the main navigation database is updated.

### Creation Methods
1.  **Lat/Long (LL):** Direct coordinate entry (e.g., `N45W030`).
2.  **Place/Bearing/Distance (PBD):** Defines a point based on a known fix (e.g., `LMG/330/20` - 20NM on the 330 radial from LMG).
3.  **Place-Bearing/Place-Bearing (PBX):** Defines a point at the intersection of two radials (e.g., `LMG330/CGC090`).
4.  **Along Track (PD):** A distance before or after a waypoint along the current flight path.
