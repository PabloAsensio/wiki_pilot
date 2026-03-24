---
layout: default
title: "022-06-04 - Aeroplane: flight mode annunciator (FMA)"
parent: "022-06 - Aeroplane: Automatic Flight Control Systems"
grand_parent: "022 - Instrumentation"
nav_order: 4
---

# Flight Mode Annunciator (FMA)

## Propósito y Ubicación

El **Flight Mode Annunciator (FMA)** es la interfaz principal para que los pilotos monitoricen el estado del Sistema de Control de Vuelo Automático (AFCS). Actúa como la única fuente de verdad sobre "qué está haciendo el sistema", a diferencia de los interruptores en el panel de control (MCP/FCU), que solo indican lo que el piloto ha *solicitado*.

- **Ubicación**: Típicamente en la parte superior de la Pantalla Principal de Vuelo (PFD).
- **Función**: Muestra el estado de:
  - Activación del Piloto Automático (AP).
  - Estado del Director de Vuelo (FD).
  - Modos y estado del Empuje Automático (A/THR).
  - Capacidades de aterrizaje (ej. CAT III Dual, Autoland).

## Estructura de la Pantalla

El FMA suele dividirse en columnas, de izquierda a derecha (diseño típico Airbus/Boeing):
1.  **Modo de Empuje (Autothrust)**: (ej. `SPD`, `THR CLB`, `IDLE`).
2.  **Modo Vertical**: (ej. `ALT`, `V/S -1000`, `G/S`).
3.  **Modo Lateral**: (ej. `HDG`, `NAV`, `LOC`).
4.  **Capacidad de Aproximación / Estado AP**: (ej. `AP1+2`, `LAND 3`, `SINGLE CH`).

### Estados de los Modos

El FMA distingue entre modos que están controlando activamente la aeronave y modos que están esperando capturar un objetivo.

- **Modos Activados (Engaged/Active)**:
  - Típicamente en **Verde**.
  - Letra más grande o línea superior.
  - Ejemplo: `ALT` (Mantenimiento de altitud), `HDG SEL` (Volando rumbo seleccionado).
- **Modos Armados (Armed)**:
  - Típicamente en **Blanco**, **Cian** o **Ámbar**.
  - Letra más pequeña o línea inferior.
  - Ejemplo: `G/S` (en blanco) significa que la Senda de Planeo está armada pero aún no capturada.

## Importancia Operacional

### Cambios de Modo y Conciencia Situacional
Los pilotos deben monitorizar de cerca el FMA porque no todos los cambios de modo van acompañados de alertas sonoras distintas.
- **Atención Visual**: Cuando un modo cambia (ej. de Armado a Activado), un **recuadro** blanco o verde suele rodear el nuevo modo durante unos segundos (ej. 10s) para atraer la mirada del piloto.
- **Procedimientos Operativos Estándar (SOPs)**: El Pilot Flying (PF) generalmente debe **cantar** cualquier cambio en el FMA (ej. "Speed", "Alt Star", "Glideslope Captured"). El Pilot Monitoring (PM) debe verificar y confirmar ("Check").

### Reversión de Modo
A veces la automatización cambia de modo sin orden del piloto para proteger la aeronave o porque se pierde una señal.
- **Ejemplo**: Si el avión sube en modo `V/S` pero falta empuje, la velocidad cae. Para evitar la entrada en pérdida, el AP puede revertir automáticamente de `V/S` a `Level Change` o `Speed` para bajar el morro.
- Estos cambios no comandados ("Reversiones de Modo") a menudo van acompañados de un aviso sonoro único (ej. "Triple Click") y una indicación parpadeante.

## Consecuencias de Ignorar el FMA

No monitorizar el FMA puede llevar a:
1.  **Estados Indeseados de la Aeronave**: Ej. creer que el AP está en `LNAV` cuando ha revertido a `HDG` por una discontinuidad en el plan de vuelo, haciendo que el avión vuele recto en lugar de virar.
2.  **Confusión**: El piloto puede "pelear" con la automatización si cree que está en un modo cuando realmente está en otro.
3.  **Incidentes de Seguridad**: La mayoría de los accidentes relacionados con la automatización implican "Confusión sobre el modo actual" o "Falta de conciencia de modo (Mode Awareness)".
