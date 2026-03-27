---
layout: default
title: "Flight Mode Annunciator (FMA): Active/Armed Modes and Mode Awareness"
description: "Understand FMA structure, active versus armed mode indications, mode reversions, and crew callout discipline to avoid automation confusion."
keywords:
  - "flight level"
  - "minimum speed"
  - "magnetic headings"
  - "compass turns"
parent: "022-06 - Aeroplane: Automatic Flight Control Systems"
grand_parent: "022 - Instrumentation"
nav_order: 4
---

# Flight Mode Annunciator (FMA): Active/Armed Modes and Mode Awareness

## Purpose and Location

The **Flight Mode Annunciator (FMA)** is the primary interface for pilots to monitor the status of the Automatic Flight Control System (AFCS). It acts as the single source of truth for "what the system is doing," as opposed to the switches on the control panel (MCP/FCU), which only indicate what the pilot has *requested*.

- **Location**: Typically at the very top of the Primary Flight Display (PFD).
- **Function**: Displays the status of:
  - Autopilot (AP) engagement.
  - Flight Director (FD) status.
  - Autothrust (A/THR) modes and status.
  - Landing capabilities (e.g., CAT III Dual, Autoland).

## Structure of the Display

The FMA is usually divided into columns, from left to right (typical layout like Airbus/Boeing):
1.  **Autothrust Mode**: (e.g., `SPD`, `THR CLB`, `IDLE`).
2.  **Vertical Mode**: (e.g., `ALT`, `V/S -1000`, `G/S`).
3.  **Lateral Mode**: (e.g., `HDG`, `NAV`, `LOC`).
4.  **Approach Capability / AP Status**: (e.g., `AP1+2`, `LAND 3`, `SINGLE CH`).

### Mode States

The FMA distinguishes between modes that are actively controlling the aircraft and modes that are waiting to capture a target.

- **Engaged (Active) Modes**:
  - Typically shown in **Green**.
  - Usually larger font or on the top line of the text box.
  - Example: `ALT` (Maintaining altitude), `HDG SEL` (Flying selected heading).
- **Armed Modes**:
  - Typically shown in **White**, **Cyan**, or **Amber** (depending on aircraft).
  - Usually smaller font or on the bottom line.
  - Example: `G/S` (in white) means Glide Slope is armed but not yet captured.

## Operational Importance

### Mode Changes and Awareness
Pilots must closely monitor the FMA because distinct audible or visual alerts do not accompany all mode changes.
- **Visual Attention**: When a mode changes (e.g., from Armed to Engaged), a white or green **box** typically surrounds the new mode for a few seconds (e.g., 10 seconds) to draw the pilot's eye.
- **Standard Operating Procedures (SOPs)**: The Pilot Flying (PF) is usually required to **call out** any FMA change (e.g., "Speed", "Alt Star", "Glideslope Captured"). The Pilot Monitoring (PM) must verify and confirm ("Check").

### Mode Reversion
Sometimes the automation changes modes uncommanded by the pilot to protect the aircraft or because a signal is lost.
- **Example**: If the aircraft climbs in `V/S` mode but lacks sufficient thrust, the speed decreases. To prevent a stall, the AP may automatically revert from `V/S` to `Level Change` or `Speed` mode to lower the nose.
- These uncommanded changes ("Mode Reversions") are often accompanied by a unique **aural warning** (e.g., "Triple Click") and a flashing indication to alert the crew to the deviation from the intended plan.

## Consequences of Ignoring FMA

Failing to monitor the FMA can lead to:
1.  **Undesirable Aircraft States**: E.g., believing the AP is in `LNAV` when it has actually reverted to `HDG` due to a flight plan discontinuity, causing the aircraft to fly straight ahead instead of turning.
2.  **Confusion**: The pilot may be fighting the automation if they believe it is in one mode while it is actually in another.
3.  **Safety Incidents**: Most automation-related accidents involve "Confusion about the current mode" or "Lack of mode awareness."
