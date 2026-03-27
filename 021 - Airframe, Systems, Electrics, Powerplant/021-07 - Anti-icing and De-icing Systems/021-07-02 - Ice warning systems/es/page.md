---
title: "Sistemas de Aviso de Hielo y Tecnologías de Detección"
description: "Métodos de detección de hielo por sonda vibratoria, presión diferencial y observación visual, con lógica de sistemas consultivos y primarios."
---

# Sistemas de Aviso de Hielo y Tecnologías de Detección

Los sistemas de advertencia de hielo proporcionan a las tripulaciones de vuelo alertas oportunas sobre la acumulación de hielo en la aeronave. Estos pueden variar desde simples señales visuales hasta sofisticados sistemas de detección automática.

## Tipos de Detectores

### Sonda Vibratoria (por ejemplo, Rosemount)
- **Principio:** Una sonda cilíndrica corta vibra axialmente a una **frecuencia resonante** referenciada.
- **Detección:** A medida que el hielo se acumula en la sonda, su masa aumenta, causando que la **frecuencia de vibración disminuya**. Este cambio se detecta y activa una advertencia.
- **Operación:** La sonda está equipada con un elemento calefactor para derretir el hielo después de la detección, permitiendo que el sistema se reinicie y continúe monitoreando la tasa de acumulación.
- **Tecnología:** A menudo utiliza **cristales piezoeléctricos** para detectar el cambio en la frecuencia.

### Presión Diferencial (por ejemplo, Smiths)
- **Principio:** Un tubo hueco con orificios en sus bordes de ataque y salida.
- **Detección:** En condiciones normales, la presión del aire aumenta en la sonda. En condiciones de hielo, los orificios en el borde de ataque se bloquean por el hielo.
- **Mecanismo:** El bloqueo causa una **disminución en la presión dinámica** dentro de la sonda. El cambio resultante en la diferencia de presión entre los orificios activa la advertencia.
- **Calentamiento:** La sonda se calienta para limpiar el hielo. Los **orificios más pequeños tienden a limpiarse primero**.

### Detectores Visuales/Manuales (por ejemplo, Hot Rod)
- **Diseño:** Una sonda/varilla simple montada fuera de la ventana de la cabina en el campo de visión del piloto.
- **Función:** Los pilotos observan visualmente la acumulación de hielo.
- **Característica:** Incluye un calentador (a menudo operado manualmente) para limpiar el hielo y permitir la evaluación de la tasa de acumulación.
- **Referencia Ocular:** Los requisitos de diseño aseguran que las indicaciones visuales de hielo (como la acumulación en los limpiaparabrisas) sean visibles desde la **posición correcta de referencia ocular** del piloto.

## Clasificaciones del Sistema

- **Sistema Consultivo (Advisory):** La tripulación utiliza principalmente los criterios del manual de vuelo (Temperatura Total del Aire, humedad visible) para activar el antihielo. El detector sirve solo como respaldo.
- **Sistema Primario:**
    - **Automático:** El detector **activa automáticamente** los sistemas de protección contra hielo en el momento óptimo.
    - **Manual:** La tripulación activa los sistemas basándose en la indicación **primaria** del detector.
