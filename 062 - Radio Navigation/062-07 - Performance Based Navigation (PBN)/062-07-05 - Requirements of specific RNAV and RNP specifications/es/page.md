La OACI identifica varias especificaciones de navegación dentro del concepto PBN, divididas en familias RNAV y RNP. La diferencia fundamental es que las especificaciones **RNP requieren monitorización y alerta** del rendimiento a bordo, mientras que las RNAV no.

## Especificaciones RNP

El Manual PBN de la OACI identifica siete especificaciones de navegación bajo la familia RNP:

1.  **RNP 4**: Para aplicaciones de navegación oceánica y continental remota.
2.  **RNP 2**: Para aplicaciones en ruta oceánica remota y continental.
3.  **RNP 1**: Para llegadas, salidas y fases inicial, intermedia y frustrada de la aproximación.
4.  **Advanced RNP (A-RNP)**: Para navegación en todas las fases del vuelo.
5.  **RNP APCH**: Para aplicaciones de navegación durante la fase de aproximación.
6.  **RNP AR APCH** (Authorisation Required): Para aplicaciones de navegación durante la fase de aproximación que requieren autorización específica.
7.  **RNP 0.3**: Específica para operaciones de helicópteros en varias fases.

### RNP APCH (Aproximación RNP)

Es la especificación principal para aproximaciones GNSS. Permite aproximaciones hasta 3 mínimos diferentes:

*   **LNAV (Navegación Lateral)**: Aproximación 2D (no precisión). Solo proporciona guía lateral. Similar a una aproximación VOR/DME.
*   **LNAV/VNAV (Navegación Lateral/Vertical)**: Aproximación 3D (APV - Aproximación con Guía Vertical). Utiliza **Baro-VNAV** (altimetría barométrica) o SBAS para la guía vertical.
*   **LPV (Localizer Performance with Vertical guidance)**: Aproximación 3D de alta precisión. Utiliza **SBAS** (como EGNOS o WAAS) para guía lateral y vertical. Requiere un **Bloque de Datos FAS** (Final Approach Segment) que define geométricamente la trayectoria.

#### Consideraciones de Baro-VNAV
En aproximaciones LNAV/VNAV basadas en Baro-VNAV, la guía vertical depende de la altitud barométrica.
*   **Efecto de la Temperatura**: Los altímetros están calibrados para la atmósfera estándar (ISA). En temperaturas **más bajas que la estándar**, la altitud verdadera es **menor** que la indicada. Esto puede reducir peligrosamente el margen de franqueamiento de obstáculos.
*   **Limitaciones**: La mayoría de las aproximaciones RNP tienen una temperatura mínima publicada (ej. "Uncompensated Baro-VNAV not authorized below -8°C").
*   **Ajuste QNH**: Es crítico tener el QNH correcto. Un QNH incorrecto desplazará toda la trayectoria vertical.

### RNP AR APCH (RNP con Autorización Requerida)
Utilizada para aproximaciones complejas (ej. terrenos difíciles, trayectorias curvas en final).
*   Requiere **autorización específica** del estado para la operación, que cubre el equipo del avión, el entrenamiento de la tripulación y los procedimientos del operador.
*   Permite valores RNP menores a 0.3 NM (hasta RNP 0.1) y tramos RF (Radius to Fix) en el segmento final.

## Especificaciones RNAV

*   **RNAV 10 (designada como RNP 10)**: Para áreas oceánicas y remotas. Requiere una precisión lateral de ±10 NM durante el 95% del tiempo. Típicamente requiere **dos sistemas de navegación de largo alcance (LRNS)** independientes (ej. INS, IRS/FMS o GNSS).
*   **RNAV 5**: Para fase en ruta continental (B-RNAV en Europa). Es la única especificación que **permite la entrada manual de waypoints** por parte del piloto, aunque se recomienda el uso de base de datos.
*   **RNAV 1 y RNAV 2**: Para fases en ruta, llegadas (STAR) y salidas (SID).

## Requisitos Operacionales Comunes

### Base de Datos de Navegación
*   **Recuperación por Nombre**: Para **RNAV 1, RNAV 2, RNP 1, RNP 2 y RNP APCH**, los procedimientos (SID, STAR, Aproximaciones) deben ser recuperados de la base de datos de navegación a bordo por su **nombre de procedimiento** y deben conformarse a la carta publicada.
*   **Prohibición de Entrada Manual**: No está permitido crear waypoints manualmente (latitud/longitud o rho/theta) para procedimientos RNAV 1/2 o RNP (excepto RNAV 5).
*   **Modificaciones**: Se permite modificar la ruta insertando o borrando waypoints específicos en respuesta a autorizaciones ATC (ej. "Directo a"), pero no alterar la definición de la trayectoria entre el FAF y el MAPt en una aproximación.

### Terminología de Aproximaciones (OACI/EASA)
La OACI está transicionando de "Precisión/No Precisión" a operaciones de aproximación **2D** (solo lateral) y **3D** (lateral y vertical).
*   **Tipo A**: Mínimos (MDH/DH) ≥ 250 ft.
*   **Tipo B**: Mínimos (DH) < 250 ft. (Solo posible con guía 3D).
*   Una aproximación RNP APCH a mínimos **LPV** (hasta 200 ft) se considera una operación 3D Tipo B, equivalente operacionalmente a una ILS CAT I.
