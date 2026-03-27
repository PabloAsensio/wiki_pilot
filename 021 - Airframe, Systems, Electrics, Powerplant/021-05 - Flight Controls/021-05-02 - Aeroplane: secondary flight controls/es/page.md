---
title: "Controles Secundarios de Vuelo: Flaps, Slats y Sistemas de Trim"
description: "Operación de controles secundarios, lógica de alivio de carga y protección de asimetría en flaps, y arquitectura de trim con salvaguardas de runaway."
---

# Controles Secundarios de Vuelo: Flaps, Slats y Sistemas de Trim

Los controles de vuelo secundarios incluyen dispositivos hipersustentadores (flaps y slats) y sistemas de compensación (trim). Estos dispositivos permiten a la aeronave cambiar su configuración aerodinámica para diferentes fases del vuelo, como el despegue, el aterrizaje y el crucero eficiente.

## Flaps y Slats

Los flaps y slats se utilizan para aumentar la sustentación y la resistencia, permitiendo volar a velocidades más bajas.

- **Tipos:**
    - Las aeronaves ligeras a menudo usan flaps planos (plain) o de curvatura (camber).
    - Las aeronaves de transporte grandes suelen utilizar **flaps Fowler ranurados**.
- **Control y Operación:**
    - Un selector en la cabina envía señales a las computadoras de control, que accionan una **unidad hidromecánica o motor hidráulico**. Este motor mueve un sistema de transmisión para mover las superficies.
    - **Operación de Emergencia:** Si falla el sistema hidráulico principal, la extensión de emergencia a menudo se logra a través de un **motor eléctrico** que impulsa el mismo tren de engranajes, o un sistema hidráulico alternativo. Los sistemas neumáticos **no** se utilizan para flaps ya que carecen de un control preciso.

### Sistemas de Protección

- **Alivio de Carga de Flaps (Limitador de Carga):**
    - **Propósito:** Protege los flaps de daños estructurales debido a cargas de aire excesivas.
    - **Función:** Si la velocidad del aire excede la velocidad máxima de flaps extendidos ($V_{FE}$) para una configuración específica, el sistema **retrae automáticamente los flaps** a una configuración más baja o intermedia. Una vez que la velocidad disminuye, pueden volver a extenderse.
    - **Mecanismo:** Algunos sistemas utilizan "blowback" (el flujo de aire empuja los flaps hacia arriba), mientras que otros utilizan presión hidráulica para moverlos físicamente.

- **Protección de Asimetría:**
    - **Riesgo:** El despliegue asimétrico de los flaps (un lado extendiéndose más que el otro) crea un momento de alabeo peligroso debido a la sustentación y resistencia desiguales.
    - **Función:** Los sensores comparan las posiciones de los flaps en ambas alas con gran precisión. Si se detecta una asimetría, el sistema **detiene los flaps inmediatamente** y alerta a los pilotos.
    - **Importante:** **NO** intenta corregir automáticamente la asimetría (por ejemplo, extendiendo/retrayendo un lado) ya que esto podría agravar la situación si una superficie está atascada.

## Sistemas de Compensación (Trim)

Los sistemas de compensación reducen la carga de trabajo del piloto neutralizando las fuerzas de control.

- **Estabilizador Horizontal Ajustable (THS):**
    - Una superficie de cola horizontal completamente móvil, generalmente accionada por un **gato hidráulico** (tornillo sin fin).
    - Se controla mediante interruptores de compensación, no directamente por la columna de control.

- **Protección contra Trim Runaway:**
    - **Definición:** Movimiento no comandado del compensador, que puede llevar a la pérdida de control.
    - **Característica de Seguridad:** La mayoría de los sistemas de compensación eléctricos requieren que **dos interruptores de palanca** se operen simultáneamente. Un interruptor libera el freno del compensador y el otro alimenta el motor. Esto evita el runaway si un solo interruptor falla o hace corto.
