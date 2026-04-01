---
title: "Atmósfera Estándar Internacional (ISA): Gradiente Térmico, Temperatura y Presión"
description: "Guía ATPL sobre la atmósfera estándar internacional (ISA), con valores a nivel del mar, gradiente térmico y presión estándar en aviación."
keywords: ["atmosfera estandar", "atmosfera isa", "atmósfera estándar internacional", "isa aeronautica", "valores ISA meteorología ATPL", "temperatura y presión estándar vuelo", "OACI atmósfera estándar"]
---

# Atmósfera Estándar Internacional (ISA): Gradiente Térmico, Temperatura y Presión


La Atmósfera Estándar Internacional (ISA) es un modelo atmosférico hipotético utilizado como referencia para la navegación aérea y el diseño de aeronaves.

## Valores Estándar

![Modelo de Atmósfera Estándar (ISA)](https://upload.wikimedia.org/wikipedia/commons/9/9d/Comparison_US_standard_atmosphere_1962.svg)

*   **Nivel del Mar (MSL)**:
    *   Temperatura: **+15°C**
    *   Presión: **1013.25 hPa**
    *   Densidad: **1.225 kg/m³**
*   **Troposfera**:
    *   Gradiente Térmico (Lapse Rate): La temperatura disminuye a razón de **2°C por cada 1000 ft** (o 0.65°C por cada 100 m).
*   **Tropopausa**:
    *   Altitud: **36,090 ft** (11 km).
    *   Temperatura: **-56.5°C**.
*   **Estratosfera Inferior**:
    *   Desde la tropopausa hasta aprox. 20 km (65,000 ft), la temperatura se mantiene constante (**Isotérmica**) a **-56.5°C**.

## Cálculos de Temperatura ISA

Para calcular la temperatura estándar a una altitud determinada (en la troposfera):

$$T_{ISA} = 15 - (2 \times \frac{Altitud}{1000})$$

**Ejemplos:**
*   A **18,000 ft**: $15 - (2 \times 18) = 15 - 36 = \mathbf{-21^\circ C}$.
*   A **20,000 ft**: $15 - (2 \times 20) = 15 - 40 = \mathbf{-25^\circ C}$.
*   A **30,000 ft**: $15 - (2 \times 30) = 15 - 60 = \mathbf{-45^\circ C}$.

Si la temperatura real es diferente a la ISA, se expresa como una desviación (ej. ISA +10, ISA -5).
*   Si a 18,000 ft la temperatura real es -35°C (siendo ISA -21°C), la desviación es ISA -14°C.
*   *Nota: Si la temperatura es más fría que ISA, la densidad del aire será mayor que la estándar.*

## Niveles de Presión y Vuelo

Relación entre Niveles de Vuelo (FL) y presión en hPa:

| Nivel de Vuelo (FL) | Presión (hPa) |
| :--- | :--- |
| FL050 | 850 |
| FL100 | 700 |
| FL140 | 600 |
| FL180 | 500 |
| **FL240** | **400** |
| FL300 | 300 |
| FL340 | 250 |
| **FL390** | **200** |
| FL450 | 150 |

## Gradientes Térmicos (Lapse Rates)

![Gradientes Adiabáticos (DALR y SALR)](https://upload.wikimedia.org/wikipedia/commons/d/d4/Adiabatic_lapse_rate.svg)

1.  **ELR (Environmental Lapse Rate)**: Es el cambio real de temperatura con la altura en un momento y lugar dados. El promedio ISA es 2°C/1000 ft.
2.  **DALR (Dry Adiabatic Lapse Rate)**: Tasa de enfriamiento de una parcela de aire **no saturado** que asciende. Valor constante: **3°C/1000 ft**.
3.  **SALR (Saturated Adiabatic Lapse Rate)**: Tasa de enfriamiento de una parcela de aire **saturado** (100% humedad). Valor variable (aprox. **1.8°C/1000 ft**). Es menor que el DALR porque la condensación del vapor de agua libera **calor latente**, lo que calienta la parcela y reduce su tasa de enfriamiento.
