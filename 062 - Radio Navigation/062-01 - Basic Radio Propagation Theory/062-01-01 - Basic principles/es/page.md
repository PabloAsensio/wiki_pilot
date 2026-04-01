---
title: "Principios Básicos de Propagación"
description: "Aprende los principios basicos de ondas de radio aplicados a la radionavegacion aeronautica."
keywords:
    - "principios de propagacion"
    - "radionavegacion"
    - "ondas de radio en aviacion"
---

# Principios Básicos de Propagación

La radio navegación se fundamenta en la transmisión y recepción de ondas electromagnéticas. Para comprender estos sistemas, es crucial dominar conceptos como el espectro de frecuencias, las propiedades de las ondas y los métodos de modulación.

## Espectro de Frecuencias

El espectro electromagnético se divide en bandas logarítmicas, donde cada banda abarca un rango de frecuencias que comienza con un valor y termina en uno diez veces superior. Todas las bandas comienzan con el número 3.

| Banda | Frecuencia | Aplicaciones Principales |
| :--- | :--- | :--- |
| **VLF** (Very Low Frequency) | 3 - 30 kHz | Navegación de largo alcance (poco uso actual). |
| **LF** (Low Frequency) | 30 - 300 kHz | **NDB / ADF**. |
| **MF** (Medium Frequency) | 300 - 3.000 kHz | **NDB / ADF**, radiodifusión comercial. |
| **HF** (High Frequency) | 3 - 30 MHz | **Comunicaciones de largo alcance** (transoceánicas). |
| **VHF** (Very High Frequency) | 30 - 300 MHz | **Comunicaciones ATC**, VOR, ILS Localizer, VDF. |
| **UHF** (Ultra High Frequency) | 300 - 3.000 MHz | ILS Glide Path, DME, SSR, GNSS. |
| **SHF** (Super High Frequency) | 3 - 30 GHz | Radioaltímetro, Radar Meteorológico, MLS. |
| **EHF** (Extremely High Frequency) | 30 - 300 GHz | Comunicaciones satelitales avanzadas. |

**Regla mnemotécnica:** *"**V**ery **L**ovely **M**aidens **H**ave **V**ery **U**seful **S**ewing **E**quipment"*.

## Propiedades de las Ondas

*   **Frecuencia (f):** Número de ciclos por segundo. Se mide en **Hertz (Hz)**.
*   **Longitud de Onda ($\lambda$):** Distancia física de un ciclo completo. Se calcula como $\lambda = c / f$, donde $c$ es la velocidad de la luz ($300.000.000$ m/s).
    *   Ejemplo: Una frecuencia de 100 MHz tiene una longitud de onda de 3 metros.
*   **Ángulo de Fase:** Describe la posición exacta dentro de un ciclo de onda, medida en grados (0° a 360°). La comparación de fases es el principio base del funcionamiento del **VOR**.

## Modulación

La modulación es el proceso de imprimir información (señal moduladora) sobre una onda portadora (carrier wave).

1.  **Modulación de Amplitud (AM):** Varía la intensidad (amplitud) de la señal. Se generan dos bandas laterales (superior e inferior).
    *   **Banda Lateral Única (SSB):** En comunicaciones **HF**, se suprime una de las bandas laterales y a veces la portadora para ahorrar energía y ancho de banda.
2.  **Modulación de Frecuencia (FM):** Varía la frecuencia de la portadora.
3.  **Modulación de Fase (PM):** Invierte o desplaza la fase de la onda. Se utiliza en sistemas como **MLS** y **GNSS**.

## Clasificación ITU

La Unión Internacional de Telecomunicaciones (ITU) utiliza códigos de tres caracteres para clasificar las emisiones:

1.  **Primer carácter:** Tipo de modulación (N=Ninguna, A=Amplitud, etc.).
2.  **Segundo carácter:** Tipo de señal moduladora (0=Ninguna, 1=Digital sin subportadora, 2=Digital con subportadora, 3=Analógica).
3.  **Tercer carácter:** Tipo de información (N=Ninguna, A=Telegrafía auditiva, E=Telefonía/Voz).

**Códigos esenciales:**
*   **N0N:** Portadora sin modulación (señal base de un NDB).
*   **A1A:** Telegrafía (Morse) por interrupción de portadora (NDB antiguos).
*   **A2A:** Telegrafía (Morse) modulada en amplitud (NDB modernos, audible sin BFO).
*   **A3E:** Telefonía (Voz) modulada en amplitud (Estándar para **comunicaciones VHF**).

## Fenómenos de Interferencia

*   **Multipath Effect (Efecto Multitrayecto):** Ocurre cuando una señal llega al receptor por múltiples caminos (directo y reflejado), causando confusión o errores. Afecta a sistemas como el VOR, ILS y GNSS.
*   **Fading (Desvanecimiento):** Variación en la intensidad de la señal recibida, causada por interferencias, condiciones atmosféricas o el efecto multitrayecto.
