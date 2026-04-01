---
title: "Indicador de Velocidad Vertical (VSI/IVSI): Principio, Retardo y Error en Viraje"
description: "Aprende cómo VSI e IVSI miden la velocidad vertical con presión estática, incluyendo reducción de lag, comportamiento ante bloqueos y errores por aceleración."
keywords:
  - "altímetro"
  - "presión estática"
  - "altitud de densidad"
  - "vsi"
---
# Indicador de Velocidad Vertical (VSI/IVSI): Principio, Retardo y Error en Viraje

El **Indicador de Velocidad Vertical (VSI)** muestra la tasa de ascenso o descenso en pies por minuto (ft/min) o metros por segundo (m/s).

## Principio de Operación
El VSI mide la **tasa de cambio** de la presión estática.
*   **Cápsula:** Conectada directamente a la toma estática (la presión cambia inmediatamente).
*   **Caja:** Conectada a la toma estática a través de un orificio restringido llamado **unidad dosificadora** (la presión cambia lentamente).
*   **Operación:** Durante un ascenso, la presión dentro de la cápsula cae instantáneamente, mientras que la presión en la caja permanece más alta por un momento debido a la restricción. Esta presión diferencial hace que la cápsula se comprima, indicando un ascenso.

**Conversión aproximada:** $1 \text{ m/s} \approx 200 \text{ ft/min}$.

## VSI Instantáneo (IVSI)
Los VSI convencionales sufren de **retardo** (un retraso de varios segundos). El **IVSI** supera esto utilizando un sistema de **acelerómetro** (amortiguadores/pistones).
*   **Mecanismo:** Al iniciar un ascenso/descenso, la aceleración vertical mueve un pistón, creando un cambio de presión inmediato en la cápsula para mover la aguja antes de que se establezca el diferencial de presión estática.
*   **Error de Giro:** En virajes pronunciados (alabeo > 40°), el acelerómetro puede reaccionar a las fuerzas G, causando indicaciones erróneas.
*   **Turbulencia:** El IVSI puede ser hipersensible en turbulencia; los pilotos deben escanear tendencias en lugar de fluctuaciones instantáneas.

## Bloqueo
Dado que el VSI depende únicamente de la presión estática:
*   **Bloqueo de Estática:** La presión en la cápsula eventualmente se igualará con la presión en la caja (presión atrapada). El instrumento caerá a **cero** independientemente del movimiento vertical real de la aeronave.
*   **Bloqueo de Pitot:** Sin efecto.
