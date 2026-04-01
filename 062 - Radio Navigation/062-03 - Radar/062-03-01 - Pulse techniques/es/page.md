---
title: "Radionavegación: Tecnicas de Pulso en Radar"
description: "Comprende temporizacion de radar de pulsos, cálculo de distancia e interpretacion de eco."
keywords:
    - "técnicas de pulso"
    - "radar de pulsos"
    - "radar en aviacion"
---

# Radionavegación: Tecnicas de Pulso en Radar

## Principios Básicos del Radar

El **RADAR** (Radio Detection and Ranging) es un sistema que utiliza ondas electromagnéticas para detectar objetos y determinar su distancia y dirección.

### Radar Primario vs Secundario

*   **Radar Primario**: Emite pulsos de energía electromagnética que se reflejan en los objetos (ecos). Mide el tiempo que tarda la señal en ir y volver para calcular la distancia.
    *   Ejemplos: Radar meteorológico (AWR), Radar de vigilancia primaria (PSR), Radar de movimiento en superficie (SMR).
*   **Radar Secundario**: Utiliza un sistema de interrogador (tierra) y transpondedor (aire). El transpondedor recibe la señal y emite una respuesta codificada más fuerte.
    *   Ejemplos: SSR (Secondary Surveillance Radar), DME.

## Parámetros del Pulso

### PRF (Pulse Repetition Frequency)
Es el número de pulsos transmitidos por segundo (pps).
*   **Relación con el Rango Máximo**: El PRF determina el rango máximo teórico no ambiguo. El radar debe esperar a que el pulso regrese desde la distancia máxima antes de enviar el siguiente.
*   **Fórmula**:
    $$ \text{Rango Máximo (km)} = \frac{300,000}{2 \times \text{PRF}} $$
    *(Donde 300,000 es la velocidad de la luz en km/s)*.
*   A **menor PRF**, mayor es el tiempo de escucha y por tanto **mayor es el rango máximo**.

### Ancho de Pulso (Pulse Width)
Es la duración del pulso transmitido.
*   **Relación con el Rango Mínimo**: El radar no puede recibir mientras transmite. Por tanto, el ancho de pulso determina la distancia mínima a la que se puede detectar un objeto (blind spot).
*   **Resolución en Distancia**: Un pulso más corto permite distinguir mejor entre dos objetos cercanos en la misma dirección (mejor resolución).

### Potencia
*   **Potencia Pico (Peak Power)**: Es la potencia máxima instantánea durante la duración del pulso. Determina el alcance máximo de detección (capacidad de atravesar la atmósfera y retornar).
*   **Potencia Media**: Es la energía promediada sobre todo el ciclo (incluyendo el tiempo de silencio). Es mucho menor que la potencia pico.

## Aplicaciones

*   **ATC (Control de Tráfico Aéreo)**:
    *   Radar Primario: Para ver aeronaves sin transpondedor y meteorología.
    *   Radar Secundario (SSR): Para identificar aeronaves, obtener altitud y códigos squawk.
*   **A bordo**:
    *   Radar Meteorológico (AWR): Detección de precipitaciones y turbulencia.
    *   Radioaltímetro: Medición de altura sobre el terreno.
    *   DME: Medición de distancia (técnica de pulsos).
    *   TCAS: Evitación de colisiones (basado en SSR).
