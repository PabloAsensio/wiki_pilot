---
title: Radionavegacion: Sistema de Aterrizaje por Microondas (MLS) en Aviacion
description: Estudia el sistema MLS en aviacion, su guiado de aproximacion y referencias de frecuencia.
keywords:
  - mls aviacion
  - microwave landing system
  - sistema de aterrizaje por microondas
  - aproximacion mls
  - radioayudas de aproximacion
---

# Radionavegacion: Sistema de Aterrizaje por Microondas (MLS) en Aviacion

El **MLS (Microwave Landing System)** es un sistema de aproximación de precisión diseñado para superar las limitaciones del ILS y ofrecer mayor flexibilidad. Aunque tecnológicamente superior, su implementación ha sido limitada debido al auge de los sistemas basados en satélites (GNSS).

## Características Principales

- **Frecuencia:** Opera en la banda **SHF (5.031 - 5.091 GHz)**, con **200 canales** disponibles.
- **Principio de Operación:** Utiliza el **Time Reference Scanning Beam (TRSB)**. Un haz barre el espacio lateralmente (azimut) y verticalmente (elevación). El receptor mide el tiempo entre los barridos "hacia" y "desde" para calcular la posición angular.
- **Inmunidad:** Al operar en SHF y usar haces estrechos, es prácticamente inmune a las reflexiones de edificios o terreno (**multipath**), lo que permite su instalación en lugares donde el ILS no es viable.

## Componentes del Sistema

1.  **Estación de Azimut:** Proporciona guía lateral (±40° del eje).
2.  **Estación de Elevación:** Proporciona guía vertical (ajustable de 0.9° a 20°).
3.  **DME/P (Precision DME):** Un DME más preciso que el estándar, esencial para definir trayectorias en 3D.
4.  **Comunicaciones de Datos:** Transmite información de la estación a la aeronave.

## Ventajas sobre el ILS

- **Aproximaciones Flexibles:** Permite trayectorias **curvas y segmentadas**, lo que mejora la gestión del tráfico y reduce el ruido.
- **Selección de Senda:** El piloto puede seleccionar el ángulo de planeo deseado.
- **Instalación:** No requiere nivelar grandes extensiones de terreno frente a las antenas.
- **Canales:** Mayor número de canales para evitar interferencias entre aeropuertos cercanos.

## Uso a Bordo

- **MMR (Multi-Mode Receiver):** Las aeronaves modernas utilizan un receptor único capaz de procesar señales de ILS, MLS y GPS, simplificando la interfaz para el piloto.
- **Presentación:** La información se presenta de forma similar al ILS (barras de desviación), pero calculada por ordenador para seguir el segmento programado.
- **DME/P:** Sin un DME/P operativo, el MLS solo puede proporcionar aproximaciones directas (tipo ILS), perdiendo la capacidad de realizar aproximaciones curvas o segmentadas.
