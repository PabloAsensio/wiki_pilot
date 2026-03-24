---
title: Flight Data Recorder (FDR) - Registrador de Datos de Vuelo
---

El **FDR** registra los parámetros técnicos del vuelo para ayudar en el análisis de accidentes y la resolución de problemas (troubleshooting). Generalmente se encuentra dentro de un contenedor diseñado para sobrevivir a impactos (a prueba de golpes, incendios, color naranja) y equipado con un **Dispositivo de Localización Subacuática (ULD)**.

### Requisitos de Grabación
El tipo y número de parámetros grabados están determinados por:
1.  **Capacidad de Grabación** del sistema.
2.  **Requisitos Operativos Aplicables** (Regulaciones).

### Parámetros Obligatorios
Los parámetros comunes incluyen (pero no se limitan a):
*   Tiempo / Conteo de Tiempo Relativo.
*   Altitud de Presión y Velocidad (Airspeed).
*   Actitud (Cabeceo y Alabeo).
*   Rumbo.
*   Aceleración Normal (G Vertical).
*   Empuje/Potencia en cada motor y posiciones de las Palancas.
*   Configuración (Flaps, Slats, Spoilers, Tren).
*   Modos de Piloto Automático/Director de Vuelo.

### Operación
*   **Activación Automática**:
    *   **Inicio**: Antes de que el avión sea capaz de moverse por su propia potencia (a menudo al encender motores o energía).
    *   **Parada**: Después de que el avión es incapaz de moverse por su propia potencia (apagado de motores).
*   **Botón de Evento**: Un botón en la cabina que permite a la tripulación colocar una **Marca de Tiempo** en el flujo de datos. Esto destaca un evento específico (ej. un fallo temporal de sistema o turbulencia) para ayudar a los investigadores a localizar los datos relevantes posteriormente.
