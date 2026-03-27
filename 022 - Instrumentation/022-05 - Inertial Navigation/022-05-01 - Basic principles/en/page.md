---
title: "Inertial Navigation Basic Principles: INS, IRS, and Error Behaviour"
description: "Master INS and IRS fundamentals, from acceleration integration and strap-down architecture to Schuler-tuned and cumulative drift errors."
keywords:
    - "magnetic headings"
    - "magnetic course"
    - "points on the compass"
    - "compass turns"
---

# Inertial Navigation Basic Principles: INS, IRS, and Error Behaviour

## Inertial Navigation System (INS)

An **Inertial Navigation System (INS)** is a self-contained navigation system that provides continuous information on the aircraft's position, velocity, and attitude without relying on external references (like radio aids or GPS).

### Fundamental Operation
The core principle of an INS is the measurement and integration of **acceleration**:
1.  **Accelerometers** measure the aircraft's acceleration.
2.  **First Integration**: Integrating acceleration over time gives **velocity** (Groundspeed).
3.  **Second Integration**: Integrating velocity over time gives **distance** travelled and position relative to a known starting point.

### Inputs and Outputs
*   **Initial Inputs**: The system requires an accurate **initial position** (Latitude/Longitude) before the flight.
*   **Air Data Input**: The INS requires **True Airspeed (TAS)** input from the Air Data Computer (ADC) to calculate **Wind Velocity** (by solving the triangle of velocities: Groundspeed vector vs. TAS vector).
*   **Outputs**: Position, Track, True Heading, Groundspeed, Wind Direction/Speed, and Attitude (Pitch/Roll).

## System Types

### Stable Platform (INS)
In traditional INS (1st generation), accelerometers are mounted on a **gyro-stabilised platform**.
*   **Mechanism**: The platform is mounted in gimbals and isolated from aircraft manoeuvres.
*   **Orientation**: Torque motors keep the platform **level** (perpendicular to local vertical) and **aligned with True North**.
*   **Sensors**:
    *   **Accelerometers (2)**: Oriented North-South and East-West.
    *   **Gyroscopes**: Detect platform movement to drive the torque motors and maintain alignment.

### Strap-down System (IRS)
Modern aircraft use an **Inertial Reference System (IRS)**, which is a "strap-down" system.
*   **Mechanism**: Sensors are rigidly fixed ("strapped down") to the aircraft's airframe. There are no gimbals.
*   **Sensors**:
    *   **3 Accelerometers**: Measure acceleration along the aircraft's body axes (Longitudinal, Lateral, Vertical).
    *   **3 Ring Laser Gyros (RLG)**: Measure angular rates of rotation (Pitch, Roll, Yaw).
*   **Operation**: A computer mathematically creates a "stable platform" by processing the rate data to resolve body-axis accelerations into North/South and East/West components.
*   **Advantages**: Greater reliability (no moving parts/solid-state), higher accuracy, less maintenance, instant "spin-up" (laser light).

## Errors

INS errors are categorized into bounded and unbounded errors.

### Bounded Errors (Schuler Tuning)
*   **Behavior**: These errors oscillate and do not grow continuously over time. They tend to return to zero over a cycle.
*   **Schuler Period**: The oscillation period is **84.4 minutes**.
*   **Causes**: Platform tilt, initial misalignment, integration errors in the first stage.

### Unbounded Errors (Cumulative)
*   **Behavior**: These errors grow primarily with **time**.
*   **Inertial Drift**: The radial position error generally increases at a rate of:
    *   **1 - 2 NM/h** for older mechanical INS.
    *   Significantly less for modern Laser IRS.
*   **Causes**:
    *   **Track/Position Errors**: Azimuth misalignment, gyro drift (wander).
    *   **Distance Errors**: Levelling gyro wander, second stage integrator errors.

### Comparison table

| Feature | Stable Platform (INS) | Strap-down (IRS) |
| :--- | :--- | :--- |
| **Mounting** | Gimballed platform isolated from aircraft | Fixed to airframe |
| **Gyros** | Mechanical rate-integrating gyros | Ring Laser Gyros (RLG) - Solid State |
| **Alignment** | Mechanical leveling and torquing | Mathematical calculation |
| **Maintenance** | High (moving parts) | Low (Solid state) |
| **Accuracy** | Good | Excellent |
