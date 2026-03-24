Los tacómetros miden la velocidad de rotación del motor, expresada en Revoluciones Por Minuto (RPM).

## Tipos de tacómetros

### 1. Tacómetro mecánico
Utilizado en aeronaves de pistón más antiguas.
*   **Principio:** Un eje de transmisión flexible conecta la caja de engranajes del motor al instrumento. En el interior, un imán permanente giratorio induce **corrientes de Foucault** en una copa de arrastre de aluminio, creando un campo magnético que hace girar la copa y mueve la aguja contra un resorte.
*   **Características:** Autoalimentado (no necesita electricidad). Limitado por la longitud del eje (máx. ~2 m).

### 2. Tacómetro eléctrico
Utilizado en algunos aviones a reacción (ej. para velocidad del compresor de alta presión).
*   **Principio:** Un **tacogenerador** de CA trifásico en la caja de engranajes del motor envía una señal a un motor síncrono en el indicador. Este motor hace girar un conjunto imán/copa similar al tipo mecánico.
*   **Características:** Señal autoalimentada. La frecuencia de CA varía con las RPM.

### 3. Tacómetro electrónico
Utilizado en turbinas de gas modernas (multi-eje) y sistemas EFIS.
*   **Principio:** Utiliza una **sonda de velocidad** (bobina + imán) o sonda de inducción.
    *   **Conteo de pulsos:** La sonda se coloca cerca de los álabes del fan o de una rueda fónica con muescas. A medida que el metal pasa por la sonda, perturba el **campo magnético**, generando pulsos eléctricos.
    *   **Cálculo:** La tasa de pulsos es directamente proporcional a la velocidad del eje.
*   **Características:** Requiere una fuente de alimentación externa. Preciso.

*Nota: Aunque todos utilizan magnetismo, los sistemas electrónicos lo usan para generar pulsos para el conteo, mientras que los tipos mecánicos/eléctricos lo usan para crear par (arrastre) y mover una aguja.*
