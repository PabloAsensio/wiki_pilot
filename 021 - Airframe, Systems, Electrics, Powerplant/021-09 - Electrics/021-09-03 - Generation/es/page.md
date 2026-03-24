---
title: "Sistemas de Generación Eléctrica en Aeronaves"
description: "Generación de AC y DC, CSD, IDG, TRUs, Inversores y distribución de energía."
---

# Sistemas de Generación Eléctrica en Aeronaves

## Generación de AC

Las aeronaves grandes suelen requerir energía AC de Alto Voltaje (115/200V, 400Hz, trifásica).
*   **Generadores AC Sin Escobillas**: Usan un conjunto de **imanes permanentes** para la excitación inicial.
    *   **Generador Excitador**: Montado en el mismo eje.
    *   **Generador de Imanes Permanentes (PMG)**: Se usa específicamente para la corriente de excitación inicial y para alimentar el control del generador.
*   **Regulación de Voltaje**: El **Regulador de Voltaje** controla el voltaje de salida (lo mantiene constante a cargas/velocidades variables) ajustando la **corriente de excitación** a las bobinas de campo.
    *   Conectado en serie con la bobina de campo.
    *   Si la carga eléctrica aumenta -> El voltaje cae -> El regulador aumenta la corriente de excitación -> El voltaje vuelve a la normalidad.

### Unidad de Transmisión de Velocidad Constante (CSD) e IDG

Los generadores de AC deben girar a una velocidad constante para mantener una **frecuencia (400Hz)** constante, a pesar de las RPM variables del motor.
*   **CSD (Constant Speed Drive)**: Unidad hidromecánica que convierte la velocidad variable del motor en velocidad constante del generador.
    *   Supervisa/Ajusta: **Frecuencia de Salida**.
    *   Tiene su propio sistema de aceite independiente para lubricación y refrigeración.
    *   **Fallos**: Temperatura de aceite alta, presión de aceite baja.
*   **IDG (Integrated Drive Generator)**: Combina el **CSD y el Generador** en una sola unidad.
    *   **Desconexión**: En caso de fallo (por ejemplo, temperatura de aceite alta, presión baja), el piloto **opera el interruptor de desconexión del IDG**.
    *   **Consecuencia**: El eje de transmisión se desconecta mecánicamente. El generador queda **inutilizable por el resto del vuelo**.
    *   **Rearme**: **SOLO** puede ser reconectado en tierra por mantenimiento con el motor parado.

### Frecuencia Variable (Frequency Wild)

*   **Generadores Frequency Wild**: Generadores donde la frecuencia varía con la velocidad del motor (sin CSD/IDG).
*   **Aplicación**: Solo adecuados para **cargas resistivas** (por ejemplo, esteras antihielo/calefactores) porque la inductancia/reactancia dependen de la frecuencia.

### Generación y Conversión de DC

*   **TRU (Transformer Rectifier Unit)**:
    *   Combina un Transformador y un Rectificador.
    *   **Función**: Convierte **AC** (115V) a **DC** (28V).
    *   Se usa para alimentar buses DC y cargar baterías desde el suministro principal de AC.
    *   A menudo incluye un circuito de suavizado/filtro para minimizar la fluctuación de salida.
*   **Inversor**:
    *   **Función**: Convierte **DC** (28V) a **AC** (115V, 400Hz).
    *   **Inversor Estático**: Dispositivo de estado sólido (sin partes móviles) usado para cargas AC esenciales si falla la AC principal.
*   **Arrancador-Generador**:
    *   Combina funciones de motor de arranque y generador (común en motores de turbina).
    *   Actúa como **motor de arranque** para acelerar el motor hasta una velocidad autosostenible.
    *   Cambia para convertirse en un **generador de DC** una vez que el motor está en marcha.

### Protección y Control

*   **GCU (Generator Control Unit)**:
    *   Verifica fallos (sobrevoltaje, sobreexcitación).
    *   Controla el Disyuntor del Generador (GCB) y el Relé de Control de Excitación.
*   **Sistema de Bus Dividido (Split Bus)**: Si falla un generador, los GCB/BTB (Bus Tie Breakers) se reconfiguran para asegurar que las cargas esenciales reciban energía.
