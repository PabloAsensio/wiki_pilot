Para entender la navegación, primero debemos definir las dos trayectorias principales que sigue una aeronave:

*   **Círculo Máximo (Great Circle):** Representa la **distancia más corta** entre dos puntos en la superficie de la Tierra. Sin embargo, debido a la convergencia de los meridianos, una ruta de círculo máximo cambia constantemente de dirección (rumbo verdadero) a medida que avanza, excepto en el Ecuador o cuando se vuela directamente norte-sur a lo largo de un meridiano.
*   **Línea de Rumbo (Rhumb Line):** Es una línea que corta a todos los meridianos con el **mismo ángulo**, lo que significa que mantiene una dirección constante. Aunque es más fácil de volar con una brújula, la distancia recorrida es siempre mayor que la del círculo máximo (excepto en el Ecuador o en rumbos norte-sur).

## Diferencias Clave y Curvatura
En una carta de proyección estereográfica polar, el Polo es el punto de tangencia. Aquí, los meridianos son líneas rectas que irradian desde el polo y los paralelos son círculos concéntricos.

*   **Curvatura:** Las líneas de rumbo aparecen curvas cóncavas hacia el polo, mientras que los círculos máximos se consideran líneas casi rectas cerca del polo, aunque en realidad son ligeramente cóncavas hacia el polo en proyecciones lejanas al centro.
*   **Latitud:** Cuanto mayor es la latitud (más cerca del polo), **menor es la curvatura** aparente de los círculos máximos en la carta.

La diferencia entre la ruta de círculo máximo y la línea de rumbo es más notable cuando el **Ángulo de Conversión** es mayor.

## Convergencia y Ángulo de Conversión
La diferencia angular entre estas dos trayectorias se rige por la **Convergencia** de los meridianos.

*   **Convergencia:** Es el ángulo de inclinación entre dos meridianos a una latitud dada. Se calcula como:
    \[ \text{Convergencia} = \text{Cambio de Longitud} \times \sin(\text{Latitud Media}) \]
*   **Ángulo de Conversión (CA):** Es la diferencia angular entre la dirección del círculo máximo y la línea de rumbo. Equivale a la mitad de la convergencia.
    \[ \text{Ángulo de Conversión} = \frac{1}{2} \times \text{Convergencia} \]

Como se muestra en el siguiente gráfico, tanto la convergencia como el ángulo de conversión aumentan significativamente a medida que nos alejamos del Ecuador hacia los polos.

![Convergencia y Ángulo de Conversión vs Latitud](../assets/Convergencia_y_Angulo_de_Conversión_vs_Latitud.png)

Por lo tanto, la discrepancia entre volar un círculo máximo o una línea de rumbo es mayor cuando:
1.  Aumenta el **Cambio de Longitud**.
2.  Aumenta la **Latitud Media**.

## Variación en la Distancia
La regla general establece que la diferencia en distancia entre una ruta de círculo máximo y una de línea de rumbo **aumenta** si:
*   Se incrementa la latitud de la ruta.
*   Se incrementa la diferencia de longitud entre los puntos.

Por ejemplo, la diferencia de distancia entre dos puntos separados por 20° de longitud será mucho mayor a 60° de latitud que a 20° de latitud.

## Regla Práctica: DIID
Para calcular rumbos y corregir la trayectoria entre un círculo máximo y una línea de rumbo, se utiliza la regla mnemotécnica **D-I-I-D** para el hemisferio norte:

*   **D (Decrease):** Al volar hacia el **Oeste** (West), el rumbo del círculo máximo **Disminuye**.
*   **I (Increase):** Al volar hacia el **Este** (East), el rumbo del círculo máximo **Incrementa**.

| Hemisferio | Dirección | Comportamiento del Rumbo (Great Circle) |
| :--- | :--- | :--- |
| **Norte** | Oeste | Disminuye (Decrease) |
| **Norte** | Este | Incrementa (Increase) |
| **Sur** | Oeste | Incrementa (Increase) |
| **Sur** | Este | Disminuye (Decrease) |

Al aplicar el ángulo de conversión, recuerde que el rumbo de Círculo Máximo siempre "tira" hacia el polo en comparación con la Línea de Rumbo.

