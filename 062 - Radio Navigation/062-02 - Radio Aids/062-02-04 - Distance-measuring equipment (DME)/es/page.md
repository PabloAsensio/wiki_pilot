---
title: "Radionavegación: Equipo de Medicion de Distancia (DME)"
description: "Comprende principios de DME, distancia inclinada y uso operativo con VOR e ILS."
keywords:
    - "equipo de medicion de distancia"
    - "distancia inclinada dme"
    - "radionavegacion"
---

# Radionavegación: Equipo de Medicion de Distancia (DME)

El **DME (Distance Measuring Equipment)** es un sistema de radar secundario que proporciona la distancia entre una aeronave y una estación terrestre. Opera en la banda **UHF (962 - 1213 MHz)**.

## Principio de Funcionamiento

Se basa en la medición del tiempo de viaje de pulsos de radio:
1.  El **interrogador** (a bordo) envía pares de pulsos pseudo-aleatorios.
2.  El **transpondedor** (tierra) recibe los pulsos, espera **50 microsegundos** y los retransmite en una frecuencia desplazada en **63 MHz**.
3.  El equipo a bordo mide el tiempo total, resta el retraso de 50 $\mu$s y calcula la distancia.

## Slant Range (Distancia Oblicua)

![Diagrama de Slant Range DME](https://upload.wikimedia.org/wikipedia/commons/7/76/DME_Slant_and_Plan_range.jpg)

El DME mide la distancia directa entre la antena del avión y la estación, no la distancia horizontal sobre el suelo. Esto se conoce como **Slant Range**.
- El error es máximo cuando se vuela directamente sobre la estación, donde el DME indicará la **altitud de la aeronave** (en NM).
- 1 NM $\approx$ 6080 pies.

## Modos de Operación

- **SEARCH (Búsqueda):** El equipo envía hasta **150 pares de pulsos por segundo (ppps)** para engancharse a la estación.
- **TRACK (Seguimiento):** Una vez enganchado, la tasa de pulsos baja (típicamente a **24-30 ppps**) para mantener el seguimiento.
- **MEMORY (Memoria):** Si la señal se pierde momentáneamente, el equipo mantiene la última tasa de cambio de distancia durante **8-10 segundos** antes de volver a modo búsqueda.

## Asociación y Frecuencias

- El DME suele estar **asociado** a un VOR o ILS. El piloto sintoniza la frecuencia VHF del VOR/ILS y el equipo sintoniza automáticamente la frecuencia UHF del DME emparejado.
- Si están asociados, el identificador Morse del DME se escucha cada 30-40 segundos (con un tono más agudo) intercalado con el del VOR.

## Saturación del Faro

Un faro DME puede atender a un máximo de aproximadamente **100 aeronaves** simultáneamente (unas 2700 ppps). Si se supera este límite, el faro se **satura** y prioriza las señales más fuertes (generalmente de las aeronaves más cercanas).

## Cálculos Derivados

- **Groundspeed (GS):** El equipo calcula la velocidad sobre el suelo basándose en la **tasa de cambio de la distancia**. Solo es precisa si se vuela directamente hacia o desde la estación.
- **DME Arc:** Volar manteniendo una distancia constante. En este caso, la GS indicada por el DME será **cero**.
