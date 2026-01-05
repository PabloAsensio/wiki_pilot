## Visibilidad

### Definición y Reporte
Según el **Anexo 3 de la OACI**, la visibilidad para fines aeronáuticos se define como la mayor de las distancias a las que:
1.  Un objeto negro de dimensiones adecuadas, situado cerca del suelo, puede ser visto y reconocido cuando se observa contra un fondo brillante.
2.  Luces de aproximadamente **1.000 candelas** pueden ser vistas e identificadas contra un fondo no iluminado.

**Visibilidad Reinante (Prevailing Visibility):**
Es el mayor valor de visibilidad, observado de acuerdo con la definición de "visibilidad", que se alcanza dentro de al menos la mitad del círculo del horizonte o dentro de al menos la mitad de la superficie del aeródromo. Estas áreas pueden comprender sectores contiguos o no contiguos.
*   En METAR y SPECI, se recomienda reportar la visibilidad reinante.
*   Cuando la visibilidad es inferior a **1.500 m**, se debe reportar también el RVR.

### Alcance Visual en la Pista (RVR)
El **RVR (Runway Visual Range)** es la distancia sobre la cual el piloto de una aeronave que se encuentra sobre el eje de una pista puede ver las señales de superficie de la pista o las luces que la delimitan o que señalan su eje.

*   **Medición:** Se realiza mediante **transmisómetros** (o dispersómetros) situados a lo largo de la pista (zona de toma de contacto, punto medio y extremo de parada). También puede evaluarse mediante observación humana contando luces o marcas visibles.
*   **Reporte:**
    *   En METAR/SPECI se prefija con "R", seguido de la pista y el valor (ej. R18/450).
    *   Se reporta en **metros** (aunque algunos países como EE.UU. usan pies).
    *   Pasos de reporte:
        *   25 m (si RVR < 400 m).
        *   50 m (si RVR 400 - 800 m).
        *   100 m (si RVR > 800 m).
*   **Diferencia:** El RVR suele ser mayor que la visibilidad reinante y es específico para la dirección de la pista.

## Nubes

### Reporte de Cantidad
La cantidad de nubes se reporta en **oktas** (octavos de cielo cubierto):
*   **FEW:** 1 a 2 oktas.
*   **SCT (Scattered):** 3 a 4 oktas.
*   **BKN (Broken):** 5 a 7 oktas.
*   **OVC (Overcast):** 8 oktas.

### Techo de Nubes (Ceiling)
Es la altura sobre el suelo o el agua de la base de la capa de nubes más baja por debajo de 6.000 m (20.000 ft) que cubre **más de la mitad del cielo** (es decir, BKN u OVC).

### Visibilidad Vertical (VV)
Cuando el cielo está oscurecido y no se pueden pronosticar o ver las nubes (ej. niebla densa), se reporta la visibilidad vertical en lugar de la nubosidad. Se indica como "VV" seguido del valor en pies (ej. VV002 = 200 ft).

### Medición
*   **Ceilómetro:** Instrumento (generalmente láser) utilizado para medir la altura de la base de las nubes.

## Viento

### Medición y Reporte
*   **Instrumento:** **Anemómetro**, posicionado estándarmente a **10 metros (33 ft)** sobre el nivel del terreno, alejado de obstrucciones.
*   **Promedios:**
    *   **METAR:** Velocidad y dirección media de los últimos **10 minutos**.
    *   **ATIS / ATC:** Velocidad y dirección media de los últimos **2 minutos**.
*   **Rachas (Gusts):** Desviaciones instantáneas de la velocidad media. Se reportan en el METAR (con la letra "G") si la velocidad máxima excede a la media en **10 nudos o más**. Esto aplica tanto a aumentos como a disminuciones (calmas momentáneas).

## Radar Meteorológico de A bordo (Airborne Weather Radar)

### Principio de Funcionamiento
El radar detecta **gotas de precipitación** (lluvia, nieve húmeda, granizo húmedo) basándose en su **reflectividad**.
*   **No detecta:** Turbulencia en aire claro (CAT), nubes sin precipitación, niebla, o hielo seco (granizo seco/nieve seca tienen baja reflectividad).
*   **Pantalla:**
    *   **Rojo:** Alta reflectividad (precipitación intensa).
    *   **Amarillo:** Precipitación media.
    *   **Verde:** Baja reflectividad (precipitación ligera).
    *   **Magenta:** A menudo indica turbulencia (en radares con función Doppler).

### Atenuación y Sombras
*   **Atenuación:** La energía del radar es absorbida o dispersada por precipitación intensa, impidiendo ver lo que hay detrás.
*   **Sombra (Shadow):** Un área negra detrás de un eco rojo indica que la señal ha sido totalmente atenuada. **Peligro:** Puede haber una tormenta severa oculta en la sombra.
    *   *Regla:* Si hay una sombra, asuma que hay actividad severa detrás. Si no hay tormenta delante de la zona oscura, podría ser una montaña o un lago (dependiendo del "tilt" de la antena).

### Detección de Turbulencia
Algunos radares modernos usan el **efecto Doppler** para detectar el movimiento horizontal de las gotas de lluvia, indicando posible turbulencia (función TURB). Generalmente efectiva solo hasta 40 NM y requiere presencia de precipitación ("wet turbulence").

### Formas Peligrosas
*   **Ganchos (Hooks), Dedos, Arcos:** Indican actividad convectiva severa, posible rotación (mesociclón) y riesgo de **tornados** o granizo severo.
*   **Forma de U:** Indica corrientes verticales fuertes y granizo severo.

## Imágenes de Satélite

Se utilizan dos tipos principales de imágenes para analizar el clima:

| Característica | Visible (VIS) | Infrarrojo (IR) |
| :--- | :--- | :--- |
| **Fuente** | Luz solar reflejada. | Radiación térmica (temperatura). |
| **Disponibilidad** | Solo de día. | 24 horas (día y noche). |
| **Apariencia Nubes** | Blancas. | Blancas (si son frías/altas), Grises (si son bajas/cálidas). |
| **Tierra/Mar** | Tierra gris, Mar negro. | Tierra cálida oscura, Tierra fría más clara. |
| **Uso principal** | Ver textura y espesor. | Ver altura de topes nubosos. |

**Interpretación Combinada:**
*   **Ambas brillantes:** Nube alta y espesa (ej. CB, actividad convectiva).
*   **Visible brillante / IR oscuro:** Nube baja o niebla (temperatura similar a la superficie).
*   **Visible tenue / IR brillante:** Nube alta y delgada (ej. Cirrostratos).

**Ceniza Volcánica:**
Se detecta monitoreando imágenes visibles e infrarrojas. En IR, la ceniza, al elevarse y enfriarse, aparece blanca (similar a nubes frías).

## Otros Instrumentos y Reportes

*   **Radiosonda:** Instrumento llevado por un globo que mide **presión, temperatura y humedad** relativa mientras asciende.
*   **Termómetro:** Mide la temperatura del aire. Se coloca en un **Abrigo de Stevenson** (a 1.25 - 2 m del suelo) para protegerlo de la radiación solar directa y precipitación, permitiendo la circulación de aire.
*   **Aeronotificaciones (Air-reports):**
    *   **Rutinas:** Posición e información meteorológica básica.
    *   **Especiales (ARS):** Se emiten cuando se encuentran condiciones peligrosas (ej. turbulencia severa, engelamiento fuerte, ondas de montaña, tormentas, ceniza volcánica).
