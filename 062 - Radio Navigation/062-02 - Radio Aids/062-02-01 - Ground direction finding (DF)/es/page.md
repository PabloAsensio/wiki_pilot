---
title: Radionavegación: Radiogoniometria Terrestre (DF)
description: Comprende la radiogoniometria terrestre y sus aplicaciónes en navegacion aerea.
keywords:
  - radiogoniometria terrestre
  - df navegacion
  - radioayudas
---

# Radionavegación: Radiogoniometria Terrestre (DF)

El **VDF** (VHF Direction Finding) es un sistema que permite a una estación terrestre determinar la dirección desde la cual proviene una señal de radio VHF transmitida por una aeronave.

## Principios de Funcionamiento

*   **Equipo en la aeronave:** Solo requiere una **radio VHF estándar**. No se necesita equipo adicional.
*   **Equipo en tierra:** Utiliza una antena direccional especial, comúnmente una **Antena Adcock** (un arreglo de dipolos verticales). El sistema mide la diferencia de fase de la señal entrante en los distintos dipolos para calcular la dirección.
*   **Frecuencia:** Opera en la banda VHF (118-137 MHz), la misma que se usa para comunicaciones de voz.
*   **Alcance:** Al usar ondas VHF, el alcance es de **línea de visión (Line-of-Sight)**. Depende de la altura de la aeronave y de la estación, así como de la potencia de transmisión y obstáculos del terreno.

## Información Proporcionada

El controlador u operador de la estación terrestre puede proporcionar al piloto los siguientes rumbos (bearings):

*   **QDM:** Rumbo magnético **hacia** la estación (Magnetic Heading to steer). Es el rumbo que el piloto debe volar para ir directo a la estación (sin viento).
*   **QDR:** Rumbo magnético **desde** la estación (Magnetic Bearing from). Es la radial magnética en la que se encuentra el avión respecto a la estación.
*   **QUJ:** Rumbo verdadero **hacia** la estación (True Bearing to).
*   **QTE:** Rumbo verdadero **desde** la estación (True Bearing from).

**Nota importante:** Los rumbos proporcionados por el VDF **no corrigen la deriva por viento**. El piloto es responsable de calcular y aplicar la corrección de deriva necesaria.

## Precisión y Clasificación

La OACI (ICAO) clasifica las estaciones VDF según su precisión:

| Clase | Precisión |
| :--- | :--- |
| **Clase A** | $\pm 2^\circ$ |
| **Clase B** | $\pm 5^\circ$ |
| **Clase C** | $\pm 10^\circ$ |
| **Clase D** | Peor que la Clase C |

La precisión puede verse afectada por reflexiones en edificios, terreno irregular (site errors) y propagación multipath.

## Determinación de la Posición

*   **Triangulación:** Utilizando dos o más estaciones VDF separadas geográficamente, se puede determinar la posición de una aeronave encontrando el punto donde se cruzan las líneas de posición (QTE).
*   **Auto-triangulación:** Sistemas modernos, como los utilizados en frecuencias de emergencia (121.5 MHz), pueden triangular automáticamente la posición de una aeronave que transmite y mostrarla instantáneamente en la pantalla del controlador.
