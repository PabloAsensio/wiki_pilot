---
title: "Computador de Datos de Aire (ADC): Entradas, Salidas y Lógica de Cálculo de TAS"
description: "Aprende la arquitectura del ADC en ATPL Instrumentación: entradas pitot-estáticas y TAT, derivación de SAT, cálculo de TAS y distribución de datos a sistemas."
keywords:
    - "altitud de densidad"
    - "densidad del aire"
    - "altímetro"
    - "adc"
---
# Computador de Datos de Aire (ADC): Entradas, Salidas y Lógica de Cálculo de TAS

El **Computador de Datos de Aire (ADC)** es un ordenador digital que procesa las entradas de varios sensores para calcular parámetros de vuelo precisos para los instrumentos y sistemas de vuelo (EFIS, FMS, AFCS, Transpondedor, etc.).

## Entradas
El ADC recibe datos brutos de:
1.  **Presión Total ($P_t$):** De los tubos Pitot.
2.  **Presión Estática ($P_s$):** De las tomas estáticas.
3.  **Temperatura Total del Aire (TAT):** De sondas de temperatura (ej. Rosemount).
4.  **Ángulo de Ataque (AoA):** De veletas/sondas alfa.

## Salidas
Basándose en estas entradas, el ADC calcula:
*   **Altitud:** Altitud de Presión, Altitud corregida barométricamente.
*   **Velocidad:** IAS, CAS, **TAS**, Número de Mach.
    *   *Nota:* El ADC es esencial para calcular la **TAS**, ya que compensa los errores de posición, compresibilidad y **densidad** utilizando la SAT derivada de la entrada TAT. ($TAS = f(CAS, P_s, SAT)$).
*   **Temperatura:** **SAT** (Temperatura Estática del Aire) se calcula a partir de la TAT y el número de Mach.
*   **Avisos:** Exceso de velocidad (VMO/MMO), avisos de pérdida.

## Redundancia
Las aeronaves modernas suelen poseer dos ADC independientes (ADC 1 y ADC 2) alimentados por sensores independientes.
*   **Fallo:** Las instalaciones de conmutación permiten que los instrumentos se alimenten del ADC alternativo si uno falla.
*   **Reserva:** Los instrumentos de reserva (ASI, Altímetro) suelen tener sus propias fuentes directas de pitot/estática, separadas del sistema ADC.

## Cálculo Clave
El ADC calcula la **Temperatura Estática del Aire (SAT)**, que no se puede medir directamente en vuelo. Utiliza la **TAT** medida y el número de Mach para derivar la SAT, que luego se usa para calcular la **Velocidad Verdadera (TAS)**.
