---
title: "Aerodynamic Coefficients"
description: "Understanding Lift and Drag formulas and their coefficients."
keywords: ["lift formula", "drag formula", "CL", "CD", "angle of attack", "stall"]
---

# Aerodynamic Coefficients


## The Formulas
$$ L = C_L \cdot \frac{1}{2} \rho V^2 \cdot S $$
$$ D = C_D \cdot \frac{1}{2} \rho V^2 \cdot S $$

*   **$L$ / $D$**: Lift / Drag Force (Newtons).
*   **$C_L$ / $C_D$**: Coefficient of Lift / Drag (Unitless). Determined by shape and Angle of Attack.
*   **$\frac{1}{2} \rho V^2$**: Dynamic Pressure ($q$).
*   **$S$**: Wing Surface Area ($m^2$).

## Coefficient of Lift ($C_L$) vs Angle of Attack ($\alpha$)
*   **Linear Region**: As $\alpha$ increases, $C_L$ increases linearly.
*   **$C_{L_{max}}$**: The maximum lift coefficient achievable.
*   **Stall**: Beyond $C_{L_{max}}$ (Critical Angle of Attack, approx 16°), the airflow separates, and $C_L$ drops dramatically while Drag increases.
*   **Zero Lift Angle**: For a symmetrical aerofoil, $C_L=0$ at $\alpha=0$. For a cambered aerofoil, $C_L=0$ at a slightly negative $\alpha$ (e.g., -4°).

## Lift/Drag Ratio ($L/D$)
*   Efficiency of the aerofoil.
*   **Max $L/D$**: Corresponds to the most efficient angle of attack (approx 4°). Used for maximum range (in props) or maximum glide.
*   At $L/D_{max}$, Drag is continuously minimum (Induced Drag = Parasite Drag).

## Factors Affecting $C_L$
1.  **Angle of Attack**: Primary factor.
2.  **Camber**: More camber = higher $C_{L_{max}}$ (e.g., Flaps).
3.  **Aspect Ratio**: Higher AR increases slope of lift curve.
4.  **Surface Condition**: Ice/dirt reduces $C_{L_{max}}$ and Critical Angle.
