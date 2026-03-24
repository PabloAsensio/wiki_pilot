---
layout: default
title: "022-06-03 - Flight director: design and operation"
parent: "022-06 - Aeroplane: Automatic Flight Control Systems"
grand_parent: "022 - Instrumentation"
nav_order: 3
---

# Flight Director: Design and Operation

## Principios

El **Flight Director (FD)** proporciona una guía visual al piloto para interceptar y mantener una trayectoria de vuelo deseada con la actitud óptima. El computador del FD calcula la **dirección y magnitud** de las entradas de control (cabeceo y alabeo) necesarias para satisfacer los modos de guía de vuelo seleccionados.

- **Visualización**: Se presenta como barras de comando en el Indicador de Actitud (ADI) o Pantalla Principal de Vuelo (PFD).
- **Función**:
  - **Vuelo manual**: El piloto manipula los controles manualmente para centrar las barras de comando.
  - **Vuelo automático**: Cuando el Piloto Automático (AP) está activado, este sigue los mismos comandos calculados por el FD.

### Barras de Comando

Existen dos tipos principales de presentación: "Barras cruzadas" (común en Airbus) y "Barras en V" (común en Boeing/sistemas antiguos).

1.  **Barra Vertical (Comando de Alabeo/Roll)**:
    - Se mueve a izquierda o derecha.
    - Indica la corrección necesaria en el **ángulo de alabeo** (canal de roll) para seguir la trayectoria lateral (Rumbo, Nav, Localizador, etc.).
    - Para seguirla: Si la barra se mueve a la izquierda, el piloto debe alabear a la izquierda.
2.  **Barra Horizontal (Comando de Cabeceo/Pitch)**:
    - Se mueve hacia arriba o hacia abajo.
    - Indica la corrección necesaria en el **ángulo de cabeceo** (canal de pitch) para seguir el perfil vertical (Altitud, V/S, Senda de planeo, Velocidad, etc.).
    - Para seguirla: Si la barra sube, el piloto debe tirar de la palanca (subir el morro).

> **Nota**: El FD indica correcciones de *actitud* (pitch y bank), no posición relativa directamente, aunque seguirlas corrige la posición.

## Operación y Uso

Los modos disponibles para el Flight Director son **idénticos** a los disponibles para el Piloto Automático. Se seleccionan en el mismo panel:
- **MCP (Mode Control Panel)** en Boeing.
- **FCU (Flight Control Unit)** en Airbus.

### Modos de Operación

- **Solo FD (Vuelo Manual)**: El piloto vuela a mano siguiendo estrictamente las barras del FD para lograr la trayectoria deseada. Reduce la carga de trabajo al convertir datos complejos de navegación en objetivos simples de actitud.
- **FD + AP (Vuelo Automático)**: El AP está activado y los servos mueven las superficies de control para seguir los comandos del FD. El rol del piloto pasa a ser **siguiente (monitoring)** de que el AP sigue correctamente las indicaciones del FD.
- **Despegue (TO/GA)**:
  - Se activa con los interruptores TO/GA.
  - Comando inicial: Cabeceo fijo arriba (ej. 10°-15°) y alas niveladas.
  - Tras la rotación: El pitch comanda una velocidad objetivo (ej. $V_2 + 20$ kt) y el roll mantiene la derrota o rumbo de pista.

### Coordinación de la Tripulación (Multi-pilot)

- **Pilot Flying (PF)**: Vuela la aeronave (manual o gestionando el AP) y canta los cambios de modo.
- **Pilot Monitoring (PM)**: Monitoriza parámetros, listas de chequeo y comunicaciones.
- **SOPs**: Ambos pilotos deben monitorizar el FMA (Flight Mode Annunciator) para confirmar que los modos seleccionados en el MCP/FCU están realmente activados o armados.

## Fallos y Desconexión

Si las barras del FD desaparecen o aparece una bandera de fallo:
- **No** activar el piloto automático ciegamente (usa los mismos datos).
- **Investigar** la causa (verificar FMA).
- Revertir a vuelo "raw data" (actitud básica y navegación pura) si es necesario.
- Si los comandos del FD son erráticos o contradicen los datos básicos, el FD debe ser **desconectado** (OFF) para limpiar la pantalla y evitar confusión.

### Indicaciones

- **Barras Cedradas**: La aeronave tiene el pitch y bank requeridos para satisfacer el modo activo.
- **Barras Desviadas**: Se requiere input de control en la dirección de la barra para volver a la trayectoria.
