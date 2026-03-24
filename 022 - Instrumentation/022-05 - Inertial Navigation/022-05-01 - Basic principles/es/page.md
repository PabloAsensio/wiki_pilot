---
title: "Principios Básicos"
description: "Fundamentos de los Sistemas de Navegación Inercial (INS) y Sistemas de Referencia Inercial (IRS), incluyendo la integración de la aceleración y tipos de sistemas."
keywords: ["INS", "IRS", "acelerómetros", "giroscopios", "integración", "Schuler tuning", "strap-down"]
---

## Sistema de Navegación Inercial (INS)

Un **Sistema de Navegación Inercial (INS)** es un sistema de navegación autónomo que proporciona información continua sobre la posición, velocidad y actitud de la aeronave sin depender de referencias externas (como radioayudas o GPS).

### Funcionamiento Fundamental
El principio central de un INS es la medición e integración de la **aceleración**:
1.  Los **acelerómetros** miden la aceleración de la aeronave.
2.  **Primera Integración**: Integrar la aceleración con respecto al tiempo da la **velocidad** (Groundspeed).
3.  **Segunda Integración**: Integrar la velocidad con respecto al tiempo da la **distancia** recorrida y la posición relativa al punto de inicio.

### Entradas y Salidas
*   **Entradas Iniciales**: El sistema requiere una **posición inicial** precisa (Latitud/Longitud) antes del vuelo.
*   **Entrada de Datos de Aire**: El INS requiere entrada de **Velocidad Verdadera (TAS)** del Computador de Datos de Aire (ADC) para calcular la **Velocidad del Viento** (resolviendo el triángulo de velocidades: vector Groundspeed vs. vector TAS).
*   **Salidas**: Posición, Derrota (Track), Rumbo Verdadero (True Heading), Velocidad Terrestre (Groundspeed), Dirección/Velocidad del Viento y Actitud (Cabeceo/Alabeo).

## Tipos de Sistemas

### Plataforma Estable (INS)
En los INS tradicionales (1ª generación), los acelerómetros están montados en una **plataforma giro-estabilizada**.
*   **Mecanismo**: La plataforma está montada en giroscopios (gimbals) y aislada de las maniobras de la aeronave.
*   **Orientación**: Motores de torque mantienen la plataforma **nivelada** (perpendicular a la vertical local) y **alineada con el Norte Verdadero**.
*   **Sensores**:
    *   **Acelerómetros (2)**: Orientados Norte-Sur y Este-Oeste.
    *   **Giróscopos**: Detectan el movimiento de la plataforma para accionar los motores y mantener la alineación.

### Sistema "Strap-down" (IRS)
Las aeronaves modernas utilizan un **Sistema de Referencia Inercial (IRS)**, que es un sistema "strap-down" (adosado).
*   **Mecanismo**: Los sensores están fijados rígidamente a la estructura de la aeronave. No hay gimbals.
*   **Sensores**:
    *   **3 Acelerómetros**: Miden la aceleración a lo largo de los ejes del cuerpo del avión (Longitudinal, Lateral, Vertical).
    *   **3 Giróscopos Láser de Anillo (RLG)**: Miden las tasas angulares de rotación (Cabeceo, Alabeo, Guiñada).
*   **Operación**: Un computador crea matemáticamente una "plataforma estable" procesando los datos de tasa para resolver las aceleraciones de los ejes del cuerpo en componentes Norte/Sur y Este/Oeste.
*   **Ventajas**: Mayor fiabilidad (sin partes móviles/estado sólido), mayor precisión, menos mantenimiento, "arranque" instantáneo (luz láser).

## Errores

Los errores del INS se clasifican en errores acotados y no acotados (acumulativos).

### Errores Acotados (Schuler Tuning)
*   **Comportamiento**: Estos errores oscilan y no crecen continuamente con el tiempo. Tienden a volver a cero durante un ciclo.
*   **Periodo Schuler**: El periodo de oscilación es de **84.4 minutos**.
*   **Causas**: Inclinación de la plataforma, desalineación inicial, errores de integración en la primera etapa.

### Errores No Acotados (Acumulativos)
*   **Comportamiento**: Estos errores crecen principalmente con el **tiempo**.
*   **Deriva Inercial**: El error de posición radial generalmente aumenta a una tasa de:
    *   **1 - 2 NM/h** para INS mecánicos antiguos.
    *   Significativamente menos para IRS Láser modernos.
*   **Causas**:
    *   **Errores de Derrota/Posición**: Desalineación en azimut, deriva del giróscopo (wander).
    *   **Errores de Distancia**: Wander del giróscopo de nivelación, errores del integrador de segunda etapa.

### Tabla comparativa

| Característica | Plataforma Estable (INS) | Strap-down (IRS) |
| :--- | :--- | :--- |
| **Montaje** | Plataforma en gimbals aislada del avión | Fijado a la estructura (fuselaje) |
| **Giróscopos** | Giróscopos mecánicos de tasa-integración | Giróscopos Láser de Anillo (RLG) - Estado Sólido |
| **Alineación** | Nivelación mecánica y torques | Cálculo matemático |
| **Mantenimiento** | Alto (partes móviles) | Bajo (Estado sólido) |
| **Precisión** | Buena | Excelente |
