---
title: "Aproximación y Aterrizaje Clase A"
description: "Cálculos de performance de aterrizaje, requisitos de despacho y factores."
keywords: ["Clase A", "distancia de aterrizaje", "LDR", "motor y al aire", "aterrizaje frustrado", "gradiente de ascenso"]
---

## Requisitos de Ascenso

### Ascenso de Aproximación (OEI)
Durante una aproximación (un motor inoperativo), si se inicia un Go-Around:
*   **Configuración**: Flaps de Aproximación, Tren Arriba, OEI, Empuje de Despegue.
*   **Requisito de Gradiente**:
    *   **Dos Motores**: 2.1%.
    *   **Tres Motores**: 2.3%.
    *   **Cuatro Motores**: 2.4%.

### Ascenso de Aterrizaje (AEO)
También conocido como "Balked Landing" (Go-Around desde muy baja altitud/toque).
*   **Configuración**: Flaps de Aterrizaje, Tren Abajo, AEO, Empuje de Despegue.
*   **Requisito de Gradiente**: 3.2% (para todos los tipos de aeronaves).
*   Esto asegura que la aeronave pueda ascender de manera segura incluso en configuración completa de aterrizaje.

## Distancia de Aterrizaje Requerida (LDR)

La distancia horizontal desde una altura de pantalla de **50 pies** hasta una parada completa.

### Factores Operacionales (Despacho)
En la etapa de planificación (Despacho), la aeronave debe ser capaz de aterrizar dentro de una fracción de la pista disponible (LDA).

*   **Pista Seca**: LDR $\le 60\%$ de LDA (o LDA $\ge 1.67 \times$ LDR).
*   **Pista Mojada**: LDR $\le 60\%$ de LDA, luego multiplicar la distancia requerida por 1.15.
    *   Resultado: LDA $\ge 1.92 \times$ LDR Seca.

### Cálculo En Vuelo
Una vez en vuelo, para el aterrizaje real, se utiliza la distancia de aterrizaje "En Vuelo" o "Asesora" (a menudo llamada ALD u OLD). Esto elimina el gran factor de seguridad de 1.67 pero añade un margen operacional más pequeño (ej. +15%).

## Factores que Afectan la LDR
*   **Masa**: Mayor masa $\rightarrow$ mayor $V_{REF}$ $\rightarrow$ mayor distancia. ($Distancia \propto Masa^2$).
*   **Altitud**: Mayor altitud de densidad $\rightarrow$ mayor TAS para la misma IAS $\rightarrow$ mayor distancia.
*   **Viento**: El viento en cola aumenta la distancia significativamente.
*   **Pendiente**: La pendiente descendente aumenta la distancia.
*   **Superficie**: Agua/Hielo/Nieve reduce la acción de frenado, aumentando la distancia.
