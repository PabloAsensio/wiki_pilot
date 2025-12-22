Las cartas aeronáuticas son representaciones fundamentales para la navegación aérea, actuando como una "Tierra reducida" en un plano. Su función principal es mostrar la relación entre las distancias en el mapa y las distancias reales en el planeta, permitiendo a los pilotos planificar y ejecutar vuelos con precisión. A continuación, se detallan los conceptos clave para entender su funcionamiento.

## La Escala de la Carta

La **escala de la carta** es la relación entre una longitud medida en el mapa y la distancia correspondiente en la Tierra. Se expresa mediante la fórmula:

**Escala = Distancia en la Carta / Distancia en la Tierra**

Para comparar escalas, se utiliza una regla sencilla basada en el denominador de la fracción representativa:
*   **A mayor denominador, menor escala**: Cubre más área pero con menos detalle (ej. 1:2,000,000).
*   **A menor denominador, mayor escala**: Cubre menos área pero con más detalle (ej. 1:500,000).

Por ejemplo, al calcular la escala en una latitud de 45°N donde 6 cm en el mapa representan 1 grado de longitud, obtenemos una escala aproximada de **1:1,309,562** . Es crucial recordar convertir todas las medidas a la misma unidad (como centímetros) antes de realizar el cálculo.

## Cálculo de Distancias (Apartamiento)

Para determinar la distancia real entre dos meridianos a una latitud específica, se utiliza la fórmula de **apartamiento (departure)**. Debido a que los meridianos convergen hacia los polos, la distancia entre ellos disminuye a medida que aumenta la latitud.

**Apartamiento (NM) = Cambio de Longitud x 60 x cos(latitud)**

Esta fórmula permite calcular la distancia en Millas Náuticas (NM) que separa dos puntos de longitud distinta situados en el mismo paralelo.

## Proyecciones Cartográficas

Existen diferentes formas de proyectar la superficie esférica de la Tierra en un plano, cada una con características propias.

### Proyección Cónica Conforme de Lambert
En esta proyección, la escala es exacta solo en los **paralelos estándar**. Sus características principales son:
*   La escala disminuye entre los paralelos estándar y aumenta fuera de ellos.
*   La **convergencia de la carta** es constante y se calcula multiplicando el cambio de longitud por el seno del paralelo de origen (conocido como la "constante del cono").
*   Una línea recta en esta carta aproxima un **círculo máximo**, lo cual es ideal para la navegación de radio.

### Proyección Mercator
Es una proyección cilíndrica donde la escala se expande a medida que nos alejamos del Ecuador.
*   La expansión de la escala es proporcional a la secante de la latitud.
*   Para resolver problemas de escala en Mercator, se utiliza la relación: **Denominador A x cos(Lat B) = Denominador B x cos(Lat A)**.

## Convergencia y Ortomorfismo

Una propiedad esencial de las cartas de navegación es el **ortomorfismo** (o conformidad), que garantiza que los ángulos medidos en la carta sean iguales a los ángulos en la Tierra. Esto asegura que los rumbos de navegación sean correctos.

*   **Convergencia de la Carta**: Es el ángulo de inclinación entre meridianos en el mapa.
*   **Convergencia de la Tierra**: Es el ángulo real de inclinación de los meridianos en el planeta.
*   **Ángulo de Conversión**: Es la diferencia angular entre el círculo máximo (ruta más corta) y la línea de rumbo (loxodrómica). Se calcula como la mitad de la convergencia.

## Aplicación Práctica: Velocidad y Tiempo

El uso correcto de la escala permite calcular la **Ground Speed (GS)** o velocidad sobre el terreno. Si conocemos la distancia en el mapa y el tiempo que toma recorrerla, primero convertimos la distancia del mapa a distancia terrestre usando la escala, y luego aplicamos la fórmula:

**GS = Distancia Terrestre / Tiempo de Vuelo**

Por ejemplo, si medimos 13.8 cm en una carta con escala donde 1 cm equivale a 3.1 NM, la distancia real es 42.78 NM. Si volamos ese tramo en 15 minutos, nuestra velocidad sobre el terreno sería de 171 nudos.
