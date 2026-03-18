---
title: "Aerodinámica: Conceptos Básicos y Definiciones"
description: "Leyes fundamentales de la aerodinámica incluyendo el Principio de Bernoulli y la Ecuación de Continuidad."
keywords: ["Bernoulli", "ecuación de continuidad", "presión estática", "presión dinámica", "IAS", "TAS", "CAS"]
---

## La Atmósfera
*   **Composición**: 78% Nitrógeno, 21% Oxígeno, 1% Otros (Argón, CO2).
*   **ISA (Atmósfera Estándar Internacional)**: Usada para calibración y comparación.
    *   Temperatura: 15°C (288.15 K) al Nivel Medio del Mar (MSL). Gradiente vertical -1.98°C/1000 pies hasta 11km (Tropopausa).
    *   Presión: 1013.25 hPa (29.92 inHg) al MSL.
    *   Densidad: 1.225 kg/m³ al MSL.

## Ecuación de Continuidad
Para un flujo estacionario de un fluido incompresible (el flujo subsónico se trata como incompresible):
$$ A_1 V_1 = A_2 V_2 $$
*   **$A$**: Área.
*   **$V$**: Velocidad.
*   Si el área de la sección transversal de un tubo **disminuye**, la velocidad del fluido **aumenta**.

## Principio de Bernoulli
Sujeto a que el flujo sea estacionario, incompresible y no viscoso (sin fricción). La suma de la presión estática y la presión dinámica es constante a lo largo de una línea de corriente.
$$ P_{est\acute{a}tica} + \frac{1}{2}\rho V^2 = Constante $$
$$ P_{est\acute{a}tica} + P_{din\acute{a}mica} = P_{total} $$
*   A medida que la velocidad ($V$) **aumenta** (debido a un tubo convergente), la presión dinámica **aumenta**, y la presión estática ($P_{est\acute{a}tica}$) **disminuye**.
*   Esto explica la generación de sustentación: el aire que acelera sobre la superficie superior curvada de un ala tiene menor presión estática que el aire debajo.

## Velocidades (Airspeeds)
*   **IAS (Velocidad Indicada)**: Leída del instrumento. Impulsada por la presión dinámica ($q = \frac{1}{2}\rho V^2$).
*   **CAS (Velocidad Calibrada)**: IAS corregida por error de instrumento y posición.
*   **EAS (Velocidad Equivalente)**: CAS corregida por compresibilidad (significativo > 300kt / Mach 0.6).
*   **TAS (Velocidad Verdadera)**: La velocidad real de la aeronave a través de la masa de aire. Corregida por error de densidad.
    *   $TAS = EAS \times \frac{1}{\sqrt{\sigma}}$ (donde $\sigma$ es la densidad relativa).
    *   A IAS constante, la TAS **aumenta** con la altitud (aprox 2% por cada 1.000 pies).
