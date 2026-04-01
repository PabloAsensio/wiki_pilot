---
title: "Humedad"
description: "Comprende los conceptos de humedad en aviación: humedad relativa (RH), punto de rocío (dew point), mixing ratio y sus fórmulas para exámenes de meteorología."
keywords: ["humedad relativa aviación", "cálculo de relative humidity ATPL", "punto de rocío dew point meteorología", "mixing ratio temperatura del aire", "meteorología aeronáutica humedad", "variación diurna humedad relativa"]
---

# Humedad


La humedad es la medida de la cantidad de vapor de agua presente en el aire.

## Conceptos Clave

### 1. Humedad Relativa (RH - Relative Humidity)
Es la relación entre la cantidad de vapor de agua que contiene el aire y la cantidad máxima que podría contener a esa temperatura, expresada en porcentaje.

*   **Fórmula Aproximada:**
    $$RH \approx 100 - 5 \times (T - T_d)$$
    Donde $T$ es la temperatura del aire y $T_d$ es el punto de rocío.
*   **Fórmula Exacta (basada en Mixing Ratio):**
    $$RH = \frac{\text{Humidity Mixing Ratio (HMR)}}{\text{Saturation Mixing Ratio (SMR)}} \times 100$$
*   **Relación con la Temperatura:**
    *   Si la temperatura **aumenta** (y el contenido de agua se mantiene constante), la capacidad del aire para contener agua aumenta, por lo tanto, la **Humedad Relativa disminuye**.
    *   Si la temperatura **disminuye**, la capacidad disminuye, y la **Humedad Relativa aumenta**.
*   **Variación Diurna:**
    *   **Máxima RH:** Al amanecer (temperatura mínima).
    *   **Mínima RH:** A primera hora de la tarde (temperatura máxima).

### 2. Punto de Rocío (Dew Point - $T_d$)
Es la temperatura a la cual el aire debe enfriarse (a presión constante) para alcanzar la saturación (RH = 100%).

*   El punto de rocío **nunca** puede ser mayor que la temperatura del aire ($T_d \le T$).
*   Si $T = T_d$, el aire está **saturado**.
*   Cambiar la temperatura del aire **no cambia** el punto de rocío (a menos que la temperatura baje por debajo del punto de rocío, causando condensación).

### 3. Saturación
Ocurre cuando el aire contiene la máxima cantidad de vapor de agua posible para su temperatura y presión.
*   **RH = 100%**.
*   **T = Td**.
*   Cualquier enfriamiento adicional o adición de vapor de agua causará **condensación** (nubes, niebla, rocío).

**Formas de saturar el aire:**
1.  **Añadir vapor de agua** (ej. evaporación de lluvia).
2.  **Enfriar el aire** (ej. ascenso adiabático, enfriamiento por radiación nocturna).

---

## Presión de Vapor sobre Hielo vs Agua
La presión de vapor de saturación sobre el **hielo** es **menor** que sobre el agua líquida a la misma temperatura.
*   Esto significa que el aire se satura más rápido sobre hielo que sobre agua.
*   Favorece el crecimiento de cristales de hielo a expensas de las gotas de agua (Proceso Bergeron-Findeisen).
*   El "Punto de Escarcha" (Frost Point) es mayor que el Punto de Rocío cuando la temperatura está bajo cero.

## Distribución Global del Vapor de Agua
*   **Polos:** ~0 g/m³ (aire muy frío, poca capacidad).
*   **Ecuador:** ~25 g/m³ (aire cálido, alta capacidad).
*   El vapor de agua se concentra en la troposfera inferior (0-5% del volumen del aire).

---

## Cálculos Prácticos

**Ejemplo 1:**
*   Temperatura ($T$): 18°C
*   Punto de Rocío ($T_d$): 12°C
*   $RH = 100 - 5 \times (18 - 12) = 100 - 30 = 70\%$

**Ejemplo 2:**
*   Contenido actual (HMR): 10 g/kg
*   Capacidad máxima (SMR): 15 g/kg
*   $RH = (10 / 15) \times 100 = 66.7\%$
