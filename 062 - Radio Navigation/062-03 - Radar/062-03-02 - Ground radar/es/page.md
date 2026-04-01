---
title: "Radar Terrestre"
description: "Aprende uso de radar terrestre primario y secundario en vigilancia ATS."
keywords:
    - "radar terrestre"
    - "vigilancia atc"
    - "radionavegacion"
---

# Radar Terrestre

## Radar de Vigilancia Primario (PSR)

El **PSR (Primary Surveillance Radar)** es el tipo más básico de radar utilizado en tierra para el control de tráfico aéreo.

### Principio de Funcionamiento
Funciona emitiendo pulsos de energía electromagnética desde una antena giratoria y detectando los ecos reflejados por los objetos (aviones, nubes, terreno).

*   **Información Proporcionada**: Proporciona únicamente **posición en 2D**:
    *   **Distancia (Range)**: Calculada midiendo el **tiempo** que tarda el pulso en ir y volver (basado en la velocidad de la luz). Es una distancia oblicua (slant range).
    *   **Marcación (Bearing)**: Determinada por el **azimut** de la antena en el momento de recibir el eco.
*   **Limitaciones**:
    *   No proporciona altitud.
    *   No identifica a la aeronave (no da códigos ni matrículas).
    *   Puede verse afectado por el clima (lluvia, nubes) y el terreno (clutter).

## Radar de Movimiento en Superficie (SMR/ASMR)

El **ASMR (Airport Surface Movement Radar)** o **ASMI (Airfield Surface Movement Indicator)** es un radar de corto alcance diseñado para monitorizar el tráfico en el suelo del aeropuerto.

*   **Función**: Proporcionar a los controladores una imagen clara y detallada de todas las aeronaves y vehículos en las pistas y calles de rodaje, especialmente útil en condiciones de baja visibilidad.
*   **Características**:
    *   **Alta Definición**: Requiere una resolución muy alta para distinguir objetos cercanos.
    *   **Frecuencia Alta**: Opera en frecuencias muy altas (bandas SHF o EHF) para lograr la resolución necesaria con antenas de tamaño razonable.
    *   **Detección de Tamaño**: En sistemas analógicos antiguos, la alta definición permitía estimar el tamaño de la aeronave por el tamaño del eco en la pantalla.
*   **Sistemas Modernos**: Se integran con datos de transpondedor (multilateración) para etiquetar los objetivos con identificación, mejorando la seguridad y eficiencia (A-SMGCS).

## Requisitos de Información ATS

Para proporcionar servicio de vigilancia ATS, la información mínima requerida es:
1.  **Posición** (proporcionada por PSR o SSR).
2.  **Información de Mapa** (referencia de la estructura del espacio aéreo).

Si se dispone de SSR (Radar Secundario), se añade:
*   **Modo A**: Posición 2D + Código de identificación (Squawk).
*   **Modo C**: Posición 3D (añade altitud de presión).
*   **Modo S**: Datos adicionales y enlace de datos selectivo.
