---
title: "Sistema de Alerta de Altitud: Alertas de Captura/Desviación y Requisitos"
description: "Comprende la lógica de alerta de altitud para captura y desviación, umbrales regulatorios de aplicación e integración de señales ADC/MCP."
keywords:
    - "altitude alert"
    - "flight level"
    - "minimum speed"
    - "altímetro"
---

# Sistema de Alerta de Altitud: Alertas de Captura/Desviación y Requisitos

## Descripción General

El **Sistema de Alerta de Altitud** está diseñado para prevenir "violaciones de nivel" (level busts) alertando a la tripulación de vuelo cuando se aproximan a una altitud seleccionada o se desvían de una altitud asignada.

## Funciones

El sistema proporciona dos tipos principales de alertas:

1.  **Alerta de Adquisición (Aproximación):**
    *   Se activa cuando la aeronave se aproxima a la altitud preseleccionada durante un ascenso o descenso.
    *   Típicamente se activa en un umbral específico antes de alcanzar el objetivo (p. ej., 900 pies o 750 pies antes).
    *   *Indicación:* Visual (luz fija o intermitente/recuadro) y a menudo Auditiva (campanilla momentánea).

2.  **Alerta de Desviación:**
    *   Se activa cuando la aeronave **se desvía** de la altitud seleccionada por más de un límite preestablecido mientras se mantiene un vuelo nivelado.
    *   *Umbrales:* Típicamente **200 pies** (Airbus) o **300 pies** (Boeing).
    *   *Indicación:* Visual (Luz Ámbar intermitente o Recuadro en PFD) y Auditiva (Campanilla continua o repetida).

## Requisitos Legales

Según las regulaciones, el sistema es obligatorio para:
*   Todas las aeronaves **Turborreactores**.
*   Aeronaves propulsadas por turbina con una Masa Máxima de Despegue (MTOM) **superior a 5.700 kg**.
*   Aeronaves propulsadas por turbina capaces de transportar **más de 9 pasajeros**.

## Interfaz del Sistema
*   **Entradas:**
    *   **Altitud Barométrica:** Del Ordenador de Datos de Aire (ADC).
    *   **Altitud Seleccionada:** Establecida por el piloto en el Panel de Control de Modo (MCP) o Unidad de Control de Vuelo (FCU).
*   **Alertas:**
    *   **Visual:** Luz **Ámbar** o Marco Ámbar en la Cinta de Altitud del PFD.
    *   **Auditiva:** Acorde C, Pitido o Campanilla.
