---
title: "Sistemas de Alerta de Vuelo (FWS): Prioridades, CWS y Respuesta de Tripulación"
description: "Aprende la arquitectura FWS, niveles de prioridad de alertas, canales visuales/auditivos y disciplina de cabina para gestionar advertencias de forma segura."
keywords:
    - "warning systems"
    - "master caution"
    - "flight level"
    - "minimum speed"
---

# Sistemas de Alerta de Vuelo (FWS): Prioridades, CWS y Respuesta de Tripulación

## Visión General del Sistema

El **Sistema de Alerta de Vuelo (FWS)** monitorea continuamente los sensores de la aeronave para detectar condiciones anormales. Utiliza una lógica interna para priorizar estas condiciones y presentarlas a la tripulación mediante medios visuales, auditivos y táctiles.

Las aeronaves modernas integran estas funciones en sistemas como **EICAS** (Sistema de Indicación de Motor y Alerta a la Tripulación) en Boeing o **ECAM** (Monitor Centralizado Electrónico de Aeronave) en Airbus.

## Jerarquías de Alerta

Las alertas se clasifican típicamente en tres niveles de prioridad:

| Nivel | Prioridad | Visual | Auditivo | Acción de la Tripulación | Ejemplos |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Nivel A** | **Advertencia (Warning)** | Master Warning **Rojo** + Mensaje | Continuo (Campana, Sirena, Voz) | Reconocimiento **inmediato** y acción correctiva. | Fuego de Motor, Exceso de Velocidad, Entrada en Pérdida, Altitud de Cabina, Configuración. |
| **Nivel B** | **Precaución (Caution)** | Master Caution **Ámbar** + Mensaje | Tono Único/Repetido (p. ej., campana simple) | **Conciencia inmediata**, acción posterior. | Fallo Sist. Hidráulico, Fallo Generador, Combustible Bajo, Frenos Calientes. |
| **Nivel C** | **Aviso (Advisory)** | Cualquiera (p. ej., Blanco, Cian) excepto Rojo/Verde | Ninguno | **Conciencia**. | Estado del Sistema, Mensajes de Memo. |

## Procedimiento de Manejo

Una disciplina estándar para manejar alertas (especialmente Precauciones/Advertencias) es:

1.  **Reconocer (Acknowledge)** el fallo (Identificar la luz/mensaje).
2.  **Silenciar (Silence)** la alerta auditiva (si es aplicable/permitido).
3.  **Iniciar (Initiate)** el procedimiento apropiado (Leer lista de verificación ECAM/EICAS).
4.  **Avisar (Advise)** al ATC (si el fallo afecta el perfil de vuelo o la capacidad).

## Componentes

### Sistema Central de Alerta (CWS)
*   **Panel Anunciador:** Un panel que contiene luces específicas para varios sistemas, centralizado para minimizar el tiempo de escaneo.
*   **Luces Master Warning/Caution:** Ubicadas en el campo de visión principal del piloto (glareshield) para llamar la atención hacia el CWS o EICAS/ECAM.

### Alertas Auditivas y Táctiles
*   **Auditivas:** Diseñadas para atraer la atención a través de un canal sensorial diferente.
    *   **Fuego:** Campana.
    *   **Exceso de Velocidad/Configuración:** Sirena o batidero (clacker).
    *   **Desconexión AP:** Carga de caballería, lamento o tono.
*   **Táctiles:**
    *   **Stick Shaker:** Vibración de la columna de control para Advertencia de Entrada en Pérdida.

## Escenarios Específicos
*   **Desconexión del Piloto Automático:** La desconexión deliberada o no comandada activa una luz de **Advertencia Roja** y una alerta **Auditiva Continua** hasta que es reconocida (silenciada) por la tripulación.
*   **Exceso de Velocidad:** Exceder VMO/MMO activa un **Master Warning** y una alerta auditiva específica (sirena/clacker de overspeed).
