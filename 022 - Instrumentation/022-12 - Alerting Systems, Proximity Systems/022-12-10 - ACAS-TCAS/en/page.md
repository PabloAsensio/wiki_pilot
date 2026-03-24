---
title: ACAS (Airborne Collision Avoidance System) / TCAS
---

**ACAS** (Airborne Collision Avoidance System) is the ICAO standard for systems designed to prevent mid-air collisions. **TCAS II** (Traffic Alert and Collision Avoidance System) is the equipment that meets this standard.
*   **Principle**: Operates independently of ground-based ATC. Uses transponder interrogations (Mode C or S) to detect nearby aircraft.
*   **Requirement**: Mandatory for turbine-powered aircraft > 5,700 kg or > 19 passengers.

### Equipment and Operation
TCAS II interrogates the transponders of other aircraft to determine:
1.  **Range**: From the time delay of the reply.
2.  **Bearing**: Using directional antennas.
3.  **Altitude**: From the Mode C/S reply (pressure altitude).

*   **Vertical Guidance Only**: TCAS II provides resolution advisories (RAs) only in the **vertical plane** (climb/descend). It does not issue turn commands.
*   **Coordination**: If both aircraft are TCAS II equipped, they coordinate via Mode S data link to ensure complementary maneuvers (e.g., one climbs, the other descends).

### Display Symbology
Traffic is displayed on the Navigation Display (ND) or a dedicated IVSI (Instantaneous Vertical Speed Indicator).

| Symbol | Description | Meaning |
|---|---|---|
| **Hollow Cyan/White Diamond** | Other Traffic | Traffic detected but not currently a threat (> 6 NM or > 1200 ft vertical). |
| **Solid Cyan/White Diamond** | Proximate Traffic | Traffic nearby (< 6 NM and < 1200 ft vertical) but not yet a threat. |
| **Solid Amber Circle** | **Traffic Advisory (TA)** | Potential threat (~40 seconds to CPA). "Traffic, Traffic". Visual search required. |
| **Solid Red Square** | **Resolution Advisory (RA)** | Collision threat (~25 seconds to CPA). Immediate vertical maneuver required. |

*   **Data Tag**: Shows relative altitude in hundreds of feet (e.g., `+10` is 1000 ft above) and a trend arrow if climbing/descending > 500 fpm.

### Alerts and Pilot Actions
1.  **Traffic Advisory (TA)**: "TRAFFIC, TRAFFIC".
    *   **Action**: Do **not** maneuver based solely on a TA. Visually search for the intruder. Prepare for a possible RA.
2.  **Resolution Advisory (RA)**: e.g., "CLIMB, CLIMB", "DESCEND, DESCEND", "MONITOR VERTICAL SPEED".
    *   **Action**:
        *   **Autopilot**: Disconnect immediately.
        *   **Fly**: Follow the green arc / Avoid the red arc on the VSI.
        *   **ATC**: Notify as soon as possible ("TCAS RA").
        *   **Clear of Conflict**: Return to clearance only when "CLEAR OF CONFLICT" is heard.

### Inhibitions and Limitations
*   **No Altitude Data**: If an intruder has a Mode A transponder (no altitude reporting), TCAS cannot generate an RA (vertical separation unknown), only a TA (bearing/range known).
*   **Low Altitude Inhibitions**:
    *   **< 1000 ft (approx)**: "TA ONLY" mode usually active (descent RAs inhibited to prevent flying into terrain).
    *   **< 1450 ft**: "INCREASE DESCENT" inhibited.
    *   **< 400 ft**: All alerts inhibited.
*   **Performance**: "CLIMB" RAs may be inhibited at high altitudes (performance limit) or with landing gear/flaps extended (configuration limit).
