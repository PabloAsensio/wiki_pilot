---
title: "Radar Pulse Techniques: Range and Timing"
description: "Understand pulse radar timing, range calculation, and signal interpretation."
keywords:
    - "radar pulse techniques"
    - "pulse radar"
    - "aviation radar"
---

# Radar Pulse Techniques: Range and Timing

## Basic Radar Principles

**RADAR** (Radio Detection and Ranging) is a system that uses electromagnetic waves to detect objects and determine their distance and direction.

### Primary vs Secondary Radar

*   **Primary Radar:** Emits pulses of electromagnetic energy that reflect off objects (echoes). It measures the time it takes for the signal to travel back and forth to calculate distance.
    *   Examples: Airborne Weather Radar (AWR), Primary Surveillance Radar (PSR), Surface Movement Radar (SMR).
*   **Secondary Radar:** Uses an interrogator (ground) and transponder (air) system. The transponder receives the signal and emits a stronger coded reply.
    *   Examples: SSR (Secondary Surveillance Radar), DME.

## Pulse Parameters

### PRF (Pulse Repetition Frequency)
It is the number of pulses transmitted per second (pps).
*   **Relation to Maximum Range:** The PRF determines the theoretical maximum unambiguous range. The radar must wait for the pulse to return from the maximum distance before sending the next one.
*   **Formula:**
    $$ \text{Maximum Range (km)} = \frac{300,000}{2 \times \text{PRF}} $$
    *(Where 300,000 is the speed of light in km/s)*.
*   The **lower the PRF**, the longer the listening time and therefore the **greater the maximum range**.

### Pulse Width
It is the duration of the transmitted pulse.
*   **Relation to Minimum Range:** The radar cannot receive while transmitting. Therefore, the pulse width determines the minimum distance at which an object can be detected (blind spot).
*   **Range Resolution:** A shorter pulse allows better distinction between two objects close together in the same direction (better resolution).

### Power
*   **Peak Power:** It is the maximum instantaneous power during the pulse duration. It determines the maximum detection range (ability to penetrate the atmosphere and return).
*   **Average Power:** It is the energy averaged over the entire cycle (including the silence time). It is much lower than the peak power.

## Applications

*   **ATC (Air Traffic Control):**
    *   Primary Radar: To see aircraft without transponders and weather.
    *   Secondary Radar (SSR): To identify aircraft, obtain altitude and squawk codes.
*   **Airborne:**
    *   Weather Radar (AWR): Detection of precipitation and turbulence.
    *   Radio Altimeter: Measurement of height above terrain.
    *   DME: Distance measurement (pulse technique).
    *   TCAS: Collision avoidance (based on SSR).
