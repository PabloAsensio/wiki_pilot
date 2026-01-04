El uso de PBN introduce conceptos y funcionalidades específicas en los sistemas de navegación para mejorar la eficiencia y capacidad del espacio aéreo.

## Tipos de Waypoints (Puntos de Recorrido)
*   **Fly-by Waypoint**: El piloto o el sistema anticipa el viraje para evitar sobrepasar el siguiente segmento de vuelo. El viraje comienza *antes* de llegar al waypoint. Es la forma estándar de viraje en rutas RNAV.
*   **Fly-over Waypoint**: La aeronave debe sobrevolar físicamente el waypoint antes de iniciar cualquier viraje. Se utiliza cuando es necesario seguir una trayectoria específica por razones de obstáculos o procedimientos (ej. MAPt).

## Trayectorias de Radio Fijo (Fixed Radius Paths - FRP)
Son trayectorias curvas precisas que el sistema RNP debe ser capaz de volar.

### 1. Radius to Fix (RF) Leg
*   **Uso**: Procedimientos **Terminales y de Aproximación**.
*   **Definición**: Se define por un **radio**, una **longitud de arco** y un **fix** (punto final).
*   **Requisito**: Requiere piloto automático o director de vuelo con capacidad de "roll-steering".
*   **Precisión**: Mantiene la misma precisión (RNP) durante el viraje que en los tramos rectos.

### 2. Fixed Radius Transition (FRT)
*   **Uso**: Procedimientos **En Ruta**.
*   **Propósito**: Permite rutas paralelas más cercanas en el espacio aéreo superior.
*   **Radios Estándar**:
    *   **22.5 NM** para rutas de gran altitud (por encima de FL 195).
    *   **15 NM** para rutas de baja altitud.

## Funciones Específicas del Sistema
*   **Offset Lateral (SLOP - Strategic Lateral Offset Procedure)**:
    *   Capacidad de volar paralelo a la ruta definida a una distancia específica (generalmente en incrementos de 1 NM hasta 20 NM).
    *   Se usa para contingencias o para reducir el riesgo de colisión por pérdida de precisión vertical (wake turbulence).
    *   El sistema suele cancelar el offset automáticamente en áreas terminales, aproximaciones, esperas o virajes de >90°.
*   **ARINC 424 Path Terminators**: Estándar de codificación de bases de datos de navegación que define cómo el FMS interpreta y vuela los procedimientos (SIDs, STARs, IAPs). Define 24 tipos de segmentos (ej. RF, TF - Track to Fix, CF - Course to Fix).

## Diferencias Clave
*   **Fly-by vs RF**: Un viraje *fly-by* varía su radio y punto de inicio según la velocidad y el viento (no es una trayectoria fija sobre el suelo). Un viraje *RF* es una trayectoria fija sobre el suelo (radio constante), independientemente de la velocidad o el viento.
