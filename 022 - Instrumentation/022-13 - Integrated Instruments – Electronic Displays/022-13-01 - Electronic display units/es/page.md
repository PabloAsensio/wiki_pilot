---
title: Electronic Display Units (EFIS Architecture)
---

Los sistemas modernos **EFIS** (Electronic Flight Instrument Systems) utilizan **Unidades de Visualización (DUs)** (pantallas CRT o LCD) para presentar la información de vuelo. Una característica clave es la **redundancia** e **intercambiabilidad** de las pantallas para asegurar que la información crítica permanezca disponible en caso de fallo de hardware.

### Disposición Típica (Airbus/Boeing)
*   **DU Exterior (Outboard)**: Generalmente el **PFD** (Primary Flight Display - Pantalla Principal de Vuelo).
*   **DU Interior (Inboard)**: Generalmente el **ND** (Navigation Display - Pantalla de Navegación).
*   **DUs Centrales**: Superior e Inferior para Motor/Sistemas (EICAS/ECAM).

### Lógica de Fallo de Pantalla (Conmutación Automática)
Dado que la información del **PFD** (Actitud, Velocidad, Altitud) es crítica para la seguridad del vuelo ("máxima importancia"):

1.  **Fallo del DU Exterior (Falla la pantalla del PFD)**:
    *   La **imagen del PFD se transfiere automáticamente** al **DU Interior** (pantalla del ND).
    *   La información del ND asume una prioridad menor y es desplazada (o puede seleccionarse en otra pantalla).
    *   *Principio*: Se pierde la pantalla de Navegación para salvar la Pantalla Principal de Vuelo.

2.  **Fallo del DU Interior (Falla la pantalla del ND)**:
    *   El PFD permanece en el DU Exterior.
    *   La pantalla del ND se queda en blanco (se pierde la info de ND en esa pantalla).

3.  **Fallo del DU Central Superior (Falla Motor/Avisos)**:
    *   La **pantalla Primaria de Motor/Avisos se transfiere automáticamente** al **DU Inferior**.
    *   La información que estaba en el DU Inferior (ej. parámetros secundarios, listas de chequeo) puede compactarse o desplazarse.

### Independencia
*   El lado del Capitán y del Primer Oficial son generalmente independientes para esta conmutación.
*   Si falla la pantalla PFD del Capitán, se cambia a la **pantalla ND del Capitán** (no a la del Copiloto).
