---
title: "Información para la planificación de vuelo"
description: "Información meteorológica para la planificación: TAF, AIRMET, SIGMET y briefings pre-vuelo."
keywords: ["planificación de vuelo meteorología", "TAF AIRMET SIGMET aviación", "briefing meteorológico ATPL", "piloto planificación tiempo"]
---

## Reportes Meteorológicos de Aeródromo (METAR y SPECI)

![Equipamiento de Procesamiento de METAR y TAF](https://upload.wikimedia.org/wikipedia/commons/9/91/Metar_2010.jpg)

### METAR (Meteorological Aerodrome Report)
Es un informe rutinario de las condiciones meteorológicas observadas en un aeródromo. Se emite generalmente cada 30 o 60 minutos.

### SPECI (Special Report)
Es un informe especial que se emite cuando ocurren cambios significativos (deterioro o mejora) en las condiciones meteorológicas entre los reportes rutinarios (ej. cambio de viento, visibilidad, nubes bajas, o inicio/fin de tormentas).

### Decodificación Básica
Ejemplo: `EGKK 191050Z 09002KT 0200 R08R/0350 VV001 M03/M02 Q1008`

*   **Identificador:** `EGKK` (Gatwick).
*   **Fecha/Hora:** `191050Z` (Día 19 a las 10:50 UTC).
*   **Viento:** `09002KT` (090 grados, 2 nudos).
*   **Visibilidad:** `0200` (200 metros).
*   **RVR:** `R08R/0350` (Pista 08 Derecha, 350 metros).
    *   Tendencias: `U` (Increasing/Aumentando), `D` (Decreasing/Disminuyendo), `N` (No change/Sin cambios).
    *   Prefijos: `P` (Más de, ej. P1500), `M` (Menos de, ej. M0050).
*   **Nubes/Visibilidad Vertical:** `VV001` (Visibilidad vertical 100 pies - cielo oscurecido).
    *   `FEW`, `SCT`, `BKN`, `OVC`.
    *   `NSC`: No Significant Clouds (sin nubes operativamente significativas, pero no CAVOK).
    *   `CAVOK`: Visibilidad $\ge$ 10 km, sin nubes por debajo de 5000 ft o MSA, sin fenómenos significativos (CB/TCU).
*   **Temperatura/Punto de Rocío:** `M03/M02` (-3°C / -2°C).
*   **QNH:** `Q1008` (1008 hPa).

### Pronóstico de Tendencia (Trend Forecast)
Se añade al final del METAR y es válido por **2 horas**.
*   **NOSIG:** Sin cambios significativos previstos.
*   **BECMG:** Cambio gradual o regular a nuevas condiciones.
*   **TEMPO:** Fluctuaciones temporales (menos de 1 hora cada vez, y menos de la mitad del periodo total).

## Pronósticos de Aeródromo (TAF)

El TAF (Terminal Aerodrome Forecast) describe las condiciones meteorológicas esperadas en un aeródromo durante un periodo específico (generalmente 9, 24 o 30 horas).

### Indicadores de Cambio
*   **BECMG (Becoming):** Cambio permanente esperado dentro del periodo de tiempo indicado.
*   **TEMPO (Temporary):** Condiciones temporales que duran menos de una hora.
*   **PROB30 / PROB40:** Probabilidad del 30% o 40% de que ocurra un fenómeno (generalmente usado con TEMPO).

## Información en Ruta (SIGMET y AIRMET)

### SIGMET
Información sobre fenómenos meteorológicos en ruta que pueden afectar la seguridad de **todas las aeronaves**.
*   **Validez:** Máximo 4 horas (6 horas para Ceniza Volcánica y Ciclones Tropicales).
*   **Fenómenos:**
    *   Tormentas (TS) (Oscurecidas, Embebidas, Frecuentes, Línea de turbonada).
    *   Turbulencia Severa (SEV TURB).
    *   Engelamiento Severo (SEV ICE).
    *   Ondas de Montaña Severas (SEV MTW).
    *   Tormentas de polvo/arena fuertes.
    *   Ceniza Volcánica (VA).
    *   Ciclón Tropical (TC).

### AIRMET
Similar al SIGMET pero para fenómenos que afectan la seguridad de vuelos a **baja altura** (generalmente por debajo de FL100 o FL150 en zonas montañosas) y que no fueron incluidos en el pronóstico de área.

## Avisos y Alertas

### Avisos de Aeródromo (Aerodrome Warnings)
Información concisa sobre condiciones que podrían afectar adversamente a las aeronaves **en tierra** (incluyendo estacionadas) y a las instalaciones.
*   Ejemplos: Viento fuerte, granizo, nieve, helada, engelamiento en tierra.

### Alerta de Cortante de Viento (Wind Shear Alert)
Avisos sobre la existencia observada o esperada de cortante de viento en la trayectoria de aproximación o despegue (entre el nivel de pista y 500 m / 1600 ft).

### Avisos de Ceniza Volcánica y Ciclones
Emitidos por los **VAAC** (Volcanic Ash Advisory Centres) y **TCAC** (Tropical Cyclone Advisory Centres) para guiar a las oficinas de vigilancia meteorológica en la emisión de SIGMETs.

## Servicios de Información de Vuelo

### ATIS (Automatic Terminal Information Service)
Emisión continua (voz o enlace de datos D-ATIS) de información rutinaria para aeronaves llegando o saliendo. Contiene información operativa (pista en uso) y meteorológica (viento, visibilidad, nubes, temp, QNH).

### VOLMET
Radiodifusión de información meteorológica (METAR, SPECI, TAF, SIGMET) para aeronaves **en vuelo**.

## Reportes desde Aeronaves (AIREP)

*   **AIREP Rutinario:** Posición e información básica.
*   **AIREP Especial (ARS):** Se debe emitir obligatoriamente cuando se encuentran condiciones peligrosas no pronosticadas o significativas, tales como:
    *   Turbulencia moderada o severa.
    *   Engelamiento moderado o severo.
    *   Ondas de montaña severas.
    *   Tormentas con o sin granizo.
    *   Nube de ceniza volcánica.
