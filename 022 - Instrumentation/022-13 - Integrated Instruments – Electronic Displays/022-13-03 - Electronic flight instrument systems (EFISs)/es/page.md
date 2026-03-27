---
title: "Sistemas EFIS: Modos PFD/ND y Lógica de Instrumentación de Reserva"
description: "Aprende la arquitectura EFIS, modos de presentación en PFD y ND, superposiciones del panel de control y operación ISIS ante fallos de pantallas primarias."
keywords:
    - "efis"
    - "pfd nd"
    - "flight level"
    - "minimum speed"
---

# Sistemas EFIS: Modos PFD/ND y Lógica de Instrumentación de Reserva

El **EFIS** reemplaza los instrumentos electromecánicos con pantallas CRT o LCD. El sistema típicamente consta de dos pantallas principales para cada piloto: el **PFD** (Primary Flight Display - Pantalla Principal de Vuelo) y el **ND** (Navigation Display - Pantalla de Navegación).

## Primary Flight Display (PFD)
Combina los instrumentos de vuelo de la "T Básica" en una sola pantalla dinámica.
*   **Disposición**:
    *   **Centro**: Indicador de Actitud (AI) con barras del Director de Vuelo (FD).
    *   **Izquierda**: Indicador de Velocidad (Cinta de Velocidad). Incluye bugs de velocidad ($V_1$, $V_R$, $V_2$), vectores de tendencia y número de Mach.
    *   **Derecha**: Altímetro (Cinta de Altitud) y Variómetro (VSI).
    *   **Abajo Centro**: Indicación de Rumbo/Derrota (segmento de Rosa de los Vientos).
    *   **Arriba**: **FMA** (Flight Mode Annunciator) - Muestra el estado del Piloto Automático/Mando de Gases.
*   **Radioaltímetro**: Se muestra por debajo de 2500 ft AGL.

## Navigation Display (ND) / EHSI
El ND muestra datos de navegación y puede operarse en varios modos seleccionados a través del **Panel de Control EFIS**.

### Modos de Visualización Comunes
| Modo | Descripción | Orientación | Características |
|---|---|---|---|
| **MAP / ARC** | Vista expandida (arco ~90°). Mapa móvil. | Rumbo o Derrota Arriba | Waypoints, Plan de Vuelo, **Meteorología**, **Terreno**, **Tráfico**. Modo de vuelo más común. |
| **VOR / ROSE** | Rosa completa de 360°. | Rumbo Arriba | Barra de desviación VOR (estilo RMI). Avión en el centro. |
| **APP / ILS** | Rosa completa o Expandida. | Rumbo Arriba | Desviación ILS (Loc/GS). |
| **PLAN** | Mapa estático. | **Norte Verdadero Arriba** | Usado para revisar el plan de vuelo (recorrer waypoints). **Sin Meteorología/Terreno**. |

### Centro (CTR) vs Expandido (EXP)
*   **CTR (Rosa Completa)**: Símbolo del avión en el centro. Vista de 360°.
*   **EXP (Expandido/Arco)**: Avión abajo. Sector de vista frontal. Mejor resolución hacia adelante.
*   **Radar Meteorológico (WXR)**: Típicamente **no** puede mostrarse en modos VOR/ILS de Rosa Completa o PLAN. Requiere un modo Expandido/Mapa.

## Panel de Control EFIS
Permite al piloto seleccionar:
*   **Modo**: MAP, VOR, APP, PLAN.
*   **Rango/Escala**: ej. 10, 20, 40, ... 640 NM.
*   **Superposiciones**: WXR (Meteorología), TERR (Terreno), TFC (Tráfico), WPT (Waypoints), ARPT (Aeropuertos), STA (Radioayudas).
*   **Ajuste Barométrico**: QNH/STD.

## Instrumentos de Reserva (ISIS)
En caso de fallo total del EFIS, se requieren **Instrumentos de Reserva (Standby)**.
*   **ISIS** (Integrated Standby Instrument System): Una sola pantalla electrónica pequeña que combina Actitud, Altitud y Velocidad.
*   **Independencia**: Opera con fuentes pitot/estáticas, giroscopios y suministros eléctricos independientes.
*   **Desafíos**: A menudo tienen mayores errores de paralaje, menor tamaño y son más difíciles de leer que las pantallas principales.
