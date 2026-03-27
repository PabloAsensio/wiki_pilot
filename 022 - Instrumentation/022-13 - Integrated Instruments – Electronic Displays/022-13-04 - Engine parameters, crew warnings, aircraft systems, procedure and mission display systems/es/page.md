---
title: "EICAS y ECAM: Parámetros de Motor, Alertas y Checklists Electrónicas"
description: "Comprende la filosofía de presentación EICAS/ECAM, la integración de alertas y las limitaciones de checklists que exigen juicio técnico y disciplina CRM."
keywords:
    - "eicas"
    - "ecam"
    - "flight level"
    - "minimum speed"
---

# EICAS y ECAM: Parámetros de Motor, Alertas y Checklists Electrónicas

Las aeronaves modernas utilizan sistemas electrónicos para monitorizar los parámetros del motor, sistemas de la aeronave y proporcionar alertas a la tripulación. Los dos sistemas principales son **EICAS** (Boeing) y **ECAM** (Airbus).

## Visión General del Sistema
| Característica | **EICAS** (Boeing) | **ECAM** (Airbus) |
|---|---|---|
| **Pantalla Primaria** | Pantalla Superior | E/WD (Engine/Warning Display) |
| **Contenido** | N1/EPR, EGT, Advertencias, Precauciones | N1/EPR, EGT, Combustible, Flaps, Advertencias, Memos |
| **Pantalla Secundaria** | Pantalla Inferior | SD (System/Display) |
| **Contenido** | Hidráulica, Presurización, Info Secundaria Motor, Estado | Sinópticos del Sistema (Esquemas), Estado |

## Modos de Visualización EICAS
1.  **Operacional**: Parámetros del sistema en tiempo real seleccionados por la tripulación.
2.  **Estado (Status)**: Usado para el despacho (MEL). Muestra posiciones de controles de vuelo, cantidad de hidráulico, oxígeno, etc.
3.  **Mantenimiento**: Solo uso en tierra para solución de problemas.

## Listas de Chequeo Electrónicas (ECL) y Procedimientos
Estos sistemas muestran automáticamente la lista de chequeo apropiada cuando los sensores detectan un fallo.

### Limitaciones y Juicio del Piloto
El ordenador activa las listas basándose en **umbrales de sensores**, pero carece de "contexto" o conciencia del daño físico.
*   **Fuga de Combustible**: Si una fuga causa un desequilibrio, el sistema puede activar una lista de "Desequilibrio de Combustible" pidiendo **Abrir Alimentación Cruzada (Crossfeed)**.
    *   *Peligro*: Hacerlo bombearía el combustible bueno por la borda a través de la fuga.
    *   *Acción*: Los pilotos deben diagnosticar la fuga (Combustible Usado vs A Bordo) antes de seguir la ECL.
*   **Daño en el Motor**: Si un motor falla por daño severo (ej. vibración, explosión).
    *   *Peligro*: La ECL para un apagado simple podría sugerir un "Reencendido" (Relight).
    *   *Acción*: No intentar reencender un motor dañado.

## CRM y Procedimientos Operativos Estándar (SOPs)
Para prevenir errores irreversibles (como apagar el motor equivocado):
1.  **Confirmar el Fallo**: Ambos pilotos deben estar de acuerdo en el diagnóstico.
2.  **Leer y Hacer (Read & Do)**: Seguir la lista de chequeo lenta y metódicamente.
3.  **Interruptores con Guarda / Palancas de Empuje**: El Piloto Monitorizando (PM) **nunca** debe mover una palanca de empuje, master de motor o interruptor con guarda sin la **confirmación** explícita del Piloto Volando (PF).
