---
title: "ACAS/TCAS: Avisos de Tráfico, Resoluciones e Inhibiciones"
description: "Comprende la lógica de vigilancia ACAS/TCAS, simbología TA/RA, maniobras verticales coordinadas, inhibiciones a baja altura y secuencia de respuesta."
keywords:
    - "tcas"
    - "acas"
    - "traffic advisory"
    - "resolution advisory"
---

# ACAS/TCAS: Avisos de Tráfico, Resoluciones e Inhibiciones

**ACAS** (Airborne Collision Avoidance System - Sistema Anticolisión de A bordo) es el estándar de la OACI para sistemas diseñados para prevenir colisiones en el aire. **TCAS II** (Traffic Alert and Collision Avoidance System) es el equipo que cumple con este estándar.
*   **Principio**: Opera independientemente del ATC en tierra. Utiliza interrogaciones de transpondedor (Modo C o S) para detectar aeronaves cercanas.
*   **Requisito**: Obligatorio para aviones de turbina > 5.700 kg o > 19 pasajeros.

## Equipo y Operación
El TCAS II interroga los transpondedores de otras aeronaves para determinar:
1.  **Distancia (Range)**: Por el retardo de tiempo de la respuesta.
2.  **Marcación (Bearing)**: Usando antenas direccionales.
3.  **Altitud**: De la respuesta en Modo C/S (altitud de presión).

*   **Solo Guía Vertical**: El TCAS II proporciona avisos de resolución (RAs) solo en el **plano vertical** (ascender/descender). No emite comandos de viraje.
*   **Coordinación**: Si ambas aeronaves tienen TCAS II, coordinan sus maniobras a través del enlace de datos Modo S para asegurar maniobras complementarias (ej. uno asciende, el otro desciende).

## Simbología en Pantalla
El tráfico se muestra en la Pantalla de Navegación (ND) o en un IVSI dedicado (Variómetro Instantáneo).

| Símbolo | Descripción | Significado |
|---|---|---|
| **Rombo Cian/Blanco Hueco** | Otro Tráfico | Tráfico detectado pero no es amenaza actual (> 6 NM o > 1200 ft vertical). |
| **Rombo Cian/Blanco Sólido** | Tráfico Próximo | Tráfico cercano (< 6 NM y < 1200 ft vertical) pero aún no es amenaza. |
| **Círculo Ámbar Sólido** | **Aviso de Tráfico (TA)** | Amenaza potencial (~40 seg al CPA). "Tráfico, Tráfico". Búsqueda visual requerida. |
| **Cuadrado Rojo Sólido** | **Aviso de Resolución (RA)** | Amenaza de colisión (~25 seg al CPA). Maniobra vertical inmediata requerida. |

*   **Etiqueta de Datos**: Muestra la altitud relativa en cientos de pies (ej. `+10` es 1000 ft por encima) y una flecha de tendencia si asciende/desciende > 500 fpm.

## Alertas y Acciones del Piloto
1.  **Aviso de Tráfico (TA)**: "TRAFFIC, TRAFFIC".
    *   **Acción**: **No** maniobrar basándose solo en un TA. Buscar visualmente al intruso. Prepararse para un posible RA.
2.  **Aviso de Resolución (RA)**: ej. "CLIMB, CLIMB", "DESCEND, DESCEND", "MONITOR VERTICAL SPEED".
    *   **Acción**:
        *   **Piloto Automático**: Desconectar inmediatamente.
        *   **Volar**: Seguir el arco verde / Evitar el arco rojo en el variómetro (VSI).
        *   **ATC**: Notificar tan pronto como sea posible ("TCAS RA").
        *   **Libre de Conflicto**: Volver a la autorización solo cuando se escuche "CLEAR OF CONFLICT".

## Inhibiciones y Limitaciones
*   **Sin Datos de Altitud**: Si un intruso tiene transpondedor Modo A (sin reporte de altitud), el TCAS no puede generar un RA (separación vertical desconocida), solo un TA (marcación/distancia conocidas).
*   **Inhibiciones a Baja Altitud**:
    *   **< 1000 ft (aprox)**: Modo "TA ONLY" generalmente activo (RAs de descenso inhibidos para evitar volar hacia el terreno).
    *   **< 1450 ft**: "INCREASE DESCENT" inhibido.
    *   **< 400 ft**: Todas las alertas inhibidas.
*   **Rendimiento**: Los RAs de "CLIMB" pueden inhibirse a grandes altitudes (límite de rendimiento) o con tren/flaps extendidos (límite de configuración).
