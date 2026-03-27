---
title: "Alineación y Operación INS/IRS: Modos NAV-ATT y Control de Deriva"
description: "Aprende la alineación inercial, el gyrocompassing hacia norte verdadero, la lógica de modos NAV/ATT y la verificación de deriva post-vuelo."
keywords:
    - "rumbos magnéticos"
    - "curso magnético"
    - "compass turns"
    - "points on the compass"
---

# Alineación y Operación INS/IRS: Modos NAV-ATT y Control de Deriva

## Proceso de Alineación

El Sistema de Referencia Inercial (IRS) debe alinearse en tierra antes del vuelo para establecer una base de navegación. Este proceso es crítico para una operación precisa.

### Requisitos
*   **Aeronave Estacionaria**: La aeronave no debe moverse durante la alineación. El movimiento perturba la detección de la gravedad y la rotación de la Tierra.
*   **Entrada de Posición**: El piloto debe ingresar la posición actual (Latitud y Longitud) a través del CDU del FMS o ISDU.

### Fases de la Alineación
1.  **Nivelación (Determinación de la Vertical Local)**:
    *   Los acelerómetros detectan el vector de gravedad.
    *   El sistema establece la **Vertical Local** (hacia abajo) y crea un plano horizontal (matemáticamente en IRS, mecánicamente en INS).
2.  **Gyrocompassing (Alineación con el Norte Verdadero)**:
    *   El sistema detecta la rotación de la Tierra (tasa aprox. 15°/hora).
    *   Dado que la Tierra rota alrededor del eje del Norte Verdadero, el sistema puede determinar la dirección del **Norte Verdadero** midiendo el componente horizontal de la rotación terrestre.
    *   **Cálculo de Latitud**: Midiendo la magnitud del vector de rotación terrestre, el sistema puede estimar su propia **Latitud**. Compara esta latitud calculada con la entrada del piloto para verificar errores graves.
    *   **Longitud**: El sistema **no puede** determinar la Longitud; depende completamente de la entrada del piloto.

### Tiempo de Alineación
*   **Duración**: Típicamente **10 minutos** en latitudes medias.
*   **Latitudes Altas**: La alineación toma más tiempo a medida que aumenta la latitud (el vector de velocidad rotacional de la Tierra es más vertical, haciendo difícil detectar el componente horizontal).
*   **Límite**: La alineación es generalmente imposible por encima de **82° de Latitud** (regiones polares) debido a la insuficiente tasa terrestre horizontal.

## Modos de Operación (MSU - Unidad Selectora de Modo)

El selector de modo típicamente tiene las siguientes posiciones:

1.  **OFF**: Sistema apagado.
2.  **ALIGN**: Inicia el proceso de alineación y nivelación. Usado para realineación rápida o cuando no se desea apagado total.
3.  **NAV**: Modo de operación normal para vuelo. Proporciona todos los datos (Actitud, Rumbo, Posición, Velocidad).
4.  **ATT (Actitud)**: Modo de reversión.
    *   Se usa si falla el modo de Navegación o se pierde la alineación en vuelo.
    *   Proporciona solo **Actitud** (Cabeceo/Alabeo) y **Rumbo**.
    *   **Entrada de Rumbo**: En modo ATT, el rumbo muchas veces necesita ser ingresado/actualizado manualmente de forma periódica (ej. cada 15 min) o sincronizado.
    *   **Pérdida de Navegación**: Los datos de posición y velocidad terrestre (GS) no están disponibles.

## Monitoreo de Rendimiento (Deriva)

Los errores en los sistemas inerciales se acumulan con el tiempo (Deriva o Drift). Los pilotos verifican la precisión del sistema después del vuelo.

### Verificación Post-Vuelo
*   **Condición**: Aeronave estacionada y quieta.
*   **Velocidad Terrestre Residual (Residual Groundspeed)**: La lectura de Groundspeed (GS) debería ser idealmente **cero**. Una GS residual alta indica un error/deriva excesiva.
*   **Deriva de Posición**: Comparando la posición calculada con las coordenadas conocidas de la puerta de embarque.
    *   La deriva se mide en **NM/hora**.
    *   Cálculo: `Error Total de Posición (NM) / Tiempo de Vuelo (Horas)`.
    *   Los límites varían según la unidad, pero típicamente la deriva debe ser baja (ej. < 2 NM/hr para INS, significativamente mejor para IRS).

## Puntos Clave y Advertencias
*   **Movimiento de la Aeronave**: Si el avión se mueve durante la alineación, el proceso se reinicia o falla.
*   **Discrepancia de Latitud**: Si la latitud ingresada difiere significativamente de la latitud sensada, el sistema rechazará la alineación (luz de alineación parpadeando).
*   **Error de Longitud**: Ingresar una longitud incorrecta no es detectado por el sistema (ya que no puede sensar longitud) pero desplaza todo el mapa de navegación, resultando en un error de posición durante todo el vuelo.
*   **Realineación en Vuelo**: No es posible para calibración de posición/norte. Solo se puede activar el modo de Actitud (ATT) si se pierde NAV.
