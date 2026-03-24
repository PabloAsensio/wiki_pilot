The **Machmeter** displays the Mach number ($M$), which is the ratio of the aircraft's True Airspeed (TAS) to the Local Speed of Sound (LSS).

## Formula
$$M = \frac{TAS}{LSS}$$

*   **LSS** depends *only* on temperature ($LSS \approx 39 \sqrt{T_{Kelvin}}$). Warmer air $\rightarrow$ higher speed of sound.
*   Since $LSS$ decreases with altitude (due to temperature drop), for a constant TAS in a climb, Mach Number **increases**.

## Principle of Operation
The mechanical Machmeter derives the Mach number by measuring the **ratio** of dynamic pressure ($P_t - P_s$) to static pressure ($P_s$).
$$M \propto \sqrt{\frac{P_t - P_s}{P_s}}$$
It combines an **airspeed capsule** (dynamic pressure) and an **altitude capsule** (static pressure) via a mechanical linkage. It does **not** assume any air temperature or density; the pressure ratio is sufficient.

## Climb/Descent Relationships (Constant Mach)
When climbing at a Constant Mach Number (assuming standard atmosphere):
1.  **Temperature** decreases $\rightarrow$ **LSS** decreases.
2.  **TAS** must decrease to keep the ratio $M$ constant.
3.  **CAS/IAS** decreases (due to density reduction).
*(Mnemonic: "Temperature down $\rightarrow$ TAS down").*

**Stall Margin:** In a constant Mach climb, since CAS is decreasing, the margin above the stall speed ($V_s$) reduces.

## Errors
*   **Blockage:** Influenced by both pitot and static blockages (similar to ASI and Altimeter errors).
*   **Compressibility:** The Machmeter is inherently designed to account for compressibility effects.
