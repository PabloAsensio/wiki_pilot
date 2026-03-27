---
title: "Sistemas de Protección contra Incendios en Aeronaves: Detección, Extinción y Procedimientos"
description: "Comprende los sistemas de protección contra incendios en aeronaves: tecnologías de detección, lógica de extinción y procedimientos operacionales."
---
# Sistemas de Protección contra Incendios en Aeronaves: Detección, Extinción y Procedimientos

## Sistemas de Detección de Fuego
Los compartimentos de motor y APU usan **detección térmica/calor** (no humo debido al alto flujo de aire).

### 1. Lazo Gaseoso (Neumático)
*   **Principio**: Leyes de los Gases (Presión $\propto$ Temperatura).
*   **Componente**: Tubo de acero inoxidable lleno de gas inerte y material absorbente de gas.
*   **Operación**:
    *   El fuego calienta el tubo.
    *   El gas se expande, **la presión aumenta**.
    *   A una presión predeterminada, un **interruptor de presión** se cierra para activar la alarma.
*   **Monitorización de Fallos**:
    *   Si el tubo tiene una fuga, la presión cae.
    *   Un **interruptor de baja presión** detecta esto y activa una alerta de **Fallo** (inhibe falsas alarmas de fuego).

### 2. Lazo Continuo (Eléctrico)
*   **Principio**: Propiedades de material termistor (Cambio de Resistencia/Capacitancia con calor).
*   **Componente**: Un cable central embebido en material termistor dentro de un tubo conductivo.
*   **Operación**:
    *   Al subir la temperatura, **la resistencia disminuye** (Coeficiente de Temperatura Negativo) o la capacitancia aumenta.
    *   La corriente fluye entre el cable central y el tubo (tierra).
    *   Cuando la corriente excede un umbral, se activa la alarma.
*   **Reinicio**: El sistema se reinicia automáticamente cuando baja la temperatura (fuego extinguido).
*   **Redundancia (Doble Lazo)**:
    *   Aviones modernos usan dos lazos paralelos (A y B).
    *   **Lógica AND**: Ambos lazos deben detectar fuego para activar la advertencia (minimiza falsas alarmas).
    *   **Fallo**: Si una lazo falla (ej. corto a tierra), el sistema puede revertir a operación "Single Loop" o indicar fallo. Una condición de **baja resistencia Y baja capacitancia** típicamente indica un fallo/corto.

## Extinción de Incendios
*   **Mecanismo**: Botellas de descarga de alta tasa (esferas) con agente extintor (reemplazo de Halon).
*   **Activación**: **Cartuchos disparados eléctricamente (Squibs)** rompen un disco frangible para liberar el agente.
*   **Regulaciones (CS 25.1195)**:
    *   Los motores deben tener **dos descargas separadas** disponibles.
    *   Configuración: Típicamente 2 botellas compartidas entre motores, o 2 dedicadas.
        *   *Alimentación cruzada*: La Botella 1 puede descargarse en el Motor 1 O en el Motor 2.

## Procedimiento Operacional
1.  **Detección**:
    *   **Auditiva**: Campana continua/chime o voz ("Engine Fire").
    *   **Visual**: Master Warning (Rojo) + Luz en Palanca de Fuego (Roja).
2.  **Aislamiento (Tirar de la Palanca de Fuego)**:
    *   **Arma** los squibs (cartuchos explosivos).
    *   **Cierra Combustible** (Válvula de Corte LP).
    *   **Cierra Hidráulico** (Válvula de Corte).
    *   **Cierra Sangrado de Aire** (Bleed Valve).
    *   **Dispara el Generador** (Relé de Campo/Breaker).
    *   **Desactiva Reversa**.
3.  **Extinción (Rotar la Palanca)**:
    *   El piloto rota la palanca a Izquierda (Botella 1) o Derecha (Botella 2).
    *   El agente se descarga en el compartimento.

## Prueba de Fuego (Fire Test)
*   Simula una condición de fuego (ej. calentando un elemento de prueba o simulando baja resistencia eléctricamente).
*   **Éxito**: Todas las luces se iluminan + Advertencia auditiva.
*   **Fallo**: Sin indicación o luz específica de "Loop Fault" (si verifica continuidad).
