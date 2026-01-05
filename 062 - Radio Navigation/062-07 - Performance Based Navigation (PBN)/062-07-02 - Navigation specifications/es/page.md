Las especificaciones de navegación definen los requisitos de rendimiento (precisión, integridad, etc.) que deben cumplir la aeronave y la tripulación para operar en un espacio aéreo definido.

## Tipos de Especificaciones
Existen dos tipos principales, diferenciados por el requisito de monitoreo y alerta a bordo:

1.  **RNAV (Area Navigation)**:
    *   **NO** requiere monitoreo y alerta de rendimiento a bordo (On-board performance monitoring and alerting).
    *   Ejemplos: RNAV 10, RNAV 5, RNAV 1.
2.  **RNP (Required Navigation Performance)**:
    *   **SÍ** requiere monitoreo y alerta de rendimiento a bordo.
    *   El sistema alerta al piloto si no se cumple con la precisión requerida (ANP > RNP).
    *   Ejemplos: RNP 4, RNP 1, RNP APCH.

## Aplicación por Fase de Vuelo (Resumen)

| Especificación | Fase de Vuelo Típica | Precisión Lateral (95%) | Notas |
| :--- | :--- | :--- | :--- |
| **RNAV 10 (RNP 10)** | Oceánica / Remota | 10 NM | Usado en NAT HLA. A pesar del nombre "RNP 10", es una especificación RNAV (sin alerta). |
| **RNP 4** | Oceánica / Remota | 4 NM | Permite separación lateral reducida (ej. 30 NM o 50 NM). |
| **RNP 2** | En ruta (Continental y Oceánica/Remota) | 2 NM | Versátil para zonas con poca infraestructura terrestre. |
| **RNAV 5** | En ruta Continental | 5 NM | Usado en Europa (B-RNAV). También para llegadas (STAR) fuera de 30 NM/MSA. |
| **RNAV 2** | En ruta Continental, Salidas/Llegadas | 2 NM | Común en EE.UU. |
| **RNAV 1** | Terminal (Salidas/Llegadas) | 1 NM | P-RNAV en Europa. Requiere cobertura radar o GNSS. |
| **RNP 1** | Terminal (Salidas/Llegadas) | 1 NM | Similar a RNAV 1 pero con alerta. Usado donde no hay vigilancia ATS robusta. |
| **RNP APCH** | Aproximación (Inicial, Intermedia, Final, Frustrada) | 0.3 NM (Final) | Aproximaciones GNSS estándar (LNAV, LNAV/VNAV, LPV). |
| **RNP AR APCH** | Aproximación (Authorisation Required) | 0.3 - 0.1 NM | Para terrenos complejos. Requiere autorización específica y entrenamiento. |
| **RNP 0.3** | Todas (excepto Oceánica y Final Approach) | 0.3 NM | Específico para **helicópteros**. |

## Puntos Clave
*   **Aprobación Operacional**: Una aprobación para una especificación más estricta (ej. RNP 0.3) **NO** implica aprobación automática para una menos estricta (ej. RNP 4), ya que los requisitos funcionales pueden ser diferentes.
*   **Designación**: La "X" en RNAV X o RNP X indica la precisión lateral en millas náuticas que debe mantenerse el 95% del tiempo.
*   **NAT HLA**: Requiere RNP 10 (RNAV 10) o RNP 4.
