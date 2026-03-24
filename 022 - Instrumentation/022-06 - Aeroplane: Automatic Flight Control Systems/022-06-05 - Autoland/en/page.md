---
layout: default
title: "022-06-05 - Autoland"
parent: "022-06 - Aeroplane: Automatic Flight Control Systems"
grand_parent: "022 - Instrumentation"
nav_order: 5
---

# Autoland Systems

## Purpose and Components

The **Automatic Landing System (Autoland)** allows aircraft to land in poor weather conditions where visual references are degraded (e.g., fog, low ceiling) below Category I minima.

Key components required:
- **Radio Altimeter (RA)**: Provides precise height Above Ground Level (AGL) for the flare maneuver.
- **Autopilot (AP)**: Usually multiple channels (redundancy).
- **Autothrust (A/THR)**: Manages speed and retards thrust at touchdown.
- **Ground Signals**: ILS (Instrument Landing System) or MLS.

## System Redundancy Levels

EASA CS-AWO defines classification based on system behavior after a failure:

### Fail-Passive
- **Behavior**: In the event of a failure, there is **no significant out-of-trim condition** or deviation.
- **Outcome**: The automatic landing is **NOT completed**. The pilot must take over manual control (usually performing a Go-Around).
- **Usage**: Category II or Category III A.

### Fail-Operational
- **Behavior**: In the event of a failure, the approach, flare, and landing **CAN be completed** by the remaining part of the system.
- **Outcome**: The system reverts to a fail-passive state after the first failure.
- **Requirement**: Typically requires 3 Autopilots (or 2 monitored architectures).
- **Usage**: Category III B.

### Fail-Operational Hybrid
- Consists of a primary **Fail-Passive** automatic system combined with an **independent guidance system** (e.g., a Head-Up Display - HUD).
- If the auto-system fails, the HUD provides guidance for the pilot to complete the landing manually.

## Alert Height (AH)

Alert Height is a specific radio altitude (typically between 100 ft and 200 ft), defined for **Fail-Operational** systems.

- **Failure ABOVE Alert Height**: The approach must be discontinued (Go-Around) unless reversion to higher minima (e.g., CAT I) is possible and prepared.
- **Failure BELOW Alert Height**: The failure is usually ignored (masked), and the approach continues automatically, provided no "AUTOLAND" red warning is triggered. The logic is that the risk of a go-around close to the ground exceeds the risk of landing with reduced (but sufficient) redundancy.

## Autoland Sequence (Typical Profile)

1.  **Approach (APP) Selected**: LOC and G/S armed. Second/Third AP engages to provide redundancy.
2.  **Capture**: LOC and G/S become active (Green) on FMA.
3.  **Low Altitude (~1500 ft)**: "FLARE" and "ROLLOUT" modes arm. System verifies redundancy (e.g., "LAND 3" or "CAT 3 DUAL").
4.  **Flare (~50 ft RA)**:
    - **FLARE** engages (Green).
    - AP uses Radio Altimeter to pitch up and reduce descent rate.
    - FD bars typically retract or disappear to avoid commanding large inputs during touchdown.
5.  **Thrust Reduction (~27-30 ft RA)**:
    - **IDLE** / **RETARD** engages. Throttles move to idle.
6.  **Touchdown & Rollout**:
    - **ROLLOUT** engages. AP uses rudder and nose wheel steering to maintain centerline using the Localizer signal.

## Limitations and Warnings

- **Wind Limits**: Autoland has stricter wind limits than manual landing (e.g., Max Crosswind 15-25 kt).
- **Autoland Warning**: A flashing red light/msg indicating the system acts as if it cannot land safely. Triggers include:
    - Failure of both Radio Altimeters.
    - Excessive ILS deviation (LOC or Glide).
    - Loss of ILS signal (though Glide signal loss below ~100 ft might be tolerated as the aircraft is in "attitude hold" transitioning to flare).
