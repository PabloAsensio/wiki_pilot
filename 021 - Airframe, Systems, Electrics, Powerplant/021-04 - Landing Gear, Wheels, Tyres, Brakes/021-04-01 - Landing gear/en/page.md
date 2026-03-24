**Introduction**

The landing gear system supports the aircraft during taxi, takeoff, and landing. It is a complex system involving retraction mechanisms, locking devices, and emergency extension capabilities. Understanding its operation and limitations is crucial for safe flight.

## Landing Gear Operation and Control

Most modern aircraft landing gear systems are **active systems**, powered by hydraulics.

- **Power Source:** The hydraulic pressure is primarily provided by **engine-driven pumps**, which are driven by the accessory gearbox. While electric pumps exist, the heavy load during retraction is mainly handled by the engine-driven pumps.
- **Indication:**
    - **Down and Locked:** Indicated by **3 green lights** in the cockpit.
    - **Transit/Unsafe:** A red "gear unsafe" light illuminates if the gear position does not match the selector lever or is not locked.
    - **Aural Warning:** An aural warning must sound if a **landing is attempted when the landing gear is not locked down** (typically triggered by low throttle settings or radio altitude).

## Retraction and Locking Mechanisms

To prevent inadvertent operation and ensure the gear remains in the correct position, several safety mechanisms are used:

- **Anti-Retract Latch:** Physically prevents the gear selector lever from being moved to the "UP" position when the aircraft is on the ground.
- **Uplocks:** Mechanical locks (often **hook locks**) that hold the gear in the retracted position.
- **Downlocks (Overcentre Locks):**
    - **Geometric/Overcentre Lock:** Mainly used as a **downlock**. It uses the geometry of the drag/side stays to lock the gear in the extended position.
    - **Mechanism:** It requires a small force to lock (often locking automatically upon extension) but needs hydraulic or mechanical force to unlock (break the overcentre condition).

## Emergency Extension

If the main hydraulic system fails, an emergency extension system is available to lower the gear.

- **Methods:**
    - **Gravity Free-Fall:** The most common method. Mechanical uplocks are released, and the gear falls under its own weight.
    - **Mechanical Hand Crank:** Manually turning gears to operate actuators.
    - **Hand Pump:** Manually pumping hydraulic fluid to actuators.
    - **Compressed Nitrogen/Air (Blowdown):** Using stored gas pressure to release locks or power actuators.
- **Sequence:**
    1. **Release Hydraulic Pressure:** Often by bypassing the cut-off valve.
    2. **Unlock Doors:** Release door uplocks.
    3. **Unlock Gear:** Release mechanical **uplocks**.
- **Result:** The gear extends and locks down automatically (via overcentre springs/geometry). **Gear doors usually remain open** as there is no system to retract them. This is typically a one-time, non-reversible operation.

## Component Functions

- **Torsion Link (Torque Link):**
    - **Function:** Connects the inner (sliding) and outer (fixed) cylinder of the oleo strut to **prevent the inner cylinder from twisting** or rotating within the outer cylinder.
    - **Stress:** It transmits steering torque and prevents shimmy. It experiences maximum stress during **tight turns on the ground**.
- **Shuttle Valve:** Allows an actuator to be powered by an alternate pressure source (emergency) if the primary source fails.

## Speed Limitations

Operating the landing gear incurs drag and structural loads, necessitating specific speed limits:

- **$V_{LO}$ (Landing Gear Operating Speed):** The maximum speed at which it is safe to **extend or retract** the landing gear. If these differ, they are designated as $V_{LO(EXT)}$ and $V_{LO(RET)}$.
- **$V_{LE}$ (Landing Gear Extended Speed):** The maximum speed at which the aircraft can safely fly with the **gear extended and locked**. This is typically higher than $V_{LO}$.
