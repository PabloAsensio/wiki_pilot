---
title: "Caudalímetros de Combustible: Flujo Volumétrico/Gravimétrico e Integración"
description: "Estudia los métodos de medición de flujo de combustible y el cálculo integrado de combustible usado para verificar consumo, detectar fugas y predecir combustible en destino."
keywords:
    - "fuel flow"
    - "fuel used"
    - "flight level"
    - "minimum speed"
---
# Caudalímetros de Combustible: Flujo Volumétrico/Gravimétrico e Integración

Los caudalímetros de combustible proporcionan a los pilotos y a los ordenadores de a bordo datos en tiempo real sobre el rendimiento del motor y el consumo de combustible.

## Principios de medición
Los caudalímetros miden la cantidad de combustible suministrado a los motores por unidad de tiempo. Hay dos métodos principales de medición:
*   **Volumétrico:** Muestra volumen por unidad de tiempo (ej., US gal/h, Litros/h). Susceptible a errores de densidad por cambios de temperatura.
*   **Gravimétrico:** Muestra **masa** por unidad de tiempo (ej., **kg/h**, lb/h). Este es el estándar para el Transporte Aéreo Comercial, ya que proporciona una medida más consistente y precisa del contenido energético.

## Consumo total de combustible (Fuel Used)
Para determinar el combustible total consumido durante un vuelo, el sistema utiliza la **integración**.
*   **Proceso:** Un ordenador integra matemáticamente la tasa de consumo de combustible (flujo) sobr el tiempo.
    *   $\text{Consumo Total} = \int (\text{Flujo de Combustible}) dt$
*   **Función:** Este cálculo tiene en cuenta todas las variables que afectan al consumo (cambios de altitud, velocidad, meteorología).
*   **Utilidad:** El "Combustible Usado" calculado se compara con el "Combustible a Bordo" (FOB) de los sensores del tanque. Esta verificación cruzada permite a la tripulación y al Sistema de Gestión de Vuelo (FMS):
    1.  Verificar una quema de combustible precisa.
    2.  **Detectar fugas** (si Combustible Usado + Restante no es igual al FOB Inicial).
    3.  Predecir con precisión el combustible en destino.

Un **Caudalímetro Integrado** es un instrumento que muestra tanto el Flujo de Combustible instantáneo como el Combustible Total Usado.
