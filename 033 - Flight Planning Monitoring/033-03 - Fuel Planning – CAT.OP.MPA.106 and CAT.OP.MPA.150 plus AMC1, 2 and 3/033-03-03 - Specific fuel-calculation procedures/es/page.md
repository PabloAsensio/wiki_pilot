---
title: "Procedimientos de Cálculo de Combustible"
description: "Cómo calcular segmentos específicos de combustible usando tablas de performance."
keywords: ["flujo de combustible", "alcance integrado", "nam", "ngm", "gravedad específica"]
---

## Gravedad Específica (SG) / Densidad

El combustible se vende por volumen (litros/galones) pero se calcula por masa (kg/lbs) para la performance.
*   **Fórmula**: $Masa = Volumen \times Densidad$
*   **Densidad Jet A1**: Típicamente alrededor de **0.8 kg/L** (varía con la temperatura).
*   Combustible caliente es menos denso (más volumen para el mismo peso).
*   Combustible frío es más denso (menos volumen para el mismo peso).

## Cálculo de Flujo de Combustible

### Alcance Integrado
Para vuelos largos, el consumo de combustible reduce el peso del avión, lo que a su vez reduce el consumo de combustible.
*   **Cálculo**: Hecho paso a paso (típicamente por hora) o usando tablas acumuladas (Tablas de Planificación de Vuelo).
*   **Millas Aéreas Náuticas (NAM)**: Distancia volada a través de la masa de aire.
    *   $NAM = TAS \times Tiempo$
    *   $Combustible = NAM \times (Flujo / TAS)$
*   **Millas Terrestres Náuticas (NGM)**: Distancia sobre el terreno (corregida por viento).
    *   $NGM = GS \times Tiempo$

### Combustible de Espera (Holding)
Calculado a "Velocidad de Espera" usualmente a **1.500 pies** sobre la elevación del destino (para Reserva Final) o a altitud de crucero (para espera de Contingencia).
*   La velocidad de espera es usualmente menor que la de crucero ($V_{MD}$ usualmente para máxima autonomía) para minimizar el flujo.

## Planes de Vuelo Computarizados (CFP)
Los sistemas modernos automatizan estos cálculos, proporcionando un registro con:
*   **Zone Fuel**: Combustible para cada tramo.
*   **Min Fuel**: Mínimo regulatorio.
*   **Take-off Fuel**: Combustible real a bordo al despegue.
*   **Burn-off**: Consumo esperado.
