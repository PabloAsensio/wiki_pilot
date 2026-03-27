---
title: "Overspeed Warning System: VMO/MMO Limits, Barber Pole, and Aural Alerts"
description: "Learn overspeed warning logic, PFD barber-pole interpretation, VMO/MMO and configuration limits, plus immediate crew alerting behavior."
keywords:
    - "overspeed"
    - "vmo mmo"
    - "minimum speed"
    - "flight level"
---

# Overspeed Warning System: VMO/MMO Limits, Barber Pole, and Aural Alerts

## Overview

The **Overspeed Warning System** is a mandatory safety feature designed to alert the flight crew when the aircraft exceeds its maximum operating speeds ($V_{MO}$ / $M_{MO}$). Its primary purpose is to prevent inadvertent excursions beyond the certified structural limits of the airframe.

## Indications

### Visual (PFD Speed Tape)
On modern Primary Flight Displays (PFD):
*   **Speed Tape:** A vertical moving scale (White on Grey).
*   **Maximum Speed Strip ($V_{MAX}$):** A **Red and Black striped bar** (often called the "Barber Pole") descends from the top of the scale to indicate the upper speed limit.
*   **$V_{MAX}$ Definition:** The strip starts at the **lowest** limiting speed for the current configuration:
    1.  **$V_{MO}$ / $M_{MO}$:** Maximum Operating Speed / Mach.
    2.  **$V_{LE}$:** Maximum Landing Gear Extended Speed.
    3.  **$V_{FE}$:** Maximum Flaps Extended Speed.

### Aural
*   **Alert:** A distinctive, continuous sound (e.g., "Clacker", Siren, or Voice Warning) triggers immediately upon exceeding the limit.

## System Logic
The Warning System monitors Air Data Computer (ADC) inputs. If Indicated Airspeed (IAS) or Mach Number exceeds the calculated limit, the Master Warning (Level A) is triggered.
