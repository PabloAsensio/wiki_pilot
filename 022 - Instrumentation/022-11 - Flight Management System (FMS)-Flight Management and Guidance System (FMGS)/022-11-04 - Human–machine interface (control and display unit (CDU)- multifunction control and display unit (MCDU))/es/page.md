---
title: "Interfaz CDU/MCDU: Lógica de Entrada, Flujo EXEC y Redundancia"
description: "Comprende la interacción tripulación-FMS en CDU/MCDU: uso de scratchpad, lógica LSK/EXEC, campos obligatorios y redundancia operacional dual."
keywords:
    - "mcdu"
    - "cdu"
    - "flight level"
    - "minimum speed"
---

# Interfaz CDU/MCDU: Lógica de Entrada, Flujo EXEC y Redundancia

## Descripción General

La **Unidad de Control y Visualización (CDU)**, o **Unidad de Visualización y Control Multifunción (MCDU)** en aviones Airbus, es la interfaz principal entre la tripulación de vuelo y el Ordenador de Gestión de Vuelo (FMC).

Permite a la tripulación:
*   Introducir datos de navegación y rendimiento.
*   Monitorizar el progreso del vuelo.
*   Gestionar funciones de vuelo automático.
*   Enviar comandos no FMS (p. ej., ACARS, Datalink) en MCDUs modernas.

## Componentes de la Interfaz

La unidad consta de una pantalla de visualización y un teclado.

### Disposición de la Pantalla (Display)
*   **Línea de Título:** Muestra el nombre de la página actual (p. ej., `INIT`, `LEGS`, `PROG`).
*   **Líneas de Etiqueta (Label):** Texto pequeño que identifica el campo de datos debajo de él.
*   **Líneas de Datos:** Los valores reales (datos calculados o entradas del piloto).
*   **Scratchpad (Panel de Escritura):** La línea inferior de la pantalla.
    *   Muestra caracteres alfanuméricos escritos por el piloto *antes* de que se inserten en un campo de datos.
    *   Muestra mensajes del sistema (p. ej., `CHECK GW`, `GPS PRIMARY`).

### Controles
*   **Teclas de Selección de Línea (LSK):** Botones a la izquierda (1L-6L) y derecha (1R-6R) de la pantalla utilizados para:
    *   Mover datos desde el scratchpad a un campo.
    *   Seleccionar elementos o indicaciones (p. ej., ` <ACTIVATE> `).
*   **Teclado:** Teclado alfanumérico para entrada de datos.
*   **Tecla EXEC:** El botón "Ejecutar" (a menudo iluminado) actúa como la tecla "Enter" o "Confirmar" para activar un plan de vuelo modificado.

### Simbología de Datos
*   **Cuadros Ámbar (`[][][]`):** Indican entrada de datos **Obligatoria** necesaria para que el FMS funcione (p. ej., ZFW, Nivel de Vuelo de Crucero).
*   **Guiones Azul/Verde (`-----`):** Indican entrada de datos **Opcional** (p. ej., datos de Viento, desviación de Temp).

## Secuencia de Configuración Pre-Vuelo

Se utiliza un flujo lógico estándar para inicializar el FMS:

1.  **IDENT:** **"¿Quién soy?"**
    *   Inicio identificando Modelo de Aeronave, Clasificación de Motor y validez de la Base de Datos de Navegación.
2.  **POS INIT:** **"¿Dónde estoy?"**
    *   Alineación IRS.
    *   Entrada de Posición Presente (Latitud/Longitud).
3.  **RTE (Ruta):** **"¿A dónde voy?"**
    *   Aeropuertos de Origen y Destino.
    *   Definición de Ruta (Aerovías, Waypoints, Procedimientos).
4.  **PERF INIT:** **"¿Cómo/Cuándo llegaré?"**
    *   **Peso Cero Combustible (ZFW):** Entrada obligatoria crítica del loadsheet para calcular el Peso Bruto.
    *   **Combustible:** Entrada de Combustible Bloque para planificación (el FMS generalmente lee FOB real de sensores).
    *   **Cost Index:** Estrategia económica.
    *   **Altitud de Crucero:** Nivel planificado.

## Redundancia Operacional

*   **Configuración Dual:** En una instalación FMS dual, los datos introducidos en una CDU se comunican típicamente (crosstalk) al otro FMC.
*   **Visualización Independiente:** Aunque se compartan las bases de datos, cada piloto puede seleccionar diferentes páginas en su respectiva CDU (p. ej., Piloto A ve `LEGS`, Piloto B ve `PROG`).
*   **Operación Cruzada:** En casos de fallo (p. ej., Fallo de FMGC 1 y MCDU 2), la MCDU 1 restante a menudo puede comunicarse con el FMGC 2 para mantener el control.
