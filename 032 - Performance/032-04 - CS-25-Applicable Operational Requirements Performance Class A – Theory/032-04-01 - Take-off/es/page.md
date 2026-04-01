---
title: "Performance Clase A (CS-25): Teoría de despegue"
description: "Análisis detallado de velocidades de despegue, distancias y escenarios de fallo de motor para aviones Clase A."
keywords: ["Clase A", "despegue", "V1", "VR", "V2", "ASDR", "TODR", "TORR", "campo equilibrado"]
---

# Performance Clase A (CS-25): Teoría de despegue


## Velocidades Clave

La performance de Clase A se define por velocidades críticas:
*   **$V_1$ (Velocidad de Decisión)**: La velocidad máxima a la cual el piloto debe tomar la primera acción para detener la aeronave dentro de la distancia de aceleración-parada. También es la velocidad mínima a la cual la aeronave puede continuar el despegue tras un fallo de motor.
*   **$V_R$ (Velocidad de Rotación)**: La velocidad a la cual se inicia la rotación. $V_R \ge V_1$.
*   **$V_2$ (Velocidad de Seguridad al Despegue)**: La velocidad objetivo a alcanzar a la altura de pantalla (35 pies) con un motor inoperativo. Asegura performance de ascenso y controlabilidad.
*   **$V_{MCG}$ (Velocidad Mínima de Control en Tierra)**: Velocidad mínima para mantener el control direccional en tierra usando solo controles aerodinámicos (timón) tras un fallo de motor. $V_1 \ge V_{MCG}$.
*   **$V_{MCA}$ (Velocidad Mínima de Control en Aire)**: Velocidad mínima para mantener el control direccional en el aire. $V_2 \ge 1.1 V_{MCA}$.

## Distancias Requeridas

![Diagrama de distancias declaradas](https://upload.wikimedia.org/wikipedia/commons/0/04/Aim_fig_4-3-5_Declared_Distances_with_Full-Standard_Runway_Safety_Areas%2C_Runway_Object_Free_areas%2C_and_Runway_Protection_Zones.jpg)

### Distancia de Despegue Requerida (TODR)
La distancia horizontal desde la suelta de frenos hasta el punto donde la aeronave alcanza una altura de pantalla de **35 pies**.
*   **Condición**: La mayor de:
    1.  **OEI**: Distancia con fallo de motor crítico en $V_{EF}$ (justo antes de $V_1$).
    2.  **AEO**: Distancia con todos los motores operativos $\times 1.15$.

### Distancia de Aceleración-Parada Requerida (ASDR)
La distancia para acelerar a $V_1$, experimentar un fallo de motor, reconocerlo (1 segundo) y llevar la aeronave a una parada completa.
*   **Condición**: La mayor de:
    1.  **OEI**: Parada con un motor fallado y empuje inverso (si está acreditado, usualmente no en pista seca).
    2.  **AEO**: Parada con todos los motores operativos (Despegue Rechazado por otras razones).

### Carrera de Despegue Requerida (TORR)
La distancia para acelerar hasta el despegue (Lift-off) más una porción de la distancia en el aire hasta la altura de pantalla.
*   Relevante cuando la pista tiene una **Zona Libre de Obstáculos (Clearway)**.
*   **OEI**: Carrera hasta el punto medio entre LOF y 35 pies.
*   **AEO**: Carrera hasta el punto medio entre LOF y 35 pies $\times 1.15$.

## Longitud de Campo Equilibrada (Balanced Field)
Una condición donde **TODR = ASDR**.
*   Ocurre a un valor específico de $V_1$.
*   Si $V_1$ es menor, ASDR es más corta pero TODR es más larga.
*   Si $V_1$ es mayor, TODR es más corta pero ASDR es más larga.
*   La Longitud de Campo Equilibrada es la longitud de campo mínima requerida para un peso dado si $V_1$ está optimizada.
