**Introducción**
Los sistemas fly-by-wire (FBW) reemplazan los controles de vuelo manuales convencionales con una interfaz electrónica. Las entradas del piloto se convierten en señales electrónicas, se procesan por computadoras de control de vuelo y luego se envían a los actuadores que mueven las superficies de control. Estos sistemas operan bajo diferentes "leyes" o "modos" dependiendo de la salud del sistema y los datos disponibles.

## Leyes de Control y Degradación

Los sistemas FBW están diseñados con redundancia. Cuando ocurren fallas (por ejemplo, pérdida de sensores o computadoras), el sistema se degrada a un nivel más bajo de automatización y protección.

### Ley Normal (Airbus) / Modo Normal (Boeing)
Este es el modo operativo estándar con todos los sistemas funcionando.
- **Funcionalidad:** Proporciona control total en los tres ejes.
- **Protecciones:** La protección completa de la envolvente de vuelo está activa (por ejemplo, entrada en pérdida, exceso de velocidad, ángulo de alabeo, actitud de cabeceo).
- **Características:** El piloto automático está disponible. Los sistemas como el alivio de carga de maniobra y la supresión de ráfagas están activos.
- **Operación:** Las computadoras (por ejemplo, PFCs en Boeing) procesan las entradas del piloto con leyes de control complejas para optimizar la estabilidad y el manejo.

### Ley Alterna (Airbus) / Modo Secundario (Boeing)
Ocurre cuando hay fallas (por ejemplo, pérdida de múltiples sensores, fallas de computadora).
- **Funcionalidad:** El sistema revierte a cálculos simplificados.
- **Protecciones:**
    - **Airbus (ALT1/ALT2):** Algunas protecciones se pierden o degradan. Por ejemplo, **se pierde la Protección de Actitud de Cabeceo**, y la Protección de Baja Energía es reemplazada por **Estabilidad de Baja Velocidad** (se introduce una advertencia sonora de "STALL" en lugar de recuperación automática). La protección de Ángulo de Alabeo puede perderse en ALT2.
    - **Boeing:** Se pierden la **protección de la envolvente**, la supresión de ráfagas y el **piloto automático**.
- **Manejo:** La aeronave sigue siendo controlable, pero las cualidades de manejo pueden cambiar (por ejemplo, el elevador y el timón pueden ser más sensibles).

### Ley Directa (Airbus) / Modo Directo (Boeing)
El nivel más bajo de control de vuelo por computadora, generalmente resultado de múltiples fallas críticas (por ejemplo, pérdida de todas las computadoras de control de vuelo o unidades de referencia inercial).
- **Funcionalidad:** Las entradas de control del piloto se envían **directamente** a los actuadores de superficie de control sin refinamiento por computadora.
- **Protecciones:** **SE PIERDEN TODAS las protecciones.** El piloto tiene autoridad total sin restricciones pero sin redes de seguridad.
- **Piloto Automático:** **Siempre se pierde.**
- **Compensación (Trim):**
    - **Airbus:** El compensador automático (autotrim) está inoperativo; se requiere **compensación manual** (usando la rueda de trim).
    - **Boeing:** El interruptor de cancelación manual de trim de timón puede estar inoperativo.
- **Características:** El movimiento de la superficie de control es directamente proporcional al movimiento de la palanca de mando/columna.
