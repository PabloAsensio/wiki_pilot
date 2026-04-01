---
title: "Coeficientes Aerodinámicos"
description: "Entendiendo las fórmulas de Sustentación y Resistencia y sus coeficientes."
keywords: ["fórmula de sustentación", "fórmula de resistencia", "CL", "CD", "ángulo de ataque", "pérdida"]
---

# Coeficientes Aerodinámicos


## Las Fórmulas
$$ L = C_L \cdot \frac{1}{2} \rho V^2 \cdot S $$
$$ D = C_D \cdot \frac{1}{2} \rho V^2 \cdot S $$

*   **$L$ / $D$**: Fuerza de Sustentación / Resistencia (Newtons).
*   **$C_L$ / $C_D$**: Coeficiente de Sustentación / Resistencia (Adimensional). Determinado por la forma y el Ángulo de Ataque.
*   **$\frac{1}{2} \rho V^2$**: Presión Dinámica ($q$).
*   **$S$**: Área de Superficie Alar ($m^2$).

## Coeficiente de Sustentación ($C_L$) vs Ángulo de Ataque ($\alpha$)
*   **Región Lineal**: A medida que $\alpha$ aumenta, $C_L$ aumenta linealmente.
*   **$C_{L_{max}}$**: El máximo coeficiente de sustentación alcanzable.
*   **Pérdida (Stall)**: Más allá de $C_{L_{max}}$ (Ángulo de Ataque Crítico, aprox 16°), el flujo de aire se separa, y el $C_L$ cae dramáticamente mientras la Resistencia aumenta.
*   **Ángulo de Sustentación Cero**: Para un perfil simétrico, $C_L=0$ a $\alpha=0$. Para un perfil curvado, $C_L=0$ a un $\alpha$ ligeramente negativo (ej. -4°).

## Relación Sustentación/Resistencia ($L/D$)
*   Eficiencia del perfil.
*   **Max $L/D$**: Corresponde al ángulo de ataque más eficiente (aprox 4°). Usado para máximo alcance (en hélices) o máximo planeo.
*   En $L/D_{max}$, la Resistencia es mínima (Resistencia Inducida = Resistencia Parásita).

## Factores que Afectan $C_L$
1.  **Ángulo de Ataque**: Factor primario.
2.  **Curvatura**: Más curvatura = mayor $C_{L_{max}}$ (ej. Flaps).
3.  **Alargamiento (Aspect Ratio)**: Mayor AR aumenta la pendiente de la curva de sustentación.
4.  **Condición de Superficie**: Hielo/suciedad reduce $C_{L_{max}}$ y el Ángulo Crítico.
