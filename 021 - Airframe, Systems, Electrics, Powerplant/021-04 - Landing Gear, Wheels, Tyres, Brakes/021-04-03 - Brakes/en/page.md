---
title: "Aircraft Brake Systems: Auto-Brake, RTO, and Anti-Skid Logic"
description: "Auto-brake landing and RTO modes, anti-skid interaction, disarm conditions, and braking performance implications on different runway states."
---

# Aircraft Brake Systems: Auto-Brake, RTO, and Anti-Skid Logic

The brake system provides the means to stop the aircraft during landing and rejected take-off (RTO). Modern aircraft employ advanced systems like Anti-Skid and Auto-Brake to optimize braking performance and safety.

## Auto-Brake System Operation

The auto-brake system assists pilots by automatically applying wheel brakes during landing and RTO.

- **Landing Mode:**
    - Provides a **predetermined, constant rate of deceleration** (e.g., knots lost per second).
    - The system modulates **brake pressure** to achieve this target deceleration.
    - **Effect of Reverse Thrust:** If reverse thrust is used, it contributes to the deceleration. The auto-brake system compensates by **reducing brake pressure** to maintain the same total deceleration rate. This results in **cooler brakes**, but **does not change the deceleration rate**.
    - **Weight independence:** The constant deceleration target is maintained regardless of aircraft weight (assuming sufficient friction exists).

- **Rejected Take-Off (RTO) Mode:**
    - Applies **maximum brake pressure** immediately when the system is triggered.
    - Unlike landing mode, it does **not** target a specific deceleration rate; it aims for maximum stopping power. The actual deceleration may vary due to runway conditions (e.g., slippery spots).
    - **Performance vs. Manual Braking:** RTO and maximum manual braking can achieve the same deceleration rate. However, RTO offers a safety benefit because **it reacts immediately**, whereas manual braking involves pilot reaction time, leading to a longer stopping distance.

- **Disarming Conditions:**
    The auto-brake system will disarm immediately if:
    - The pilot applies **manual braking**.
    - Any **thrust lever is advanced** after landing.
    - The speed brake lever is moved to the DOWN detent.
    - The system is switched to OFF or DISARM.

## Anti-Skid System

The anti-skid system determines if a wheel is about to lock up and reduces brake pressure to maintain tire rotation and maximum braking efficiency.

- **Interaction with Auto-Brake:** The auto-brake system relies on the anti-skid system. If the anti-skid system is **inoperative**, the **auto-brake system will not function**.
- **Performance Impact:** Failure of the anti-skid system increases the distance required to stop on **both wet and dry runways**.
- **In RTO Mode:** While RTO commands maximum pressure, the anti-skid system may still modulate (reduce) this pressure to prevent wheel lock-up on slippery surfaces.
