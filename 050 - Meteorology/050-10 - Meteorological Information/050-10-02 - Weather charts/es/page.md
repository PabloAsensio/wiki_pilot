---
title: "Mapas meteorológicos"
description: "Cómo leer mapas meteorológicos: análisis de superficie, tiempo significativo (SIGWX) y mapas de vientos en altura."
keywords: ["mapas meteorológicos aviación", "mapas SIGWX vuelo", "análisis de superficie ATPL", "leer mapas viento gran altitud"]
---

# Mapas meteorológicos


## Cartas de Tiempo Significativo (SIGWX)

Las cartas de tiempo significativo (SIGWX) proporcionan un pronóstico de los fenómenos meteorológicos importantes para la aviación.

![Carta de Pronóstico Aeronáutico](https://upload.wikimedia.org/wikipedia/commons/d/df/Aviation_weather_forecast_chart.png)

### Simbología de Frentes
*   **Frente Cálido:** Semicírculos rojos.
*   **Frente Frío:** Triángulos azules.
*   **Frente Ocluido:** Semicírculos y triángulos alternados (púrpura).
    *   **Oclusión Fría:** La línea de oclusión sigue la línea del frente frío.
*   **Frente Estacionario:** Semicírculos y triángulos en lados opuestos de la línea.

### Fenómenos Significativos
*   **Niebla (Fog):** Símbolo de líneas horizontales.
*   **Humo (Smoke):** Símbolo específico.
*   **Bruma (Haze):** Símbolo de infinito (∞).
*   **Ciclón Tropical:** Símbolo de espiral con dos brazos.
*   **Volcán:** Símbolo de trapecio con humo/ceniza.

### Corrientes en Chorro (Jet Streams)
Se representan como líneas gruesas con flechas.
*   **Núcleo:** La velocidad del viento en el núcleo se indica con barbas/banderas (ej. 120 kt).
*   **Altitud:** Se indica el nivel de vuelo del núcleo (ej. FL370).
*   **Profundidad:** Se indican los niveles inferior y superior entre los cuales el viento excede los 80 kt (ej. FL230 - FL440).
*   **Cambio de Viento:** Las líneas discontinuas paralelas al Jet indican zonas de Turbulencia en Aire Claro (CAT).

### Tropopausa
*   **Altura:** Se indica en cientos de pies dentro de rectángulos (ej. 350 = FL350).
*   **Centros de Alta/Baja:** Encerrados en polígonos con una "H" (High) o "L" (Low).
    *   La tropopausa es más alta en el ecuador y más baja en los polos.
    *   En un Jet Stream, la tropopausa es más baja en el lado frío (polar) y más alta en el lado cálido.

### Nubes y Peligros Asociados
En las cartas SIGWX, la mención de **CB (Cumulonimbus)** implica automáticamente la presencia de:
*   Tormentas (TS).
*   Granizo (GR).
*   Turbulencia Moderada o Severa.
*   Engelamiento Moderado o Severo.

**Cobertura:**
*   **ISOL (Aislado):** < 50% del área (individuales).
*   **OCNL (Ocasional):** 50-75% del área (bien separados).
*   **FRQ (Frecuente):** > 75% del área (poca o ninguna separación).
*   **EMBD (Embebido):** Dentro de otras capas de nubes.

## Predicción Numérica del Tiempo (NWP)

### Sistema de Rejilla 3D
Los modelos meteorológicos dividen la atmósfera en una rejilla tridimensional.
*   **Datos Horizontales:** Latitud y Longitud.
*   **Datos Verticales:** Altura o Presión.
*   No se usa el tiempo como eje de la rejilla en sí, sino que se calculan pasos de tiempo.

### WAFC (World Area Forecast Centre)
Existen dos centros (Londres y Washington) designados para preparar y emitir pronósticos globales.
*   Generan pronósticos de rejilla (gridded forecasts) de viento, temperatura, humedad, tropopausa, CB, engelamiento y turbulencia.
*   Estos datos se integran en los sistemas de planificación de vuelo.

### Reportes de Pilotos
Los datos de aeronaves (AIREP/PIREP) se pueden fusionar en los sistemas de procesamiento para mejorar la **conciencia situacional** y refinar los modelos de predicción futuros.

## Cartas de Superficie

Muestran la presión al nivel del mar mediante isobaras.
*   **Baja Presión (Ciclón/Depresión):** El aire gira en sentido antihorario (Hemisferio Norte). Vientos convergen y ascienden -> Mal tiempo.
*   **Alta Presión (Anticiclón):** El aire gira en sentido horario (Hemisferio Norte). Vientos divergen y descienden (subsidencia) -> Buen tiempo, pero posible niebla/bruma por inversión.
*   **Collado (Col):** Zona entre dos altas y dos bajas. Vientos calmos. En verano propicio para tormentas de masa de aire; en invierno para niebla.
*   **Cuña (Ridge):** Extensión de alta presión. Buen tiempo.
*   **Vaguada (Trough):** Extensión de baja presión. Mal tiempo.

## Cartas de Viento y Temperatura en Altura

Muestran la dirección e intensidad del viento y la temperatura a niveles de vuelo específicos.

### Interpretación
*   **Barbas de Viento:**
    *   Línea corta: 5 kt.
    *   Línea larga: 10 kt.
    *   Triángulo/Bandera: 50 kt.
    *   La dirección es desde donde sopla el viento (comparar con los meridianos locales para el Norte Verdadero).
*   **Temperatura:** Se indica junto a la estación o en la rejilla.
    *   **Cálculo de Desviación ISA:**
        1.  Calcular Temp. ISA estándar: $15 - (2 \times \text{Altitud en miles de pies})$.
        2.  Comparar con la Temp. Real (OAT).
        3.  Ejemplo a FL180 con OAT -30°C:
            *   ISA FL180 = $15 - (2 \times 18) = 15 - 36 = -21^\circ\text{C}$.
            *   Diferencia: $-30$ es 9 grados más frío que $-21$.
            *   Desviación: ISA -9°C.
