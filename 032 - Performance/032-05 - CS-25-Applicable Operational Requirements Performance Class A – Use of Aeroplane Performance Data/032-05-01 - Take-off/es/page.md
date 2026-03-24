---
title: "Datos de Despegue Clase A"
description: "Uso de cartas y tablas de performance para cálculos de despegue Clase A."
keywords: ["Clase A", "cartas de despegue", "RTOW", "Peso de Despegue Regulado", "velocidades V", "alineación"]
---

## Peso de Despegue Regulado (RTOW)

El peso máximo para el despegue es el menor de:
1.  **Límite de Campo**: Definido por la longitud de pista (TODR, ASDR) y pendiente.
2.  **Límite de Obstáculos**: Definido por la trayectoria neta de vuelo librando obstáculos.
3.  **Límite de Velocidad de Neumáticos**: Velocidad máxima en tierra para los neumáticos.
4.  **Límite de Energía de Frenos**: Energía máxima que los frenos pueden absorber durante un RTO.
5.  **Límite Estructural**: Masa Máxima de Despegue (MTOM) definida por el fabricante.
6.  **Límite de Ascenso**: Capacidad para cumplir con el gradiente de ascenso WAT (Peso, Altitud, Temperatura) del 2.4% en el segundo segmento.

## Margen de Alineación (LUA)

Los cálculos de performance asumen que el despegue comienza al inicio de la pista. Sin embargo, los aviones necesitan espacio para alinearse.
*   **Ajuste**: Se debe restar una distancia de "Margen de Alineación" (Line-Up Allowance - LUA) de la TORA/ASDA para tener en cuenta la longitud de pista consumida durante la alineación.
*   **Valores**: varían según el tamaño del avión y el ángulo de alineación (giro de 90° vs 180°). Ej. una entrada de 90° podría usar menos pista que un giro de 180° sobre la pista.

## Análisis de Despegue Simplificado
Las cartas usualmente proveen correcciones para:
*   **Viento**: Viento de cara aumenta el RTOW, viento de cola lo disminuye significativamente.
*   **Altitud de Presión**: Mayor altitud $\rightarrow$ menor empuje $\rightarrow$ menor RTOW.
*   **Temperatura**: Mayor temperatura $\rightarrow$ menor empuje $\rightarrow$ menor RTOW.
*   **Pendiente**: Pendiente descendente ayuda a la aceleración (mayor RTOW), ascendente dificulta.
*   **Superficie de Pista**: Mojada/Contaminada reduce la altura de pantalla a 15 pies (para mojada) y degrada la capacidad de frenado.

## Determinación de Velocidades V
Una vez que se conoce el Peso de Despegue Real (TOW) (y se confirma $\le$ RTOW), las velocidades V ($V_1, V_R, V_2$) se extraen de las tablas/FMS basándose en:
1.  Peso Real.
2.  Configuración de Flaps.
3.  Altitud de Presión y Temperatura.
4.  Condición de Pista (Pista mojada a menudo requiere una $V_1$ menor para mejorar la capacidad de frenado).
