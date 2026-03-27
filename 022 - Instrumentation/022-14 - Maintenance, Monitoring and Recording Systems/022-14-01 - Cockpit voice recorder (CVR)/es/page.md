---
title: "Cockpit Voice Recorder (CVR): Alcance de Grabación, Activación y Supervivencia"
description: "Aprende la arquitectura del CVR, lógica de activación, canales de audio obligatorios y características de supervivencia para investigación de accidentes."
keywords:
    - "cvr"
    - "flight recorder"
    - "flight level"
    - "minimum speed"
---

# Cockpit Voice Recorder (CVR): Alcance de Grabación, Activación y Supervivencia

El **CVR** está diseñado para grabar el entorno auditivo de la cabina de vuelo para asistir en investigaciones de accidentes.

## Operación y Capacidad
*   **Duración de Grabación**: Históricamente preserva las **últimas 2 horas** de grabación (grabación en bucle). Las nuevas regulaciones a menudo exigen duraciones más largas (ej. 25 horas) para aeronaves modernas.
*   **Activación**: Se energiza automáticamente:
    *   En vuelo.
    *   En tierra con al menos **un motor en marcha**.
*   **Componentes**:
    *   **Micrófono de Área**: Típicamente ubicado en el panel superior (overhead) para capturar el sonido general de la cabina (interruptores, alertas, conversaciones).
    *   **Registrador a Prueba de Impactos**: Alojado en la sección de cola para máxima supervivencia, equipado con una **Baliza de Localización Subacuática (ULB)**.
    *   **Panel de Control**: Incluye un botón de prueba y un **Botón de Evento** para marcar momentos específicos en la cinta para una recuperación rápida.

## Información Grabada
Según **CS-25** / **EASA AIR OPS**, el CVR debe grabar:
1.  **Comunicaciones de Radio**: Transmitidas y recibidas.
2.  **Entorno Aural**: A través del **Micrófono de Área** (sonidos de la cabina).
3.  **Interfono**: Comunicaciones entre miembros de la tripulación de vuelo.
4.  **Ayudas a la Navegación**: Identificadores de audio (código Morse) de las radios de navegación.
5.  **Megafonía (PA)**: Anuncios realizados por la tripulación de vuelo.

*   *Nota*: **No** graba típicamente las comunicaciones entre auxiliares de vuelo (estaciones entre cabinas) a menos que llamen a la cabina de pilotos.
