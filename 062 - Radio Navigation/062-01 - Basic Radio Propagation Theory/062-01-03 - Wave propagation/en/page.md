---
title: Radio Navigation: Wave Propagation
description: Study radio wave propagation modes and their operational impact on navigation.
keywords:
  - wave propagation
  - radio signal propagation
  - aviation navigation
---

# Radio Navigation: Wave Propagation

The way radio waves travel from the transmitter to the receiver depends on their frequency and the environment.

## Propagation Modes

### 1. Space Waves
These are **Line-of-Sight** waves. They travel in a straight line through the atmosphere.
*   It is the primary mode for **VHF, UHF, SHF, and EHF**.
*   Range is limited by the curvature of the Earth and obstacles.
*   **Theoretical Range Formula (VHF):**
    $$Distance (NM) = 1.23 \times (\sqrt{Height_{Tx}(ft)} + \sqrt{Height_{Rx}(ft)})$$

### 2. Ground/Surface Waves
These waves follow the curvature of the Earth due to **diffraction**.
*   Effective at low frequencies (**VLF, LF, MF**).
*   Range depends on power and surface type (greater range over sea than over land).
*   Used by **NDBs**.

### 3. Sky Waves
These are waves that refract in the **ionosphere** and return to Earth, allowing communications beyond the horizon.
*   Primary propagation mode for **HF** (and MF at night).
*   Allows transoceanic and global communications.

## The Ionosphere

A layer of the atmosphere ionized by solar radiation. It mainly affects HF waves.
*   **Layers:** D, E, F1, F2.
*   **D Layer:** Exists only during the day and **absorbs** low-frequency waves (LF/MF), preventing their propagation as sky waves.
*   **Night:** The D layer disappears, allowing MF and HF waves to reach the upper layers (E and F) and refract, drastically increasing range (and interference).

### Key HF Propagation Concepts
*   **Skip Distance:** The minimum distance from the transmitter to where the first sky wave returns to Earth.
    *   Increases with frequency.
    *   Increases if the ionosphere is higher (night).
*   **Skip Zone (Dead Zone):** An annular area where no signal is received: it is too far for the ground wave but too close for the first sky wave.
*   **Fading:** Signal fluctuation due to changes in the ionosphere or interference between multiple paths (e.g., sky wave vs. ground wave).

## Phenomena and Errors

### Doppler Effect
Change in perceived frequency due to relative motion between source and receiver.
*   Frequency **increases** if approaching, **decreases** if receding.
*   Used in: **DVOR** (to create the variable phase signal), **GNSS** (to determine velocity), MTI Radars, and Weather Radars (to detect turbulence).

### ADF Errors (LF/MF Waves)
*   **Night Effect:** Interference between ground wave and sky wave at night. Causes needle oscillation.
*   **Coastal Refraction:** The wave bends towards the coast when passing from land to sea (change in speed).
*   **Mountain Effect:** Reflections in mountainous terrain.
*   **Thunderstorms:** Lightning emits signals in LF/MF bands that attract the ADF needle.
*   **Quadrantal Error:** Deviation caused by the metal of the aircraft itself. Maximum at relative bearings 045°, 135°, 225°, 315°.

## Physical Phenomena
*   **Refraction:** Change of direction when passing into a medium with different density (e.g., ionosphere).
*   **Diffraction:** Bending of the wave around obstacles (allows ground wave).
*   **Reflection:** Bouncing off surfaces (ground, buildings).
*   **Absorption:** Loss of energy (e.g., D layer).
