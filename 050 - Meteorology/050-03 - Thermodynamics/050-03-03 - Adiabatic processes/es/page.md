---
title: "Procesos adiabáticos"
description: "Explicación clara de los procesos adiabáticos, el gradiente térmico (DALR y SALR), y la estabilidad atmosférica para exámenes de meteorología en aviación."
keywords: ["meteorología ATPL procesos adiabáticos", "diferencia DALR y SALR", "gradiente térmico ambiental aviación", "estabilidad atmosférica para pilotos", "exámenes EASA meteorología", "expansión adiabática aviación", "diagrama termodinámico aviación"]
---

Un proceso adiabático es aquel en el que **no hay transferencia de calor** hacia o desde el sistema. El cambio de temperatura se debe únicamente a la expansión o compresión del gas.

## Mecanismo Físico

### 1. Expansión Adiabática (Enfriamiento)
*   Cuando una parcela de aire **asciende**, la presión atmosférica disminuye.
*   La parcela se **expande** (aumenta su volumen).
*   Para expandirse, la parcela realiza trabajo consumiendo su propia energía interna.
*   Resultado: La temperatura de la parcela **disminuye**.

### 2. Compresión Adiabática (Calentamiento)
*   Cuando una parcela de aire **desciende**, la presión atmosférica aumenta.
*   La parcela se **comprime** (disminuye su volumen).
*   El entorno realiza trabajo sobre la parcela.
*   Resultado: La temperatura de la parcela **aumenta**.

---

## Gradientes Térmicos (Lapse Rates)

![Adiabatic Lapse Rate](https://upload.wikimedia.org/wikipedia/commons/d/d4/Adiabatic_lapse_rate.svg)

### DALR (Dry Adiabatic Lapse Rate) - Gradiente Adiabático Seco
*   Es la tasa de enfriamiento del aire **no saturado** (seco) cuando asciende.
*   **Valor Constante:** $3^\circ C / 1000 \text{ ft}$ ($1^\circ C / 100 \text{ m}$).

### SALR (Saturated Adiabatic Lapse Rate) - Gradiente Adiabático Saturado
*   Es la tasa de enfriamiento del aire **saturado** (dentro de una nube) cuando asciende.
*   **Valor Variable:** Promedio $\approx 1.8^\circ C / 1000 \text{ ft}$ ($0.6^\circ C / 100 \text{ m}$).
*   **¿Por qué es menor que el DALR?** Porque al condensarse el vapor de agua, se libera **calor latente**, lo que contrarresta parte del enfriamiento por expansión.

### ELR (Environmental Lapse Rate) - Gradiente Ambiental
*   Es el perfil real de temperatura de la atmósfera en un momento y lugar dados.
*   **Valor ISA:** $2^\circ C / 1000 \text{ ft}$ ($0.65^\circ C / 100 \text{ m}$).
*   Determina la estabilidad de la atmósfera.

---

## Estabilidad Atmosférica
La estabilidad se determina comparando el ELR con el DALR y el SALR.

| Condición | Relación | Descripción |
| :--- | :--- | :--- |
| **Inestabilidad Absoluta** | **ELR > DALR** | El aire es inestable tanto si está seco como saturado. La parcela siempre será más cálida que el entorno y seguirá subiendo. |
| **Inestabilidad Condicional** | **SALR < ELR < DALR** | El aire es estable si está seco, pero inestable si se satura. Es la condición más común. |
| **Estabilidad Absoluta** | **ELR < SALR** | El aire es estable tanto si está seco como saturado. La parcela siempre será más fría que el entorno y tenderá a bajar. (Incluye isotermas e inversiones). |
| **Estabilidad Neutra** | **ELR = DALR** (seco) <br> **ELR = SALR** (saturado) | La parcela tiene la misma temperatura que el entorno y no tiende a subir ni bajar. |

### Estabilidad de Masas de Aire

*   **Masa de Aire Cálido (más caliente que la superficie):**
    *   Se enfría desde abajo $\rightarrow$ Se vuelve **Estable**.
    *   Nubes estratiformes (ST, SC), mala visibilidad, turbulencia ligera, posible niebla.
*   **Masa de Aire Frío (más fría que la superficie):**
    *   Se calienta desde abajo $\rightarrow$ Se vuelve **Inestable**.
    *   Nubes cumuliformes (CU, CB), chubascos, buena visibilidad (excepto en chubascos), turbulencia moderada/fuerte.

---

## Diagramas Termodinámicos (Tefigrama)

![Tephigram Diagram](https://upload.wikimedia.org/wikipedia/commons/4/48/Tephigram.png)

Son diagramas termodinámicos utilizados para analizar la estabilidad y predecir niveles de condensación.

*   Si la curva de estado de la parcela (DALR/SALR) está a la **derecha** de la curva de temperatura ambiental (ELR), la parcela es más cálida $\rightarrow$ **Inestable** (asciende).
*   Si está a la **izquierda**, la parcela es más fría $\rightarrow$ **Estable** (resiste el ascenso).
