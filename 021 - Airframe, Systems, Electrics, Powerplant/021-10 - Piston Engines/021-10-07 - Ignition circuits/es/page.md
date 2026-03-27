---
title: "Circuitos de Encendido en Motores de Pistón: Magnetos y Acoplamiento por Impulso"
description: "Estudia el funcionamiento de los circuitos de encendido por magneto, el acoplamiento por impulso y la lógica de puesta a tierra para una operación segura."
---
# Circuitos de Encendido en Motores de Pistón: Magnetos y Acoplamiento por Impulso

Una **magneto** es un generador eléctrico autónomo accionado por el motor, diseñado para suministrar alto voltaje a las bujías. No requiere una batería externa para funcionar, lo que la hace una fuente de ignición independiente y fiable para motores de aviación.

## Construcción y Funcionamiento

La magneto consta de un imán permanente giratorio y dos bobinados:
*   **Bobinado Primario**: Pocas vueltas de hilo **grueso** (Baja Tensión).
*   **Bobinado Secundario**: Muchas vueltas de hilo **fino** (Alta Tensión).

### Principio de Funcionamiento
1.  Al girar el imán, induce corriente en el bobinado primario.
2.  Un **ruptor** (accionado por leva) interrumpe el circuito primario.
3.  Esta interrupción causa un **colapso rápido del campo magnético**.
4.  El campo colapsado induce un **voltaje muy alto** en el bobinado secundario.
5.  Un **distribuidor** dirige este pulso de alto voltaje a la bujía correcta mediante cables de alta tensión.

## Acoplamiento por Impulso (Impulse Coupling)

A bajas revoluciones (durante el arranque), la magneto gira demasiado lento para producir una chispa fuerte. Se utiliza un **Acoplamiento por Impulso** para solucionar esto:
*   **Mecanismo**: Un embrague cargado por resorte entre el eje del motor y el de la magneto.
*   **Función 1 (Retraso)**: Retrasa la chispa para asegurar que la ignición ocurra después del Punto Muerto Superior (evitando el retroceso).
*   **Función 2 (Aceleración)**: Tensa el resorte y lo libera rápidamente, haciendo girar la magneto lo suficientemente rápido para generar una chispa fuerte para el arranque.
*   Una vez arranca el motor, la fuerza centrífuga desacopla el mecanismo.

## Interruptor de Encendido y Puesta a Tierra (Massa)

A menudo se hace referencia a la prueba de magnetos ("Mag Check") o prueba de corte ("Dead Cut").
*   **Interruptor OFF**: El interruptor de encendido funciona **poniendo a tierra (masa) el circuito primario**. Esto detiene la generación de alto voltaje.
*   **Interruptor ON**: Se rompe la conexión a tierra, permitiendo que los platinos controlen el circuito.
*   **Cable de Tierra Roto**: Si el cable de tierra se rompe, la magneto está **permanentemente ENCENDIDA** ("Caliente"). El motor no se detendrá al girar la llave a OFF.
    *   **Peligro**: ¡La hélice está viva! Moverla podría arrancar el motor.
    *   **Acción**: Si el motor no se detiene con la llave, párelo cortando la mezcla de combustible (Idle Cut-Off).
