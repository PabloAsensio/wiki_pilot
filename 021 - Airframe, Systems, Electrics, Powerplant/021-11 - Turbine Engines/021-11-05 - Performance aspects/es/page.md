---
title: "Aspectos de Rendimiento en Turbinas de Gas: Flat Rating, Temperatura Flex y EPR"
description: "Explora conceptos de rendimiento en turbinas de gas: comportamiento flat-rated, despegue con empuje reducido por temperatura flex e indicación EPR."
---
# Aspectos de Rendimiento en Turbinas de Gas: Flat Rating, Temperatura Flex y EPR

## Empuje y Presión
*   **Aceleración del Aire**: A medida que el motor acelera el aire, la **presión dinámica aumenta** y la presión estática disminuye (principio de Bernoulli).
*   **Empuje Específico**: Definido como Empuje Neto por unidad de Flujo Másico de Aire.
    *   Si el flujo de aire de entrada aumenta (debido a mayor velocidad/densidad) manteniendo el empuje neto constante, el **empuje específico disminuye**.

## Motores "Flat-Rated" (Potencia Nominal Constante)
Los motores de turbina suelen estar "flat-rated" para proporcionar un rendimiento consistente en un rango de temperaturas y proteger los componentes.

*   **Rango Flat-Rated (OAT Fría/Estándar)**:
    *   Ocurre cuando la Temperatura Exterior (OAT) está **por debajo** de la "temperatura flat-rated" (típicamente alrededor de ISA +15°C).
    *   El empuje está limitado por **límites de presión interna** (Flujo Másico Máximo / Estructural).
    *   El motor produce un **empuje máximo constante** aunque la OAT baje más.
*   **Rango Limitado por Temperatura (OAT Caliente)**:
    *   Ocurre cuando la OAT está **por encima** de la temperatura flat-rated.
    *   El empuje está limitado por **EGT/TGT** (Temperatura de Gases de Escape/Turbina) para prevenir la fusión o "creep" (fluencia) de los álabes de la turbina.
    *   A medida que la OAT aumenta, el **empuje máximo disponible disminuye**.

## Despegue con Empuje Reducido (Flex / Assumed Temp)
Se usa para extender la vida del motor utilizando menos empuje del máximo cuando el rendimiento de despegue lo permite (poco peso, pista larga).

*   **Principio**: Se "engaña" al FADEC/Computador haciéndole creer que el aire exterior está más caliente de lo que realmente está.
*   **Método**:
    *   El piloto introduce una **Temperatura Asumida** (Assumed Temperature o Flex Temp) en el FMS.
    *   Esta temperatura asumida es **más alta** que la OAT real.
    *   Como el motor está "limitado por temperatura" a altas OATs, el computador calcula un **límite de N1/EPR más bajo**.
    *   **Resultado**: El motor produce menos empuje, operando más frío (menor EGT), reduciendo el desgaste.

## Indicación de Empuje: EPR
*   **EPR (Engine Pressure Ratio)**: Parámetro primario de empuje en muchos jets (otros usan N1).
*   **Definición**: La relación entre la **Presión de Salida de la Turbina de Baja** ($P_{salida}$) y la **Presión de Entrada al Compresor** ($P_{entrada}$).
    *   $$EPR = \frac{\text{Presión Total a la Salida de la Turbina}}{\text{Presión Total a la Entrada del Compresor}}$$
*   **Sensores**: Pueden ser fuelles electromecánicos o transductores digitales.
