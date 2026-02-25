## Definiciones Clave

![Ajustes de Altímetro (QNH, QFE, QNE)](https://upload.wikimedia.org/wikipedia/commons/b/bb/FL_QNE_QNH_QFE.png)

*   **Altitud Verdadera (True Altitude)**: La altura real de la aeronave sobre el nivel medio del mar (MSL).
*   **Altitud Indicada (Indicated Altitude)**: La lectura del altímetro cuando está ajustado al **QNH** local.
*   **Altitud de Presión (Pressure Altitude)**: La lectura del altímetro cuando está ajustado a la presión estándar (**1013.2 hPa**). Se utiliza para volar en **Niveles de Vuelo (FL)**.
*   **QNH**: Presión atmosférica reducida al nivel del mar según la atmósfera estándar. Al calar QNH en tierra, el altímetro indica la **elevación del aeródromo**.
*   **QFE**: Presión atmosférica medida en el aeródromo. Al calar QFE en tierra, el altímetro indica **cero**.
*   **QFF**: Presión atmosférica reducida al nivel del mar considerando la temperatura real.

## Errores del Altímetro

El altímetro es esencialmente un barómetro que mide presión y la convierte a altitud asumiendo condiciones estándar (ISA). Si las condiciones no son estándar, la indicación será errónea.

![Influencia de la Temperatura en el Altímetro](https://upload.wikimedia.org/wikipedia/commons/2/25/Temperature%27s_influence_on_aircraft_altimeters.png)

### Error de Presión
*   **De Alta a Baja (High to Low)**: Si vuelas hacia una zona de menor presión sin ajustar el altímetro (manteniendo el ajuste anterior más alto), el altímetro indicará más altitud de la que realmente tienes.
    *   *"High to Low, Look out below"* -> **Altitud Verdadera < Altitud Indicada**. (Peligroso).
*   **De Baja a Alta (Low to High)**: Si vuelas hacia una zona de mayor presión, el altímetro indicará menos altitud de la real.
    *   **Altitud Verdadera > Altitud Indicada**.

### Error de Temperatura
*   **Aire Frío (Colder than ISA)**: La columna de aire se contrae. Para una misma presión, la altitud real es menor.
    *   *"Warm to Cold, Don't be bold"* -> **Altitud Verdadera < Altitud Indicada**. (Peligroso).
*   **Aire Caliente (Warmer than ISA)**: La columna de aire se expande.
    *   **Altitud Verdadera > Altitud Indicada**.

## Cómo hacer los ejercicios de altimetría

### Perspectiva del piloto en la aeronave

Antes de entrar en los cálculos, es importante entender cómo se viven estas correcciones desde la cabina:

*   **En tierra antes de despegar**: Recibes el QNH del ATIS o de la torre de control. Lo introduces en el altímetro (la ventanilla de Kollsman) y el altímetro debería indicar la elevación del aeródromo. Si hay una diferencia significativa (más de ±50 ft), el altímetro puede tener un error de instrumento.
*   **Durante el ascenso**: Al alcanzar la **Altitud de Transición (TA)**, cambias el ajuste del altímetro de QNH a **1013 hPa** y empiezas a volar en Niveles de Vuelo (FL).
*   **Durante el descenso**: Al descender y cruzar el **Nivel de Transición (TL)**, cambias de 1013 hPa al QNH del destino, para que el altímetro vuelva a indicar altitud sobre el nivel del mar.
*   **Vuelo a baja altitud**: Si vuelas a baja altura en un día frío, recuerda que la altitud real puede ser **inferior** a la indicada. Mantén márgenes de seguridad adicionales sobre el terreno.

### 1. Corrección de Presión
Se asume un gradiente barométrico de **30 ft por hPa** (o 27 ft/hPa si se especifica).

$$Corrección = (QNH - 1013) \times 30$$

*   Si QNH > 1013: Altitud Indicada > Altitud de Presión.
*   Si QNH < 1013: Altitud Indicada < Altitud de Presión.

### 2. Corrección de Temperatura (Regla del 4%)
La altitud verdadera cambia aproximadamente un **4% por cada 10°C de desviación ISA**.

$$Corrección\_Temp = 4 \times (Desviación\_ISA) \times \frac{Altitud\_Indicada}{1000}$$

*   **Más caliente que ISA**: Sumar corrección (True Alt > Indicated Alt).
*   **Más frío que ISA**: Restar corrección (True Alt < Indicated Alt).

*Nota: La corrección de temperatura se aplica a la columna de aire entre la estación (aeródromo) y la aeronave. Si se calcula la altitud verdadera sobre el terreno, usar (Altitud Indicada - Elevación Estación) en la fórmula.*

## Procedimientos de Transición

*   **Altitud de Transición (TA)**: Altitud a la cual (o por debajo de la cual) la posición vertical se controla por referencia a altitudes (QNH). Al ascender y cruzar la TA, se cambia a 1013 hPa.
*   **Nivel de Transición (TL)**: El nivel de vuelo más bajo disponible para usar por encima de la altitud de transición. Al descender y cruzar el TL, se cambia a QNH.
*   **Capa de Transición**: Espacio entre la TA y el TL.
