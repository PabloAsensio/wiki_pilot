---
title: "Radioaltímetro (RA): Principio FMCW, Integración e Impacto de Fallos"
description: "Estudia el funcionamiento del radioaltímetro, medición FMCW, calibración a geometría de toque e integración con autoland, GPWS/TAWS y TCAS."
keywords:
    - "radio altímetro"
    - "altímetro"
    - "flight level"
    - "minimum speed"
---

# Radioaltímetro (RA): Principio FMCW, Integración e Impacto de Fallos

## Descripción General

El **Radioaltímetro (RA)**, o Radar Altímetro, es un sistema autónomo a bordo que mide la **Altura Verdadera** de la aeronave sobre el terreno inmediatamente debajo de ella (Sobre el Nivel del Terreno - AGL).

## Principio de Operación

*   **Rango de Frecuencia:** Opera en la banda SHF (4200 MHz - 4400 MHz).
*   **Método:** Transmite una **Onda Continua Modulada en Frecuencia (FMCW)** hacia abajo.
*   **Cálculo:** Mide la diferencia de frecuencia entre la onda transmitida y la onda recibida reflejada desde el suelo. Esta diferencia es proporcional al retardo de tiempo y, por tanto, a la altura.
*   **Rango de Operación:** Típicamente indica de **0 a 2.500 pies**. Por encima de esta altitud, la pantalla generalmente se apaga.

## Calibración y Altura Residual

*   **Ubicación de la Antena:** Las antenas están ubicadas en la parte inferior del fuselaje.
*   **Altura Residual:** La distancia vertical entre las antenas y la parte más baja del tren de aterrizaje (ruedas principales).
*   **Indicación:** El sistema está calibrado para indicar **0 pies** cuando las ruedas principales tocan el suelo en la actitud de aterrizaje.

## Integración del Sistema

El Radioaltímetro es un sensor crítico que proporciona datos a múltiples sistemas de la aeronave:

1.  **AFCS (Piloto Automático y Director de Vuelo):**
    *   Esencial para operaciones de **Autoland** (controlando Flare y Rollout).
    *   Desconecta la señal de senda de planeo típicamente a 50 pies.
2.  **Autothrottle (A/T):**
    *   Activa el modo **"RETARD"** durante el aterrizaje (reduciendo el empuje a ralentí a alturas específicas, p. ej., 20-30 pies).
3.  **GPWS / TAWS:**
    *   Fuente primaria de datos de altura para calcular las tasas de aproximación al terreno.
4.  **TCAS / ACAS:**
    *   Se utiliza para **inhibir** ciertos Avisos de Resolución (RAs) cerca del suelo (p. ej., RAs de "Descender" se inhiben por debajo de 1.100 pies AGL).

## Implicaciones Operativas de Fallo

*   **Capacidad Autoland:** La pérdida de un RA degrada típicamente la capacidad de Autoland (p. ej., de Fallo-Operacional a Fallo-Pasivo o prohibiendo el Autoland por completo).
*   **Lecturas Falsas:** Un RA defectuoso que indique una altura baja (p. ej., < 50 pies) durante el crucero podría hacer que el Autothrottle entre erróneamente en modo **RETARD**, reduciendo el empuje a ralentí.
