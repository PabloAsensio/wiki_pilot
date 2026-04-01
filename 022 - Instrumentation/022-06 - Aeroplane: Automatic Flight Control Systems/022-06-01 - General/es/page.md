---
title: "Principios Generales AFCS: Lazos de Control, Modos y Supervisión de Tripulación"
description: "Visión general del control automático de vuelo: lazos interno/externo, lógica de modos y responsabilidades PF/PM en monitorización."
keywords:
  - "flight level"
  - "minimum speed"
  - "rumbos magnéticos"
  - "compass turns"
---

# Principios Generales AFCS: Lazos de Control, Modos y Supervisión de Tripulación

## Visión General del Sistema de Control de Vuelo Automático (AFCS)

El **Sistema de Control de Vuelo Automático (AFCS)** reduce la carga de trabajo del piloto, mejora la precisión del vuelo y minimiza el estrés en los controles de vuelo. Típicamente consiste en:
*   **Sistema de Director de Vuelo y Piloto Automático (AFDS)**: Controla el cabeceo y el alabeo para seguir una trayectoria o mantener parámetros (ej. altitud).
*   **Empuje Automático (Autothrust - A/T)**: Gestiona el empuje del motor para controlar la velocidad o la tasa de ascenso/descenso.

### Roles de los Pilotos
En aeronaves multipiloto, se definen roles para garantizar la seguridad:
*   **Pilot Flying (PF - Piloto Volando)**: Se concentra en "volar la aeronave" (controlar actitud, velocidad, trayectoria) y gestionar el AFCS.
*   **Pilot Monitoring (PM - Piloto Monitoreando)**: Monitorea los parámetros de vuelo, canta desviaciones, maneja las comunicaciones con ATC y gestiona listas de verificación/sistemas.

## Lazos de Control

Los pilotos automáticos utilizan **sistemas de control de lazo cerrado** para mantener la estabilidad y seguir trayectorias.

### Tipos de Lazos
1.  **Lazo Interno (Estabilidad)**: Detecta el desplazamiento (ej. desde un giróscopo de tasa) y lo corrige para estabilizar la aeronave alrededor de su Centro de Gravedad (CG). Reacción rápida.
2.  **Lazo Externo (Guiado)**: Toma comandos del Panel de Control de Modos (MCP) o del Computador de Gestión de Vuelo (FMC) para guiar la trayectoria de la aeronave (ej. mantener altitud, interceptar rumbo).

### Mecanismo de Retroalimentación (Feedback)
Un lazo cerrado compara el estado **real** (feedback) con el estado **deseado** (entrada).
*   **Ejemplo**: El sistema comanda un movimiento del elevador. Un sensor de retroalimentación mide la **posición real** del elevador y la compara con la posición comandada para asegurar la precisión.
*   **Oscilaciones**: Si el sistema es demasiado sensible o sobrecompensa, puede causar **oscilaciones autoinducidas** (inestabilidad).

## Modos de Operación

### Modos Básicos (Estabilización)
Operan a través de los lazos internos para mantener la actitud de la aeronave.
*   **Mantenimiento de Actitud (Attitude Hold)**: Mantiene el ángulo de Cabeceo y Alabeo.
*   **Alas Niveladas (Wings Level)**: Mantiene las alas niveladas.

### Modos de Guiado
Operan a través de los lazos externos para navegar en el espacio 3D.
*   **Vertical**: Mantenimiento de Altitud (ALT), Velocidad Vertical (V/S), Senda de Planeo (G/S), VNAV.
*   **Lateral**: Rumbo (HDG), Derrota (TRK), LNAV, Localizador (VOR/LOC).

## Desconexión y Seguridad

### Intervención Manual
La tripulación debe estar lista para desconectar el piloto automático si se comporta de manera anormal (ej. grandes oscilaciones de cabeceo cerca del suelo).
*   **Métodos de Desconexión**: Presionar el botón de desconexión instintiva en la columna de control/sidestick, empujar la palanca/columna más allá de un umbral, o usar el botón en el MCP/FCU.
*   **Advertencias**: La desconexión activa advertencias auditivas/visuales.

### Protección de la Envolvente
Los sistemas modernos (especialmente Fly-By-Wire) incluyen protecciones para evitar que la aeronave exceda límites seguros (Pérdida/Stall, Exceso de Velocidad, Alabeo Excesivo).
*   **Limitación de Velocidad Comandada**: Evita exceder VMO/MMO o velocidades de pérdida.
*   **Reversión de Modo**: Si se aproxima un límite (ej. velocidad de pérdida), el AFCS puede revertir modos automáticamente (ej. a cambio de nivel) para proteger la aeronave.
