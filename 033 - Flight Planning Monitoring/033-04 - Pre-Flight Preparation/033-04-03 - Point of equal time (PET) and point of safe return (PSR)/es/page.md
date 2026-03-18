---
title: "Cálculos de PET y PSR"
description: "Cálculos del punto crítico y punto de no retorno para la planificación de vuelo."
keywords: ["PET", "PSR", "Punto de Tiempo Igual", "Punto de Retorno Seguro", "Punto Crítico", "ETP"]
---

## Punto de Tiempo Igual (PET) / Punto Crítico (CP)
El punto a lo largo de la ruta donde toma el **mismo tiempo** continuar al destino que retornar a la salida (o proceder a un alternativo).
*   Importante para escenarios de Fallo de Motor o Despresurización.
*   **Concepto**: Dado que el viento afecta la Velocidad Terrestre (GS) de manera diferente a la ida vs la vuelta (viento de cara se vuelve de cola), el PET se desplaza **hacia el viento**.
*   **Fórmula**:
    $$
    Distancia_{PET} = \frac{D \times GS_{Retorno}}{GS_{Retorno} + GS_{Destino}}
    $$
    *   $D$: Distancia Total.
    *   $GS_{Retorno}$: Velocidad Terrestre retornando.
    *   $GS_{Destino}$: Velocidad Terrestre continuando.

## Punto de Retorno Seguro (PSR) / Punto de No Retorno (PNR)
El punto más lejano a lo largo de la ruta desde el cual la aeronave puede retornar al aeropuerto de salida (o alternativo) con las reservas de combustible requeridas aún intactas.
*   Más allá de este punto, la aeronave **debe** proceder al destino (u otro alternativo en ruta).
*   **Fórmula**:
    $$
    Tiempo_{PSR} = \frac{Autonomía_{Segura} \times GS_{Retorno}}{GS_{Retorno} + GS_{Ida}}
    $$
    *   $Autonomía_{Segura}$: Autonomía utilizable total menos reservas.
    *   $GS_{Ida}$: Velocidad terrestre de ida.
