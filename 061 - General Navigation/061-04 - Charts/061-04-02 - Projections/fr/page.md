Navegar por el mundo requiere traducir una esfera tridimensional (la Tierra) a un mapa plano bidimensional. Este proceso se realiza mediante **proyecciones**, y cada una tiene sus propias reglas y distorsiones. A continuación, explicamos de forma sencilla cómo funcionan las principales proyecciones utilizadas en aviación, integrando todos los conceptos teóricos y matemáticos esenciales.

## Conceptos Fundamentales de Navegación

Antes de estudiar los mapas, debemos entender cómo se comportan las líneas y los ángulos sobre la superficie terrestre:

*   **Ortodromia (Great Circle):** Es la distancia más corta entre dos puntos en una esfera. Su dirección cambia constantemente a medida que cruzamos meridianos. En la mayoría de las cartas, buscamos que estas rutas aparezcan como líneas rectas.
*   **Loxodromia (Rhumb Line):** Es una línea que mantiene una dirección constante, cortando todos los meridianos con el mismo ángulo. Es fácil de volar (solo sigues un rumbo fijo en la brújula), pero no es la ruta más corta. En las cartas polares, es una curva cóncava hacia el polo.
*   **Convergencia (Convergency):** Es el ángulo de inclinación entre dos meridianos. En la Tierra, los meridianos se juntan en los polos.
    *   Fórmula: **Convergencia = Cambio de Longitud × Seno (Latitud Media)**.
*   **Ángulo de Conversión:** Es la diferencia angular entre la dirección de la Ortodromia y la Loxodromia.
    *   Regla clave: **Ángulo de Conversión = ½ Convergencia**.

***

## 1. Proyección Estereográfica Polar

Esta carta se crea imaginando un plano plano que toca la Tierra en uno de los Polos (punto de tangencia). Es ideal para la navegación en latitudes altas.

*   **Graticula (Red Geográfica):** Los **meridianos** son líneas rectas que irradian desde el polo. Los **paralelos** son círculos concéntricos cuya distancia aumenta al alejarse del polo.
*   **Factor de Convergencia (n=1):** En esta carta, la convergencia es máxima e idéntica a la realidad polar.
    *   **Convergencia de Carta = Cambio de Longitud**.
*   **Comportamiento de las Rutas:**
    *   Una línea recta dibujada pasando por el polo es un meridiano.
    *   Las **Ortodromias** (círculos máximos) son casi rectas cerca del polo, pero técnicamente son curvas ligeramente cóncavas hacia el polo.
    *   Las **Loxodromias** son curvas pronunciadas, siempre cóncavas hacia el polo de proyección.
*   **Escala:** Es correcta solo en el Polo. Se expande a medida que nos alejamos (proporcional a la secante al cuadrado de la mitad de la co-latitud).

***

## 2. Proyección Cónica Conforme de Lambert

Es la carta estándar para la aviación en latitudes medias. Se utiliza un cono que "corta" la Tierra, intersectándola en dos **Paralelos Estándar**.

*   **Paralelo de Origen:** Es la latitud central matemática de la proyección, ubicada a medio camino entre los dos paralelos estándar. Aquí la convergencia de la carta es igual a la convergencia de la Tierra.
    *   Cálculo: *(Paralelo Estándar 1 + Paralelo Estándar 2) / 2*.
*   **Constante del Cono (n):** Define cuánto se ha "aplanado" el cono (0 es un cilindro, 1 es un plano).
    *   **Constante del Cono = Seno (Paralelo de Origen)**.
*   **Convergencia de Carta:** Es constante en todo el mapa.
    *   **Convergencia = Cambio de Longitud × Constante del Cono**.
*   **Escala:** Es exacta en los paralelos estándar. Se **contrae** (se reduce) entre ellos (mínima en el paralelo de origen) y se **expande** (aumenta) fuera de ellos. El error de escala se mantiene típicamente menor al **1%**.
*   **Ortomórfica:** Sí, como todas las cartas de navegación, conserva los ángulos y formas en áreas pequeñas.

***

## 3. Proyección Mercator Directa

Es una proyección cilíndrica donde el cilindro envuelve la Tierra tocando el **Ecuador** (su paralelo de origen).

*   **Graticula:** Los **meridianos** son líneas rectas paralelas y espaciadas uniformemente. Los **paralelos** son líneas rectas paralelas que se separan más a medida que se alejan del Ecuador.

*   **Convergencia Cero:** Como los meridianos son paralelos, nunca se tocan. La convergencia de la carta es cero.
*   **Rutas:**
    *   Las **Loxodromias** son líneas rectas perfectas (su gran ventaja).
    *   Las **Ortodromias** son curvas convexas hacia el polo (cóncavas al Ecuador).
*   **Escala Variable:** La escala es correcta solo en el Ecuador y aumenta rápidamente hacia los polos (como la secante de la latitud).
*   **La Fórmula "ABBA":** Para calcular distancias o escalas a diferentes latitudes en una Mercator, usamos esta relación matemática:
    *   **Distancia A × Cos(Latitud B) = Distancia B × Cos(Latitud A)**.

***

## Reglas Prácticas de Dirección

Para resolver problemas de dirección entre dos puntos (A y B):

1.  **Calcular Convergencia:** Dependiendo de la proyección (Cambio de Longitud para Polar; Cambio de Longitud × Seno de Latitud para Lambert).
2.  **Calcular Ángulo de Conversión:** Dividir la convergencia por 2.
3.  **Aplicar la Regla del Hemisferio:**
    *   La **Ortodromia** siempre está más cerca del Polo que la Loxodromia.
    *   En una carta Lambert o Polar, la Ortodromia es la línea más recta; la Loxodromia se curva hacia el ecuador.
    *   **GCT (Rumbo Ortodrómico) = RLT (Rumbo Loxodrómico) ± Ángulo de Conversión**.

