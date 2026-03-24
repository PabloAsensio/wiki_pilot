---
title: "Sistemas de Carburación e Inyección"
description: "Principios de carburadores y sistemas de inyección, formación de hielo en la admisión, control de mezcla y cebado."
---

# Sistemas de Carburación e Inyección

## Principios del Carburador

*   **Función**: Mezcla combustible y aire en las proporciones correctas antes de entregarlo a los cilindros.
*   **Operación**: Basado en el **Principio de Bernoulli**.
    *   El aire acelera a través de un **Venturi**, causando una **caída en la presión estática y la temperatura**.
    *   Esta caída de presión succiona combustible de la cámara del flotador hacia la corriente de aire.
*   **Difusor**: Mantiene una **relación de mezcla constante** en una amplia gama de velocidades del motor (evita que la mezcla se vuelva demasiado rica con un alto flujo de aire).
    *   Utiliza un conducto de equilibrio de presión para sangrar aire en la boquilla de combustible, reduciendo la succión.
*   **Bomba de Aceleración**: Evita un corte temporal de **mezcla pobre** durante el avance rápido del acelerador.
    *   Inyecta un chorro de combustible en el venturi cuando se abre rápidamente el acelerador, igualando el rápido aumento en el flujo de aire.

### Formación de Hielo en la Admisión

*   **Susceptibilidad**: Afecta **tanto** a carburadores como a sistemas de inyección de combustible (aunque los carburadores son más propensos debido al enfriamiento por vaporización del combustible).
*   **Factores de Formación de Hielo en el Carburador**:
    *   **Evaporación del Combustible**: Absorbe calor latente, enfriando el aire.
    *   **Efecto Venturi/Acelerador**: La caída de presión causa una caída de temperatura de hasta 30°C.
    *   **Resultado**: Se forma hielo en las paredes del venturi y en la válvula de mariposa, restringiendo el flujo de aire (caída de RPM/Presión del Colector).
*   **Calefacción del Carburador**:
    *   **Acción**: Suministra aire caliente y sin filtrar a la admisión.
    *   **Efecto**: Derrite el hielo.
    *   **Efectos Secundarios**:
        *   El aire caliente es **menos denso** $\rightarrow$ **La Potencia cae** (~15%) y **La Mezcla se enriquece**.
        *   La combustión se vuelve menos eficiente (riesgo de detonación a alta potencia).
    *   **Indicación**: Caída inicial en RPM (debido al aire caliente), seguida de un aumento en RPM (a medida que el hielo se derrite y se restaura el flujo de aire).
    *   **Uso**: Usar completamente ENCENDIDO cuando se sospeche formación de hielo. Evitar el uso prolongado a alta potencia (despegue/ascenso) para evitar detonación y pérdida de potencia.

### Cebado (Priming) y Arranque

*   **Propósito**: Inyectar combustible extra para arrancar (enriquecer la mezcla), especialmente en condiciones frías.
*   **Bomba de Cebado**: Fuerza combustible atomizado **directamente en los puertos de admisión del cilindro** (evitando el carburador).
*   **Bombeo del Acelerador**: Utiliza la bomba de aceleración para inyectar combustible en el carburador. Menos efectivo y conlleva un mayor riesgo de **incendio de inducción**.
*   **Incendio de Inducción en el Arranque**:
    *   **Procedimiento**: **Continuar Girando el Motor** (Cranking). Esto succiona las llamas de vuelta al motor.
    *   Si el motor arranca: Ejecutar a RPM moderadas para extinguir.
    *   Si falla el arranque: Apagar, mezcla corta (idle cut-off), selector de combustible apagado, master apagado, evacuar, extinguir.

### Inyección de Combustible

*   **Operación**: El combustible se inyecta continuamente en el puerto de admisión (justo antes de la válvula).
*   **Ventajas**: Sin restricción de venturi (más potencia), distribución uniforme de la mezcla, inmune a la formación de hielo por *refrigeración* (aunque la formación de hielo por impacto aún es posible).
*   **Componentes**: Bomba accionada por el motor, unidad de control de combustible/aire, válvula de colector, boquillas inyectoras.
