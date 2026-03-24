---
title: "Motores Eléctricos de Aeronave y Principios de Control"
description: "Principios de motores DC, par motor, fuerza contra-electromotriz y modos de fallo (agarrotamiento, embalamiento)."
---

# Motores Eléctricos de Aeronave y Principios de Control

## Principios Básicos

*   **Función**: Convertir energía eléctrica en energía mecánica (rotación).
*   **Fuerza Contra-electromotriz (Back EMF)**: Un voltaje generado por el rotor giratorio que se opone al voltaje suministrado.
    *   Actúa como una "resistencia" al flujo de corriente.
    *   Proporcional a la velocidad (RPM).
    *   **Alta Velocidad** $\rightarrow$ Alta Back EMF $\rightarrow$ Baja Corriente.
    *   **Baja Velocidad/Parado** $\rightarrow$ Baja/Nula Back EMF $\rightarrow$ Alta Corriente.

### Relaciones de Par y Potencia

*   **Potencia ($P$)**:
    *   Eléctrica: $P = \text{Voltaje} (V) \times \text{Corriente} (I)$
    *   Mecánica: $P = \text{Par} (T) \times \text{RPM}$
*   **Par ($T$)**: La fuerza de giro.
    *   $T \propto \text{Corriente} \times \text{Fuerza del Campo Magnético}$
    *   De las ecuaciones de potencia: **$T = (V \times I) / \text{RPM}$**
    *   **Alta Corriente** $\rightarrow$ **Alto Par**.

### Cambios Operacionales (Motor DC)

*   **Aumentar la Carga Mecánica**:
    1.  El motor se ralentiza (las RPM disminuyen).
    2.  La Back EMF disminuye (menos oposición).
    3.  **La Corriente Aumenta**.
    4.  **El Par Aumenta** (para igualar la carga).
    5.  La potencia de salida aumenta.

### Modos de Fallo

#### Agarrotamiento del Rotor (Motor Bloqueado)
*   **Condición**: El rotor está físicamente impedido de girar (RPM = 0).
*   **Back EMF**: Cero (sin movimiento).
*   **Corriente**: **Aumenta masivamente** (fluye la máxima corriente posible).
*   **Par**: **Aumenta masivamente** (par de arranque máximo).
*   **Riesgo**: Sobrecalentamiento, fusión de cables/fusibles, fuego.

#### Embalamiento del Rotor (Sin Carga)
*   **Condición**: La carga mecánica se elimina repentinamente (por ejemplo, rotura del eje).
*   **Respuesta**: El motor acelera rápidamente.
*   **Back EMF**: Aumenta significativamente.
*   **Corriente**: **Disminuye** (debido a la alta Back EMF).
*   **Par**: **Disminuye**.
*   **Riesgo**: Exceso de velocidad/destrucción mecánica (si es bobinado en serie).

### Arrancadores-Generadores (Starter-Generators)

*   **Definición**: Una sola unidad que actúa como motor de arranque (para arrancar el motor) y luego como generador (una vez que el motor está en marcha).
*   **Fuentes de Energía para Accionar el Generador** (Cuando actúa como generador):
    *   Motor en Marcha
    *   APU
    *   RAT (Turbina de Aire de Impacto)
    *   Motor Hidráulico
*   **Fuentes de Energía para Accionar el Arrancador** (Cuando actúa como motor):
    *   Batería Interna
    *   Unidad de Potencia en Tierra (GPU)
    *   *Nota: La RAT no puede alimentar el arrancador.*
