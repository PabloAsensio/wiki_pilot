La radio navegación se basa en la transmisión y recepción de ondas electromagnéticas para determinar la posición y guiar a una aeronave. Para comprender su funcionamiento, es esencial conocer el espectro de frecuencias, los tipos de modulación y los principios físicos que rigen estas ondas.

## El Espectro de Frecuencias

Las ondas de radio se clasifican en bandas según su frecuencia. Cada banda comienza en un valor y termina en uno 10 veces superior, comenzando generalmente con el número 3.

| Banda | Siglas | Rango de Frecuencia | Aplicaciones Comunes |
| :--- | :--- | :--- | :--- |
| **Very Low Frequency** | **VLF** | 3 - 30 kHz | Navegación de largo alcance |
| **Low Frequency** | **LF** | 30 - 300 kHz | NDB / ADF |
| **Medium Frequency** | **MF** | 300 - 3000 kHz | NDB / ADF, Comunicaciones AM |
| **High Frequency** | **HF** | 3 - 30 MHz | Comunicaciones de largo alcance |
| **Very High Frequency** | **VHF** | 30 - 300 MHz | Radio ATC, VOR, ILS Localizer |
| **Ultra High Frequency** | **UHF** | 300 - 3000 MHz | ILS Glide Path, DME, SSR, GNSS |
| **Super High Frequency** | **SHF** | 3 - 30 GHz | Radar Meteorológico, Radioaltímetro |
| **Extremely High Frequency** | **EHF** | 30 - 300 GHz | Aplicaciones especializadas |

Una regla mnemotécnica común en inglés para recordar el orden es: *"**V**ery **L**ovely **M**aidens **H**ave **V**ery **U**seful **S**ewing **E**quipment"*.

## Propiedades de las Ondas

- **Longitud de onda ($\lambda$):** Es la distancia física de un ciclo completo. Se calcula con la fórmula:
  $$\lambda = \frac{c}{f}$$
  Donde $c$ es la velocidad de la luz ($300,000,000$ m/s o $300$ si la frecuencia $f$ está en MHz).
- **Fase y Ángulo de Fase:** El **ángulo de fase** describe la posición exacta en un ciclo de onda (de 0° a 360°). Comparar la fase de dos señales es el principio de funcionamiento del **VOR**.
- **Polarización:** Describe la orientación del campo eléctrico. Puede ser **lineal** (vertical u horizontal), **circular** o **elíptica**.

## Modulación y Clasificación ITU

La **modulación** es el proceso de añadir información (voz o datos) a una onda portadora de alta frecuencia. La ITU clasifica las emisiones con tres caracteres:

1.  **Primer símbolo:** Tipo de modulación de la portadora (ej. **A** para amplitud, **F** para frecuencia, **N** para sin modulación).
2.  **Segundo símbolo:** Naturaleza de la señal moduladora (ej. **1** para datos digitales sin subportadora, **3** para analógica).
3.  **Tercer símbolo:** Tipo de información transmitida (ej. **A** para Morse auditivo, **E** para voz).

Ejemplos clave:
- **N0N:** Portadora sin modulación (usada por NDB).
- **A1A:** Morse por interrupción de portadora (NDB antiguos).
- **A2A:** Morse modulado en amplitud (NDB modernos).
- **A3E:** Voz modulada en amplitud (Comunicaciones VHF).

En **HF**, se utiliza frecuentemente la **Banda Lateral Única (SSB)** para reducir la potencia necesaria y el ancho de banda.

## Sistemas de Navegación y Presentación

- **Navigation Display (ND):** Ofrece modos como **MAP** (o ARC) para progreso de vuelo, **PLAN** (norte arriba) y modos específicos para **VOR** o **ILS**.
- **FMS (Flight Management System):** Utiliza el **Filtro de Kalman** para combinar datos de múltiples fuentes (IRS, GPS, Radio) y calcular la posición más precisa.
- **Datalink (CPDLC/ACARS):** Permite la comunicación de texto entre piloto y controlador o compañía mediante VHF, HF o **SATCOM**.

## Errores y Fenómenos

- **Fading (Desvanecimiento):** Variación en la intensidad de la señal causada por interferencias, clima o propagación por múltiples trayectorias.
- **Efecto Multipath:** Ocurre cuando una señal llega a la antena por varios caminos (directo y reflejado), causando errores en la determinación de la dirección, común en radares y ADF.
