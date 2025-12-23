La navegación durante las fases de ascenso y descenso requiere cálculos específicos para determinar la velocidad, el tiempo y la distancia con precisión. A diferencia del vuelo de crucero nivelado, donde las condiciones son relativamente constantes, el ascenso y el descenso implican cambios continuos en la altitud, lo que afecta a la **Velocidad Verdadera (TAS)** y al efecto del viento. A continuación, se explican los conceptos y reglas clave para dominar estos cálculos.

## Determinación del Viento y TAS Promedio

Para resolver problemas de navegación en estas fases, no se utiliza el viento o la TAS de una sola altitud, sino un promedio representativo. Las normativas de aprendizaje establecen las siguientes reglas empíricas para calcular la **Velocidad Terrestre (GS)** promedio:

*   **Para problemas de Ascenso:** Se utiliza la TAS y el Viento (W/V) a la altitud correspondiente a **2/3 de la altitud de crucero** (o 2/3 de la diferencia de altitud sumados a la base).
*   **Para problemas de Descenso:** Se utiliza la TAS y el Viento (W/V) a la altitud correspondiente a **1/2 de la altitud de descenso** (o la mitad de la capa a descender).

Por ejemplo, si una aeronave asciende desde el nivel del mar (0 ft) hasta **FL270** (27,000 ft), la altitud de referencia para los cálculos sería 18,000 ft ($27,000 \times 2/3$). Si el ascenso es entre 4,000 ft y 8,000 ft, la altitud a utilizar sería 6,667 ft ($4,000 + 2/3 \times 4,000$).

## Cálculo de la Velocidad Terrestre (Groundspeed)

Una vez determinada la altitud de referencia, se debe obtener la **Velocidad Terrestre (GS)**. Esto generalmente implica tres pasos:

1.  **Hallar la Temperatura:** Calcular la temperatura estándar (ISA) para esa altitud y ajustarla con la desviación dada (por ejemplo, ISA +5ºC).
2.  **Calcular la TAS:** Usar un computador de vuelo (como el E6B o CRP-5) para convertir la Velocidad Calibrada (CAS) a **Velocidad Verdadera (TAS)**, aplicando correcciones de compresibilidad si la velocidad es alta (superior a 300 kt).
3.  **Aplicar el Viento:** Usar la dirección y velocidad del viento en la altitud de referencia para encontrar la GS efectiva. Si no se dan datos exactos para esa altitud, se debe interpolar entre los vientos dados en niveles superiores e inferiores.

## Gradientes y Régimen de Ascenso/Descenso

Es crucial distinguir entre el ángulo de subida/bajada y la velocidad vertical.

*   **Gradiente de Ascenso/Descenso:** Es la relación entre el cambio de altura y la distancia horizontal recorrida, expresada usualmente como un porcentaje (%).
    *   Fórmula: $\text{Gradiente (\%)} = \frac{\text{Cambio de Altura}}{\text{Distancia Horizontal}} \times 100$
*   **Régimen de Ascenso (ROC) / Descenso (ROD):** Es la velocidad vertical, medida en pies por minuto (ft/min o fpm).

Existe una relación directa entre el gradiente, la velocidad terrestre y el régimen vertical. Una regla práctica (basada en la regla 1:60) para estimar el **Régimen de Descenso** necesario es:

$$ROD (ft/min) \approx \text{Gradiente (\%)} \times GS (kt)$$

O para un ángulo de planeo estándar de 3 grados:
$$ROD \approx 5 \times GS$$

Por ejemplo, para una **GS** de 120 kt en una pendiente de 3° (aprox 5%), el régimen sería de unos 600 fpm.

## Cálculo de Tiempo y Distancia

Finalmente, para determinar cuánto tiempo tomará alcanzar una altitud o recorrer una distancia durante estas maniobras:

*   **Tiempo de Ascenso/Descenso:** Se divide la diferencia de altura total entre el **Régimen de Ascenso (ROC)** o **Régimen de Descenso (ROD)** promedio.
    *   $\text{Tiempo} = \frac{\text{Diferencia de Altura}}{\text{Régimen (fpm)}}$
*   **Distancia Terrestre:** Se multiplica la **Velocidad Terrestre (GS)** promedio por el tiempo calculado.
    *   $\text{Distancia} = GS \times \text{Tiempo}$

Es fundamental recordar que las altitudes y distancias deben estar en las mismas unidades para los cálculos de gradiente (usualmente pies, donde 1 Milla Naútica (NM) ≈ 6,080 pies).

