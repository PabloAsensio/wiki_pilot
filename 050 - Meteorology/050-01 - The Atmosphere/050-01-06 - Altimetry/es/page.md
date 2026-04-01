---
title: "Altimetría"
description: "Aprenda todo sobre altimetría en aviación: presiones QNH, QFE, QNE y diferencias entre la altitud verdadera, indicada y teórica (Pressure Altitude)."
keywords: ["altimetría aviación QNH QFE QNE", "altitud verdadera vs altitud de presión", "ajuste de altímetro vuelo", "meteorología ATPL altimetría", "niveles de vuelo altímetro"]
---

# Altimetría


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

### Perspectiva del piloto en la aeronave: Ejemplo práctico

Así es cómo se viven estas correcciones en la cabina. Veamos un ejercicio completo:

**Situación**: Estás en aproximación a un aeródromo en un día de invierno. Dispones de los siguientes datos:
*   QNH del destino: **1003 hPa**
*   Altitud Indicada actual: **5.000 ft** (altímetro calado a QNH)
*   OAT (temperatura exterior): **-5°C**
*   Elevación del aeródromo: **500 ft**

**Paso 1 – Corrección de Presión** (pasar de Altitud Indicada a Altitud de Presión):

$$Corrección = (1003 - 1013) \times 30 = -10 \times 30 = -300 \text{ ft}$$

El QNH está por debajo de 1013, así que tu Altitud de Presión (con 1013 calado) sería **5.300 ft**. Dicho de otro modo, tu altímetro *subestima* lo alto que estás en términos de presión estándar.

**Paso 2 – Corrección de Temperatura** (obtener la Altitud Verdadera):

Temperatura ISA a 5.000 ft = 15 − (5 × 2) = **+5°C**  
Desviación ISA = OAT − ISA = −5 − 5 = **−10°C** (más frío que ISA)

$$Corrección\_Temp = 4 \times (-10) \times \frac{5.000}{1.000} = -200 \text{ ft}$$

Altitud Verdadera = 5.000 − 200 = **4.800 ft**

**Interpretación desde la cabina**: Tu altímetro marca 5.000 ft con QNH, pero en realidad estás a **4.800 ft** sobre el nivel del mar. El aeródromo está a 500 ft, por lo que la separación real sobre el terreno es de solo 4.300 ft — **200 ft menos** de lo que indica el altímetro. En días fríos como este, aplica siempre márgenes de seguridad adicionales sobre el terreno.

> 💡 **Regla práctica**: En condiciones de baja presión y/o frío intenso, la altitud real siempre es **menor** que la indicada. El altímetro te "miente a tu favor" en el examen pero puede ser peligroso en el vuelo real.

## Procedimientos de Transición

*   **Altitud de Transición (TA)**: Altitud a la cual (o por debajo de la cual) la posición vertical se controla por referencia a altitudes (QNH). Al ascender y cruzar la TA, se cambia a 1013 hPa.
*   **Nivel de Transición (TL)**: El nivel de vuelo más bajo disponible para usar por encima de la altitud de transición. Al descender y cruzar el TL, se cambia a QNH.
*   **Capa de Transición**: Espacio entre la TA y el TL.
