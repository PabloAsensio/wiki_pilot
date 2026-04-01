---
title: "Use of Performance Based Navigation (PBN)"
description: "Learn practical use cases of PBN in terminal and en-route operations."
keywords:
    - "use of pbn"
    - "performance based navigation"
    - "rnav operations"
---

# Use of Performance Based Navigation (PBN)

The use of PBN introduces specific concepts and functionalities in navigation systems to improve airspace efficiency and capacity.

## Waypoint Types
*   **Fly-by Waypoint:** The pilot or system anticipates the turn to avoid overshooting the next flight segment. The turn begins *before* reaching the waypoint. It is the standard form of turning in RNAV routes.
*   **Fly-over Waypoint:** The aircraft must physically fly over the waypoint before initiating any turn. Used when it is necessary to follow a specific path due to obstacles or procedures (e.g., MAPt).

## Fixed Radius Paths (FRP)
These are precise curved paths that the RNP system must be capable of flying.

### 1. Radius to Fix (RF) Leg
*   **Use:** **Terminal and Approach** procedures.
*   **Definition:** Defined by a **radius**, an **arc length**, and a **fix** (endpoint).
*   **Requirement:** Requires autopilot or flight director with "roll-steering" capability.
*   **Accuracy:** Maintains the same accuracy (RNP) during the turn as in straight segments.

### 2. Fixed Radius Transition (FRT)
*   **Use:** **En-route** procedures.
*   **Purpose:** Allows closer parallel routes in upper airspace.
*   **Standard Radii:**
    *   **22.5 NM** for high altitude routes (above FL 195).
    *   **15 NM** for low altitude routes.

## Specific System Functions
*   **Lateral Offset (SLOP - Strategic Lateral Offset Procedure):**
    *   Capability to fly parallel to the defined route at a specific distance (usually in 1 NM increments up to 20 NM).
    *   Used for contingencies or to reduce collision risk due to loss of vertical precision (wake turbulence).
    *   The system usually cancels the offset automatically in terminal areas, approaches, holds, or turns >90°.
*   **ARINC 424 Path Terminators:** Navigation database coding standard that defines how the FMS interprets and flies procedures (SIDs, STARs, IAPs). Defines 24 segment types (e.g., RF, TF - Track to Fix, CF - Course to Fix).

## Key Differences
*   **Fly-by vs RF:** A *fly-by* turn varies its radius and start point according to speed and wind (it is not a fixed ground track). An *RF* turn is a fixed ground track (constant radius), regardless of speed or wind.
