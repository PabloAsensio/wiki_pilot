---
title: Electronic Display Units (EFIS Architecture)
---

Modern **EFIS** (Electronic Flight Instrument Systems) utilize **Display Units (DUs)** (CRT or LCD screens) to present flight information. A key feature of these systems is the **redundancy** and **interchangeability** of the displays to ensure critical information remains available in case of a hardware failure.

### Typical Layout (Airbus/Boeing)
*   **Outboard DU**: Usually the **PFD** (Primary Flight Display).
*   **Inboard DU**: Usually the **ND** (Navigation Display).
*   **Center DUs**: Upper and Lower for Engine/Systems (EICAS/ECAM).

### Display Failure Logic (Automatic Switching)
Because **PFD** information (Attitude, Airspeed, Altitude) is critical for safe flight ("utmost importance"):

1.  **Outboard DU Failure (PFD Screen Fails)**:
    *   The **PFD image automatically transfers** to the **Inboard DU** (ND screen).
    *   The ND information assumes a lower priority and is displaced (or can be selected on another screen).
    *   *Principle*: You lose the Nav display to save the Primary Flight display.

2.  **Inboard DU Failure (ND Screen Fails)**:
    *   The PFD remains on the Outboard DU.
    *   The ND screen goes blank (ND info lost on that screen).

3.  **Upper Center DU Failure (Engine/Warning Fails)**:
    *   The **Primary Engine/Warning display automatically transfers** to the **Lower DU**.
    *   Information previously on the Lower DU (e.g., secondary engine params, checklists) may be compacted or displaced.

### Independence
*   The Captain's side and First Officer's side are generally independent for this switching.
*   If the Captain's PFD screen fails, it switches to the **Captain's ND screen** (not the Copilot's).
