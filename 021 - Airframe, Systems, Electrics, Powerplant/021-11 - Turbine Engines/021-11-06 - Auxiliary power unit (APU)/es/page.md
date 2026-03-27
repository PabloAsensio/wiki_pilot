---
title: "Unidad de Potencia Auxiliar (APU): Funciones, Control y Protecciones"
description: "Aprende los fundamentos del APU: salidas eléctrica y neumática, secuencia de arranque, controles en cabina y protecciones de apagado automático."
---
# Unidad de Potencia Auxiliar (APU): Funciones, Control y Protecciones

## Propósito y Función
El APU es un pequeño motor de turbina de gas autónomo, típicamente ubicado en el cono de cola de la aeronave.

*   **Salidas Primarias**:
    1.  **Energía Eléctrica**: Mueve un generador (típicamente 115V AC, 400Hz) para alimentar los sistemas del avión en tierra o en vuelo (reserva).
    2.  **Energía Neumática (Sangrado de Aire)**: Suministra aire a alta presión para:
        *   **Arranque de Motores Principales**.
        *   **Aire Acondicionado** (Sistema de Control Ambiental).
        *   Anti-hielo de alas (en algunos aviones, aunque raro).
*   **Beneficios**: Hace al avión independiente de equipos de apoyo en tierra (GPU / Unidad de Arranque Neumático).

## Operación
*   **Fuente de Combustible**: Toma combustible de los tanques principales del avión (ej. Tanque Principal Izquierdo).
*   **Arranque**:
    *   Usualmente arrancado eléctricamente vía la **Batería del Avión** o **Energía de Tierra (GPU)**.
    *   **Envolvente**: Debe estar certificado para arranque y operación en altitud.
*   **Combustión**: Opera a velocidad constante (gobernado) para mantener la frecuencia del generador (400Hz).

## Controles e Indicación
*   **Interruptor Maestro (Master Switch)**:
    *   Energiza la caja de control electrónica (ECB/FADEC).
    *   Abre la **Compuerta de Admisión de Aire** (Flap).
    *   Abre la **Válvula de Aislamiento de Combustible**.
*   **Botón de Arranque (Start)**:
    *   Energiza el **motor de arranque**.
    *   Activa los sistemas de ignición.
    *   Inicia la secuencia automática de aceleración.

## Protección de Apagado Automático
El APU es capaz de protegerse apagándose automáticamente (especialmente en tierra) por condiciones como:
*   **Sobrevelocidad (Overspeed)** (Protección crítica).
*   **Baja Presión de Aceite**.
*   **Alta Temperatura de Aceite**.
*   **Sobretemperatura de EGT** (Gases de Escape).
*   **Fuego**.
*   **Flujo inverso**, **Baja velocidad**, etc.

*Nota: En vuelo, algunos apagados de protección (como alta temperatura de aceite) pueden ser inhibidos para priorizar la disponibilidad de energía eléctrica en una emergencia.*
