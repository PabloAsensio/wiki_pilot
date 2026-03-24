---
title: "Datos de Masa en Vacío y CG"
description: "Extracción de datos de referencia BEM y CG de la documentación para cálculos diarios."
keywords: ["extracción BEM", "referencia CG", "índice", "hoja de carga"]
---

## Punto de Partida para Cálculos

Para la preparación diaria del vuelo, el piloto no vuelve a pesar la aeronave. En su lugar, extrae la **Masa Básica en Vacío (BEM)** y el **CG Básico en Vacío** directamente del informe de pesaje actual de la aeronave o del **Manual de Masa y Centrado**.

### Datos de Documentación

La entrada en el manual mostrará típicamente:
*   **Número de Serie/Matrícula**: Confirmando que los datos son para la aeronave específica.
*   **Fecha de Pesaje**: Cuándo se establecieron los datos.
*   **Masa Básica en Vacío**: Valor en kg o lbs.
*   **Centro de Gravedad**: Brazo (distancia desde el datum) o **Índice**.

### Unidades de Índice (IU)

Para simplificar los cálculos y evitar números de momento grandes, los manuales a menudo convierten los momentos en **Unidades de Índice**.
*   **Fórmula de Índice**:
    $$
    \text{Índice} = \frac{\text{Masa} \times (\text{Brazo} - \text{Ref})}{\text{Constante C}} + \text{Constante K}
    $$
    *   Esto reduce los números a un tamaño más manejable (ej. escala 0-100).

Al usar un sistema de Índice, el piloto:
1.  Comienza con el **Índice Básico** (correspondiente a la BEM).
2.  Añade el **cambio de Índice** para cada elemento de carga (tripulación, pasajeros, combustible) basado en tablas o gráficos.
3.  Calcula el **Índice Total Final**.
4.  Verifica si el Índice Final está dentro de la Envolvente permitida.
