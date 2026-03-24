---
title: "Generalidades, Definiciones y Aplicaciones Básicas"
description: "Conceptos eléctricos básicos, unidades, ley de Ohm, protección de circuitos, electricidad estática y puertas lógicas."
---

# Generalidades, Definiciones y Aplicaciones Básicas

## Unidades y Definiciones Básicas

Las unidades fundamentales en los sistemas eléctricos son:

*   **Corriente ($I$)**: El flujo de carga eléctrica (electrones) a través de un conductor. Se mide en **Amperios (A)**.
*   **Voltaje ($V$)**: La diferencia de potencial entre dos puntos. Se mide en **Voltios (V)**.
*   **Resistencia ($R$)**: La oposición al flujo de corriente. Se mide en **Ohmios ($\Omega$)**.
*   **Potencia ($P$)**: La tasa de realización de trabajo o transferencia de energía. Se mide en **Vatios (W)**.
    *   $P = V \times I$
    *   También definida como Energía Transferida / Tiempo (Julios por segundo).
*   **Frecuencia ($f$)**: El número de ciclos por unidad de tiempo para corriente alterna. Se mide en **Hertzios (Hz)**.
*   **Trabajo**: Se mide en **Julios (J)**.

### Ley de Ohm

La ley de Ohm establece que la corriente que pasa por un conductor entre dos puntos es proporcional al voltaje a través de esos dos puntos.

$$V = I \times R$$

*   El voltaje es proporcional a la corriente.
*   Si el voltaje aumenta (con resistencia constante), la corriente aumenta.

### Protección de Circuitos

Los dispositivos se instalan para proteger los circuitos de la **sobrecorriente**, que es una situación donde la corriente excede la clasificación de seguridad del conductor, intentando generar calor excesivo y causando potencialmente un **incendio eléctrico**.

#### Fusibles
Un fusible es un dispositivo de protección térmica que contiene una tira que se funde ("salta") cuando la corriente excede un valor específico.
*   **Función**: Protege cables y componentes.
*   **Reemplazo**: Debe reemplazarse con un fusible del *amperaje, voltaje y tipo correctos* (rápido o lento).
*   **Clasificación Incorrecta**: Instalar un fusible de mayor amperaje permite que persista la sobrecorriente, creando un grave riesgo de incendio. En un sistema sano, un fusible incorrecto no causa problemas inmediatos, pero no ofrece protección durante un fallo.
*   **Limitadores de Corriente**: Fusibles de alto amperaje (a menudo para salidas de TRU) diseñados para soportar sobrecargas a corto plazo pero romperse en fallos sostenidos.

#### Disyuntores (Circuit Breakers - CB)
Un dispositivo rearmable que combina la función de un fusible y un interruptor.
*   **CB Térmico**: Se basa en una tira bimetálica que se calienta y se dobla para disparar el pestillo. Adecuado para sobrecorrientes pequeñas y prolongadas.
*   **CB Magnético**: Usa un electroimán para dispararse inmediatamente ante una subida de corriente alta. Mejor para respuesta rápida.
*   **Reglas de Rearme**:
    *   Si un CB salta, puede rearmarse **una vez** después de un período de enfriamiento (si es necesario).
    *   Si salta por segunda vez, **no** debe rearmarse de nuevo (indica un fallo permanente).
    *   El rearme repetido daña el sistema y aumenta el riesgo de incendio.
    *   En vuelo, un CB disparado generalmente solo se rearma si el sistema es esencial para la seguridad.

### Electricidad Estática y Conexión a Masa (Bonding)

La fricción entre la piel de la aeronave y las partículas de aire genera electricidad estática.

*   **Bonding (Conexión equipotencial)**: La conexión de todos los componentes metálicos de la aeronave con tiras de alambre flexibles.
    *   **Propósito**: Asegura un **potencial eléctrico igual** en toda la aeronave (diferencia de voltaje cero).
    *   **Previene**: Chispas entre componentes (peligro de incendio) y ruido eléctrico.
    *   También proporciona un camino de retorno para la corriente (retorno a tierra).
*   **Descargadores Estáticos (Static Wicks)**: Varillas conductoras en los bordes de salida.
    *   **Propósito**: Disipar la carga estática de vuelta a la atmósfera.
    *   **Fallo**: La falta de descargadores puede causar interferencia de radio (ruido estático en comunicaciones) y pérdida de comunicación.

### Estándares de Potencia AC

Las aeronaves grandes modernas suelen utilizar generadores de Corriente Alterna (AC).
*   **Valores Estándar**: **115/200 Voltios**, **trifásica**, **400 Hz**.
*   **Frecuencia**: 400 ciclos por segundo. La alta frecuencia permite generadores y transformadores más ligeros (eficientes para la aeronáutica).

### Puertas Lógicas

Los circuitos lógicos permiten la toma de decisiones complejas en los sistemas.

*   **Puerta AND**: La salida es 1 solo si **TODAS** las entradas son 1.
*   **Puerta OR**: La salida es 1 si **CUALQUIER** entrada es 1.
*   **Puerta NOT**: Invierte la entrada (1 se convierte en 0).
*   **Puerta NAND**: AND seguido de NOT.
*   **Puerta NOR**: OR seguido de NOT.

### Interferencia Electromagnética (EMI)

La corriente que fluye a través de un alambre crea un campo magnético que puede inducir señales no deseadas en alambres cercanos (diafonía/interferencia).

*   **Apantallamiento (Shielding/Screening)**: Una malla conductora envuelta alrededor del alambre.
*   **Función**: Bloquea la EMI para salir o entrar al alambre.
*   **Resultado**: Previene la interferencia con otros sistemas (por ejemplo, radios).

### Condensadores e Inductores (General)

*   **Condensador**: Almacena energía en un campo eléctrico. En circuitos AC, la corriente adelanta al voltaje. La alta frecuencia reduce la reactancia capacitiva (la corriente aumenta).
*   **Fuerza de Lorentz**: Fuerza ejercida sobre una partícula cargada que se mueve perpendicularmente a un campo magnético.
