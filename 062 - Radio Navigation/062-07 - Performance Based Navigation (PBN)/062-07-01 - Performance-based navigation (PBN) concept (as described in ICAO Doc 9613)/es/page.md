---
title: "Concepto PBN (ICAO Doc 9613)"
description: "Estudia el concepto PBN y su marco principal segun ICAO Doc 9613."
keywords:
    - "concepto pbn"
    - "icao doc 9613"
    - "navegacion basada en prestaciones"
---

# Concepto PBN (ICAO Doc 9613)

El concepto PBN (Navegación Basada en la Performance) especifica que los requisitos de rendimiento del sistema RNAV de la aeronave se definan en términos de precisión, integridad, disponibilidad, continuidad y funcionalidad, necesarios para las operaciones propuestas en el contexto de un concepto de espacio aéreo particular.

## Componentes del PBN
El PBN se basa en tres componentes principales:
1.  **Infraestructura de Ayudas a la Navegación (NAVAID)**: Puede ser terrestre (VOR, DME) o espacial (GNSS).
2.  **Especificación de Navegación**: Define los requisitos de rendimiento (ej. RNAV 1, RNP 4).
3.  **Aplicación de Navegación**: El uso de una especificación y la infraestructura para rutas o procedimientos específicos.

## Factores de Rendimiento
*   **Precisión (Accuracy)**: La diferencia entre la posición estimada y la posición real. Se expresa a menudo como el error lateral permitido el 95% del tiempo (ej. RNP 1 = 1 NM).
    *   **TSE (Total System Error)**: Suma de PDE (Path Definition Error), FTE (Flight Technical Error) y NSE (Navigation System Error).
*   **Integridad (Integrity)**: La confianza en la corrección de la información y la capacidad de alertar de fallos en un tiempo razonable.
*   **Continuidad (Continuity)**: La capacidad del sistema para realizar su función sin interrupciones no programadas durante la operación.
*   **Disponibilidad (Availability)**: El porcentaje de tiempo que el sistema está utilizable.
*   **Funcionalidad**: Las funciones requeridas del sistema (ej. RF legs, Baro-VNAV).

## Ámbito del PBN
*   **Fases Oceánica, En Ruta y Terminal**: PBN se limita a operaciones con requisitos de rendimiento lateral **lineal**.
*   **Fase de Aproximación**: PBN acomoda operaciones con guía lateral tanto **lineal** (LNAV) como **angular** (LPV, similar a un ILS).

## Ventajas del PBN
*   Reduce la necesidad de mantener rutas y procedimientos específicos para cada sensor.
*   Evita el desarrollo de operaciones específicas para cada nueva tecnología.
*   Permite un uso más eficiente del espacio aéreo (rutas más directas, ahorro de combustible).
*   Facilita el proceso de aprobación operacional.

## Diferencia entre Datos Crudos y Computados
*   **Datos Crudos (Raw Data)**: Navegación convencional basada en indicaciones directas de ayudas terrestres (VOR, NDB).
*   **Datos Computados (Computed Data)**: Navegación PBN donde el sistema calcula la posición integrando múltiples sensores (GNSS, IRS, DME/DME) y valida la consistencia de los datos.
