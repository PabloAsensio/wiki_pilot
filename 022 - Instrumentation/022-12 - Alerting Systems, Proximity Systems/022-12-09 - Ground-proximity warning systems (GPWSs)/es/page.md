---
title: "Sistemas GPWS/EGPWS: Modos, Lógica de Terreno y Maniobra de Escape"
description: "Aprende la lógica de modos GPWS, funciones de terreno en EGPWS, prioridades de alerta y respuesta inmediata de escape ante avisos pull up."
keywords:
    - "gpws"
    - "egpws"
    - "terrain warning"
    - "minimum speed"
---

# Sistemas GPWS/EGPWS: Modos, Lógica de Terreno y Maniobra de Escape

El **GPWS** (Ground Proximity Warning System - Sistema de Advertencia de Proximidad al Terreno) está diseñado para generar advertencias visuales y auditivas cuando la proximidad de la aeronave al terreno supone una amenaza para la seguridad, específicamente para prevenir el **CFIT** (Vuelo Controlado Contra el Terreno).

## Entradas y Operación del Sistema
El sistema requiere entradas del **Air Data Computer (ADC)** (altitud barométrica, velocidad vertical, CAS), **Radioaltímetro** (altura AGL), **ILS** (senda de planeo) y configuración de la aeronave (flaps, tren de aterrizaje).
*   **Rango de Operación**: Activo automáticamente entre **50 ft** y **2500 ft** de Radio Altitud.
*   **Requisito**: Obligatorio para aviones de turbina > 5.700 kg o > 9 pasajeros.

## Modos de Operación
El GPWS básico (no mejorado) tiene 7 modos basados en distintas condiciones:

| Modo | Condición | Alerta Aural | Advertencia Aural |
|---|---|---|---|
| **1** | Régimen de Descenso Excesivo | "SINK RATE" | "PULL UP" |
| **2** | Tasa de Cierre con el Terreno Excesiva | "TERRAIN" | "PULL UP" |
| **3** | Pérdida de Altitud tras Despegue/Go-around | "DON'T SINK" | - |
| **4** | Separación con Terreno Insegura (Config) | "TOO LOW GEAR/FLAPS/TERRAIN" | - |
| **5** | Desviación por Debajo de Senda de Planeo | "GLIDE SLOPE" (Suave) | "GLIDE SLOPE" (Fuerte) |
| **6** | Callouts de Altitud / Alabeo Excesivo | "MINIMUMS", "BANK ANGLE" | - |
| **7** | Cizalladura/Windshear (Reactivo) | "WINDSHEAR" (x3) | Sirena + Voz |

*   **Inhibición del Modo 5**: Puede ser cancelado por el piloto (por ejemplo, para aproximaciones visuales o solo localizador) usando un botón específico ("G/S INHIBIT").
*   **Prioridad del Modo 7**: Las alertas de cizalladura tienen prioridad sobre todos los demás modos del GPWS.

## GPWS Mejorado (EGPWS) / TAWS
El GPWS básico depende del radioaltímetro, que mira directamente hacia abajo. Efectivamente "mira abajo, no adelante".
*   **Limitación**: Un acantilado vertical o una elevación rápida del terreno podría no ser detectada a tiempo por el Modo 2.
*   **Solución**: El **EGPWS** (o TAWS - Terrain Awareness and Warning System) añade una función de **Evitación de Terreno con Visión Frontal (FLTA)**.
*   **Mecanismo**: Utiliza una **Base de Datos de Terreno** mundial comparada con la posición de la aeronave (GPS/FMS) para predecir conflictos.

### Pantalla de Terreno (EGPWS)
Usa la pantalla de navegación para mostrar amenazas de terreno:
*   **Rojo**: Terreno muy por encima de la altitud del avión (Advertencia/Warning).
*   **Ámbar/Amarillo**: Terreno cerca de la altitud del avión (Precaución/Caution).
*   **Verde**: Terreno seguro por debajo del avión.
*   **Magenta**: No hay datos de terreno disponibles.

## Respuesta del Piloto (Advertencia PULL UP)
Si ocurre una advertencia "PULL UP" o "TERRAIN AHEAD, PULL UP":
1.  **Piloto Automático**: Desconectar.
2.  **Cabeceo (Pitch)**: Aplicar **Palanca Atrás Máxima** (Full Aft) / Ascender hasta el límite (stick shaker/PLI).
    *   *Nota*: En aviones Fly-By-Wire, la palanca atrás a tope comanda el ángulo de ataque máximo disponible sin entrar en pérdida (protección alfa).
3.  **Empuje**: Aplicar Potencia Máxima (**TOGA**).
4.  **Aerofrenos**: Retraer.
5.  **Alabeo**: Nivelar alas.
6.  **Configuración**: No cambiar la configuración de tren o flaps hasta librar el obstáculo (consideraciones de resistencia/drag).
