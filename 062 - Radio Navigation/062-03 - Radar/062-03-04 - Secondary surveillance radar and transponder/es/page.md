---
title: "Radar Secundario y Transpondedor"
description: "Estudia operación de SSR y transpondedor, modos y uso en vigilancia ATC."
keywords:
    - "radar secundario de vigilancia"
    - "modos de transpondedor"
    - "vigilancia atc"
---

# Radar Secundario y Transpondedor

El **SSR (Secondary Surveillance Radar)** es un sistema de radar que depende de la cooperación de un equipo a bordo de la aeronave llamado **transpondedor**. A diferencia del radar primario, que funciona por reflexión pasiva, el SSR utiliza un sistema de interrogación y respuesta activa.

![Panel de Transpondedor de Aviación](https://upload.wikimedia.org/wikipedia/commons/c/cc/Transponder_in_Private_Aircraft.jpg)

## Principios de Operación

1.  **Interrogación**: La estación terrestre (interrogador) transmite pulsos codificados en la frecuencia **1030 MHz**.
2.  **Respuesta**: El transpondedor de la aeronave recibe la interrogación y transmite una respuesta codificada en la frecuencia **1090 MHz**.

### Ventajas sobre el Radar Primario
*   **Menor Potencia Requerida**: Como la señal de respuesta es generada activamente por el transpondedor (no es un eco), la señal es mucho más fuerte y requiere menos potencia de transmisión en tierra para lograr el mismo alcance.
*   **Mayor Información**: Permite transmitir datos como identificación, altitud y otros parámetros de vuelo.
*   **Sin Clutter**: No se ve afectado por ecos del terreno o meteorología.

## Modos de Operación

### Modo A (Identificación)
*   Proporciona un código de identificación de 4 dígitos (**Squawk Code**).
*   El código es octal (dígitos 0-7), permitiendo 4096 combinaciones posibles ($8^4$).
*   Interrogación: Pulsos P1 y P3 separados por **8 µs**.

### Modo C (Altitud)
*   Proporciona la **altitud de presión** (referencia 1013 hPa) en incrementos de **100 pies**.
*   Interrogación: Pulsos P1 y P3 separados por **21 µs**.

### Modo S (Selectivo)
*   **Direcciónamiento Selectivo**: Cada aeronave tiene una dirección única de **24 bits** (más de 16 millones de combinaciones), permitiendo interrogar a una aeronave específica.
*   **Datos Mejorados**: Permite enlace de datos (datalink) y transmisión de parámetros de vuelo (ELS/EHS) como callsign, velocidad, rumbo, etc.
*   **Precisión de Altitud**: Reporta altitud en incrementos de **25 pies**.
*   **Compatibilidad**: Es totalmente compatible con los modos A y C.
*   **TCAS**: Es fundamental para el funcionamiento del sistema anticolisión TCAS.

## Características Técnicas

### Supresión de Lóbulos Laterales (SLS)
Para evitar que el transpondedor responda a interrogaciones provenientes de los lóbulos laterales de la antena (que darían una posición errónea):
*   Se transmite un pulso de control **P2** 2 µs después de P1.
*   Si el transpondedor recibe P2 con mayor potencia que P1, sabe que está en un lóbulo lateral y **no responde**.

### Función IDENT (SPI)
Cuando el controlador solicita "Squawk Ident", el piloto pulsa el botón IDENT.
*   El transpondedor añade un pulso especial (SPI) a su respuesta durante unos 20 segundos.
*   Esto hace que el eco de la aeronave **parpadee o resalte** en la pantalla del controlador, facilitando su identificación positiva.

## Códigos de Emergencia
Aunque no se detallan en el texto fuente, es conocimiento estándar asociado al Modo A:
*   7700: Emergencia general.
*   7600: Fallo de comunicaciones.
*   7500: Interferencia ilícita (secuestro).
