---
title: "Vuelo Nivelado, Alcance y Autonomía"
description: "Optimización del vuelo para máxima distancia (Alcance) o máximo tiempo (Autonomía)."
keywords: ["alcance", "autonomía", "SAR", "alcance específico", "flujo de combustible", "velocidad de máximo alcance"]
---

## Alcance Específico (SR) vs. Autonomía Específica (SE)

La planificación de performance se centra en la eficiencia: cuánta distancia o tiempo se puede ganar por unidad de combustible.

![Máximo Alcance y Autonomía](https://upload.wikimedia.org/wikipedia/commons/3/34/Maximum_Endurance_and_Range.jpg)

### Alcance Específico (SR - Specific Range)
*   **Definición**: Distancia volada por unidad de combustible.
    $$
    SR = \frac{\text{Velocidad Verdadera (TAS)}}{\text{Flujo de Combustible (FF)}}
    $$
*   **Meta**: Máximo Alcance (volar tan lejos como sea posible).
*   **Condición Aerodinámica**:
    *   **Jet**: Volar a $1.32 V_{MD}$ (aprox). Optimizado donde la relación $TAS/Resistencia$ es máxima.
    *   **Hélice**: Volar a $V_{MD}$. Optimizado donde la $Resistencia$ es mínima.

### Autonomía Específica (SE - Specific Endurance)
*   **Definición**: Tiempo de vuelo por unidad de combustible.
    $$
    SE = \frac{1}{\text{Flujo de Combustible}}
    $$
*   **Meta**: Máxima Autonomía (mantenerse en el aire tanto tiempo como sea posible, ej. Esperas/Holding).
*   **Condición Aerodinámica**:
    *   **Jet**: Volar a $V_{MD}$. Mínimo Empuje requerido = Mínimo Flujo de Combustible.
    *   **Hélice**: Volar a $V_{mp}$ (Velocidad de Mínima Potencia). Mínima Potencia = Mínimo Flujo de Combustible.

## Efecto de las Variables

### Viento
*   **Alcance**: El viento en cola aumenta la Ground Speed, aumentando el Alcance. El viento en cara disminuye el Alcance.
    *   *Acción del Piloto*: Con viento en cara, aumentar ligeramente la velocidad (aumenta el Cost Index) para penetrar el viento. Con viento en cola, disminuir la velocidad para aprovechar el empuje del viento más tiempo.
*   **Autonomía**: El viento **no tiene efecto** en la Autonomía (el tiempo en el aire depende solo del flujo de combustible, no de la distancia terrestre cubierta).

### Masa (Peso)
*   **Alcance**: Mayor masa requiere mayor Sustentación ($L=W$), creando más Resistencia Inducida. Se necesita más empuje/combustible. El alcance disminuye.
    *   *Velocidad*: A medida que el peso disminuye (quema de combustible), la velocidad óptima de alcance disminuye.
*   **Autonomía**: Mayor masa requiere más potencia/empuje para mantener la altitud. La autonomía disminuye.

### Altitud
*   **Alcance Jet**: generalmente aumenta con la altitud debido a menor temperatura (mejor eficiencia del motor) y mayor TAS para la misma IAS.
*   **Alcance Hélice**: menos afectado por la altitud, limitado por la caída de rendimiento del motor.
