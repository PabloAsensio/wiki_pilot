---
title: "Sistemas de Protección de Pérdida (SPS): Stick Pusher y Prevención Activa"
description: "Comprende las estrategias activas de protección contra pérdida: lógica del stick pusher, secuencia tras aviso y diagnóstico entre aviso y protección."
keywords:
  - "stick pusher"
  - "stall protection"
  - "minimum speed"
  - "flight level"
---

# Sistemas de Protección de Pérdida (SPS): Stick Pusher y Prevención Activa

## Descripción General

Mientras que el **Sistema de Aviso de Pérdida (SWS)** proporciona una alerta, el **Sistema de Protección de Pérdida (SPS)** es un mecanismo de seguridad activo diseñado para **prevenir físicamente** que la aeronave entre en una pérdida. Actúa como una barrera final cuando el piloto no reacciona a la advertencia inicial.

## Stick Pusher (Empujador de Palanca)

El componente principal de un SPS es el **Stick Pusher**.

*   **Función:** Aplica mecánicamente una fuerza hacia adelante en la columna de control (entrada de morro abajo del elevador) para reducir forzosamente el Ángulo de Ataque (AoA).
*   **Punto de Activación:** Se activa **después** del aviso de pérdida (Stick Shaker) pero **antes** de que la aeronave exceda el Ángulo de Ataque Crítico ($AoA_{crit}$).
*   **Requisito:** Es típicamente obligatorio en grandes aviones de transporte que exhiben características de pérdida peligrosas (p. ej., "Pérdida Profunda" o "Super Pérdida" a menudo asociada con configuraciones de cola en T) donde la recuperación podría ser difícil o imposible solo para el piloto.

## Otros Métodos de Protección
Dependiendo del tipo de aeronave, un SPS también puede:
*   **Extender Flats/Slats:** Desplegar automáticamente slats de borde de ataque para aumentar el $AoA_{crit}$.
*   **Aumentar Empuje:** Comandar el Autothrottle para aplicar potencia (p. ej., protección Alpha Floor en Airbus).

## Lógica y Diagnóstico del Sistema

Comprender la distinción entre Advertencia y Protección es crucial para analizar escenarios de falla:

*   **Escenario:** La aeronave se acerca a una pérdida. El Stick Pusher se activa (el morro baja), pero **no** hubo alarma audible o vibración previa.
*   **Análisis:** El **Sistema de Protección de Pérdida** está funcionando correctamente (previno la pérdida). El **Sistema de Aviso de Pérdida** (Stick Shaker/Audio) está **inoperativo**.

| Sistema | Componente | Propósito | Acción |
| :--- | :--- | :--- | :--- |
| **SWS** | Stick Shaker / Audio | **Alertar** | Vibra la columna, suena la alarma. |
| **SPS** | Stick Pusher | **Prevenir** | Empuja el morro hacia abajo. |
