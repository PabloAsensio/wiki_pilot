---
title: "Servicios meteorológicos"
description: "Servicios meteorológicos en ruta: VOLMET, ATIS, WAFC y las transmisiones de clima en vuelo para pilotos."
keywords: ["servicios meteorológicos aviación", "VOLMET ATIS ruta", "centro mundial de pronósticos WAFC ATPL", "transmisiones clima vuelo"]
---

# Servicios meteorológicos


![Torre de Control de Tráfico Aéreo distribuyendo info ATIS](https://upload.wikimedia.org/wikipedia/commons/a/a0/The_FAA_air_traffic_control_tower_at_Philadelphia_International_Airport.jpg)

## Centros de Pronóstico de Área Mundial (WAFC)

Los **WAFC (World Area Forecast Centres)** son centros meteorológicos designados para preparar y emitir pronósticos significativos y de altitud en formato digital a nivel mundial.
*   **Responsabilidades:** Preparar pronósticos de rejilla (gridded forecasts) de:
    *   Viento y temperatura en altitud.
    *   Humedad.
    *   Altitud geopotencial.
    *   Tropopausa (nivel y temperatura).
    *   Viento máximo (dirección, velocidad y nivel).
    *   Nubes Cumulonimbus (CB).
    *   Engelamiento y Turbulencia.

## Asesoramiento de Ciclones Tropicales (TC Advisory)

Mensaje emitido por un TCAC (Tropical Cyclone Advisory Centre) con información sobre la posición, movimiento e intensidad de un ciclón tropical.

**Estructura del Código:**
1.  **TC ADVISORY:** Identificación del mensaje.
2.  **DTG:** Fecha y hora de emisión (AAAAMMDD/HHMMZ).
3.  **TCAC:** Nombre del centro (ej. MIAMI).
4.  **TC:** Nombre del ciclón (ej. DORIAN).
5.  **NR:** Número de aviso (ej. 2013/4).
6.  **OBS PSN:** Posición observada del centro (Lat/Long).
7.  **MOV:** Dirección y velocidad de movimiento (ej. NW 18 KT).
    *   `SLW` (Slow): < 3 kt.
    *   `STNR` (Stationary): < 1 kt.
8.  **INTST CHANGE:** Cambio de intensidad (ej. `INTSF` = Intensifying / Intensificándose, `WKN` = Weakening / Debilitándose, `NC` = No Change).
9.  **C:** Presión atmosférica en el centro (hPa).
10. **MAX WIND:** Viento máximo en superficie (10 min promedio).
11. **FCST PSN / MAX WIND:** Pronósticos a +6, +12, +18, +24 horas.
12. **NXT MSG EXP:** Fecha/hora del próximo mensaje.

## Servicios de Información de Vuelo (ATIS y D-ATIS)

*   **ATIS (Automatic Terminal Information Service):** Emisión continua de información rutinaria para aeronaves en llegada y salida.
*   **D-ATIS (Data Link ATIS):** Versión digital del ATIS transmitida vía enlace de datos (ACARS).
    *   **Ventaja:** Permite a los pilotos obtener la información meteorológica y operativa del aeropuerto de destino mucho antes de estar dentro del alcance de radio VHF (ej. vía SATCOM).

## Abreviaturas de Fenómenos Meteorológicos

Es crucial conocer las abreviaturas del Anexo 3 de la OACI para interpretar METAR, TAF y SIGMET:

*   **Precipitación:**
    *   **PL:** Ice Pellets (Gránulos de hielo).
    *   **GR:** Hail (Granizo, $\ge$ 5mm).
    *   **GS:** Small Hail / Snow Pellets (< 5mm).
    *   **SG:** Snow Grains (Granos de nieve).
    *   **IC:** Ice Crystals (Cristales de hielo - no se reportan como precipitación en METAR, sino como oscurecimiento si visibilidad < 5000m).
*   **Otros Fenómenos:**
    *   **SQ:** Squall (Turbonada - aumento repentino del viento de al menos 16 kt, alcanzando 22 kt o más, durando al menos 1 minuto).
    *   **PO:** Dust/Sand Whirls (Remolinos de polvo/arena).
    *   **FC:** Funnel Cloud (Nube en embudo - Tornado o Tromba marina).
    *   **SS:** Sandstorm (Tormenta de arena).
    *   **DS:** Duststorm (Tormenta de polvo).

## Grupo de Estado de la Pista (Runway State Group)

En el METAR, se puede añadir información sobre el estado de la pista si hay contaminantes (nieve, hielo, etc.).
Formato: **RDrDr/ErCrereRBrBr** (ej. `88/425035`)

*   **DrDr:** Designador de pista (`88` = Todas las pistas).
*   **Er:** Tipo de depósito (`4` = Nieve seca).
*   **Cr:** Extensión (`2` = 11% a 25%).
*   **ereR:** Profundidad (`50` = 50 mm).
*   **BrBr:** Coeficiente de fricción / Acción de frenado (`35` = 0.35 / Medio-Bueno).

## Avisos de Aeródromo y Cortante de Viento

*   **Avisos de Aeródromo:** Advierten sobre condiciones peligrosas en tierra (viento fuerte, helada, etc.).
*   **Alertas de Wind Shear:** Advierten sobre cortante de viento en la aproximación o despegue.
    *   Pueden basarse en reportes de aeronaves (ej. "Microburst reported by A320 on final approach").

## SIGMET

Información emitida por una **Oficina de Vigilancia Meteorológica (MWO)** sobre la ocurrencia o previsión de fenómenos meteorológicos en ruta que pueden afectar la seguridad de las operaciones de aeronaves (ej. Turbulencia Severa, Engelamiento Severo, Ceniza Volcánica, etc.).
