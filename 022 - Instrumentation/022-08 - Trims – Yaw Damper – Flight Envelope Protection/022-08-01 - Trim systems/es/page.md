---
layout: default
title: "Sistemas de Trim en Control de Vuelo: Auto-Trim, Mach Trim y Runaway"
description: "Aprende el funcionamiento del trim en vuelo manual y automático: lógica del THS, compensación Mach trim y acciones ante stabilizer runaway."
keywords:
    - "minimum speed"
    - "flight level"
    - "rumbos magnéticos"
    - "compass turns"
parent: "022-08 - Trims – Yaw Damper – Flight Envelope Protection"
grand_parent: "022 - Instrumentation"
nav_order: 1
---

# Sistemas de Trim en Control de Vuelo: Auto-Trim, Mach Trim y Runaway

## Propósito y Función

El propósito principal de un sistema de trimado es **aliviar al piloto de las fuerzas de control** requeridas para mantener una actitud o trayectoria de vuelo deseada.

- **Vuelo Manual**: El piloto usa el trim (mecánico o eléctrico) para anular la fuerza en la columna de control.
- **Vuelo Automático**: El Piloto Automático (AP) utiliza el sistema de **Auto-Trim** para gestionar el control de cabeceo a largo plazo.

## Auto-Trim

En aviones de transporte modernos (convencionales), el Timón de Profundidad (Elevator) controla los cambios de cabeceo a corto plazo, mientras que el **Estabilizador Horizontal Trimable (THS)** controla el trimado a largo plazo.

- **Operación**: El sistema Auto-trim mueve todo el Estabilizador Horizontal para aliviar la carga aerodinámica del timón de profundidad.
- **Objetivo**: Mantener el timón de profundidad alineado (posición neutral) con el estabilizador. Esto asegura que toda la autoridad del timón esté disponible para maniobrar.
- **Activación**:
    - **Controles Convencionales**: El Auto-trim suele estar activo **solo cuando el Piloto Automático está activado**.
    - **Fly-By-Wire (FBW)**: El Auto-trim está **siempre activo** (en Ley Normal), compensando automáticamente cambios de empuje, velocidad y configuración (flaps/tren).
- **Desconexión**: Cuando se desconecta el AP ("Hand-Over"), el avión queda en un estado correctamente trimado, evitando transitorios bruscos de cabeceo.

### Mach Trim

Los aviones de alta velocidad experimentan **Mach Tuck**: una tendencia de cabeceo hacia abajo causada por el movimiento hacia atrás del Centro de Presión (CP) y las ondas de choque a medida que aumenta el número de Mach.

- **Sistema**: El sistema **Mach Trim** es una función automática independiente.
- **Acción**: Trima automáticamente el estabilizador **hacia arriba (nose-up)** para contrarrestar la tendencia de bajar el morro.
- **Independencia**: Opera independientemente de si el Piloto Automático está activado o no.

## Operación Anormal: Trim Runaway

El **Stabilizer Runaway** es una condición donde el trim funciona continuamente sin haber sido comandado.

- **Consecuencias**: Puede llevar a fuerzas de control extremas que el timón de profundidad no pueda vencer (debido a la gran superficie del estabilizador frente al elevador).
- **Acciones del Piloto**:
    1.  Sujetar la columna de control firmemente.
    2.  Desconectar el Piloto Automático y el Autothrust.
    3.  Usar los interruptores "Stab Trim Cutout" para desactivar el motor eléctrico del trim.
    4.  Trimar manualmente (si hay rueda mecánica disponible).
