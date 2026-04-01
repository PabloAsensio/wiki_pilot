---
title: Radionavegacion: Propagacion de Ondas
description: Estudia modos de propagacion de radio y su impacto operativo en navegacion.
keywords:
  - propagacion de ondas
  - propagacion de senales
  - navegacion aerea
---

# Radionavegacion: Propagacion de Ondas

La forma en que las ondas de radio viajan desde el transmisor hasta el receptor depende de su frecuencia y del entorno.

## Modos de Propagación

### 1. Ondas de Espacio (Space Waves)
Son ondas de **línea de visión (Line-of-Sight)**. Viajan en línea recta a través de la atmósfera.
*   Es el modo principal para **VHF, UHF, SHF y EHF**.
*   El alcance está limitado por la curvatura de la Tierra y obstáculos.
*   **Fórmula de alcance teórico (VHF):**
    $$Distancia (NM) = 1.23 \times (\sqrt{Altura_{Tx}(ft)} + \sqrt{Altura_{Rx}(ft)})$$

### 2. Ondas de Superficie (Ground/Surface Waves)
Estas ondas siguen la curvatura de la Tierra debido a la **difracción**.
*   Efectivas en frecuencias bajas (**VLF, LF, MF**).
*   El alcance depende de la potencia y del tipo de superficie (mayor alcance sobre el mar que sobre tierra).
*   Utilizadas por los **NDB**.

### 3. Ondas de Cielo (Sky Waves)
Son ondas que se refractan en la **ionosfera** y regresan a la Tierra, permitiendo comunicaciones más allá del horizonte.
*   Principal modo de propagación para **HF** (y MF por la noche).
*   Permite comunicaciones transoceánicas y globales.

## La Ionosfera

Capa de la atmósfera ionizada por la radiación solar. Afecta principalmente a las ondas HF.
*   **Capas:** D, E, F1, F2.
*   **Capa D:** Existe solo de día y **absorbe** las ondas de baja frecuencia (LF/MF), impidiendo su propagación como onda de cielo.
*   **Noche:** La capa D desaparece, permitiendo que las ondas MF y HF alcancen las capas superiores (E y F) y se refracten, aumentando drásticamente el alcance (y las interferencias).

### Conceptos Clave de Propagación HF
*   **Skip Distance (Distancia de Salto):** Distancia mínima desde el transmisor hasta donde la primera onda de cielo retorna a la Tierra.
    *   Aumenta con la frecuencia.
    *   Aumenta si la ionosfera está más alta (noche).
*   **Skip Zone (Zona de Silencio):** Área anular donde no se recibe señal: está demasiado lejos para la onda de superficie pero demasiado cerca para la primera onda de cielo.
*   **Fading (Desvanecimiento):** Fluctuación de la señal debido a cambios en la ionosfera o interferencia entre múltiples caminos (ej. onda de cielo vs. onda de superficie).

## Fenómenos y Errores

### Efecto Doppler
Cambio en la frecuencia percibida debido al movimiento relativo entre fuente y receptor.
*   **Aumenta** la frecuencia si se acercan, **disminuye** si se alejan.
*   Usado en: **DVOR** (para crear la señal de fase variable), **GNSS** (para determinar velocidad), Radares MTI y Radares Meteorológicos (para detectar turbulencia).

### Errores del ADF (Ondas LF/MF)
*   **Efecto Nocturno:** Interferencia entre onda de superficie y onda de cielo por la noche. Causa oscilación de la aguja.
*   **Refracción Costera:** La onda se curva hacia la costa al pasar de tierra a mar (cambio de velocidad).
*   **Efecto de Montaña:** Reflexiones en terreno montañoso.
*   **Tormentas:** Los rayos emiten señales en bandas LF/MF que atraen la aguja del ADF.
*   **Error Cuadrantal:** Desviación causada por el metal del propio avión. Máximo en rumbos relativos 045°, 135°, 225°, 315°.

## Fenómenos Físicos
*   **Refracción:** Cambio de dirección al pasar a un medio con diferente densidad (ej. ionosfera).
*   **Difracción:** Curvatura de la onda alrededor de obstáculos (permite la onda de superficie).
*   **Reflexión:** Rebote en superficies (tierra, edificios).
*   **Absorción:** Pérdida de energía (ej. capa D).
