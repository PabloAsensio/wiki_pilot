Navegar un avión es muy diferente a conducir un coche. Mientras que un coche se agarra firmemente a la carretera, un avión se mueve dentro de una masa de aire que, a su vez, se está moviendo sobre la tierra. Para entender hacia dónde va realmente el avión y a qué velocidad, los pilotos utilizan un concepto fundamental llamado **Triángulo de Velocidades**.

A continuación, explicamos de forma sencilla cómo funcionan estas fuerzas y cómo los pilotos las calculan para llegar a su destino con precisión.

## Los Tres Vectores Fundamentales

Para resolver cualquier problema de navegación, debemos visualizar tres fuerzas o **vectores** interactuando entre sí. Un vector es simplemente una flecha que nos indica una dirección y una intensidad (velocidad).

1.  **Vector Aire (Air Vector):** Representa el movimiento del avión a través del aire. Está compuesto por:
    *   **Rumbo Verdadero (True Heading - TH):** La dirección hacia donde apunta la nariz del avión.
    *   **Velocidad Verdadera (True Airspeed - TAS):** La velocidad real del avión respecto al aire que lo rodea.

2.  **Vector Viento (Wind Vector - W/V):** Representa el movimiento de la masa de aire sobre la tierra. Se define por su dirección (desde dónde sopla) y su velocidad (intensidad en nudos).

3.  **Vector Tierra (Ground Vector):** Es el resultado final; lo que el avión realmente hace sobre el mapa. Está compuesto por:
    *   **Derrota (True Track - TT):** La línea real que el avión traza sobre el suelo.
    *   **Velocidad Terrestre (Ground Speed - GS):** La velocidad a la que el avión se desplaza sobre el terreno.

### La Suma de Vectores
El principio físico detrás de esto es la **suma vectorial**. Imagina que caminas hacia adelante en una cinta transportadora que se mueve de lado. Tu movimiento final es una diagonal. En aviación, para sumar estos vectores, colocamos la cola del **Vector Viento** en la cabeza (punta) del **Vector Aire**; el resultado, desde el inicio hasta el final, es el **Vector Tierra**.

## Conceptos de Navegación Práctica

### Deriva y Corrección
Cuando el viento sopla de costado, empuja al avión fuera de su ruta deseada.
*   **Deriva (Drift):** Es el ángulo de diferencia entre hacia dónde apunta el avión (Rumbo) y hacia dónde va realmente (Derrota). Si el viento viene de la derecha, nos empujará a la izquierda, creando una deriva a la izquierda .
*   **Ángulo de Corrección de Viento (WCA):** Para contrarrestar la deriva, el piloto debe "apuntar" el avión hacia el viento. Si el viento te empuja 10º a la izquierda, debes virar 10º a la derecha para compensar .

### Componentes del Viento
El viento rara vez sopla justo de cara o de cola; suele venir en ángulo. Los pilotos dividen este viento en dos efectos:
*   **Viento en Cara/Cola (Headwind/Tailwind):** Afecta la velocidad a la que avanzas sobre el suelo (Ground Speed).
*   **Viento Cruzado (Crosswind - XWC):** Es el responsable de empujar el avión lateralmente (Deriva) y es crítico durante el aterrizaje .

## Herramientas de Cálculo

### El Computador de Vuelo (CRP-5 / E6-B)
Los pilotos utilizan un calculador mecánico circular para resolver este triángulo. Existe una regla de oro para marcar el viento en el disco dependiendo de qué datos tienes:
*   Si conoces el **Rumbo (Heading)**, marca el viento hacia **ABAJO** desde el centro del disco .
*   Si conoces la **Derrota (Track)**, marca el viento hacia **ARRIBA** desde el centro .

### Cálculo Mental (MDR - Mental Dead Reckoning)
En vuelo, a veces no hay tiempo para usar el computador. Existen trucos matemáticos rápidos:

*   **Regla del Reloj (Clock Code) para Viento Cruzado:**
    Sirve para estimar cuánto viento cruzado tenemos según el ángulo del viento:
    *   **15º** de diferencia: Equivale a 1/4 de la fuerza del viento (25%).
    *   **30º** de diferencia: Equivale a media hora, o sea, la mitad de la fuerza (50%).
    *   **45º** de diferencia: Equivale a 3/4 de la fuerza (75%).
    *   **60º** o más: Se considera que afecta al 100% .


*   **Regla 1:60 para Deriva:**
    Para saber cuántos grados corrige el viento, se usa la fórmula:
    $$ \text{Ángulo} = \frac{\text{Viento Cruzado} \times 60}{\text{TAS}} $$
    Esto nos dice rápidamente cuántos grados debemos virar para mantener la ruta .

## Preparación de los Datos

Antes de calcular, los datos deben ser consistentes:
1.  **De CAS a TAS:** El indicador de velocidad en la cabina (Calibrated Airspeed - CAS) no es perfecto. Debe corregirse por la altitud y temperatura para obtener la **Velocidad Verdadera (TAS)**. A veces, esto implica convertir primero un Número de Mach a TAS .
2.  **Magnético vs. Verdadero:** Los mapas y la meteorología usan referencias distintas. El viento suele darse respecto al **Norte Verdadero**, mientras que las brújulas usan el **Norte Magnético**. Es vital aplicar la **Declinación Magnética (Variation)** correctamente (sumando o restando según sea Este u Oeste) antes de mezclar los datos.

