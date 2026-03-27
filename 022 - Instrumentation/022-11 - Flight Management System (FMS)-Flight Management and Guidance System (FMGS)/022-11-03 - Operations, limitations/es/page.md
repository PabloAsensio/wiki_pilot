---
title: "Operaciones y Limitaciones del FMS: Inicialización, CI, LNAV/VNAV y Precisión"
description: "Aprende la operación práctica del FMS desde IDENT/POS INIT/RTE/PERF hasta estrategia de cost index, comportamiento LNAV/VNAV y degradación de precisión."
keywords:
    - "cost index"
    - "lnav vnav"
    - "flight level"
    - "minimum speed"
---

# Operaciones y Limitaciones del FMS: Inicialización, CI, LNAV/VNAV y Precisión

## Secuencia de Inicialización

La configuración del FMS para un vuelo sigue típicamente un flujo lógico de páginas en la CDU:

1.  **Página IDENT:**
    *   La primera página que se muestra después del encendido.
    *   Utilizada para verificar el **Modelo de Aeronave**, **Tipo de Motor** y **Validez de la Base de Datos de Navegación** (fechas activas).

2.  **POS INIT (Inicialización de Posición):**
    *   Inicializa el Sistema de Referencia Inercial (IRS).
    *   Generalmente utiliza la posición **GPS** o las coordenadas del **Punto de Referencia del Aeropuerto (ARP)**.

3.  **RTE (Ruta):**
    *   Entrada de aeropuertos de **Origen** y **Destino**.
    *   Selección de una **Ruta de Compañía** o entrada manual de waypoints y aerovías.

4.  **PERF INIT (Inicialización de Rendimiento):**
    *   Entrada de **Peso Cero Combustible (ZFW)**, **Cantidad de Combustible** y **Altitud de Crucero**.
    *   **Cost Index (CI):** Un parámetro crucial que determina el perfil económico del vuelo.

## Cost Index (CI)

El Cost Index es una herramienta de gestión estratégica que equilibra el **Costo de Combustible** frente a los **Costos Operativos Relacionados con el Tiempo**.

$$ CI = \frac{\text{Costo del Tiempo}}{\text{Costo del Combustible}} $$

*   **CI = 0:** Mínimo Combustible de Viaje (Velocidad de Máximo Alcance). La aeronave vuela lentamente para ahorrar combustible.
*   **CI Alto:** Mínimo Tiempo de Vuelo. La aeronave vuela rápido, ignorando el mayor consumo de combustible.

## Cálculo de Posición y Precisión

El FMS calcula una "Posición del Sistema" mezclando datos de múltiples sensores utilizando un **Filtro de Kalman**.

### Entradas y Prioridad
1.  **GPS (GNSS):** La fuente más precisa y primaria.
2.  **DME/DME:** Posición de radio derivada de múltiples distancias DME.
3.  **VOR/DME:** Marcación y distancia desde una estación.
4.  **LOC:** Localizador para alineación lateral durante la aproximación.
5.  **IRS:** Posición inercial (se desvía con el tiempo).

### Degradación y Limitaciones
*   **Pérdida de GPS:** Si se pierden las señales GPS, el FMS revierte a la actualización Radio/IRS. La precisión de la posición puede **degradarse gradualmente** o "desplazarse" (Map Shift).
*   **RAIM (Monitorización Autónoma de Integridad del Receptor):** Esencial para **RNP** y aproximaciones basadas en GPS. La pérdida de GPS implica la pérdida de RAIM y la incapacidad de volar estas aproximaciones.
*   **Actualización en Pista:** En el despegue, aplicar potencia TOGA a menudo activa una actualización de posición a las coordenadas del umbral de la pista.

## Modos de Navegación

### Navegación Lateral (LNAV)
*   **Comando:** Sigue el plan de vuelo horizontal.
*   **Autotuning:** El FMS sintoniza automáticamente frecuencias VOR y DME para la actualización de posición sin intervención de la tripulación.
*   **Overfly vs. Fly-by:**
    *   **Fly-by:** Estándar. La aeronave anticipa el viraje para cortar la esquina.
    *   **Overfly:** La aeronave debe pasar directamente sobre el waypoint antes de iniciar el viraje.

### Navegación Vertical (VNAV)
*   **Comando:** Gestiona el perfil vertical (Ascenso, Crucero, Descenso).
*   **Referencia Barométrica:** La lógica VNAV se basa en la **Altitud Barométrica** del Ordenador de Datos de Aire (ADC).
*   **Autothrottle:** Esencial para la operación completa VNAV (gestionando interacciones velocidad/empuje).
*   **Modos:**
    *   **VNAV SPD:** El cabeceo mantiene la velocidad.
    *   **VNAV PTH:** El cabeceo mantiene la trayectoria geométrica (velocidad controlada por empuje/resistencia).
    *   **VNAV ALT:** Nivelación en una restricción o altitud MCP intermedia.

### Predicciones de Rendimiento
*   El FMS predice el consumo de combustible y tiempos de llegada (ETA).
*   **Limitación:** Las predicciones asumen que la aeronave está en una **configuración normal**. Si la aeronave vuela con **slats/flaps extendidos** o **tren abajo** por períodos prolongados (configuración anormal), la resistencia es mayor que la modelada y las **predicciones de combustible serán imprecisas**.
