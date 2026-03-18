---
title: "Performance de Descenso"
description: "Mecánica del vuelo en descenso, coeficientes de planeo y procedimientos de drift-down."
keywords: ["descenso", "planeo", "coeficiente de planeo", "drift down", "efecto del viento"]
---

## Fuerzas en Descenso

En un descenso constante, la **Componente del Peso** que actúa hacia adelante ayuda al Empuje (si lo hay) a equilibrar la Resistencia. En un planeo (empuje al ralentí), la componente del peso hacia adelante equilibra la Resistencia completamente.

$$
\text{Empuje} + \text{Componente del Peso} = \text{Resistencia}
$$

## Planeo

Para un escenario de fallo de motor, maximizar la distancia de planeo es crítico.

### Ángulo de Planeo ($\gamma$)
El ángulo de planeo depende puramente de la **Relación Sustentación-Resistencia (L/D)**.
$$
\tan \gamma = \frac{\text{Resistencia}}{\text{Sustentación}} = \frac{1}{L/D}
$$

*   **Ángulo de Planeo Mínimo (Distancia Máx)**: Ocurre a la velocidad de **Máximo L/D** ($V_{MD}$).
*   **Efecto de la Masa**: La masa **NO** afecta el ángulo de planeo ni la distancia en un planeo constante.
    *   Una aeronave más pesada planea con el *mismo ángulo* pero a una *mayor velocidad* (debido al requisito $L=W$). Llega al suelo antes, pero toca tierra en el mismo punto de distancia que una aeronave más ligera.

## Drift Down (Descenso Controlado)

Si un avión multimotor pierde un motor a gran altitud, es posible que no pueda mantener esa altitud (Empuje Disponible < Empuje Requerido). Debe descender a una altitud más baja donde pueda mantener el vuelo nivelado. Este procedimiento se llama **Drift Down**.

*   **Velocidad de Drift Down**: Usualmente Green Dot o $V_{MD}$ para minimizar la tasa de descenso.
*   **Techo Neto**: La altitud que la aeronave puede mantener con un motor inoperativo, menos un margen de seguridad (medida de franqueamiento de obstáculos).

## Factores que Afectan el Descenso

### Viento
*   **Alcance**: El viento en cara reduce la distancia terrestre cubierta (hace más pronunciada la trayectoria de descenso respecto al suelo). El viento en cola aumenta la distancia terrestre.
    *   **Estrategia de Distancia Máx de Planeo**: ¿Aumentar velocidad con viento en cara (volar ligeramente más rápido que $V_{MD}$)? Sí, para mejorar la penetración.
*   **Tasa de Descenso**: El viento no tiene efecto en la velocidad vertical de descenso (tiempo para descender), solo en la trayectoria terrestre.

### Configuración
*   **Flaps/Tren**: Aumentan la Resistencia significativamente, degradando la relación L/D. Resultado: Ángulo de descenso más pronunciado y mayor Tasa de Descenso. Se usa para perder altitud rápidamente sin ganar velocidad.
