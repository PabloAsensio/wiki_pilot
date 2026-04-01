---
title: "Performance Clase A (CS-25): Datos de drift-down y altitud de estabilización"
description: "Determinación del techo neto y la trayectoria de drift down para el franqueamiento de obstáculos."
keywords: ["drift down", "techo neto", "techo bruto", "franqueamiento de obstáculos", "techo de servicio"]
---

# Performance Clase A (CS-25): Datos de drift-down y altitud de estabilización


## Techo de Servicio vs. Techo Neto

*   **Techo Bruto (OEI):** La altitud donde la aeronave puede mantener un gradiente de ascenso de **0%** (vuelo nivelado) con un motor inoperativo.
*   **Techo Neto (OEI):** El Techo Bruto menos un margen de seguridad (ej. gradiente de 1.1%).
    *   Esta es la altitud usada para planificar el franqueamiento de obstáculos.
    *   Dado que la penalización se resta de la capacidad de ascenso, el Techo Neto es **más bajo** que el Techo Bruto.

## Análisis de Gráficos de Drift Down

Las cartas de drift down permiten al piloto determinar:
1.  **Distancia**: Qué tan lejos puede viajar la aeronave mientras desciende desde la altitud de crucero hasta la altitud de estabilización.
2.  **Tiempo**: Cuánto tomará el descenso.
3.  **Combustible**: Combustible consumido durante la maniobra.

### Procedimiento
1.  Entrar con el **Peso Bruto** en el punto de fallo de motor.
2.  Seguir las líneas para la **Desviación ISA** (Temperatura).
3.  Leer la **Altitud Inicial** (Inicio del drift down) y **Altitud Final** (Techo Neto).
4.  Leer la **Distancia** recorrida.

**Chequeo de Obstáculos**:
El piloto debe verificar que en cada punto a lo largo de la trayectoria de drift down, la **Altitud Neta** esté al menos **1.000 pies** (o 2.000 pies en montañas) por encima del terreno.

### Efecto de las Variables
*   **Peso**: Avión más pesado $\rightarrow$ Descenso más pronunciado $\rightarrow$ Techo Neto más bajo $\rightarrow$ Menor alcance de Drift Down.
*   **Temperatura**: Desviación ISA más alta (Más caliente) $\rightarrow$ Menor empuje $\rightarrow$ Techo Neto más bajo.
*   **Viento**: El viento en cola aumenta la distancia terrestre cubierta; el viento de cara la disminuye.
