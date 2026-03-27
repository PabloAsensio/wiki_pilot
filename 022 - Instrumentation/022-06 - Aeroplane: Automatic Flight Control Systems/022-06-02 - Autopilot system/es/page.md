---
title: "Modos del Piloto Automático: Sincronización, TO/GA, CWS y Conciencia FMA"
description: "Operación detallada del AP: sincronización de enganche, lógica TO/GA, modos verticales/laterales, CWS y supervisión del FMA."
keywords:
    - "flight level"
    - "minimum speed"
    - "rumbos magnéticos"
    - "compass turns"
---

# Modos del Piloto Automático: Sincronización, TO/GA, CWS y Conciencia FMA

## Conexión y Sincronización del Piloto Automático

Para una transición suave del vuelo manual al automático, el sistema de piloto automático utiliza una **función de sincronización**.
*   **Propósito**: Previene "sacudidas" o movimientos bruscos de los controles al conectarlo.
*   **Mecanismo**: Antes de la conexión, el sistema verifica que la aeronave esté compensada (trimada) y que los comandos internos del piloto automático coincidan con la posición actual de las superficies de control/servos.
*   **Fallo**: Si la sincronización falla, el piloto automático típicamente rechazará la conexión.

## Modos Mixtos: TO/GA (Despegue / Motor y Al Aire)

El modo **Take-Off / Go-Around (TO/GA)** es un modo combinado que involucra tanto al Piloto Automático como al Empuje Automático.
*   **Activación**: Típicamente se activa mediante un interruptor en las palancas de potencia.
*   **Función de Motor y Al Aire (Go-Around)**:
    *   Desconecta los modos de Aproximación (como G/S y LOC).
    *   Comanda una actitud de cabeceo hacia arriba (ej. para un ascenso de 1000-2000 pies/min).
    *   El Empuje Automático avanza a empuje de Go-Around (reducido o límite total).
    *   **Lógica**: El modo go-around comandará un ascenso **independientemente de la altitud de aproximación frustrada** seleccionada en el MCP (demanda un gradiente de ascenso positivo alejándose del suelo).

## Modos Verticales

Los modos verticales controlan el cabeceo/empuje de la aeronave para gestionar la altitud o la trayectoria vertical.
*   **Velocidad Vertical (V/S)**: Mantiene una tasa específica de ascenso/descenso (ej. 1000 pies/min). La velocidad es controlada por el balance de cabeceo/empuje (riesgo potencial de pérdida si el empuje es insuficiente).
*   **Ángulo de Trayectoria de Vuelo (FPA)**: Mantiene un ángulo geométrico específico de ascenso/descenso relativo al horizonte (ej. -3.0°). Ajusta la V/S automáticamente si cambia la velocidad terrestre (GS).
*   **Cambio de Nivel (LVL CHG) / Open Climb/Descent**: El cabeceo controla la velocidad, el empuje se ajusta a Ascenso/Ralentí. Usado para cambios de altitud eficientes.
*   **Mantenimiento de Altitud (ALT)**: Captura y mantiene una altitud barométrica específica.

## Modos Laterales

Los modos laterales controlan el alabeo para gestionar el rumbo o la derrota.
*   **Rumbo (HDG) / Derrota (TRK)**: Sigue un vector seleccionado por el piloto.
*   **LNAV (Navegación Lateral)**: Sigue el plan de vuelo del FMS (ruta de círculo máximo entre waypoints).
*   **VOC/LOC**: Intercepta y sigue señales de navegación por radio.

## Control Wheel Steering (CWS)

**Control Wheel Steering (CWS)** es un modo híbrido disponible en algunas aeronaves.
*   **Operación**: El piloto maniobra el avión manualmente usando la columna de control. Cuando el piloto libera la presión, el piloto automático **mantiene la actitud existente** (cabeceo y alabeo).
*   **Anunciación**: Muestra "CWS P" (Cabeceo) y "CWS R" (Alabeo) en el FMA.
*   **Distinción**: El piloto automático NO sigue comandos internos en este modo; responde a la presión del piloto.

## Conciencia del FMA (Anunciador de Modo de Vuelo)

Es crítico que los pilotos monitoreen el **Flight Mode Annunciator (FMA)** (parte superior del PFD).
*   **Estados No Deseados**: No notar cambios de modo puede llevar al peligro. Ejemplo: Intentar capturar una Senda de Planeo (G/S) antes de capturar el Localizador (LOC) puede resultar en un descenso hacia espacio aéreo no protegido.
*   **Ley Normal**: En aviones Fly-By-Wire, la "Ley Normal" proporciona protección completa de la envolvente de vuelo. La reversión a "Ley Directa" o "Ley Alterna" degrada estas protecciones.

## Suministro de Energía y Respaldo

*   **Dependencia del ADC**: El Piloto Automático depende del Computador de Datos de Aire (ADC). Un fallo del ADC afecta a todos los sistemas asociados (AP, FD, Autothrust).
*   **Desconexión**: Desconectar el AP (ej. vía desconexión instintiva) activa una advertencia temporal.
