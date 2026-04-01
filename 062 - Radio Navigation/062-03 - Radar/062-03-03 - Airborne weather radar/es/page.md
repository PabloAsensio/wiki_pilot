---
title: Radionavegación: Radar Meteorologico de a Bordo
description: Comprende funcionamiento, limitaciones y uso tactico del radar meteorologico de a bordo.
keywords:
  - radar meteorologico de a bordo
  - radar meteorologico aviacion
  - evitacion convectiva
---

# Radionavegación: Radar Meteorologico de a Bordo

El **Radar Meteorológico de A bordo (AWR)** es un sistema de radar primario diseñado para detectar precipitaciones y permitir a la tripulación evitar condiciones meteorológicas adversas.

## Principios de Operación

*   **Frecuencia**: Opera en la banda **SHF** (Super High Frequency), típicamente en **9.375 GHz** (Banda X).
*   **Longitud de Onda**: Aproximadamente **3.2 cm**. Esta longitud de onda es ideal para reflejarse en gotas de agua grandes y granizo húmedo, ignorando partículas muy pequeñas como niebla o llovizna.
*   **Reflectividad**:
    *   **Granizo húmedo y gotas grandes**: Alta reflectividad (Ecos fuertes).
    *   **Nieve seca y cristales de hielo**: Baja reflectividad (Ecos débiles o nulos).
    *   **Colores en Pantalla**:
        *   **Verde**: Precipitación ligera.
        *   **Amarillo/Ámbar**: Precipitación moderada.
        *   **Rojo**: Precipitación fuerte.
        *   **Magenta**: Precipitación extrema o turbulencia severa.

## Funciones y Modos

### Detección de Meteorología (Weather Mode)
Utiliza un haz cónico estrecho (**Pencil Beam**, aprox 3-5° de ancho) para escanear el frente de la aeronave.
*   **Turbulencia**: Los radares modernos (Doppler) pueden detectar turbulencia midiendo el desplazamiento de frecuencia (Doppler shift) de las gotas de lluvia en movimiento. **Solo funciona si hay precipitación** (turbulencia húmeda); no detecta turbulencia en aire claro (CAT).
*   **Windshear**: Utiliza el efecto Doppler para detectar cizalladura del viento (microbursts) por delante de la aeronave, generalmente a bajas altitudes.

### Mapeo del Terreno (Mapping Mode)
Utiliza un haz en forma de abanico (**Cosecant Squared Beam**) o inclina el haz cónico hacia abajo para obtener ecos del terreno.
*   Útil para navegación básica (líneas de costa, islas, montañas) cuando fallan otros sistemas.
*   Se distingue tierra (ecos) de agua (sin ecos).

## Gestión del Tilt (Inclinación de Antena)

El piloto debe ajustar manualmente el **Tilt** para escanear diferentes niveles de la atmósfera, aunque los sistemas modernos tienen funciones automáticas (*Auto-tilt*).

*   **Despegue/Ascenso**: Tilt **alto** (+4° a +15°) para ver la meteorología en la trayectoria de ascenso y evitar ecos de tierra cercanos.
*   **Crucero**: Tilt **bajo** (0° a -1°) para escanear la parte más reflectiva de las tormentas (niveles medios/bajos donde hay agua líquida).
    *   *Peligro*: A gran altitud, si el tilt es demasiado alto, el radar puede escanear solo la cima de la tormenta (cristales de hielo) y no mostrar nada, ocultando la actividad severa debajo (**Over-scanning**).
*   **Descenso**: Tilt ligeramente **hacia arriba** (+4° a +5°) para evitar el desorden del terreno (ground clutter) a medida que el avión baja.

## Limitaciones y Peligros

### Atenuación (Shadowing)
Las precipitaciones muy intensas pueden absorber o reflejar toda la energía del radar, impidiendo ver lo que hay detrás.
*   Aparece como una "sombra" negra detrás de un eco rojo intenso.
*   **Regla**: Nunca volar hacia una sombra de radar detrás de una tormenta; se desconoce qué hay allí (posiblemente otra tormenta severa).

### Peligro de Radiación
El radar emite radiación de microondas de alta energía. No debe operarse en tierra cuando hay personal cerca del radomo o durante el repostaje de combustible.

### Evitación de Tormentas
*   Desviarse al menos **20 NM** lateralmente de ecos intensos.
*   Preferiblemente desviarse por el lado de **barlovento** (upwind) para evitar el granizo y turbulencia que el viento puede arrastrar fuera de la nube.
*   No intentar volar por debajo de una tormenta (peligro de microbursts y granizo).
