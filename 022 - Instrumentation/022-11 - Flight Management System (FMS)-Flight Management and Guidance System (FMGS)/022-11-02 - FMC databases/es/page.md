---
title: "Bases de Datos del FMC"
---

## Descripción General

El Ordenador de Gestión de Vuelo (FMC) depende de dos bases de datos principales para realizar sus funciones: la **Base de Datos de Navegación** y la **Base de Datos de Rendimiento**. Además, un área de almacenamiento temporal permite a los pilotos definir waypoints personalizados.

## Base de Datos de Navegación (NDB)

La Base de Datos de Navegación es un repositorio digital que contiene información aeronáutica esencial para la navegación lateral y la planificación del vuelo.

### Contenido
*   **Aeropuertos y Pistas:** Ubicaciones, elevaciones, longitudes.
*   **Radioayudas:** VOR, NDB, DME y sus frecuencias.
*   **Intersecciones/Waypoints:** Coordenadas e identificadores.
*   **Aerovías:** Estructura en ruta.
*   **Procedimientos:** SIDs (Salidas), STARs (Llegadas) y Aproximaciones (ILS, RNAV, etc.).
*   **Rutas de Compañía:** Rutas predefinidas utilizadas por la aerolínea.
*   **Variación Magnética:** Datos para convertir el Norte Verdadero a Norte Magnético.

### Actualizaciones y Validez (AIRAC)
*   La base de datos sigue el **ciclo AIRAC** (Control y Regulación de Información Aeronáutica) y se actualiza cada **28 días**.
*   El FMC típicamente almacena **dos ciclos**:
    *   **Activa:** La base de datos válida actual.
    *   **Standby/Secundaria:** El ciclo adyacente (anterior o siguiente).
*   **Solo Lectura:** Los datos principales son de **solo lectura** para garantizar la integridad. Los pilotos no pueden modificar ni eliminar waypoints o procedimientos estándar.
*   **Acción del Piloto:** Los pilotos verifican las fechas de validez durante las comprobaciones previas al vuelo en la página `IDENT`. Cambiar la base de datos activa típicamente **elimina el plan de vuelo activo**.
*   *Nota:* Los datos de terreno y obstáculos generalmente se almacenan en la base de datos del **EGPWS**, no en la Base de Datos de Navegación del FMS.

## Base de Datos de Rendimiento

La Base de Datos de Rendimiento contiene datos estáticos específicos del **modelo de avión** y del **modelo de motor**.

### Contenido
*   **Modelo de Motor:** Características de empuje, parámetros de flujo de combustible en varias configuraciones de potencia y altitudes.
*   **Modelo Aerodinámico:** Polares de resistencia (limpio y configurado), características de sustentación.
*   **Límites de Velocidad:** VMO/MMO, velocidades de señalización de flaps.
*   **Datos de Optimización:** Altitudes óptimas, altitudes máximas y velocidades de crucero recomendadas (ECON).

### Propósito
El FMC utiliza estos datos para calcular:
*   **Objetivos de Empuje:** Ajustes de N1 o EPR para Despegue, Ascenso, Crucero y Motor y Al Aire.
*   **Predicciones:** Consumo de combustible, Hora Estimada de Llegada (ETA) y puntos de Inicio de Descenso (TOD).
*   **Velocidades:** Velocidades V1, VR, V2 y Green Dot (mejor sustentación-resistencia).

### Factores de Mantenimiento
Aunque los pilotos no pueden alterar el modelo principal, el personal de mantenimiento puede introducir **Factores de Resistencia (Drag)** o **Factores de Flujo de Combustible** para tener en cuenta el envejecimiento del fuselaje y la degradación del motor, asegurando que las predicciones sigan siendo precisas.

## Waypoints Definidos por el Usuario

Dado que los pilotos no pueden modificar la base de datos principal, el FMS proporciona una base de datos **Suplementaria** o **Temporal** para waypoints creados por el piloto. Estos se borran cuando se actualiza la base de datos de navegación principal.

### Métodos de Creación
1.  **Lat/Long (LL):** Entrada directa de coordenadas (p. ej., `N45W030`).
2.  **Lugar/Marcación/Distancia (PBD):** Define un punto basado en un fijo conocido (p. ej., `LMG/330/20` - 20NM en el radial 330 de LMG).
3.  **Lugar-Marcación/Lugar-Marcación (PBX):** Define un punto en la intersección de dos radiales (p. ej., `LMG330/CGC090`).
4.  **A lo largo de la ruta (PD):** Una distancia antes o después de un waypoint en la ruta de vuelo actual.
