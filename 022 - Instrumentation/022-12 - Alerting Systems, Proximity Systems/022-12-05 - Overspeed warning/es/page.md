---
title: "Sistema de Aviso de Overspeed: Límites VMO/MMO, Barber Pole y Alertas"
description: "Aprende la lógica del aviso de overspeed, interpretación del barber pole en PFD, límites VMO/MMO por configuración y alertado inmediato a la tripulación."
keywords:
    - "overspeed"
    - "vmo mmo"
    - "minimum speed"
    - "flight level"
---

# Sistema de Aviso de Overspeed: Límites VMO/MMO, Barber Pole y Alertas

## Descripción General

El **Sistema de Aviso de Exceso de Velocidad (Overspeed Warning)** es una característica de seguridad obligatoria diseñada para alertar a la tripulación de vuelo cuando la aeronave excede sus velocidades máximas de operación ($V_{MO}$ / $M_{MO}$). Su propósito principal es prevenir excursiones inadvertidas más allá de los límites estructurales certificados del fuselaje.

## Indicaciones

### Visual (Cinta de Velocidad del PFD)
En Pantallas de Vuelo Primario (PFD) modernas:
*   **Cinta de Velocidad:** Una escala vertical móvil (Blanca sobre Gris).
*   **Franja de Velocidad Máxima ($V_{MAX}$):** Una **barra a rayas Rojas y Negras** (a menudo llamada "Barber Pole") desciende desde la parte superior de la escala para indicar el límite superior de velocidad.
*   **Definición de $V_{MAX}$:** La franja comienza en la velocidad límite **más baja** para la configuración actual:
    1.  **$V_{MO}$ / $M_{MO}$:** Velocidad Máxima Operativa / Mach.
    2.  **$V_{LE}$:** Velocidad Máxima con Tren de Aterrizaje Extendido.
    3.  **$V_{FE}$:** Velocidad Máxima con Flaps Extendidos.

### Auditiva
*   **Alerta:** Un sonido distintivo y continuo (p. ej., "Clacker", Sirena o Aviso de Voz) se activa inmediatamente al exceder el límite.

## Lógica del Sistema
El Sistema de Aviso monitorea las entradas del Ordenador de Datos de Aire (ADC). Si la Velocidad Indicada (IAS) o el Número de Mach excede el límite calculado, se activa el Master Warning (Nivel A).
