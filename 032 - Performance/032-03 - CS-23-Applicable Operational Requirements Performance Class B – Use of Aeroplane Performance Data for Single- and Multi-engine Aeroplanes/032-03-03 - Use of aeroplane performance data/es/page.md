---
title: "Performance Clase B (CS-23): Uso de datos de performance de la aeronave"
description: "Cómo interpretar y usar gráficos y tablas de performance para la planificación de vuelos."
keywords: ["datos performance", "gráficos", "tablas", "altitud de densidad", "desviación ISA"]
---

# Performance Clase B (CS-23): Uso de datos de performance de la aeronave


## Interpretación de Gráficos de Performance

Los manuales proporcionan datos de performance en formatos tabulares o gráficos. Es esencial entrar en el gráfico correctamente y seguir las líneas con precisión.

### Variables Comunes
*   **Altitud de Presión (PA)**: Altitud sobre el plano de referencia estándar (1013.25 hPa).
*   **Temperatura (OAT)**: Temperatura del Aire Exterior. A menudo convertida a **Desviación ISA** (ej. ISA +10°C).
*   **Peso**: Masa de la aeronave al inicio de la fase.
*   **Componente de Viento**: Viento de cara o de cola.

### Ejemplo: Gráfico de Distancia de Despegue
1.  **Entrar con OAT**: Encontrar la temperatura en el primer eje.
2.  **Mover a Altitud de Presión**: Seguir la línea hasta la línea de referencia de PA y paralela a las líneas del gráfico hasta la PA específica.
3.  **Mover a Peso**: Moverse horizontalmente hasta la línea de referencia, luego paralelo a las líneas de peso relevantes.
4.  **Mover a Viento**: Moverse horizontalmente hasta la referencia, luego paralelo a las líneas de componente de viento.
5.  **Leer Resultado**: Moverse horizontalmente para leer la Distancia de Despegue Requerida (TODR).

## Correcciones
Siempre aplicar correcciones en el orden especificado por el gráfico (usualmente Temp $\rightarrow$ Alt $\rightarrow$ Peso $\rightarrow$ Viento $\rightarrow$ Pendiente $\rightarrow$ Superficie).

### Corrección de Pendiente
*   **Pendiente Ascendente**: Aumenta la Distancia de Despegue (la aeronave trabaja contra la gravedad). Disminuye la Distancia de Aterrizaje (la gravedad ayuda al frenado).
*   **Pendiente Descendente**: Disminuye la Distancia de Despegue (la gravedad ayuda a la aceleración). Aumenta la Distancia de Aterrizaje.

### Corrección de Superficie
*   **Hierba/Grava**: Aumenta la fricción de rodadura, aumentando la Distancia de Despegue.
*   **Mojada**: Reduce la eficacia de frenado, aumentando la Distancia de Aterrizaje.

## Interpolación y Extrapolación
*   **Interpolación**: Estimar un valor entre dos valores conocidos (ej. peso 2500 kg entre 2000 y 3000 kg). Permitido y necesario.
*   **Extrapolación**: Estimar un valor fuera del rango del gráfico. **Peligroso y generalmente prohibido** ya que las relaciones de performance pueden no ser lineales.
