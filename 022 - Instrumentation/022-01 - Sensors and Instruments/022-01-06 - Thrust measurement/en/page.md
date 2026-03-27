---
title: "Jet Thrust Measurement: N1 and EPR Indication with Sensor Cross-Check"
description: "Understand jet thrust-setting parameters N1 and EPR, including pressure-ratio logic, inlet-sensor blockage risks, and operational cross-checking techniques."
keywords:
	- "minimum speed"
	- "flight level"
	- "magnetic headings"
	- "compass turns"
---
# Jet Thrust Measurement: N1 and EPR Indication with Sensor Cross-Check

In jet engines, thrust is the direct output force. Pilots rely on specific parameters to set and monitor this power.

## Primary Thrust Parameters

### N1 (Fan Speed)
**N1** represents the rotational speed of the Low-Pressure compressor (fan).
*   Displayed as a **percentage (%)** of the maximum rated RPM.
*   The fan accelerates a large volume of air around the core, providing the majority of thrust in high-bypass engines.

### EPR (Engine Pressure Ratio)
**EPR** measures the ratio of the pressure at the exhaust to the pressure at the inlet.
*   **Formula:** $EPR = \frac{\text{Turbine Outlet Pressure } (P_t)}{\text{Compressor Inlet Pressure } (P_s)}$
*   Sensors (Pitot tubes) measure these pressures.
*   **Blockage Hazard:** If the inlet pressure sensor becomes **blocked** during takeoff (acceleration), it will fail to register the increasing ram pressure. It will "lock" at a lower pressure reading. Mathematically, dividing the rising outlet pressure by a strictly lower-than-actual inlet pressure results in an **over-reading** EPR. The gauge will show high thrust while actual thrust is low. In such cases, pilots should cross-check with **N1**.
