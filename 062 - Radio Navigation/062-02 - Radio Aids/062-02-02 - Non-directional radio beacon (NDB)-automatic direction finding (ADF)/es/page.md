El sistema se compone de una estación terrestre llamada **NDB (Non-Directional Beacon)** y un equipo a bordo denominado **ADF (Automatic Direction Finder)**. Es uno de los sistemas de navegación más antiguos y sencillos.

## Componentes y Frecuencias

- **NDB:** Transmisor terrestre que emite señales omnidireccionales en las bandas **LF y MF** (entre **190 kHz y 1750 kHz**).
- **ADF:** Receptor a bordo que utiliza una combinación de una **antena de lazo (loop)** y una **antena de sentido (sense)** para determinar la dirección de la señal.

## Modulación e Identificación

Las señales NDB se clasifican según la ITU:
- **N0N:** Portadora sin modulación.
- **A1A:** Morse por interrupción de portadora (requiere activar el **BFO** para ser audible).
- **A2A:** Morse modulado en amplitud (audible en modo ADF normal).

En aeronaves modernas, el **BFO (Beat Frequency Oscillator)** suele activarse automáticamente para permitir la identificación de señales no moduladas.

## Uso del Instrumento

- **RBI (Relative Bearing Indicator):** Muestra la **marcación relativa** (ángulo respecto al morro del avión).
- **RMI (Radio Magnetic Indicator):** Combina la información de rumbo y marcación, mostrando directamente el **QDM** (punto de la aguja) y el **QDR** (cola de la aguja).
- **Homing:** Volar manteniendo la aguja en el morro (0° relativo). Con viento, esto resulta en una trayectoria curva.
- **Tracking:** Aplicar un ángulo de corrección de deriva para mantener un **QDM** o **QDR** específico, resultando en una trayectoria recta sobre el suelo.

## Errores del ADF

El ADF es propenso a diversas interferencias y errores:
- **Efecto Nocturno:** Interferencia entre ondas de superficie y de cielo, causando oscilaciones de la aguja ("hunting").
- **Interferencia de Tormentas:** La aguja tiende a apuntar hacia las descargas estáticas de los **Cumulonimbus (CB)**.
- **Error de Inclinación (Dip Error):** Al alabear el avión, la antena no está nivelada y la aguja se desvía hacia el ala baja.
- **Refracción Costera:** La onda cambia de dirección al cruzar la costa.
- **Error Cuadrantal:** Distorsión causada por la estructura metálica del avión.
- **Falta de Aviso de Fallo:** El ADF no tiene banderas de aviso; el piloto debe **monitorear continuamente el identificador Morse**.
