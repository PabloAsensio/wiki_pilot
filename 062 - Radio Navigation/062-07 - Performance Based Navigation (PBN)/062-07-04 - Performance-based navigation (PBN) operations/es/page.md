---
title: Radionavegacion: Operaciones de Navegacion Basada en Prestaciones
description: Revisa procedimientos operacionales PBN, limitaciones y aplicacion en vuelo.
keywords:
  - operaciones pbn
  - operaciones rnp
  - operaciones de navegacion
---

# Radionavegacion: Operaciones de Navegacion Basada en Prestaciones

Las operaciones PBN se basan en la capacidad del sistema de navegación para mantener una precisión definida y, en el caso de RNP, monitorear y alertar sobre el rendimiento.

## Errores del Sistema de Navegación
La precisión total del sistema se define como **TSE (Total System Error)**. El TSE es la suma geométrica de tres componentes de error independientes:

1.  **PDE (Path Definition Error)**:
    *   Ocurre cuando la trayectoria definida en el sistema RNAV no corresponde con la trayectoria deseada sobre el terreno.
    *   Se considera **despreciable** si la base de datos de navegación es íntegra y está actualizada (ciclo AIRAC válido).
2.  **FTE (Flight Technical Error)**:
    *   Relacionado con la habilidad de la tripulación o del piloto automático para seguir la trayectoria definida.
    *   Incluye errores de centrado del CDI.
    *   Se gestiona mediante procedimientos de la tripulación o el uso del piloto automático.
3.  **NSE (Navigation System Error)**:
    *   Es la diferencia entre la posición estimada por la aeronave y su posición real.
    *   Depende de la precisión de los sensores (GNSS, DME/DME, IRS).

**TSE = PDE + FTE + NSE**

## Monitoreo y Alerta (RNP)
En las especificaciones RNP, el sistema debe monitorear el rendimiento:
*   **ANP (Actual Navigation Performance)** o **EPE (Estimated Position Error)**: Es una estimación estadística del error de posición actual (TSE o NSE dependiendo del contexto, pero funcionalmente representa la incertidumbre de la posición).
*   **RNP (Required Navigation Performance)**: Es el límite de error permitido para la operación (ej. 1.0 NM).
*   **Alerta**: Si **ANP > RNP**, el sistema alerta a la tripulación (ej. "NAV ACCUR DOWNGRAD"). Esto indica que la incertidumbre de la posición excede el límite permitido.

## Procedimientos Operacionales
*   **Base de Datos**: Debe estar actualizada al ciclo **AIRAC** vigente (cada 28 días).
*   **Desviación**: Durante una aproximación, si la desviación excede **media escala** (half-scale deflection), se debe iniciar una aproximación frustrada.
*   **Pérdida de Integridad/Precisión**: Si se recibe una alerta de integridad (ej. RAIM, LOI) o si el ANP excede el RNP antes del FAF, se debe discontinuar la aproximación.
*   **Fallo de Comunicaciones**: No es causa inmediata de frustrada en una aproximación RNP (se siguen los procedimientos de fallo de comunicaciones estándar).
