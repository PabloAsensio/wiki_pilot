# Componentes y Sistemas Adicionales

## Caja de Accesorios (Accessory Gearbox)
La caja de accesorios acciona sistemas esenciales del motor y del avión.
*   **Fuente de Energía**: Generalmente impulsada por el **eje del Compresor de Alta (HP)** (Alta velocidad) a través de una caja interna.
*   **Componentes Accionados**:
    *   **Bombas de Combustible** (Alta Presión).
    *   **Bombas de Aceite**.
    *   **Bombas Hidráulicas**.
    *   **IDG/CSD** (Generador de CA).
*   **Lubricación**: Lubricada por el **sistema de aceite del motor**.
*   **Cuello de Fusible (Shear Neck)**: Un punto débil en el eje de transmisión diseñado para romperse si un componente se agarrota (ej. un generador se bloquea). Esto protege la caja principal y el motor de daños, permitiendo que el motor siga funcionando (sin el accesorio fallado).

## Sistema de Encendido
Los motores de turbina usan sistemas de encendido de alta energía.
*   **Componentes**:
    *   **Excitador/Unidad de Encendido**: Convierte bajo voltaje (CC/CA) en alto voltaje (hasta 25,000 V).
    *   **Ignitores**: Bujías diseñadas para descargas de alta energía. Dos por motor.
*   **Operación**:
    *   **Arranque**: Chispa de alta energía para encender la mezcla.
    *   **Encendido Continuo**: Chispa de baja energía usada para prevenir el apagado de llama (flameout). Seleccionado automáticamente (por FADEC) o manualmente durante:
        *   Despegue / Aterrizaje.
        *   Precipitación fuerte / Turbulencia.
        *   Operación de anti-hielo.
        *   Aviso de pérdida o surge del motor.
*   **Tipo de Ignición**: Sistema de descarga de condensador de alta intensidad.

## Arranque del Motor
*   **Secuencia**:
    1.  **Rotación**: El starter gira el compresor de alta (N2).
    2.  **Ignición**: Se inicia la chispa.
    3.  **Combustible**: Se introduce el combustible.
*   **Tipos de Starter**:
    *   **Eléctrico**: Usado en motores pequeños y APUs (alimentado por batería).
    *   **Neumático (Air Starter)**: Usado en la mayoría de grandes turbofans. Alimentado por aire a alta presión de:
        *   **APU** (Unidad de Potencia Auxiliar).
        *   **Carro de Tierra** (GPU/ASU).
        *   **Cross-bleed** (sangrado cruzado del otro motor en marcha).

## FADEC (Control Digital del Motor de Autoridad Total)
Un sistema informático digital que gestiona todas las funciones del motor.
*   **Arquitectura**:
    *   **Canal Dual**: Dos ECUs (Unidades de Control Electrónico) independientes para redundancia (Activo/Reserva).
    *   **Fuente de Alimentación**: Un **Alternador de Imán Permanente (PMA)** dedicado en el motor proporciona energía independiente.
*   **Redundancia**:
    *   **Tolerante a Fallo Único**: Si un canal falla, el otro toma el control inmediatamente sin pérdida de rendimiento.
    *   **Fallo Total**: Si ambos canales fallan (y no hay respaldo hidromecánico), el motor se apaga (se cierra la válvula de combustible).
*   **Funciones**:
    *   Dosificación de combustible.
    *   Protección de límites del motor (Sobrevelocidad, Sobre-temperatura).
    *   Auto-arranque.
    *   Control de Inversoras de Empuje.
    *   Monitorización de salud del motor.

## Unidad de Potencia Auxiliar (APU)
Una pequeña turbina de gas situada en la cola.
*   **Propósito**: Proporciona **Energía Eléctrica** (CA) y **Aire Neumático** (para aire acondicionado y arranque de motores) en tierra y en vuelo.
*   **Arranque**: Generalmente arrancada eléctricamente usando la **batería del avión**.
