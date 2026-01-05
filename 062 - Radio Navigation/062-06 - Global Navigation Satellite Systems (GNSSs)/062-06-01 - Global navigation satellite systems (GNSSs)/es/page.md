El GNSS es un término general que engloba a los sistemas de navegación por satélite que proporcionan posicionamiento geoespacial autónomo con cobertura global.

## Sistemas Principales
Existen cuatro sistemas GNSS principales reconocidos:
*   **NAVSTAR GPS** (EE.UU.): Operativo.
*   **GLONASS** (Rusia): Operativo.
*   **Galileo** (Europa): Operativo.
*   **BeiDou** (China): Operativo.

### Interoperabilidad
*   **Nivel de Sistema**: GPS y GLONASS son interoperables a nivel de sistema. Tienen diferentes frecuencias y marcos de referencia (WGS-84 vs PZ-90), por lo que sus señales no son compatibles directamente, pero el receptor puede procesar ambas soluciones independientemente y combinarlas.
*   **Nivel de Señal**: Galileo y GPS tienen ciertas frecuencias interoperables a nivel de señal.

## NAVSTAR GPS
El sistema GPS consta de tres segmentos:

1.  **Segmento Espacial**:
    *   Constelación nominal de **24 satélites** (mínimo técnico).
    *   Orbitan en **6 planos orbitales** a una altitud aproximada de **20,200 km**.
    *   Periodo orbital de 12 horas.
2.  **Segmento de Control**:
    *   Estaciones de monitoreo y control en tierra.
    *   Mantienen la salud de la constelación, corrigen relojes atómicos y actualizan efemérides.
3.  **Segmento de Usuario**:
    *   Receptores GPS (aviones, móviles, etc.).

### Principio de Funcionamiento
El receptor calcula su posición mediante **trilateración** midiendo el tiempo que tarda la señal en viajar desde el satélite hasta el receptor (Pseudorango).
*   **3 Satélites**: Posición 2D (Latitud, Longitud) + Tiempo (si se conoce la altitud).
*   **4 Satélites**: Posición 3D (Latitud, Longitud, Altitud) + Tiempo.

### Frecuencias y Servicios
Los satélites transmiten en la banda UHF (L-Band):
*   **L1 (1575.42 MHz)**:
    *   Transporta el código **C/A** (Coarse Acquisition) y el código **P** (Precision).
    *   Proporciona el servicio **SPS** (Standard Positioning Service) para uso civil.
*   **L2 (1227.60 MHz)**:
    *   Transporta solo el código **P**.
    *   Junto con L1, proporciona el servicio **PPS** (Precise Positioning Service) para usuarios autorizados (militares).
    *   El uso de dos frecuencias permite corregir errores ionosféricos.

### Mensaje de Navegación
Cada satélite transmite:
*   **Almanaque**: Datos orbitales aproximados de *toda* la constelación.
*   **Efemérides**: Datos orbitales precisos del satélite *específico*.
*   **Corrección de Reloj**: Estado del reloj atómico del satélite.
*   **Modelo Ionosférico**: Para corregir retardos en receptores de una sola frecuencia.

## Errores del Sistema

### Fuentes de Error
1.  **Retardo Ionosférico**: Es el **error más significativo**. La ionosfera ralentiza la señal. Se mitiga con modelos matemáticos o receptores de doble frecuencia.
2.  **Errores de Reloj del Satélite**: Aunque usan relojes atómicos, existen pequeñas derivas.
3.  **Errores de Efemérides**: Diferencia entre la posición real y la esperada del satélite.
4.  **Multipath**: Reflexión de la señal en superficies (edificios, terreno) antes de llegar a la antena.
5.  **Ruido del Receptor**: Errores internos del equipo.

### Dilución de Precisión (DOP)
La geometría de los satélites afecta la precisión de la posición calculada.
*   **GDOP (Geometric Dilution of Precision)**: Medida de la calidad de la geometría.
*   **PDOP (Position Dilution of Precision)**: Dilución en la posición 3D.
*   **Valor Bajo = Mejor Precisión**.
*   **Geometría Ideal**: Un satélite directamente arriba (zenit) y tres en el horizonte separados 120°.
*   **Mala Geometría**: Satélites agrupados muy cerca unos de otros.

**Error Total = UERE (User Equivalent Range Error) × GDOP**

## Integridad (RAIM)
**RAIM (Receiver Autonomous Integrity Monitoring)** es una técnica donde el receptor usa satélites "extra" para verificar la integridad de la solución de navegación.
*   **Fault Detection (FD)**: Requiere mínimo **5 satélites**. Detecta si hay un satélite fallando pero no puede identificar cuál es.
*   **Fault Detection and Exclusion (FDE)**: Requiere mínimo **6 satélites**. Detecta y excluye el satélite defectuoso, permitiendo continuar la navegación.
*   Si se dispone de ayuda barométrica (altitud de presión), se requiere un satélite menos (4 para FD, 5 para FDE).
