---
title: "Procedimiento de Pesaje"
description: "Procedimientos para determinar la masa de la aeronave y la posición del CG mediante pesaje."
keywords: ["procedimiento de pesaje", "básculas", "puntos de pesaje", "nivelación", "datum"]
---

## Requisitos de Pesaje

El pesaje establece la **Masa Básica en Vacío (BEM)** y la **posición del CG** de la aeronave vacía.

### Preparación de la Aeronave
Antes de pesar, la aeronave debe estar en una configuración específica:
*   **Limpia**: Eliminando suciedad, hielo y nieve.
*   **Fluidos**: Drenando el combustible utilizable (el combustible no utilizable permanece y es parte de la BEM). Aceite y fluidos hidráulicos en niveles operativos.
*   **Equipo**: Todo el equipo fijo instalado (asientos, cocinas, aviónica).
*   **Nivelación**: La aeronave debe estar nivelada longitudinal y lateralmente utilizando puntos de nivelación definidos por el fabricante.

### Método de Pesaje
La aeronave se coloca sobre básculas en los **puntos de izado (gatos)** o bajo las **ruedas**.
*   **Fuerzas de Reacción**: Las básculas miden la fuerza de reacción ($R$) en cada punto (Rueda de Nariz/Cola, Ruedas Principales).
    *   $R_I, R_D$: Reacciones de Rueda Principal Izquierda y Derecha.
    *   $R_N$ o $R_C$: Reacción de Rueda de Nariz o Cola.

$$
\text{Masa Total} = R_I + R_D + R_N
$$

## Cálculo de la Posición del CG

La posición del CG se calcula utilizando el Principio de Momentos.
1.  **Definir Datum**: Generalmente la nariz, el cortafuegos o una cuaderna específica delante de la nariz.
2.  **Medir Brazos**: Distancia desde el Datum a los puntos de pesaje ($d_I, d_D, d_N$).
3.  **Suma de Momentos**: Calcular el momento para cada reacción ($Fuerza \times Distancia$).
    *   $\text{Momento} = \text{Reacción} \times \text{Brazo}$
4.  **Encontrar Brazo del CG**:
    $$
    \text{Brazo CG} = \frac{\text{Momento Total}}{\text{Masa Total}}
    $$

*Nota: Las distancias detrás del datum son positivas (+), adelante son negativas (-).*
