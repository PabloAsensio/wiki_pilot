---
title: "Flight Warning Systems (FWS)"
---

## System Overview

The **Flight Warning System (FWS)** continuously monitors aircraft sensors to detect abnormal conditions. It uses an internal logic to prioritize these conditions and present them to the crew via visual, aural, and tactile means.

Modern aircraft integrate these functions into systems like **EICAS** (Engine Indication and Crew Alerting System) on Boeing or **ECAM** (Electronic Centralized Aircraft Monitor) on Airbus.

## Alert Hierarchies

Alerts are typically classified into three priority levels:

| Level | Priority | Visual | Aural | Crew Action | Examples |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Level A** | **Warning** | **Red** Master Warning + Message | Continuous (Bell, Siren, Voice) | **Immediate** recognition and corrective action. | Engine Fire, Overspeed, Stall, Cabin Altitude, Config. |
| **Level B** | **Caution** | **Amber** Master Caution + Message | Single/Repeated Tone (e.g., chime) | **Immediate awareness**, subsequent action. | Hyd Sys Fail, Gen Fault, Fuel Low, Brake Hot. |
| **Level C** | **Advisory** | Any (e.g., White, Cyan) except Red/Green | None | **Awareness**. | System Status, Memo messages. |

## Handling Procedure

A standard discipline for handling alerts (especially Cautions/Warnings) is:

1.  **Acknowledge** the failure (Identify the light/message).
2.  **Silence** the aural warning (if applicable/allowable).
3.  **Initiate** the appropriate procedure (Read ECAM/EICAS checklist).
4.  **Advise** ATC (if the failure affects flight profile or capability).

## Components

### Central Warning System (CWS)
*   **Annunciator Panel:** A panel containing specific lights for various systems, centralized to minimize scan time.
*   **Master Warning/Caution Lights:** Located in the pilot's primary field of view (glare shield) to draw attention to the CWS or EICAS/ECAM.

### Audio & Tactile Alerts
*   **Aural:** Designed to attract attention through a different sensory channel.
    *   **Fire:** Bell.
    *   **Overspeed/Config:** Siren or Clacker.
    *   **AP Disconnect:** Cavalry Charge, Wail, or Tone.
*   **Tactile:**
    *   **Stick Shaker:** Vibration of the control column for Stall Warning.

## Specific Scenarios
*   **Autopilot Disconnect:** Deliberate or uncommanded disconnect triggers a **Red Warning** light and a **Continuous Aural** alert until acknowledged (silenced) by the crew.
*   **Overspeed:** Exceeding VMO/MMO triggers a **Master Warning** and a specific aural alert (overspeed clacker/siren).
