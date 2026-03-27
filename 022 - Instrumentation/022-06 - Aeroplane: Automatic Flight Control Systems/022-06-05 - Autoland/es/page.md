---
layout: default
title: "Sistemas Autoland: Lógica Fail-Passive/Fail-Operational y Alert Height"
description: "Estudia arquitectura autoland, clases de redundancia, lógica de decisión por alert height y secuencia flare/rollout en baja visibilidad."
keywords:
    - "flight level"
    - "minimum speed"
    - "rumbos magnéticos"
    - "compass turns"
parent: "022-06 - Aeroplane: Automatic Flight Control Systems"
grand_parent: "022 - Instrumentation"
nav_order: 5
---

# Sistemas Autoland: Lógica Fail-Passive/Fail-Operational y Alert Height

## Propósito y Componentes

El **Sistema de Aterrizaje Automático (Autoland)** permite aterrizar en condiciones meteorológicas adversas donde las referencias visuales están degradadas (niebla, techo bajo) por debajo de los mínimos de Categoría I.

Componentes clave:
- **Radio Altímetro (RA)**: Proporciona la altura precisa sobre el terreno (AGL) para la maniobra de recogida (flare).
- **Piloto Automático (AP)**: Generalmente múltiples canales (redundancia).
- **Empuje Automático (A/THR)**: Gestiona la velocidad y retarda la potencia en el toque.
- **Señales de Tierra**: ILS (Instrument Landing System).

## Niveles de Redundancia del Sistema

EASA CS-AWO define la clasificación basada en el comportamiento tras un fallo:

### Fallo Pasivo (Fail-Passive)
- **Comportamiento**: En caso de fallo, **no hay una condición significativa de fuera de trim** o desviación.
- **Resultado**: El aterrizaje automático **NO se completa**. El piloto debe tomar el control manual (generalmente ejecutando un Motor y Al Aire / Go-Around).
- **Uso**: Categoría II o Categoría III A.

### Fallo Operativo (Fail-Operational)
- **Comportamiento**: En caso de fallo, la aproximación, recogida (flare) y aterrizaje **PUEDEN completarse** con la parte restante del sistema.
- **Resultado**: El sistema revierte a un estado "fail-passive" tras el primer fallo.
- **Requisito**: Típicamente requiere 3 Pilotos Automáticos (o arquitecturas monitoreadas).
- **Uso**: Categoría III B.

### Híbrido Fallo Operativo (Fail-Operational Hybrid)
- Consiste en un sistema primario **Fail-Passive** combinado con un **sistema de guía independiente** (ej. Head-Up Display - HUD).
- Si el sistema automático falla, el HUD da la guía para que el piloto complete el aterrizaje manualmente.

## Altura de Alerta (Alert Height - AH)

La Altura de Alerta es una altura de radio específica (típicamente entre 100 ft y 200 ft), definida para sistemas **Fail-Operational**.

- **Fallo POR ENCIMA de la AH**: La aproximación debe discontinuarse (Go-Around) a menos que sea posible y esté preparada una reversión a mínimos más altos (ej. CAT I).
- **Fallo POR DEBAJO de la AH**: El fallo generalmente se ignora (se enmascara) y la aproximación continúa automáticamente, siempre que no salte una advertencia roja de "AUTOLAND". La lógica es que el riesgo de un Go-Around tan cerca del suelo supera el riesgo de aterrizar con redundancia reducida (pero suficiente).

## Secuencia de Autoland (Perfil Típico)

1.  **Modo Approach (APP)**: LOC y G/S armados. Se activan el 2º/3º AP para redundancia.
2.  **Captura**: LOC y G/S activos (Verde en FMA).
3.  **Baja Altitud (~1500 ft)**: Se arman modos "FLARE" y "ROLLOUT". El sistema verifica redundancia (ej. "LAND 3").
4.  **Flare (~50 ft RA)**:
    - **FLARE** se activa (Verde).
    - EL AP usa el Radio Altímetro para subir el morro y reducir la tasa de descenso.
    - Las barras del FD suelen retraerse o desaparecer.
5.  **Reducción de Empuje (~27-30 ft RA)**:
    - **IDLE** / **RETARD** se activa. Los gases van a ralentí.
6.  **Toque y Rodaje (Rollout)**:
    - **ROLLOUT** se activa. El AP usa el timón de dirección y la rueda de morro para mantener el eje de pista usando la señal del Localizador.

## Limitaciones y Advertencias

- **Límites de Viento**: Autoland tiene límites más estrictos que el aterrizaje manual (ej. Viento cruzado máx 15-25 kt).
- **Autoland Warning**: Luz/mensaje rojo parpadeante que indica que el sistema no puede aterrizar seguro. Se activa por:
    - Fallo de ambos Radio Altímetros.
    - Desviación excesiva de ILS (LOC o Glide).
    - Pérdida de señal ILS (aunque pérdida de Glide por debajo de ~100 ft puede tolerarse ya que el avión está en "attitude hold" transicionando al flare).
