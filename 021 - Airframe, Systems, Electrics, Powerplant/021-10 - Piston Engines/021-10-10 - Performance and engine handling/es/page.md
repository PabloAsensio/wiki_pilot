# Rendimiento y Manejo del Motor

## Factores de Rendimiento del Motor

La potencia de salida de un motor de pistón depende de varios factores:
*   **Cilindrada**: Tamaño del motor.
*   **RPM**: Velocidad de rotación.
*   **Presión Absoluta del Colector (MAP)**: Presión de la mezcla aire/combustible disponible para los cilindros.
*   **Densidad del Aire**:
    *   **Altitud**: Al aumentar la altitud, la densidad disminuye, reduciendo la potencia en motores de aspiración normal (atmosféricos).
    *   **Temperatura**: Mayor temperatura reduce la densidad del aire, reduciendo la potencia.
    *   **Humedad**: La alta humedad desplaza moléculas de aire seco por vapor de agua menos denso, reduciendo la densidad y la potencia. **La humedad afecta a los motores de pistón más significativamente que a los de turbina.**

## Turbocompresión (Aumento de Potencia)

Para mantener la potencia en altitud, se utiliza un **Turbocompresor**.
*   **Principio**: Usa la energía de los gases de escape para mover un compresor, que aumenta la presión (y densidad) del aire de admisión.
*   **Componentes**:
    *   **Turbina**: Impulsada por los gases de escape.
    *   **Compresor**: Impulsado por la turbina mediante un eje; comprime el aire de admisión (típicamente centrífugo).
    *   **Válvula de descarga (Wastegate)**: Controla la cantidad de gases de escape que van a la turbina.
        *   **Cerrada**: Máximo escape a la turbina -> Altas RPM de turbina -> **Máximo empuje (Boost)**.
        *   **Abierta**: El escape evita la turbina -> Bajas RPM de turbina -> Bajo empuje.
        *   Controlada por un actuador que sensa la MAP.
    *   **Intercooler**: Enfría el aire comprimido para aumentar aún más su densidad y **prevenir la detonación**.
*   **Tipos**:
    *   **Potenciado en Altitud (Altitude-Boosted)**: Mantiene la potencia a nivel del mar hasta una altitud mayor (Altitud Nominal). Evita la pérdida de potencia durante el ascenso.
    *   **Potenciado en Tierra (Ground-Boosted)**: Aumenta la potencia más allá de los límites normales a nivel del mar (menos común en aviación por el estrés en el motor).

## Control Digital del Motor de Autoridad Total (FADEC)

**FADEC** es un sistema electrónico que gestiona todas las funciones del motor.
*   **Control**: Operación con una sola palanca (Palanca de potencia). Sin palancas separadas de mezcla o hélice.
*   **Funciones**: Controla la inyección de combustible, el **tiempol de encendido (ignition timing)** (una mejora importante de eficiencia sobre los sistemas mecánicos) y el paso de la hélice.
*   **Redundancia**: Para prevenir la pérdida total de potencia, los sistemas FADEC tienen **dos canales separados e idénticos** (ECUs) y a menudo una fuente de energía de respaldo.
*   **Ventajas**: Eficiencia óptima, protección de límites del motor, reducción de carga de trabajo del piloto, diagnóstico fácil.
*   **Desventajas**: Complejidad, dependencia de la energía eléctrica.

## Manejo Operacional

*   **De Ascenso a Crucero**: Nivelar implica reducir potencia.
    *   **Orden**: Reducir **Presión de Admisión (MAP)** primero (Gas atrás), luego reducir **RPM** (Palanca de hélice atrás/paso grueso).
    *   Esto previene el "overboost" (sobrepresión) del motor (alta presión a bajas RPM).
*   **Comprobación de MAP**: Cuando el motor está parado en tierra, el **indicador MAP indica la presión atmosférica**.
