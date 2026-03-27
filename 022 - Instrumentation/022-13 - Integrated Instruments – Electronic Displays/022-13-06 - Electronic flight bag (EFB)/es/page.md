---
title: "Electronic Flight Bag (EFB): Clases, Funciones y Riesgos Operacionales"
description: "Estudia la funcionalidad del EFB, clases de hardware/software, límites de certificación y rutas de error operacional por entrada de datos incorrecta."
keywords:
    - "efb"
    - "performance calculation"
    - "flight level"
    - "minimum speed"
---

# Electronic Flight Bag (EFB): Clases, Funciones y Riesgos Operacionales

Un **EFB** (Cartera de Vuelo Electrónica) es un sistema electrónico utilizado por la tripulación de vuelo para realizar tareas que anteriormente se hacían con documentos de papel y herramientas manuales.

## Funcionalidad
*   **Documentación**: Almacenamiento digital de manuales (FCOM, MEL, etc.).
*   **Navegación**: Cartas Aeronáuticas (En ruta, Fichas de Aproximación), Mapas Móviles.
*   **Performance**: Cálculo de velocidades y límites de Despegue/Aterrizaje.
*   **Masa y Centrado**: Cálculos de hoja de carga.
*   *Nota*: El EFB es **distinto** del FMS (Sistema de Gestión de Vuelo) y de los sistemas de alerta (ECAM/EICAS). Típicamente **no** gestiona ACARS/CPDLC ni muestra advertencias de sistemas directamente.

## Clasificaciones de Hardware
1.  **EFB Portátil (PED)**:
    *   No es parte de la configuración certificada de la aeronave.
    *   Puede usarse dentro/fuera de la aeronave.
    *   Material de referencia solamente; requiere comprobación cruzada.
    *   **Montaje**: Debe poder retirarse **sin herramientas**.
2.  **EFB Instalado**:
    *   Certificado como parte de la aviónica de la aeronave.
    *   Incluido en la **MEL** (Lista de Equipo Mínimo) si falla.
    *   Integrado en la cabina de vuelo (pantallas, alimentación, datos).

## Clasificaciones de Software (Aplicaciones)
*   **Tipo A**: El mal funcionamiento/mal uso **no tiene efecto en la seguridad**.
    *   *Ejemplos*: Visores HTML/PDF para manuales generales, documentos no interactivos.
*   **Tipo B**: El mal funcionamiento/mal uso tiene un **efecto menor en la seguridad**.
    *   *Ejemplos*: Apps de cálculo de performance, Cartas Electrónicas (Zoom/Pan), Listas de chequeo interactivas.
    *   *Restricción*: No debe reemplazar un sistema requerido por regulaciones de aeronavegabilidad (ej. no puede reemplazar al PFD/ND).

## Problemas Operacionales
*   **Error de Entrada de Datos**: "Basura entra, basura sale". Si un piloto introduce datos de peso/meteorología incorrectos, el EFB genera **velocidades/límites incorrectos**.
*   **Fallo**: La pérdida de un EFB (especialmente en una cabina "sin papel") implica la pérdida de acceso a cartas, manuales y datos de performance. Se requiere redundancia (2º EFB o respaldo en papel).
