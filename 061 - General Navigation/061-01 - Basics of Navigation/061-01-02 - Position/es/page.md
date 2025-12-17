En la navegación aérea, la **posición** se define mediante un sistema de coordenadas que utiliza la latitud y la longitud. Aunque para simplificar los cálculos a menudo consideramos la Tierra como una esfera perfecta, la realidad es más compleja y requiere modelos precisos como el **elipsoide WGS 84** para garantizar la seguridad y exactitud en el vuelo.

## Forma de la Tierra y Referencias

La Tierra no es una esfera perfecta; debido a su rotación, está ligeramente achatada en los polos y ensanchada en el ecuador. Esta forma se conoce como **esferoide oblato** o elipsoide.
*   **Esfera**: Asumida para cálculos generales, donde 1 grado de latitud equivale a **60 NM**.
*   **Elipsoide (WGS 84)**: Modelo matemático utilizado por sistemas como el GPS. Aquí, la longitud de 1 grado de latitud varía: es menor en el ecuador (aprox. 59.7 NM) y mayor en los polos (aprox. 60.3 NM).

## Latitud: Geodésica vs. Geocéntrica

La latitud se mide como un ángulo desde el Ecuador (0°) hasta los Polos (90° N/S). Existen dos definiciones clave:
*   **Latitud Geocéntrica**: Es el ángulo medido desde el **centro de la Tierra**.
*   **Latitud Geodésica (o Geográfica)**: Es el ángulo entre el plano ecuatorial y una línea **perpendicular** a la superficie del elipsoide en el punto del observador. Esta es la latitud que se utiliza en las **cartas de navegación**.

Debido a que la Tierra no es una esfera perfecta, estas dos latitudes solo coinciden en el Ecuador y los Polos. La máxima diferencia ocurre cerca de los 45° N/S.

Para calcular el **Cambio de Latitud** entre dos puntos:
*   Si están en el **mismo hemisferio**, se restan los ángulos. Por ejemplo: 36°42'37'' - 27°48'05'' = **8°54'32''**.
*   Si están en **hemisferios opuestos**, se suman.

## Longitud y Meridianos

La **longitud** se mide como el ángulo en el plano ecuatorial entre el **Meridiano de Greenwich** (Primer Meridiano) y el meridiano del punto en cuestión. A diferencia de la latitud, la longitud geocéntrica y geodésica son idénticas porque comparten el mismo vértice en el centro de la Tierra.

Para calcular el cambio de longitud:
*   Mismo hemisferio (Este/Este o Oeste/Oeste): Restar.
*   Hemisferios diferentes (Este/Oeste): Sumar. Por ejemplo, entre 45°34'E y 09°18'W la diferencia es **54°52'**.

## Líneas de Navegación: Círculo Máximo y Línea de Rumbo

En la superficie terrestre, distinguimos dos tipos de trayectorias principales:
*   **Círculo Máximo (Great Circle)**: Es la línea que divide la Tierra en dos mitades iguales (pasa por el centro). Representa la **distancia más corta** entre dos puntos. El Ecuador y todos los meridianos son Círculos Máximos.
*   **Línea de Rumbo (Rhumb Line)**: Es una línea de **dirección constante** que corta todos los meridianos con el mismo ángulo. Los paralelos de latitud son Líneas de Rumbo (cortan los meridianos a 90°).

| Característica | Círculo Máximo | Línea de Rumbo |
| :--- | :--- | :--- |
| **Definición** | Radio igual al de la Tierra | Corta meridianos al mismo ángulo |
| **Propiedad Principal** | Distancia más corta | Dirección constante |
| **Ejemplos** | Ecuador, Meridianos | Paralelos, Ecuador, Meridianos |

## Apartamiento y Efectos Ambientales

El **Apartamiento (Departure)** es la distancia en millas náuticas (NM) a lo largo de un paralelo de latitud. Se calcula con la fórmula:
$$ \text{Apartamiento} = \text{Cambio de Longitud (min)} \times \cos(\text{Latitud}) $$
Por ejemplo, un cambio de longitud de 500 NM a una latitud de 17°46' resulta en un cambio de longitud de aproximadamente **8°45'**.

Finalmente, es crucial considerar la temperatura en la navegación vertical (**Baro-VNAV**). Temperaturas más bajas que el estándar provocan que la aeronave vuele en una trayectoria vertical real más baja (ángulo menos pronunciado), lo que puede ser peligroso cerca del terreno.
