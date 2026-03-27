---
title: "Datos de Aeródromo (AD): Resistencia de Pavimento, Distancias Declaradas y Códigos de Fricción"
description: "Revisa los datos AD sobre resistencia de pavimento con ACN-PCN, distancias declaradas TORA/TODA/ASDA/LDA y codificación de fricción en pista."
---
# Datos de Aeródromo (AD): Resistencia de Pavimento, Distancias Declaradas y Códigos de Fricción

## Resistencia de Pavimentos (Pavement Strength)
La resistencia de los pavimentos para aeronaves de más de 5,700 kg se notifica usando el método **ACN-PCN** (Aircraft Classification Number - Pavement Classification Number).
*   **ACN (Aircraft Classification Number):** Expresa el efecto relativo de una aeronave sobre un pavimento.
*   **PCN (Pavement Classification Number):** Expresa la resistencia del pavimento para operaciones sin restricciones.

**Regla General:**
*   Si **ACN ≤ PCN**, la aeronave puede operar sin restricciones.
*   El PCN reporta la capacidad del pavimento bajo cargas operativas máximas (no la carga actual).
*   Para aeronaves de **5,700 kg o menos**, se reporta la masa máxima permisible y la presión máxima de neumáticos.

> **Actualización:** La OACI está transicionando al método **ACR-PCR** (Aircraft Classification Rating - Pavement Classification Rating), aunque el ACN-PCN sigue en uso en muchas regiones.

## Distancias Declaradas (Declared Distances)
Son fundamentales para los cálculos de performance:

![Distancias Declaradas: TORA, TODA, ASDA, LDA](https://upload.wikimedia.org/wikipedia/commons/7/7b/Aim_fig_4-3-5_Declared_Distances_with_Full-Standard_Runway_Safety_Areas%2C_Runway_Object_Free_areas%2C_and_Runway_Protection_Zones.jpg)
*Diagrama ilustrativo de TORA, TODA, ASDA y LDA.*

1.  **TORA (Take-off Run Available):** Longitud de pista disponible y adecuada para el recorrido en tierra de despegue.
2.  **TODA (Take-off Distance Available):** TORA + **Clearway** (Zona libre de obstáculos).
3.  **ASDA (Accelerate-Stop Distance Available):** TORA + **Stopway** (Zona de parada).
4.  **LDA (Landing Distance Available):** Longitud de pista disponible para el aterrizaje.
    *   Afectada por el **umbral desplazado** (displaced threshold).

**Relaciones:**
*   Si no hay Clearway ni Stopway: **TORA = TODA = ASDA**.
*   Una **zona de parada (Stopway)** aumenta solo la **ASDA** (distancia para abortar el despegue). No afecta a TORA ni LDA.
*   Un **umbral desplazado** reduce la **LDA**, pero no afecta necesariamente a la TORA (se puede despegar desde el inicio físico de la pista).

## Estado de la Superficie y Coeficiente de Fricción
El coeficiente de fricción medido se correlaciona con un código y una estimación de frenado:
*   **0.40 y superior:** Bueno (Código 5).
*   **0.39 a 0.36:** Medio a bueno (Código 4).
*   **0.35 a 0.30:** Medio (Código 3).
*   **0.29 a 0.26:** Medio a pobre (Código 2).
*   **0.25 e inferior:** Pobre (Código 1).

**Pista Contaminada:** Cuando más del **25%** de la superficie está cubierta por agua (>3mm), nieve, nieve fundente o hielo.
