---
title: "Radionavegación: Sistemas de Aumentación GNSS"
description: "Comprende aumentacion terrestre, satelital y embarcada para mejorar precisión GNSS."
keywords:
    - "aumentacion gnss"
    - "gbas sbas abaas"
    - "integridad de navegacion"
---

# Radionavegación: Sistemas de Aumentación GNSS

Los sistemas de aumentación tienen como objetivo mejorar la precisión, integridad, disponibilidad y continuidad de la señal GNSS básica para cumplir con los requisitos de la aviación civil, especialmente en fases críticas como la aproximación.

## ABAS (Aircraft-Based Augmentation System)
Sistemas basados en la aeronave que utilizan redundancia de satélites o sensores a bordo.

### RAIM (Receiver Autonomous Integrity Monitoring)
Técnica donde el receptor GNSS utiliza satélites adicionales para verificar la consistencia de la solución de navegación.
*   **Fault Detection (FD)**: Requiere mínimo **5 satélites**. Detecta un fallo pero no identifica el satélite.
*   **Fault Detection and Exclusion (FDE)**: Requiere mínimo **6 satélites**. Detecta y excluye el satélite defectuoso.
*   El uso de ayuda barométrica (Baro-aiding) puede reducir el número de satélites requeridos en 1.

### AAIM (Aircraft Autonomous Integrity Monitoring)
Utiliza sensores a bordo para verificar la posición GNSS.
*   **Sensores típicos**: Altímetro barométrico, IRS (Sistema de Referencia Inercial).
*   Permite mantener la integridad incluso con menos satélites visibles.

## SBAS (Satellite-Based Augmentation System)
Sistemas de cobertura amplia (continental) que utilizan satélites geoestacionarios.
*   **Ejemplos**: **EGNOS** (Europa), **WAAS** (EE.UU.), MSAS (Japón), GAGAN (India).

### Funcionamiento
1.  Una red de estaciones de referencia en tierra (con posición conocida) monitorea las señales GNSS.
2.  Calculan correcciones (reloj, efemérides, ionosfera) y datos de integridad.
3.  Envían estos datos a una estación maestra, que los sube a satélites geoestacionarios.
4.  Los satélites geoestacionarios retransmiten la señal a los usuarios en la misma frecuencia **L1** del GPS.

### Beneficios
*   **Integridad**: Alerta de fallos en **6 segundos** (frente a horas en GPS estándar).
*   **Precisión**: Mejora la precisión horizontal y vertical.
*   **Disponibilidad**: Los satélites SBAS actúan como satélites GNSS adicionales (ranging source).
*   **Operaciones**: Permite aproximaciónes **LPV** (Localiser Performance with Vertical Guidance) con mínimos de hasta 200 ft (equivalente a CAT I).

## GBAS (Ground-Based Augmentation System)
Sistemas de cobertura local (aeropuerto) que utilizan una estación terrestre. También conocido como **LAAS** (Local Area Augmentation System).

### Funcionamiento
1.  Receptores de referencia en el aeropuerto (posición precisa conocida) miden los errores de los satélites GNSS.
2.  La estación terrestre calcula correcciones diferenciales.
3.  Transmite las correcciones, datos de integridad y datos de la trayectoria de aproximación a las aeronaves mediante una transmisión de datos en **VHF (VDB - VHF Data Broadcast)**.

### Características
*   **Cobertura**: Aproximadamente **20-30 km** (o 20 NM) desde la estación.
    *   +/- 35° hasta 15 NM.
    *   +/- 10° entre 15 y 20 NM.
*   **GLS (GBAS Landing System)**: Permite aproximaciónes de precisión (CAT I, II, III) utilizando GNSS.
*   **FAS Data Block**: Bloque de datos del Segmento de Aproximación Final que define la trayectoria geométrica de la aproximación (similar al ILS pero virtual).
*   **Canal**: Se selecciona mediante un código de canal de 5 dígitos.

### Diferencias Clave
*   **SBAS**: Cobertura amplia (continental), correcciones vía satélite, aproximaciónes LPV (APV).
*   **GBAS**: Cobertura local (aeropuerto), correcciones vía VHF, aproximaciónes GLS (Precisión).
