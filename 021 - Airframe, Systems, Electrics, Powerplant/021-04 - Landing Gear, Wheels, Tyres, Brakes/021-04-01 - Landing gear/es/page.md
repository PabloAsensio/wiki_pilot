**Introducción**

El sistema del tren de aterrizaje soporta la aeronave durante el rodaje, despegue y aterrizaje. Es un sistema complejo que implica mecanismos de retracción, dispositivos de bloqueo y capacidades de extensión de emergencia. Comprender su funcionamiento y limitaciones es crucial para un vuelo seguro.

## Operación y Control del Tren de Aterrizaje

La mayoría de los sistemas de tren de aterrizaje de aeronaves modernas son **sistemas activos**, accionados hidráulicamente.

- **Fuente de Energía:** La presión hidráulica la proporcionan principalmente las **bombas accionadas por el motor**, impulsadas por la caja de accesorios. Si bien existen bombas eléctricas, la carga pesada durante la retracción la manejan principalmente las bombas accionadas por el motor.
- **Indicación:**
    - **Abajo y Bloqueado:** Indicado por **3 luces verdes** en la cabina.
    - **Tránsito/Inseguro:** Una luz roja de "tren inseguro" se ilumina si la posición del tren no coincide con la palanca selectora o no está bloqueado.
    - **Alerta Aural:** Debe sonar una advertencia aural si se **intenta un aterrizaje cuando el tren de aterrizaje no está bloqueado abajo** (típicamente activado por configuraciones bajas de acelerador o altitud de radio).

## Mecanismos de Retracción y Bloqueo

Para evitar la operación inadvertida y asegurar que el tren permanezca en la posición correcta, se utilizan varios mecanismos de seguridad:

- **Pestillo Anti-Retracción (Anti-Retract Latch):** Evita físicamente que la palanca selectora del tren se mueva a la posición "ARRIBA" cuando la aeronave está en tierra.
- **Uplocks (Bloqueos de subida):** Bloqueos mecánicos (a menudo **bloqueos de gancho**) que mantienen el tren en la posición retraída.
- **Downlocks (Bloqueos de bajada/Sobrecéntricos):**
    - **Bloqueo Geométrico/Sobrecéntrico:** Se utiliza principalmente como un **bloqueo de bajada**. Utiliza la geometría de los puntales de arrastre/laterales para bloquear el tren en la posición extendida.
    - **Mecanismo:** Requiere una pequeña fuerza para bloquearse (a menudo bloqueándose automáticamente al extenderse) pero necesita fuerza hidráulica o mecánica para desbloquearse (romper la condición sobrecéntrica).

## Extensión de Emergencia

Si falla el sistema hidráulico principal, hay un sistema de extensión de emergencia disponible para bajar el tren.

- **Métodos:**
    - **Caída Libre por Gravedad:** El método más común. Se liberan los bloqueos mecánicos de subida y el tren cae por su propio peso.
    - **Manivela Mecánica:** Girar manualmente engranajes para operar actuadores.
    - **Bomba Manual:** Bombear manualmente fluido hidráulico a los actuadores.
    - **Nitrógeno/Aire Comprimido (Blowdown):** Usar presión de gas almacenada para liberar bloqueos o alimentar actuadores.
- **Secuencia:**
    1. **Liberar Presión Hidráulica:** A menudo puenteando la válvula de corte.
    2. **Desbloquear Puertas:** Liberar los bloqueos de subida de las puertas.
    3. **Desbloquear Tren:** Liberar los **bloqueos de subida** mecánicos.
- **Resultado:** El tren se extiende y se bloquea abajo automáticamente (mediante resortes sobrecéntricos/geometría). **Las puertas del tren generalmente permanecen abiertas** ya que no hay sistema para retraerlas. Esta es típicamente una operación única, no reversible.

## Funciones de Componentes

- **Compás de Torsión (Torsion Link/Torque Link):**
    - **Función:** Conecta el cilindro interior (deslizante) y exterior (fijo) del puntal oleoneumático para **evitar que el cilindro interior gire** o rote dentro del cilindro exterior.
    - **Estrés:** Transmite el par de dirección y previene el shimmy. Experimenta estrés máximo durante **giros cerrados en tierra**.
- **Válvula de Lanzadera (Shuttle Valve):** Permite que un actuador sea alimentado por una fuente de presión alternativa (emergencia) si falla la fuente primaria.

## Limitaciones de Velocidad

Operar el tren de aterrizaje genera resistencia y cargas estructurales, lo que requiere límites de velocidad específicos:

- **$V_{LO}$ (Velocidad de Operación del Tren de Aterrizaje):** La velocidad máxima a la que es seguro **extender o retraer** el tren de aterrizaje. Si estas difieren, se designan como $V_{LO(EXT)}$ y $V_{LO(RET)}$.
- **$V_{LE}$ (Velocidad con Tren de Aterrizaje Extendido):** La velocidad máxima a la que la aeronave puede volar con seguridad con el **tren extendido y bloqueado**. Esta es típicamente más alta que $V_{LO}$.
