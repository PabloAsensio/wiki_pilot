---
title: "Métodos de Cálculo del CG: Enfoques Matemático, Gráfico y Electrónico"
description: "Compara métodos para determinar el centro de gravedad: cálculo por momentos, herramientas gráficas/índice y procesamiento electrónico en FMC/EFB."
keywords:
  - "cálculo cg"
  - "método de momentos"
  - "método de índice"
  - "masa y centrado electrónico"
---

# Métodos de Cálculo del CG: Enfoques Matemático, Gráfico y Electrónico

## Método Matemático

El método más preciso implica calcular los momentos de todas las masas.

1.  **Datum**: Una línea de referencia fija.
2.  **Brazo**: Distancia horizontal desde el datum al CG de un componente.
3.  **Momento**: Masa × Brazo.

$$
\text{Momento Total} = \sum (\text{Masa}_i \times \text{Brazo}_i)
$$
$$
\text{Posición del CG} = \frac{\text{Momento Total}}{\text{Masa Total}}
$$

*   Los brazos detrás del datum son positivos (+).
*   Los brazos delante del datum son negativos (-).

## Método Gráfico/Índice

Para simplificar la carga de trabajo del piloto y reducir errores de cálculo, los fabricantes proporcionan:
*   **Gráficos de Carga**: El piloto lee un índice o valor de momento de un gráfico para cada elemento de carga (combustible, pasajeros, maletas).
*   **Envolventes de CG**: El índice total se traza contra la masa total para verificar que cae dentro de la envolvente segura.

Esto evita números de momento grandes y aritmética compleja, reemplazándolos con una simple suma de unidades de índice.

## Método Electrónico

Las aeronaves modernas utilizan Computadoras de Gestión de Vuelo (FMC) o Electronic Flight Bags (EFB) para calcular la masa y el CG.
*   **Entrada**: ZFM, Combustible, distribución de Pasajeros.
*   **Salida**: TOW, LAW, ZFW CG, TOW CG, ajuste de Trim.
*   **Verificación Cruzada**: Los pilotos aún deben verificar las entradas contra la hoja de carga.
