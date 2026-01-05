El **NDB** es una radioayuda terrestre que transmite una señal omnidireccional. El **ADF** es el instrumento a bordo que recibe esta señal y determina la dirección hacia la estación.

## Principios de Funcionamiento

*   **Frecuencias:** Opera en las bandas de Baja Frecuencia (LF) y Media Frecuencia (MF), típicamente entre **190 kHz y 1750 kHz**.
*   **Modulación:**
    *   **N0N:** Portadora sin modulación (señal básica).
    *   **A1A:** Identificación en código Morse mediante interrupción de la portadora (requiere activar el **BFO** - Beat Frequency Oscillator en el ADF para ser audible).
    *   **A2A:** Identificación modulada en amplitud (audible directamente, no requiere BFO).
*   **Antenas ADF:** Utiliza dos antenas:
    *   **Antena de Lazo (Loop):** Determina la dirección pero con ambigüedad de 180°.
    *   **Antena de Sentido (Sense):** Resuelve la ambigüedad para indicar si la estación está delante o detrás.

## Instrumentos e Indicaciones

*   **RBI (Relative Bearing Indicator):** Muestra el **Rumbo Relativo (Relative Bearing - RB)**, que es el ángulo entre el morro del avión y la estación. La tarjeta es fija (el norte siempre está arriba).
    *   Fórmula: $QDM = Rumbo Magnético (MH) + Rumbo Relativo (RB)$.
*   **RMI (Radio Magnetic Indicator):** Combina un girocompás con la aguja del ADF. La tarjeta gira automáticamente para mostrar el rumbo magnético del avión arriba.
    *   **Cabeza de la aguja:** Indica el **QDM** (Rumbo magnético HACIA la estación).
    *   **Cola de la aguja:** Indica el **QDR** (Rumbo magnético DESDE la estación).
*   **Precisión:** La precisión típica de un ADF durante el día es de **$\pm 5^\circ$**.

## Errores del Sistema ADF

El ADF es susceptible a numerosos errores debido a la propagación de ondas LF/MF:

1.  **Efecto Nocturno (Night Effect):** Por la noche, la capa D de la ionosfera desaparece, permitiendo que las ondas de cielo (sky waves) interfieran con las ondas de superficie. Esto causa desvanecimiento (fading) y oscilación de la aguja. Es peor al amanecer y al anochecer.
2.  **Efecto de Montaña (Mountain Effect):** La **difracción** y reflexión de las ondas en terreno montañoso causan lecturas erróneas.
3.  **Refracción Costera (Coastal Refraction):** Las ondas se aceleran sobre el agua, curvándose hacia la costa al cruzar la línea de costa en un ángulo oblicuo.
4.  **Efecto de Tormenta (Thunderstorm Effect):** Los rayos (descargas estáticas) emiten señales potentes en LF/MF. La aguja del ADF puede apuntar momentáneamente hacia el centro de la tormenta (Cumulonimbus).
5.  **Error Cuadrantal:** Desviación causada por la refracción de la señal en el fuselaje metálico del avión.
6.  **Error de Inclinación (Dip Error):** Al virar, la antena de lazo se inclina, provocando errores en la lectura.

## Uso Operacional

*   **Homing:** Volar manteniendo la aguja del ADF en el morro (RB 0°). Si hay viento cruzado, el avión describirá una trayectoria curva.
*   **Tracking:** Volar un rumbo corregido por viento para mantener una trayectoria recta hacia o desde la estación (manteniendo un QDM o QDR constante).
*   **Aproximaciones NDB:** Se consideran aproximaciones de no precisión. El piloto debe mantenerse dentro de **$\pm 5^\circ$** del rumbo de aproximación publicado para considerarse "establecido".
*   **Fallo:** A diferencia del VOR o ILS, el NDB **no tiene bandera de fallo (flag)**. El piloto debe monitorizar continuamente la identificación en código Morse; si cesa, la estación ha fallado.

## Locator Beacons

Son NDBs de **baja potencia** (10-25 NM de alcance) utilizados en aproximaciones terminales, a menudo ubicados en el marcador exterior (Outer Marker) del ILS (formando un LOM - Locator Outer Marker).
