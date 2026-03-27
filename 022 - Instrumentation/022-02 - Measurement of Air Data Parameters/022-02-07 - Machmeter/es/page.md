---
title: "Funcionamiento del Machímetro: Número Mach, Relación de Presiones y Márgenes"
description: "Estudia el principio del machímetro, la relación TAS-velocidad local del sonido y cómo el vuelo a Mach constante afecta CAS, TAS y margen de pérdida."
keywords:
	- "altitud de densidad"
	- "densidad del aire"
	- "mach"
	- "calibrated altitude"
---
# Funcionamiento del Machímetro: Número Mach, Relación de Presiones y Márgenes

El **Machímetro** muestra el número de Mach ($M$), que es la relación entre la Velocidad Verdadera de la aeronave (TAS) y la Velocidad Local del Sonido (LSS).

## Fórmula
$$M = \frac{TAS}{LSS}$$

*   **LSS** depende *únicamente* de la temperatura ($LSS \approx 39 \sqrt{T_{Kelvin}}$). Aire más cálido $\rightarrow$ mayor velocidad del sonido.
*   Dado que LSS disminuye con la altitud (por la caída de temperatura), para una TAS constante en ascenso, el Número de Mach **aumenta**.

## Principio de Operación
El Machímetro mecánico deriva el número de Mach midiendo la **relación** entre la presión dinámica ($P_t - P_s$) y la presión estática ($P_s$).
$$M \propto \sqrt{\frac{P_t - P_s}{P_s}}$$
Combina una **cápsula de velocidad** (presión dinámica) y una **cápsula de altitud** (presión estática) mediante un enlace mecánico. **No** asume ninguna temperatura o densidad del aire; la relación de presiones es suficiente.

## Relaciones Ascenso/Descenso (Mach Constante)
Al ascender a un Número de Mach Constante (asumiendo atmósfera estándar):
1.  **Temperatura** disminuye $\rightarrow$ **LSS** disminuye.
2.  **TAS** debe disminuir para mantener la relación $M$ constante.
3.  **CAS/IAS** disminuye (debido a la reducción de densidad).
*(Regla: "Baja temperatura $\rightarrow$ Baja TAS").*

**Margen de Pérdida:** En un ascenso a Mach constante, como la CAS disminuye, el margen sobre la velocidad de pérdida ($V_s$) se reduce.

## Errores
*   **Bloqueo:** Influenciado tanto por bloqueos de pitot como de estática (similar a errores de ASI y Altímetro).
*   **Compresibilidad:** El Machímetro está inherentemente diseñado para tener en cuenta los efectos de compresibilidad.
