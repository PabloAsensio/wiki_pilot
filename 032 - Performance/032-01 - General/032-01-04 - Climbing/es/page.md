---
title: "Performance de Ascenso"
description: "Mecánica del vuelo en ascenso, gradientes de ascenso y régimen de ascenso."
keywords: ["ascenso", "régimen de ascenso", "gradiente de ascenso", "ROC", "techo de servicio", "techo absoluto"]
---

## Cálculo de Performance de Ascenso

El ascenso generalmente requiere **Exceso de Empuje** o **Exceso de Potencia**. La aeronave utiliza este exceso de energía para ganar energía potencial (altitud).

### Ángulo de Ascenso ($\gamma$)
*   Determina el **Gradiente** (altura ganada por distancia recorrida).
*   Crítico para el **franqueamiento de obstáculos**.
*   Depende del **Exceso de Empuje** ($T - D$).
    $$
    \sin \gamma = \frac{\text{Empuje} - \text{Resistencia}}{\text{Peso}}
    $$
*   **Condición para Ángulo Máximo ($V_X$)**: Velocidad de vuelo donde el Exceso de Empuje es máximo. Generalmente cerca de $V_{MD}$ para jets.

### Régimen de Ascenso (ROC - Rate of Climb)
*   Determina la velocidad vertical (pies por minuto).
*   Crítico para alcanzar la altitud de crucero rápidamente (requerimientos ATC, eficiencia de tiempo).
*   Depende del **Exceso de Potencia** ($P_A - P_R$).
    $$
    ROC = \frac{\text{Potencia Disponible} - \text{Potencia Requerida}}{\text{Peso}}
    $$
*   **Condición para Régimen Máximo ($V_Y$)**: Velocidad de vuelo donde el Exceso de Potencia es máximo.

## Techos (Ceilings)

A medida que aumenta la altitud, el empuje/potencia disponible generalmente disminuye (cae la densidad del aire), mientras que la potencia/empuje requerido típicamente se mantiene constante o aumenta ligeramente (para la misma CAS). Eventualmente, el exceso llega a cero.

*   **Techo de Servicio**: La altitud donde el ROC máximo cae a un valor bajo especificado (ej. 100 ft/min para hélices, 500 ft/min para jets). Es el límite operativo práctico.
*   **Techo Absoluto**: La altitud donde el ROC máximo es **cero**. La aeronave no puede ascender más alto.
*   **Techo Aerodinámico**: (Jets) Altitud donde los límites de bataneo (buffet) por baja velocidad y por alta velocidad (mach) se encuentran ("Coffin Corner").

## Factores que Afectan el Ascenso

*   **Masa**: El aumento de peso reduce tanto el ROC como el Gradiente de Ascenso (aumenta la resistencia y la sustentación requerida).
*   **Temperatura**: Alta temperatura (menor densidad) reduce el empuje/potencia del motor, reduciendo significativamente la performance de ascenso.
*   **Flaps/Tren**: La configuración extendida aumenta la Resistencia, reduciendo el exceso de empuje/potencia, penalizando el ascenso.
