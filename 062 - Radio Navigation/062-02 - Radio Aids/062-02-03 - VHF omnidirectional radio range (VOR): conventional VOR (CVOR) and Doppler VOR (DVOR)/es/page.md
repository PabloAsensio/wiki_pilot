---
title: "Radionavegación: VOR, CVOR, DVOR y Radiofaro Omnidireccional VHF"
description: "Comprende diferencias entre VOR y DVOR, incluyendo señales, CVOR y funcionamiento del radiofaro omnidireccional VHF."
keywords:
    - "cvor"
    - "c vor"
    - "vor doppler"
    - "radiofaro omnidireccional vhf"
    - "navegacion vor"
---

# Radionavegación: VOR, CVOR, DVOR y Radiofaro Omnidireccional VHF

El **VOR** es una radioayuda de navegación que opera en la banda VHF y proporciona al piloto la dirección magnética hacia o desde la estación terrestre.

![Estación VOR](https://upload.wikimedia.org/wikipedia/commons/f/fe/D-VOR_PEK.JPG)

## Principios de Funcionamiento

*   **Frecuencias:** Opera en la banda VHF, entre **108.00 MHz y 117.975 MHz**.
    *   **108.00 - 111.95 MHz:** Compartido con el ILS. El VOR utiliza frecuencias con el **primer decimal PAR** (ej. 108.20, 108.45). El ILS usa decimales impares.
    *   **112.00 - 117.975 MHz:** Uso exclusivo para VOR.
*   **Señales:** La estación transmite dos señales de 30 Hz:
    *   **Señal de Referencia:** Omnidireccional (fase constante en todas direcciones).
    *   **Señal Variable:** Direccional (rotatoria). Su fase cambia según la dirección.
*   **Determinación del Radial:** El receptor mide la **diferencia de fase** entre ambas señales. Esta diferencia en grados corresponde al radial magnético en el que se encuentra el avión.
    *   Ejemplo: Si la diferencia de fase es 90°, el avión está en el radial 090.

## Tipos de VOR

1.  **CVOR (Conventional VOR):**
    *   Señal de Referencia: Modulada en Frecuencia (FM).
    *   Señal Variable: Modulada en Amplitud (AM) por una antena rotatoria física.
    *   Susceptible a errores de sitio (multipath).
2.  **DVOR (Doppler VOR):**
    *   Señal de Referencia: Modulada en Amplitud (AM).
    *   Señal Variable: Modulada en Frecuencia (FM) simulando la rotación mediante un anillo de antenas (Efecto Doppler).
    *   **Ventaja:** Mucho más preciso y menos susceptible a errores de sitio/multipath gracias a la señal variable en FM.
3.  **TVOR (Terminal VOR):** Baja potencia, corto alcance (25 NM), usado en aeródromos.
4.  **VOT (VOR Test Facility):** Emite una señal de prueba con diferencia de fase cero (Radial 180 en todas direcciones). Se usa en tierra para verificar el equipo (Indicación: 180 TO o 360 FROM con aguja centrada).

## Instrumentos e Indicaciones

![Indicador VOR (CDI)](https://upload.wikimedia.org/wikipedia/commons/3/32/Vor_indicator.png)

*   **CDI (Course Deviation Indicator):**
    *   **OBS (Omni Bearing Selector):** Permite seleccionar el curso deseado.
    *   **Aguja de Desviación:** Muestra la desviación angular respecto al curso seleccionado.
    *   **Escala:** Típicamente 5 puntos a cada lado. **Desviación total (Full Scale Deflection) = 10°** (2° por punto).
    *   **Indicador TO/FROM:** Indica si el curso seleccionado lleva hacia (TO) o desde (FROM) la estación.
        *   **TO:** El radial seleccionado está a más de 90° del radial actual.
        *   **FROM:** El radial seleccionado está a menos de 90° del radial actual.
*   **RMI (Radio Magnetic Indicator):**
    *   **Cola de la aguja:** Indica el **Radial** actual (QDR).
    *   **Cabeza de la aguja:** Indica el rumbo magnético hacia la estación (QDM).

## Alcance y Precisión

*   **Alcance:** Limitado por la **línea de visión (Line-of-Sight)**.
    *   Fórmula aproximada: $Distancia (NM) = 1.23 \times \sqrt{Altura (ft)}$.
*   **Precisión:** $\pm 5^\circ$ (en rutas aéreas).
*   **Establecido:** En aproximaciónes, se considera establecido dentro de **media escala de desviación (5°)**.
*   **Monitorización:** El monitor apaga el VOR o retira la identificación si el error de rumbo excede **1°** o la potencia cae más del 15%.

## Procedimientos y Conceptos Adicionales

*   **Radiales:** Siempre son magnéticos y **DESDE (FROM)** la estación. Se usa la variación magnética en la posición del **VOR**.
*   **Cono de Confusión:** Zona sobre la estación donde no se recibe señal o es errática.
*   **Scalloping:** Ondulación de la señal causada por reflexiones en el terreno.
*   **ATIS:** Algunos VOR transmiten la información ATIS del aeropuerto en su frecuencia.

## Navegación en Ruta

![Carta Enruta IFR (Aerovías VOR)](https://upload.wikimedia.org/wikipedia/commons/d/d6/Holdings_on_fligth_chart_IFR_Enroute_Low_Altitude.png)
