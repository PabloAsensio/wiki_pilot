---
title: "FMS Operations and Limitations"
---

## Initialization Sequence

Setting up the FMS for a flight typically follows a logical flow of pages on the CDU:

1.  **IDENT Page:**
    *   The first page displayed after power-up.
    *   Used to verify **Aircraft Model**, **Engine Type**, and **Navigation Database validity** (Active dates).

2.  **POS INIT (Position Initialization):**
    *   Initializes the Inertial Reference System (IRS).
    *   Typically uses the **GPS** position or the **Airport Reference Point (ARP)** coordinates.

3.  **RTE (Route):**
    *   Entry of **Origin** and **Destination** airports.
    *   Selection of a **Company Route** or manual entry of waypoints and airways.

4.  **PERF INIT (Performance Initialization):**
    *   Entry of **Zero Fuel Weight (ZFW)**, **Fuel Quantity**, and **Cruise Altitude**.
    *   **Cost Index (CI):** A crucial parameter determining the economic profile of the flight.

## Cost Index (CI)

The Cost Index is a strategic management tool that balances **Fuel Cost** against **Time-Related Operating Costs**.

$$ CI = \frac{\text{Time Cost}}{\text{Fuel Cost}} $$

*   **CI = 0:** Minimum Trip Fuel (Maximum Range Speed). The aircraft flies slowly to save fuel.
*   **High CI:** Minimum Flight Time. The aircraft flies fast, disregarding higher fuel consumption.

## Position Computation and Accuracy

The FMS calculates a "System Position" by mixing data from multiple sensors using a **Kalman Filter**.

### Inputs & Priority
1.  **GPS (GNSS):** The most accurate and primary source.
2.  **DME/DME:** Radio position derived from multiple DME distances.
3.  **VOR/DME:** Bearing and distance from a station.
4.  **LOC:** Localizer for lateral alignment during approach.
5.  **IRS:** Inertial position (drifts over time).

### Degradation & Limitations
*   **GPS Loss:** If GPS signals are lost, the FMS reverts to Radio/IRS updating. The position accuracy may **gradually degrade** or "shift" (Map Shift).
*   **RAIM (Receiver Autonomous Integrity Monitoring):** Essential for **RNP** and GPS-based approaches. Loss of GPS implies loss of RAIM and the inability to fly these approaches.
*   **Runway Update:** On takeoff, applying TOGA power often triggers a position update to the runway threshold coordinates.

## Navigation Modes

### Lateral Navigation (LNAV)
*   **Command:** Follows the horizontal flight plan.
*   **Autotuning:** The FMS automatically tunes VOR and DME frequencies for position updating without crew intervention.
*   **Overfly vs. Fly-by:**
    *   **Fly-by:** Standard. The aircraft anticipates the turn to cut the corner.
    *   **Overfly:** The aircraft must pass directly over the waypoint before initiating the turn.

### Vertical Navigation (VNAV)
*   **Command:** Manages the vertical profile (Climb, Cruise, Descent).
*   **Barometric Reference:** VNAV logic relies on **Barometric Altitude** form the Air Data Computer (ADC).
*   **Autothrottle:** Essential for full VNAV operation (managing speed/thrust interactions).
*   **Modes:**
    *   **VNAV SPD:** Pitch maintains speed.
    *   **VNAV PTH:** Pitch maintains the geometric path (speed controlled by thrust/drag).
    *   **VNAV ALT:** Level off at an intermediate constraint or MCP altitude.

### Performance Predictions
*   The FMS predicts fuel usage and arrival times (ETA).
*   **Limitation:** Predictions assume the aircraft is in a **normal configuration**. If the aircraft flies with **slats/flaps extended** or **gear down** for extended periods (abnormal config), drag is higher than modeled, and **fuel predictions will be inaccurate**.
