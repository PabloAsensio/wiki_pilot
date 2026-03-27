---
layout: default
title: "Comunicación de Voz y Data-Link: ACARS, CPDLC y D-ATIS"
description: "Estudia la arquitectura de comunicaciones aeronáuticas por voz y enlace de datos, incluyendo ACARS, CPDLC, D-ATIS, DCL y medios VHF/HF/SATCOM."
keywords:
    - "cpdlc"
    - "acars"
    - "flight level"
    - "minimum speed"
parent: "022-10 - Communication Systems"
grand_parent: "022 - Instrumentation"
nav_order: 1
---

# Comunicación de Voz y Data-Link: ACARS, CPDLC y D-ATIS

## ACARS (Aircraft Communication Addressing and Reporting System)

**ACARS** es un sistema de enlace de datos digital para transmitir mensajes cortos entre aeronaves y estaciones terrestres. Desarrollado por **ARINC** a finales de los 70, sigue siendo el estándar de la industria.

- **Propósito**:
    - **AOC (Airline Operational Control)**: Mensajes de compañía (horarios, datos de pasajeros, reportes de mantenimiento).
    - **ATC (Air Traffic Control)**: Autorizaciones, solicitudes, meteorología.
- **Gestión a Bordo**: La **CMU (Communication Management Unit)** gestiona el enrutamiento de mensajes. Se conecta a la MCDU (interfaz), y radios VHF, HF y SATCOM.
- **Terminología**:
    - **Uplink**: Mensaje de Tierra $\rightarrow$ Avión.
    - **Downlink**: Mensaje de Avión $\rightarrow$ Tierra.

## Medios de Transmisión

ACARS y otros sistemas datalink usan varias frecuencias según disponibilidad y ubicación.

1.  **VHF (Very High Frequency)**:
    - **Propiedades**: Operación en línea de visión (Line-of-sight). Alcance terrestre limitado por la curvatura de la Tierra.
    - **Velocidad/Calidad**: Buena calidad, velocidad moderada. Estándar para operaciones continentales/domésticas.
2.  **SATCOM (Comunicación Satelital)**:
    - **Propiedades**: Usa banda UHF. Cobertura global (excepto a veces Polar). **Sin limitación de línea de visión** con estaciones terrestres.
    - **Velocidad/Calidad**: **Tasa de datos más alta**, inmune a interferencia ionosférica. Alta calidad de señal.
3.  **HF (High Frequency)**:
    - **Propiedades**: Largo alcance (Oceánico/Remoto) debido a reflexión ionosférica ("skywave").
    - **Velocidad/Calidad**: **Tasa de datos más baja**, mala calidad debido a estática e interferencia. Usado solo cuando VHF/SATCOM no están disponibles (ej. regiones polares sin satcom Iridium).

## Aplicaciones

### CPDLC (Controller-Pilot Data Link Communications)
Método basado en texto para que pilotos y controladores intercambien mensajes (Autorizaciones, Solicitudes, Reportes).
- **Beneficios**: Reduce congestión de frecuencias, elimina errores de "colación/readback", permite revisar instrucciones complejas.
- **Ejemplos**: Autorizaciones Oceánicas, Modificaciones de ruta, Cambios de frecuencia.

### D-ATIS (Digital ATIS)
- Recibe el mensaje de texto ATIS (Automatic Terminal Information Service) vía enlace de datos.
- Se muestra en la MCDU o se imprime. Elimina la necesidad de escuchar y transcribir la transmisión de audio.

### DCL (Departure Clearance)
- Obtención de la autorización de salida (pre-departure clearance) vía datalink antes del arranque de motores.
- Mejora la eficiencia y reduce la carga de trabajo en rampa.
