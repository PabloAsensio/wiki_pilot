---
layout: default
title: "Sistema Yaw Damper: Amortiguación del Dutch Roll y Control de Guiñada"
description: "Comprende la arquitectura del yaw damper, la inestabilidad Dutch roll, el sensado de tasa de guiñada y el filtrado para amortiguar oscilaciones."
keywords:
    - "compass turns"
    - "rumbos magnéticos"
    - "points on the compass"
    - "minimum speed"
parent: "022-08 - Trims – Yaw Damper – Flight Envelope Protection"
grand_parent: "022 - Instrumentation"
nav_order: 2
---

# Sistema Yaw Damper: Amortiguación del Dutch Roll y Control de Guiñada

## Propósito: Contrarrestar el Dutch Roll

El propósito principal del **Yaw Damper** es prevenir el **Dutch Roll** (Balanceo Holandés), un tipo de inestabilidad dinámica común en aviones con ala en flecha.
- **Dutch Roll**: Un movimiento oscilatorio que combina alabeo y guiñada (desfasados). Ocurre porque los aviones de ala en flecha suelen tener una fuerte estabilidad lateral (estabilidad de alabeo) pero una estabilidad direccional (guiñada) más débil.
- **Función**: El Yaw Damper detecta tasas de guiñada no comandadas y aplica correcciones de timón de dirección para amortiguar la oscilación.

## Componentes y Operación del Sistema

El sistema es generalmente independiente pero puede estar integrado con el canal de dirección del Piloto Automático.

1.  **Sensor**: Utiliza un **Giróscopo de Tasa (Rate Gyro)** o datos del **IRS (Sistema de Referencia Inercial)** para detectar la **Tasa de Guiñada (Rate of Yaw)**.
2.  **Computador/Amplificador**: Procesa la señal.
3.  **Actuador**: Mueve la superficie del timón.
    - **Actuador en Serie**: Mueve el timón **sin mover los pedales** (típico del Yaw Damper). El piloto no siente esta retroalimentación.
    - **Actuador en Paralelo**: Mueve los pedales (típico para grandes inputs del AP como alineación en pista, pero no para amortiguación).

### Estado de Operación
- **Siempre Activo**: El Yaw Damper suele estar activo tanto en **vuelo manual como automático**.
- Mejora el confort y previene la inestabilidad (que podría llevar a la pérdida de control).

## Filtro Dutch Roll

Un componente crítico es el **Filtro Dutch Roll** (Filtro Pasa-Alta o Pasa-Banda).

- **Problema**: En un viraje coordinado, el avión tiene una tasa de guiñada constante. Si el Yaw Damper simplemente combatiera *cualquier* tasa de guiñada, pelearía contra el viraje del piloto.
- **Solución**: El filtro distingue entre:
    - **Virajes Estables (Baja Frecuencia)**: El filtro bloquea estas señales. La salida es cero. El timón no pelea el viraje.
    - **Dutch Roll (Alta Frecuencia/Oscilación)**: El filtro deja pasar estas señales. La tasa de guiñada cambia constantemente (derivada $\neq$ 0). El actuador amortigua el movimiento.

> **Resumen**: El Yaw Damper se opone a los *cambios* en la tasa de guiñada (oscilaciones) pero permite tasas de guiñada estables (virajes).
