---
layout: default
title: "Protección de la Envolvente de Vuelo (FEP): Pérdida, Overspeed y Límites G"
description: "Estudia la lógica de protección de envolvente en aeronaves convencionales y FBW: protección alpha, overspeed, límites de actitud y factor de carga."
keywords:
    - "minimum speed"
    - "flight level"
    - "rumbos magnéticos"
    - "compass turns"
parent: "022-08 - Trims – Yaw Damper – Flight Envelope Protection"
grand_parent: "022 - Instrumentation"
nav_order: 3
---

# Protección de la Envolvente de Vuelo (FEP): Pérdida, Overspeed y Límites G

## Concepto y Propósito

Los sistemas de **Flight Envelope Protection (FEP)** sirven para monitorizar y restringir los parámetros de vuelo de la aeronave asegurando que permanezcan dentro de los límites estructurales y aerodinámicos seguros.

- **Objetivo**: Permitir al piloto usar todas las capacidades del avión sin miedo a entrar en un estado inseguro (pérdida, exceso de carga, exceso de velocidad).
- **Implementación**:
    - **Aviones Convencionales**: A menudo limitado a advertencias (Stick Shaker) o intervenciones mecánicas simples (Stick Pusher). La acción correctiva depende en gran medida del piloto.
    - **Aviones Fly-By-Wire (FBW)**: Los Computadores de Control de Vuelo (FCC) procesan las entradas del piloto y evitan activamente que las superficies de control se muevan de forma que excedan los límites. Esto se conoce como **"Protección Dura" (Hard Protection)**.

## Protecciones Clave

1.  **Protección de Pérdida (Alto Ángulo de Ataque - AoA)**
    - **Advertencia**: Stick Shaker (vibra la columna para simular el bataneo pre-pérdida).
    - **Prevención (Convencional)**: Stick Pusher (mecánicamente empuja el morro abajo).
    - **Prevención (FBW)**:
        - **Alpha Prot**: El sistema comanda activamente morro abajo para evitar que el AoA aumente.
        - **Alpha Floor**: El Autothrust comanda automáticamente potencia TO/GA si el AoA es crítico.
        - **Alpha Max**: El avión no puede exceder el AoA máximo incluso con la palanca totalmente atrás.

2.  **Protección de Exceso de Velocidad (Overspeed)**
    - Previene exceder $V_{MO}$ (Velocidad Operativa Máxima) o $M_{MO}$ (Mach Operativo Máximo).
    - **Acción**:
        - Inhibe el trim de morro abajo.
        - Comanda una maniobra de pitch-up (morro arriba) para cambiar velocidad por altitud.
        - Reduce el empuje (si A/THR está activo).
    - **Override**: En escenarios de descenso de emergencia, los pilotos pueden necesitar anular protecciones "suaves", pero las "duras" suelen permanecer para evitar daños estructurales.

3.  **Protección de Actitud (Cabeceo y Alabeo)**
    - **Límites de Pitch**: Previene actitudes excesivas de morro arriba (riesgo de pérdida) o morro abajo (picado) (ej. +30° / -15°).
    - **Límites de Bank**: Previene alabeos excesivos (riesgo de espiral), típicamente limitado a 67° en ley normal FBW. Si se suelta la palanca, el avión retorna a un ángulo estándar (ej. 33°).

4.  **Protección de Factor de Carga (G-Load)**
    - Previene sobreesfuerzos en la estructura (sobrecarga).
    - Limita las Gs comandadas (ej. Configuración limpia: +2.5g a -1.0g).

## Protección Suave vs. Dura

- **Protección Suave (Soft)**: Retorna el avión a la envolvente segura o advierte al piloto, pero **puede ser anulada (overridden)** aplicando más fuerza a los controles.
- **Protección Dura (Hard)**: **No puede ser anulada** por el piloto en Ley Normal. El computador limita estrictamente la deflexión de las superficies para mantenerse dentro de la envolvente.

> **Nota**: En caso de fallos de sistema (pérdida de sensores, fallo de computador), los sistemas FBW pueden revertir a **Ley Alternativa** o **Ley Directa**, donde algunas o todas las protecciones se pierden, dejando solo estabilidad básica o control directo.
