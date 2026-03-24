---
title: Engine Parameters and Alerting Systems (EICAS / ECAM)
---

Modern aircraft use electronic systems to monitor engine parameters, aircraft systems, and provide crew alerts. The two main systems are **EICAS** (Boeing) and **ECAM** (Airbus).

### System Overview
| Feature | **EICAS** (Boeing) | **ECAM** (Airbus) |
|---|---|---|
| **Primary Display** | Upper Display | E/WD (Engine/Warning Display) |
| **Content** | N1/EPR, EGT, Warnings, Cautions | N1/EPR, EGT, Fuel, Flaps, Warnings, Memos |
| **Secondary Display** | Lower Display | SD (System/Display) |
| **Content** | Hydraulics, Pressurization, Eng 2ndary, Status | System Synoptics (Schematics), Status |

### EICAS Display Modes
1.  **Operational**: Real-time system parameters selected by the crew.
2.  **Status**: Used for dispatch (MEL). Shows flight control positions, hydraulic qty, oxygen, etc.
3.  **Maintenance**: Ground use only for troubleshooting.

### Electronic Checklists (ECL) & Procedures
These systems automatically display the appropriate checklist when a failure is detected by sensors.

#### Limitations & Pilot Judgement
The computer triggers checklists based on **sensor thresholds**, but it lacks "context" or awareness of physical damage.
*   **Fuel Leak**: If a leak causes an imbalance, the system may trigger a "Fuel Imbalance" checklist prompting to **Open Crossfeed**.
    *   *Danger*: Doing so would pump the good fuel overboard through the leak.
    *   *Action*: Pilots must diagnose the leak (Fuel Used vs Fuel On Board) before following the ECL.
*   **Engine Damage**: If an engine fails due to severe damage (e.g., vibration, loud bang).
    *   *Danger*: The ECL for a simple flameout might suggest a "Relight".
    *   *Action*: Do not attempt to relight a damaged engine.

### CRM and Standard Operating Procedures (SOPs)
To prevent irreversible errors (like shutting down the wrong engine):
1.  **Confirm the Failure**: Both pilots must agree on the diagnosis.
2.  **Read & Do**: Follow the checklist slowly and methodically.
3.  **Guarded Switches / Thrust Levers**: The Pilot Monitoring (PM) must **never** move a thrust lever, engine master, or guarded switch without explicit **confirmation** from the Pilot Flying (PF).
