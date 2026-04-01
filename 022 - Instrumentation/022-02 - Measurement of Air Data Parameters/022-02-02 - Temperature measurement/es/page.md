---
title: "Medición de Temperatura del Aire: SAT, TAT y Ram Rise"
description: "Aprende los principios de SAT, TAT y ram rise en instrumentación aérea para calcular TAS y correcciones térmicas en vuelo."
keywords:
  - "altitud de densidad"
  - "densidad del aire"
  - "temperatura total del aire"
  - "temperatura estática del aire"
---
# Medición de Temperatura del Aire: SAT, TAT y Ram Rise

La medición precisa de la temperatura del aire es crucial para calcular la Velocidad Verdadera (TAS) y monitorizar el rendimiento del motor.

## Definiciones de Temperatura
*   **Temperatura Estática del Aire (SAT) / Temperatura Exterior (OAT):** La temperatura del aire no perturbado a través del cual vuela la aeronave.
*   **Temperatura Total del Aire (TAT):** La temperatura medida por una sonda que recibe el flujo de aire. Siempre es **mayor** que la SAT debido a los efectos de calentamiento.
*   **Ram Rise (Aumento por impacto):** La diferencia entre TAT y SAT ($TAT = SAT + \text{Ram Rise}$).

## Efectos de Calentamiento
A medida que la aeronave se mueve por el aire, la temperatura medida por la sonda aumenta debido a dos factores:
1.  **Calentamiento Cinético:** Causado por la fricción entre las moléculas de aire y la superficie de la sonda.
2.  **Calentamiento Adiabático:** Causado por la compresión del aire al ser frenado en la sonda.

## Medición y Cálculo
*   En aeronaves modernas con un Computador de Datos de Aire (ADC), la **TAT** es el valor medido (usando una sonda Rosemount, por ejemplo).
*   No hay una sonda OAT directa. En su lugar, el ADC calcula internamente la **SAT** (y OAT) restando el Ram Rise calculado y teniendo en cuenta el factor de recuperación de la sonda a partir de la TAT medida.
*   **Fórmula:** $TAT = SAT (1 + 0.2 \times K \times M^2)$, donde K es el factor de recuperación y M es el número de Mach.
