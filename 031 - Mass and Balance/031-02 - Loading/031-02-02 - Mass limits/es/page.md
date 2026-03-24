---
title: "Límites de Masa y Cálculos"
description: "Determinación de la carga de tráfico máxima permitida basada en los límites de masa."
keywords: ["límites de masa", "cálculo de carga de tráfico", "MTOM", "MLM", "MZFM", "masa regulada de despegue"]
---

## Determinación de la Carga de Tráfico Máxima

Para encontrar la carga de tráfico máxima permitida para un vuelo, debemos calcular la carga permitida por cada uno de los tres límites principales:
1.  Límite de **Masa Máxima de Despegue (MTOM)**.
2.  Límite de **Masa Máxima de Aterrizaje (MLM)**.
3.  Límite de **Masa Máxima Sin Combustible (MZFM)**.

La *menor* de las tres cargas de tráfico resultantes es el factor limitante (Regulated Traffic Load).

### 1. Límite MTOM
$$
\text{Carga Tráfico Máx (MTOM)} = \text{MTOM} - \text{DOM} - \text{Combustible Despegue}
$$

### 2. Límite MLM
Dado que la aeronave quema combustible durante el viaje, puede despegar más pesada que el límite de aterrizaje.
$$
\text{Masa Despegue Máx permitida por MLM} = \text{MLM} + \text{Combustible Viaje}
$$
$$
\text{Carga Tráfico Máx (MLM)} = (\text{MLM} + \text{Combustible Viaje}) - \text{DOM} - \text{Combustible Despegue}
$$
*Alternativamente:* Carga Tráfico Máx = MLM - DOM - Combustible Reserva (Aterrizaje).

### 3. Límite MZFM
$$
\text{Carga Tráfico Máx (MZFM)} = \text{MZFM} - \text{DOM}
$$
*Nota: El combustible no es parte de la ZFM.*

## Ejemplo de Cálculo

Dados:
*   DOM: 35.000 kg
*   MTOM: 65.000 kg
*   MLM: 55.000 kg
*   MZFM: 52.000 kg
*   Combustible de Viaje: 8.000 kg
*   Combustible al Despegue: 15.000 kg

Calcular Carga de Tráfico Máxima:

1.  **Basado en MTOM**:
    $$65.000 - 35.000 - 15.000 = 15.000 \text{ kg}$$
2.  **Basado en MLM**:
    *   Masa máx al despegue permitida por límite aterrizaje: $55.000 + 8.000 = 63.000 \text{ kg}$
    *   Carga Tráfico: $63.000 - 35.000 - 15.000 = 13.000 \text{ kg}$
3.  **Basado en MZFM**:
    $$52.000 - 35.000 = 17.000 \text{ kg}$$

**Resultado**: El valor más bajo es **13.000 kg** (limitado por la Masa de Aterrizaje).
