---
layout: default
title: "Sistema Autothrust: Modo SPEED, Modo THRUST y Protecciones de Vuelo"
description: "Comprende la lógica del autothrust/autothrottle: modos SPEED y THRUST, diferencias Boeing/Airbus y protecciones de velocidad y alpha floor."
keywords:
    - "minimum speed"
    - "flight level"
    - "rumbos magnéticos"
    - "compass turns"
parent: "022-09 - Autothrust – Automatic Thrust Control System"
grand_parent: "022 - Instrumentation"
nav_order: 1
---

# Sistemas de Empuje Automático (Autothrust)

## Propósito y Principios

El sistema de **Autothrust** (Airbus) o **Autothrottle** (Boeing) automatiza el control de la potencia de los motores. Establece el empuje requerido para satisfacer las demandas de la fase de vuelo actual, reduciendo la carga de trabajo del piloto y optimizando la eficiencia de combustible.

- **Parámetros de Control Primarios**:
    - **N1**: Velocidad de rotación del compresor de baja presión (Fan). Usado en la mayoría de turbofans de alto índice de derivación (ej. CFM56).
    - **EPR (Engine Pressure Ratio)**: Relación de presión entre la descarga de la turbina y la entrada del compresor. Usado en algunos motores (ej. Rolls-Royce).

## Modos de Operación

El sistema opera en dos modos fundamentales distintos, dependiendo de cómo el Piloto Automático (AP) esté controlando el cabeceo del avión.

### 1. Modo SPEED (Control de Velocidad)
- **Función**: El A/THR varía el empuje del motor para mantener una **Velocidad Objetivo** seleccionada (IAS o Mach).
- **Uso**: Se usa cuando la trayectoria (perfil vertical) del avión está fijada por el AP.
    - **Vuelo Nivelado**: AP mantiene Altitud (`ALT HOLD`) $\rightarrow$ A/THR mantiene Velocidad (`SPEED`).
    - **Ascenso/Descenso con V/S**: AP mantiene una Tasa de Ascenso/Descenso específica (`V/S`) $\rightarrow$ A/THR ajusta el empuje para mantener la Velocidad (`SPEED`).
    - **Aproximación**: AP sigue la Senda de Planeo (`G/S`) $\rightarrow$ A/THR mantiene Velocidad (`SPEED`).

### 2. Modo THRUST (Control de Empuje)
- **Función**: El A/THR establece un **Régimen de Empuje Fijo** (ej. Máximo Ascenso, Ralentí, Despegue). El AP controla la velocidad ajustando el cabeceo del avión ("Speed on Pitch").
- **Uso**: Se usa durante grandes cambios de altitud para maximizar la eficiencia.
    - **Ascenso (Level Change / Open Climb)**: A/THR fija **Empuje de Ascenso** (`N1`, `THR CLB`) $\rightarrow$ AP varía el cabeceo para mantener la Velocidad.
    - **Descenso (Level Change / Open Descent)**: A/THR fija **Empuje de Ralentí** (`IDLE`, `THR IDLE`) $\rightarrow$ AP baja el morro para mantener la Velocidad.
    - **Despegue / Motor y Al Aire**: A/THR fija potencia **TO/GA** $\rightarrow$ Piloto/AP vuela una actitud para mantener $V_2$ o velocidad objetivo.

## Variantes de Diseño

### Palancas de Gases Móviles (ej. Boeing)
- Las palancas son movidas por un servomotor y se **mueven físicamente** para coincidir con el empuje comandado por el computador.
- **Ventaja**: Retroalimentación táctil; el piloto "siente" lo que hacen los motores.

### Palancas de Gases Estáticas (ej. Airbus FBW)
- Las palancas permanecen en un **detent** fijo (ej. CL - Climb) durante la operación automática.
- El computador varía la potencia del motor virtualmente.
- **Indicación**: El piloto debe mirar el **FMA** y los instrumentos de motor para conocer el empuje real. Para desconectar, las palancas deben igualarse a la indicación actual (o moverse a Idle).

## Protecciones

- **Alpha Floor (Airbus)**: Si el Ángulo de Ataque aumenta peligrosamente, el A/THR comanda automáticamente empuje **TO/GA**, incluso si el sistema estaba apagado.
- **Protección de Límites**: El sistema evita que los motores excedan la línea roja (límites de $N_1$ o EGT).
- **Protección de Velocidad**: Evita seleccionar velocidades por debajo de $V_{LS}$ (Velocidad Seleccionable Más Baja) o por encima de $V_{max}$.
