---
title: "Performance de Crucero Clase A"
description: "Optimización del vuelo de crucero: estrategias de velocidad y planificación de combustible."
keywords: ["Clase A", "crucero", "LRC", "MRC", "cost index", "margen de buffet"]
---

## Estrategias de Crucero

### Crucero de Máximo Alcance (MRC)
*   Velocidad: Corresponde a $1.32 V_{MD}$ (para jets).
*   Objetivo: Máxima distancia por kg de combustible.
*   Desventaja: La velocidad puede ser lenta, sensible a la inestabilidad de velocidad.

### Crucero de Largo Alcance (LRC)
*   Velocidad: Típicamente un 4% más rápida que MRC (99% del alcance específico máximo).
*   Objetivo: Proporciona el 99% del alcance de MRC pero con una estabilidad de velocidad significativamente mejor y mayor velocidad de bloque.
*   Estándar histórico antes del Cost Index.

### Cost Index (CI)
*   Los Sistemas de Gestión de Vuelo (FMS) modernos optimizan la velocidad basándose en la relación entre el **Costo del Tiempo** y el **Costo del Combustible**.
    $$
    CI = \frac{\text{Costo del Tiempo (\$ por hora)}}{\text{Costo del Combustible (\$ por kg)}}
    $$
*   **CI = 0**: Minimizando el costo de combustible (Máximo Alcance). Velocidad cercana a MRC.
*   **CI = Máx**: Minimizando el tiempo (Máxima Velocidad). Volando a $V_{MO}/M_{MO}$.

## Márgenes de Buffet

A grandes altitudes, el rango de velocidad es limitado:
*   **Buffet de Baja Velocidad**: Causado por el inicio de pérdida (alto Ángulo de Ataque). Ocurre a $V_{S1g} \times \text{factor de carga}$.
*   **Buffet de Alta Velocidad**: Causado por ondas de choque (efectos Mach).
*   **Factor de Carga**: Virar aumenta el factor de carga (g), lo que aumenta la velocidad de pérdida, acercando los buffets.

**Requisito Operativo**: Usualmente se requiere un margen mínimo de protección de **1.3g** de factor de carga hasta el inicio del buffet para la selección de la altitud de crucero. Esto asegura que la aeronave pueda alabear (virar) sin entrar en pérdida o exceso de velocidad.
