---
title: "Medición de Empuje en Reactores: Indicaciones N1 y EPR con Verificación"
description: "Comprende los parámetros de ajuste de empuje N1 y EPR, la lógica de relación de presiones, riesgos de bloqueo en sensores y verificación cruzada operativa."
keywords:
	- "minimum speed"
	- "flight level"
	- "rumbos magnéticos"
	- "compass turns"
---
# Medición de Empuje en Reactores: Indicaciones N1 y EPR con Verificación

En los motores a reacción, el empuje es la fuerza de salida directa. Los pilotos dependen de parámetros específicos para ajustar y monitorizar esta potencia.

## Parámetros principales de empuje

### N1 (Velocidad del Fan)
**N1** representa la velocidad de rotación del compresor de Baja Presión (fan).
*   Se muestra como un **porcentaje (%)** de las RPM máximas nominales.
*   El fan acelera un gran volumen de aire alrededor del núcleo, proporcionando la mayor parte del empuje en motores de alto índice de derivación.

### EPR (Relación de Presión del Motor)
**EPR** mide la relación entre la presión en el escape y la presión en la entrada.
*   **Fórmula:** $EPR = \frac{\text{Presión de Salida de Turbina } (P_t)}{\text{Presión de Entrada de Compresor } (P_s)}$
*   Sensores (tubos Pitot) miden estas presiones.
*   **Peligro de bloqueo:** Si el sensor de presión de entrada se **bloquea** durante el despegue (aceleración), no registrará el aumento de la presión dinámica. Se "bloqueará" en una lectura de presión más baja. Matemáticamente, dividir la presión de salida (que aumenta) por una presión de entrada estrictamente inferior a la real da como resultado una EPR **sobreindicada**. El indicador mostrará un empuje alto mientras que el empuje real es bajo. En tales casos, los pilotos deben verificar con **N1**.
