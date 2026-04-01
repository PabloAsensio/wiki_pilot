---
title: "Distance Measuring Equipment (DME)"
description: "Understand DME principles, slant range, and operational use with VOR and ILS."
keywords:
    - "distance measuring equipment"
    - "dme slant range"
    - "radio navigation"
---

# Distance Measuring Equipment (DME)

**DME (Distance Measuring Equipment)** is a secondary radar system that provides the distance between an aircraft and a ground station. It operates in the **UHF band (962 - 1213 MHz)**.

## Operating Principle

It is based on measuring the travel time of radio pulses:
1.  The **interrogator** (airborne) sends pairs of pseudo-random pulses.
2.  The **transponder** (ground) receives the pulses, waits **50 microseconds**, and retransmits them on a frequency offset by **63 MHz**.
3.  The airborne equipment measures the total time, subtracts the 50 $\mu$s delay, and calculates the distance.

## Slant Range

![DME Slant Range Diagram](https://upload.wikimedia.org/wikipedia/commons/7/76/DME_Slant_and_Plan_range.jpg)

DME measures the direct distance between the aircraft antenna and the station, not the horizontal distance over the ground. This is known as **Slant Range**.
- The error is maximum when flying directly over the station, where the DME will indicate the **aircraft's altitude** (in NM).
- 1 NM $\approx$ 6080 feet.

## Operating Modes

- **SEARCH:** The equipment sends up to **150 pulse pairs per second (ppps)** to lock onto the station.
- **TRACK:** Once locked, the pulse rate drops (typically to **24-30 ppps**) to maintain tracking.
- **MEMORY:** If the signal is momentarily lost, the equipment maintains the last rate of change of distance for **8-10 seconds** before returning to search mode.

## Association and Frequencies

- The DME is usually **associated** with a VOR or ILS. The pilot tunes the VOR/ILS VHF frequency, and the equipment automatically tunes the paired DME UHF frequency.
- If associated, the DME Morse identifier is heard every 30-40 seconds (with a higher pitch) interleaved with the VOR identifier.

## Beacon Saturation

A DME beacon can serve a maximum of approximately **100 aircraft** simultaneously (about 2700 ppps). If this limit is exceeded, the beacon becomes **saturated** and prioritizes stronger signals (usually from closer aircraft).

## Derived Calculations

- **Groundspeed (GS):** The equipment calculates groundspeed based on the **rate of change of distance**. It is only accurate if flying directly towards or away from the station.
- **DME Arc:** Flying maintaining a constant distance. In this case, the GS indicated by the DME will be **zero**.
