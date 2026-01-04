Las ondas de radio pueden viajar desde el transmisor al receptor siguiendo diferentes trayectorias, dependiendo principalmente de su frecuencia y de las condiciones atmosféricas.

## Modos de Propagación

1.  **Ondas de Espacio (Space Waves):** Viajan en línea recta (**Line-of-Sight**). Es el modo principal para frecuencias **VHF y superiores**. Su alcance está limitado por la curvatura de la Tierra y obstáculos físicos.
    - Fórmula de alcance teórico: $Alcance (NM) = 1.23 \times (\sqrt{H_T} + \sqrt{H_R})$
2.  **Ondas de Superficie (Ground/Surface Waves):** Siguen la curvatura de la Tierra gracias a la **difracción**. Son efectivas en frecuencias bajas (**LF y MF**) y viajan mejor sobre el mar que sobre tierra.
3.  **Ondas de Cielo (Sky Waves):** Son ondas que se dirigen hacia la atmósfera y regresan a la Tierra tras ser **refractadas** por la **ionosfera**. Este fenómeno permite comunicaciones de muy larga distancia en la banda **HF**.

## La Ionosfera y el Fenómeno de "Skip"

La ionosfera es una región de la atmósfera ionizada por la radiación solar. Se divide en capas (**D, E, F1, F2**).
- **Capa D:** Presente solo de día, absorbe las ondas de baja frecuencia (LF/MF), impidiendo su propagación por onda de cielo durante el día.
- **Skip Distance (Distancia de Salto):** Es la distancia desde el transmisor hasta el punto donde la primera onda de cielo regresa a la Tierra. Aumenta con frecuencias más altas y con una ionosfera más elevada (noche).
- **Skip Zone (Zona de Silencio):** Área entre el límite del alcance de la onda de superficie y el punto donde regresa la primera onda de cielo. En esta zona no se recibe señal.

## Errores en la Navegación (ADF/NDB)

El sistema ADF es especialmente sensible a errores de propagación:
- **Efecto Nocturno:** Causado por la interferencia entre la onda de superficie y la onda de cielo (que aparece al desaparecer la capa D por la noche). Provoca oscilaciones en la aguja ("hunting").
- **Refracción Costera:** La onda cambia de velocidad y dirección al cruzar de tierra a mar, desviándose hacia la costa.
- **Efecto de Montaña:** Reflexiones en el terreno que causan lecturas erróneas.
- **Error Cuadrantal:** Distorsión del frente de onda causada por la estructura metálica del avión.

## Fenómenos Físicos Clave

- **Refracción:** Cambio de dirección al pasar entre medios de distinta densidad (ej. capas de la atmósfera).
- **Difracción:** Capacidad de las ondas para bordear obstáculos o seguir la curvatura terrestre.
- **Reflexión:** Rebote de la onda sobre una superficie (tierra, mar o edificios).
- **Absorción:** Pérdida de energía de la onda al interactuar con la materia (especialmente en la capa D o por lluvia).
- **Efecto Doppler:** Cambio aparente de frecuencia debido al movimiento relativo entre emisor y receptor. Se utiliza en el **DVOR**, **GNSS** y radares para medir velocidad o detectar movimiento.
