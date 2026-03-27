---
title: "Medición de Presión Pitot-Estática: Presión Estática, Total y Dinámica"
description: "Estudia la medición de presión pitot-estática para ATPL Instrumentación: presión estática, total, dinámica y efectos de bloqueos en instrumentos."
keywords:
    - "altímetro"
    - "altitud de densidad"
    - "presión estática"
    - "sistema pitot estática"
    - "calibrated altitude"
---
# Medición de Presión Pitot-Estática: Presión Estática, Total y Dinámica

La medición de la presión es fundamental para la instrumentación de vuelo. El **Sistema Pitot-Estática** proporciona los datos de presión brutos necesarios para determinar la velocidad, la altitud y la velocidad vertical.

## Principios de Presión
*   **Presión Estática ($P_s$):** La presión atmosférica que rodea a la aeronave. Actúa sobre todas las superficies y disminuye con la altitud.
*   **Presión Total (Pitot) ($P_t$):** La suma de la presión estática y la presión dinámica creada por el movimiento hacia adelante de la aeronave.
*   **Presión Dinámica ($q$):** La presión determinada por la velocidad y densidad del flujo de aire ($q = 1/2 \rho V^2$).
    *   Relación: **$P_t = P_s + q$**

## Componentes del Sistema
1.  **Tomas Estáticas:** Orificios situados en el fuselaje (a menudo emparejados para cancelar errores de deslizamiento) donde el flujo de aire no está perturbado. Alimentan al **Altímetro**, **VSI** y **ASI**.
2.  **Tubo Pitot:** Un tubo abierto orientado al flujo de aire relativo. Mide la **Presión Total** y alimenta SOLAMENTE al **ASI** (y Machímetro/ADC).

## Bloqueos y Errores
*   **Bloqueo de Estática:**
    *   **Altímetro:** Se congela a la altitud donde ocurrió el bloqueo.
    *   **VSI:** Indica cero.
    *   **ASI:** Se comporta como un altímetro al revés (Indica menos en ascenso / Indica más en descenso).
    *   **Toma estática alternativa (cabina):** Si se utiliza, la menor presión en la cabina (debido a la succión aerodinámica) hace que el Altímetro y el Velocímetro **indiquen más** y el VSI indique un ascenso momentáneo.
*   **Bloqueo de Pitot:**
    *   **ASI:** Se comporta como un altímetro (Indica más en ascenso / Indica menos en descenso).
