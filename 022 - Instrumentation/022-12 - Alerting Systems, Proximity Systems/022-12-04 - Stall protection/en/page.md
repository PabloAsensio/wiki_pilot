---
title: "Stall Protection Systems (SPS)"
---

## Overview

While the **Stall Warning System (SWS)** provides an alert, the **Stall Protection System (SPS)** is an active safety mechanism designed to **physically prevent** the aircraft from entering a stall. It acts as a final barrier when the pilot fails to react to the initial warning.

## Stick Pusher

The primary component of an SPS is the **Stick Pusher**.

*   **Function:** It mechanically applies a forward force to the control column (elevator nose-down input) to forcefully reduce the Angle of Attack (AoA).
*   **Activation Point:** It activates **after** the stall warning (Stick Shaker) but **before** the aircraft exceeds the Critical Angle of Attack ($AoA_{crit}$).
*   **Requirement:** It is typically mandatory on large transport aircraft that exhibit dangerous stall characteristics (e.g., "Deep Stall" or "Super Stall" often associated with T-tail configurations) where recovery might be difficult or impossible for the pilot alone.

## Other Protection Methods
Depending on the aircraft type, an SPS may also:
*   **Extend Flats/Slats:** Automatically deploying leading-edge slats to increase the $AoA_{crit}$.
*   **Increase Thrust:** Commanding the Autothrottle to apply power (e.g., Alpha Floor protection on Airbus).

## System Logic & Diagnostics

Understanding the distinction between Warning and Protection is crucial for analyzing failure scenarios:

*   **Scenario:** The aircraft approaches a stall. The Stick Pusher activates (nose drops), but there was **no** prior audible alarm or vibration.
*   **Analysis:** The **Stall Protection System** is functioning correctly (it prevented the stall). The **Stall Warning System** (Stick Shaker/Audio) is **inoperative**.

| System | Component | Purpose | Action |
| :--- | :--- | :--- | :--- |
| **SWS** | Stick Shaker / Audio | **Alert** | Vibrates column, sounds alarm. |
| **SPS** | Stick Pusher | **Prevent** | Pushes nose down. |
