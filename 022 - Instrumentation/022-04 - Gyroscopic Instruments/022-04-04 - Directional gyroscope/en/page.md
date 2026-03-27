---
title: "Directional Gyro (DG): Heading Stability, Drift, and Re-Synchronization"
description: "Learn DG operation for stable heading reference, including real/apparent drift, transport wander, and periodic synchronization with magnetic compass."
keywords:
	- "magnetic headings"
	- "magnetic course"
	- "compass turns"
	- "points on the compass"
---
# Directional Gyro (DG): Heading Stability, Drift, and Re-Synchronization

The **Directional Gyro (DG)** or Direction Indicator (DI) provides a stable heading reference, free from the turning and acceleration errors of a magnetic compass.

## Principles
*   **Gyro:** **Horizontal Axis** (Tied gyro).
*   **Degrees of Freedom:** **2** (Pitch and Roll of the aircraft do not affect it).
*   **Operation:** The gyro stays rigid in space while the aircraft turns around it. The instrument detects this relative motion and drives the compass card.

## Drift and Synchronization
The DG has **no magnetic sensing capability**. It is purely inertial.
1.  **Real Drift:** Caused by friction.
2.  **Apparent Drift:** Caused by Earth's rotation ($15^\circ/hr \times \sin Lat$).
3.  **Transport Wander:** Caused by moving across the globe.

Because of this drift, the pilot must **manually synchronize** the DG with the Magnetic Compass:
*   **When:** Every 10-15 minutes.
*   **Condition:** Only in **straight, level, unaccelerated flight** (when the magnetic compass is accurate).

## Advantages over Magnetic Compass
*   **Stable:** No oscillation or swinging.
*   **No turning errors:** Does not overshoot/undershoot on N/S headings.
*   **No acceleration errors:** Does not show false turns during speed changes.
