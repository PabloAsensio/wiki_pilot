---
title: "Diseño y Arquitectura del FMS"
---

## Descripción General

El **Sistema de Gestión de Vuelo (FMS)** es un componente fundamental de la aviónica moderna que reduce la carga de trabajo de la tripulación automatizando las tareas de navegación, optimización del rendimiento y planificación del vuelo. En la terminología de Airbus, a menudo se conoce como **Sistema de Gestión y Cálculo de Vuelo (FMGS)**.

La funcionalidad principal del sistema implica gestionar la **trayectoria 4D** de la aeronave (Lateral, Vertical y Tiempo) y optimizar el rendimiento (consumo de combustible, velocidad, altitud).

## Arquitectura Dual del FMS

Las aeronaves comerciales modernas suelen emplear una arquitectura **Dual FMS**, que consta de dos Ordenadores de Gestión de Vuelo (FMC) y dos Unidades de Visualización y Control (CDU/MCDU).

### Modos de Operación

1.  **Modo Dual (Normal):**
    *   Ambos FMC calculan operaciones de forma independiente y se sincronizan a través de un **bus de comunicación cruzada (cross-talk)**.
    *   Un FMC actúa como **Maestro**, el otro como **Esclavo**.
    *   Los datos introducidos en una MCDU se propagan a ambas.
    *   El FMC Maestro envía comandos al piloto automático, director de vuelo y autothrottle.

2.  **Modo Independiente:**
    *   Se selecciona automáticamente si hay un **desacuerdo significativo** entre los dos FMC (p. ej., diferentes versiones de bases de datos).
    *   El bus de comunicación cruzada se desconecta efectivamente; hay **cero comprobación cruzada**.
    *   Cada FMC controla independientemente las pantallas (ND/PFD) de su lado.

3.  **Modo Único (Single):**
    *   Se selecciona automáticamente si **falla un FMC**.
    *   El FMC operativo restante controla las pantallas y periféricos de ambos lados.
    *   *Implicación:* Se pierde la redundancia y algunas operaciones (como ciertos procedimientos RNP/RNAV o categorías de Autoland) pueden degradarse.

### Escenarios de Falla

*   **Falla de FMC:** El sistema revierte a **Modo Único**. La tripulación utiliza el FMC restante para ambos lados.
*   **Falla de CDU/MCDU:** El sistema generalmente permanece en **Modo Dual**. La tripulación puede controlar ambos FMC utilizando la CDU funcional restante.
*   **Falla del Bus Cross-talk:** El sistema revierte a **Modo Independiente**.

## Funciones Principales

El FMS proporciona cuatro categorías principales de asistencia:

1.  **Navegación y Guía:**
    *   Navegación Lateral y Vertical (LNAV/VNAV).
    *   Definición de una trayectoria 4D (Latitud, Longitud, Altitud, Tiempo).
    *   Sintonización automática (**Autotuning**) de frecuencias de radionavegación (VOR, DME, ILS).
    *   **Función Overfly:** Obliga a la aeronave a volar directamente sobre un waypoint antes de virar, en lugar de anticipar el viraje para cortar la esquina (Fly-by).

2.  **Planificación de Vuelo:**
    *   Creación y modificación de planes de vuelo (waypoints, aerovías, procedimientos).
    *   Predicción de trayectoria.

3.  **Cálculos de Rendimiento:**
    *   Optimización de velocidades, altitudes y consumo de combustible.
    *   Cálculos para configuraciones específicas (p. ej., Motor Inoperativo).
    *   Determinación de velocidades-V y Centro de Gravedad (en algunos sistemas).

4.  **Determinación de Posición:**
    *   El FMS calcula una posición "Mezcla IRS/GPS/Radio" utilizando un **Filtro de Kalman**.
    *   **Entradas:** IRS (Inercial, más confiable/disponible), GPS (Más preciso), DME/DME, VOR/DME, LOC.
    *   Típicamente se da prioridad a la actualización **GPS** debido a su alta precisión.

## Integración con la Aeronave

*   **Autothrottle:** El FMS requiere un sistema de autothrottle para gestionar completamente los perfiles de navegación vertical (VNAV) (gestionando objetivos de velocidad y empuje).
*   **Bases de Datos:** El FMS depende de bases de datos de navegación y rendimiento que deben estar actualizadas (ciclos AIRAC).
*   **Enlace de Datos:** Aunque la MCDU a menudo sirve como interfaz para ACARS/CPDLC, estas son funciones de comunicación separadas, no funciones principales de navegación FMS.

## Tabla Resumen: Modos FMS

| Modo | Condición de Activación | Estado |
| :--- | :--- | :--- |
| **Dual** | Operación Normal | Lógica Maestro/Esclavo, sincronizada vía cross-talk. |
| **Independiente** | Desacuerdo de Datos | Desacoplado, sin cross-talk, cálculos separados. |
| **Único** | Falla de FMC | Un FMC controla ambos lados (Redundancia perdida). |
