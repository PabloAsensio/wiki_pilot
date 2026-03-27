---
layout: default
title: "Future Air Navigation Systems (FANS): AFN, CPDLC y Contratos ADS-C"
description: "Aprende la arquitectura FANS 1/A para operaciones oceánicas y remotas, incluyendo logon AFN, mensajería CPDLC y vigilancia ADS-C por contrato."
keywords:
    - "cpdlc"
    - "ads-c"
    - "flight level"
    - "minimum speed"
parent: "022-10 - Communication Systems"
grand_parent: "022 - Instrumentation"
nav_order: 2
---

# Future Air Navigation Systems (FANS): AFN, CPDLC y Contratos ADS-C

## Concepto y Objetivos

**FANS** es una arquitectura de sistemas desarrollada por la OACI para mejorar las comunicaciones, navegación y vigilancia (CNS) para la gestión del tráfico aéreo.

- **Objetivo Principal**: Manejar el aumento del tráfico aéreo de manera segura y eficiente, particularmente en áreas oceánicas y remotas donde la cobertura de radar y el contacto directo por radio son limitados.
- **Cambio Clave**: Pasar de la comunicación por voz al **Enlace de Datos (Data Link)** digital.

## Aplicaciones Principales (FANS 1/A)

FANS 1/A es el paquete de aviónica típicamente instalado en aviones comerciales (Boeing/Airbus) para soportar estas funciones.

### 1. ATS Facility Notification (AFN)
También conocido como el **"Log On"**. Antes de usar los servicios FANS, la aeronave debe identificarse ante la Unidad de Servicios de Tránsito Aéreo (ATSU).
- **Proceso**: El piloto permite que el sistema del avión envíe un mensaje de "Log On" (generalmente vía MCDU).
- **Datos Transmitidos**:
    - Indicativo de llamada (Callsign).
    - **Capacidades de Data Link** (qué puede hacer el avión).
    - Información del Plan de Vuelo.
- **Resultado**: Establece el "apretón de manos" electrónico requerido para CPDLC y ADS-C.

### 2. CPDLC (Controller-Pilot Data Link Communications)
Sistema de enlace de datos bidireccional que permite el intercambio de mensajes de texto entre el piloto y el controlador aéreo.
- **Uso**: Solicitudes de autorización no urgentes, cambios de frecuencia y reportes.
- **Ventajas**:
    - **Reducción de Congestión en Frecuencia**: Libera canales de voz para comunicaciones críticas.
    - **Claridad**: Elimina acentos, estática y errores de colación (readback/hearback).
    - **Eficiencia**: Permite revisar e imprimir autorizaciones complejas (ej. "Ascienda para alcanzar FL350 para las 1230Z").

### 3. ADS-C (Automatic Dependent Surveillance - Contract)
Técnica de vigilancia donde la aeronave transmite automáticamente datos de posición derivados de sus sistemas de navegación a bordo (GPS/FMS) al centro de control (ATC).
- **"Contrato"**: La tasa de reporte es controlada por la estación terrestre (ATC), no por el piloto.
    - **Contrato Periódico**: Enviar posición cada X minutos/segundos.
    - **Contrato por Evento**: Enviar posición si cambia la altitud/rumbo o se pasa un waypoint.
    - **Contrato bajo Demanda**: Enviar posición inmediatamente al solicitarse.
- **Modo Emergencia**: Si se activa un MAYDAY, el sistema cambia a un contrato de reporte de alta frecuencia.

> **Nota**: No confundir ADS-C (Contrato Punto-a-Punto con ATC vía Satcom/VHF) con **ADS-B** (Broadcast/Radiodifusión a todos vía 1090MHz ES). FANS usa principalmente ADS-C.
