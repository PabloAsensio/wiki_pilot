---
title: "Vuelo por Cable (FBW)"
description: "Sistemas de control de vuelo electrónicos y protección de la envolvente de vuelo."
keywords: ["fly-by-wire", "computadora de control de vuelo", "protección", "alpha floor", "stick pusher"]
---

# Vuelo por Cable (FBW)


## Concepto
Reemplaza los enlaces mecánicos (cables/varillas) con señales eléctricas.
*   Input del Piloto -> Computadora -> Actuador -> Superficie de Control.
*   Las computadoras pueden modificar los inputs para asegurar estabilidad y prevenir exceder límites.

## Protección de la Envolvente de Vuelo
Los sistemas FBW (como las Leyes de Airbus) previenen que el piloto entre en pérdida o sobre-esfuerce la aeronave.
1.  **Protección de Alta Velocidad**: Automáticamente pica arriba o reduce empuje para prevenir exceso de velocidad.
2.  **Protección de Alto Ángulo de Ataque (Protección Alpha)**:
    *   **Alpha Floor**: Aplica automáticamente empuje TO/GA si la velocidad/AoA se vuelve críticamente peligrosa.
    *   **Alpha Max**: Limita el máximo AoA que el piloto puede comandar.
3.  **Protección de Ángulo de Banqueo**: Limita el ángulo de banqueo (ej. a 67° o 33°).
4.  **Protección de Factor de Carga**: Limita la carga G (ej. +2.5g / -1.0g).

## Ley Normal vs Ley Directa
*   **Ley Normal**: Protecciones completas activas.
*   **Ley Directa**: Sin protecciones. Relación directa palanca-superficie. Ocurre si fallan múltiples computadoras/sensores.
