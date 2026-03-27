---
title: "Sistemas de Aviso de Pérdida (SWS): Márgenes, Entradas y Alertas"
description: "Estudia el funcionamiento del SWS: márgenes CS-25, lógica basada en AoA, señales táctiles/auditivas/visuales e implicaciones de fallos de sensor."
keywords:
	- "stall warning"
	- "ángulo de ataque"
	- "minimum speed"
	- "flight level"
---

# Sistemas de Aviso de Pérdida (SWS): Márgenes, Entradas y Alertas

## Descripción General

El **Sistema de Aviso de Pérdida (SWS)** es un sistema de seguridad crítico diseñado para alertar a la tripulación de vuelo de una condición inminente de pérdida. Su función principal es proporcionar una advertencia clara y distintiva con suficiente margen para permitir al piloto tomar medidas preventivas antes de que ocurra la pérdida real.

## Regulaciones (CS-25)

Para grandes aviones de transporte, las regulaciones (CS-25.207) dictan criterios de rendimiento específicos para el SWS:

*   **Margen:** La advertencia debe comenzar a una velocidad que exceda la velocidad de pérdida en no menos de **5 nudos** o **5% de CAS** (lo que sea mayor).
*   **Condiciones:** La advertencia debe ser efectiva tanto en vuelo recto como en virajes, y con el tren de aterrizaje y los flaps en cualquier posición normal.
*   **Duración:** La advertencia debe continuar hasta que el ángulo de ataque se reduzca aproximadamente al valor en el que se inició la advertencia.

## Operación del SWS

### Aviones Ligeros
*   **Sensor:** Típicamente una **Veleta Móvil** (Flapper Switch) ubicada en el borde de ataque del ala.
*   **Mecanismo:** A medida que el Ángulo de Ataque (AoA) aumenta, el punto de estancamiento se mueve hacia abajo, causando que el flujo de aire levante la veleta. Esto cierra un microinterruptor.
*   **Alerta:** Zumbador sonoro o luz intermitente en la cabina.
*   **Hielo:** La veleta a menudo se calienta eléctricamente para evitar la acumulación de hielo.

### Aviones de Transporte Grandes
Las aeronaves modernas utilizan un sistema más sofisticado impulsado por ordenadores digitales.

#### Entradas
Para calcular el umbral de pérdida correcto, los ordenadores SWS requieren varias entradas:
1.  **Ángulo de Ataque (Alpha):** La entrada principal, medida por sondas Alpha en el fuselaje.
2.  **Configuración:** **Posición de Flaps y Slats** (los dispositivos hipersustentadores cambian el AoA de pérdida).
3.  **Velocidad Aerodinámica (CAS):** Para asegurar que se cumpla el margen de 5% / 5 kt.
4.  **Lógica Aire/Tierra:** Para inhibir el sistema mientras está en tierra.
5.  **Empuje:** (En algunos sistemas).

#### Tipos de Advertencia
*   **Táctil (Háptico):** **Stick Shaker** (Vibrador de Palanca). Un motor de peso excéntrico hace vibrar la columna de control para simular el bataneo aerodinámico previo a la pérdida.
*   **Auditiva:** Sonidos distintivos (p. ej., sonido de "Cricket", bocina continua) o voz sintética (**"STALL, STALL"**).
*   **Visual:** Luz de Master Warning **Roja** o indicaciones específicas en el PFD.

## Escenarios de Falla
*   **Sonda Alpha Congelada:** Si el sensor AoA se congela (p. ej., debido a hielo) en un valor específico, el ordenador puede no detectar un ángulo de ataque creciente, resultando en que **no se active ninguna advertencia de pérdida**.

## Distinción de la Protección
Es importante distinguir entre **Advertencia** y **Protección**:
*   **Aviso de Pérdida (Stick Shaker):** Alerta al piloto *antes* de la pérdida.
*   **Protección de Pérdida (Stick Pusher):** Empuja físicamente la columna de control hacia adelante para *prevenir* la pérdida si el piloto ignora la advertencia (discutido en la siguiente sección).
