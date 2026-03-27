---
title: "Válvula de Flujo y Brújula Giro-Magnética: Modo Esclavo y Modo Libre"
description: "Aprende el principio de detección de la válvula de flujo y la operación de la brújula giro-magnética, incluyendo corrección en modo esclavo y uso en modo libre."
keywords:
	- "rumbos magnéticos"
	- "brújula giro magnética"
	- "magnetic headings"
	- "points on the compass"
---
# Válvula de Flujo y Brújula Giro-Magnética: Modo Esclavo y Modo Libre

La **Válvula de Flujo** (o Detector de Flujo) es un sensor utilizado en sistemas de brújula de lectura remota para detectar la **componente horizontal** del campo magnético terrestre sin las partes móviles y los errores de una brújula de lectura directa.

## Construcción y Operación
Consta de tres brazos dispuestas a 120°, hechas de hierro blando, con bobinas de excitación y de captación.
*   **Detección:** Detecta el campo magnético horizontal electrónicamente.
*   **Ubicación:** Instalada en una ubicación con mínima interferencia magnética de la aeronave (ej. **Punta de ala** o **Estabilizador Vertical**).
*   **Ventaja:** "Siente en lugar de buscar". No gira físicamente para alinearse con el Norte; en su lugar, emite una señal eléctrica que representa el rumbo magnético.

## Brújula Giro-Magnética
La Válvula de Flujo es el elemento sensor de una Brújula Giro-Magnética.
*   **Principio:** Combina la **precisión** a largo plazo de la referencia del norte magnético (Válvula de Flujo) con la **estabilidad** a corto plazo de un giroscopio.
*   **Válvula de Flujo:** Detecta el norte magnético (Referencia a largo plazo).
*   **Giroscopio:** Proporciona estabilidad durante virajes y aceleraciones (Referencia a corto plazo).
*   **Detector de Error y Amplificador:** Compara el rumbo del giroscopio con el de la válvula de flujo y usa un motor de torque para "eslavizar" o corregir la deriva del giroscopio.

## Modos de Operación
1.  **Modo Esclavo (Slaved):** Operación normal. El giroscopio se corrige automáticamente al Norte Magnético mediante las señales de la Válvula de Flujo.
2.  **Modo Libre (Free/DG):** Se usa si falla la válvula de flujo o en regiones de extrema variación/inclinación magnética (cerca de los polos). El giroscopio funciona como un Giro Direccional (DG) estándar y debe verificarse/ajustarse manualmente contra una brújula de reserva periódicamente.
