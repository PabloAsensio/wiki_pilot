**Introducción**
Los controles de vuelo primarios (elevador, alerones y timón) son responsables de controlar la rotación de la aeronave sobre sus tres ejes. Dependiendo del tamaño y velocidad de la aeronave, estos controles pueden ser operados manualmente, asistidos por potencia o completamente motorizados.

## Tipos de Sistemas de Control

- **Controles Reversibles:**
    - **Características:** Existe un enlace mecánico directo que transmite efectivamente la fuerza en ambos sentidos. Una fuerza aplicada a los controles de cabina mueve la superficie de control, y las **cargas aerodinámicas sobre la superficie mueven los controles de cabina**.
    - **Retroalimentación (Feedback):** El piloto siente naturalmente la carga aerodinámica.
    - **Aplicación:** Se encuentra en sistemas manuales y parcialmente motorizados.
    - **Comportamiento en Tierra:** El viento que mueve la superficie de control **hará que los controles de cabina se muevan**.

- **Controles Irreversibles:**
    - **Características:** El sistema es **completamente motorizado** (hidráulico o fly-by-wire). Las entradas desde la cabina mueven válvulas o sensores que actúan sobre la superficie, pero las **fuerzas en la superficie no se transmiten de vuelta a la cabina**.
    - **Retroalimentación (Feedback):** No contiene **sentimiento natural**.
    - **Comportamiento en Tierra:** El viento que mueve la superficie de control (por ejemplo, el timón soplado a deflexión total) **NO causará movimiento de los controles de cabina** (pedales del timón).

## Tacto Artificial (Artificial Feel)

Dado que los sistemas irreversibles no proporcionan retroalimentación natural, se requiere una **Unidad de Tacto Artificial**.
- **Propósito:** Proporcionar al piloto resistencia táctil y fuerzas de centrado.
- **Función:** La fuerza aplicada a los controles de cabina debe ser proporcional a la **deflexión del control** y a la **velocidad de la aeronave** (presión dinámica).

## Comportamiento del Sistema de Compensación (Trim)

En sistemas completamente motorizados (irreversibles) con tacto artificial, la operación del compensador difiere según el eje:
- **Compensador de Elevador:** El compensado típicamente cambia la referencia para la unidad de tacto pero **no mueve la columna de control** a una nueva posición neutral. La posición de fuerza cero permanece centrada.
- **Compensador de Alerones y Timón:** El compensado usualmente **cambia la posición de fuerza cero** de los controles. La rueda de control o los pedales del timón se moverán físicamente en la dirección del compensador.

## Bloqueos de Ráfaga (Gust Locks)

Los bloqueos de ráfaga (internos o externos) se utilizan para proteger las superficies de control y los enlaces de daños causados por el viento cuando la aeronave está estacionada.
- **Requisito:** Deben existir precauciones de diseño (como enclavamientos mecánicos con los aceleradores) para **evitar que la aeronave despegue con los bloqueos de ráfaga activados**.
- **Relevancia:** Particularmente importante para sistemas de control **reversibles** donde el viento puede golpear fácilmente las superficies contra sus topes.

## Redundancia

Para garantizar la seguridad, los sistemas de control de vuelo emplean redundancia:
- **Múltiples Actuadores:** Uso de más de un actuador (a menudo alimentados por diferentes sistemas hidráulicos) por superficie de control.
- **Múltiples Superficies:** Uso de múltiples superficies para la misma función (por ejemplo, usar spoilers para asistir a los alerones para el control de alabeo).
