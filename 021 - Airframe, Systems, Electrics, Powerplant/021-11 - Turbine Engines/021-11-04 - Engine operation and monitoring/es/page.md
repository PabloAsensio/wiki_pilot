# Operación y Monitorización del Motor

## Control y Monitorización del Motor

*   **Monitorización de Vibraciones**: Usado para detectar deficiencias mecánicas en partes rotatorias (cojinetes, ejes).
    *   **Principio**: Acelerómetros (piezoeléctricos) miden la vibración. Las señales son **filtradas** para aislar frecuencias relevantes.
*   **Tendencias del Motor (Trending)**: Comparar datos reales del motor con modelos de rendimiento esperados para **detectar anomalías y planificar mantenimiento** antes de que ocurra un fallo.
*   **Estado FADEC**: Diseñado con redundancia.
    *   Un canal activo, uno en reserva.
    *   **Tolerante a Fallo Único**: El motor opera normalmente tras el fallo de un componente.
    *   **Chequeo de Redundancia**: Pérdida de energía al FADEC = **Apagado del Motor**.

## Instrumentos de Monitorización (Ejemplos)
*   **RPM (N1, N2)**: Indicación primaria de potencia (especialmente **N1** y **EPR**).
*   **EGT/TGT**: Temperatura de Gases de Escape. Crítica para la salud de la turbina (límite de fluencia/creep).
*   **Flujo de Combustible**: Indica consumo y salud (ej. fugas).
*   **Sistema de Aceite**:
    *   **Presión**: Vital para lubricación. Baja presión a menudo lleva a alta temperatura.
    *   **Temperatura**: Alta temp indica fallo de refrigeración o fricción. Presión más alta de lo normal al arranque (aceite frío) es normal.
    *   **Detector de Virutas (Chip Detector)**: Detecta partículas metálicas en el aceite (desgaste interno).
*   **Bypass del Filtro de Combustible**: Indica bloqueo del filtro; se suministra combustible sin filtrar para evitar privación al motor.

## Regímenes de Potencia Ralentí (Idle)
*   **Ralentí de Tierra (Ground Idle)**: RPM bajas para evitar velocidad excesiva en rodaje.
*   **Ralentí de Vuelo (Flight Idle)**: RPM más altas que en tierra.
    *   **Propósito**: Permite una aceleración rápida (spool-up) a máxima potencia (ej. para un **motor y al aire / go-around** o reversas).
    *   **Activación**: Circuitos lógicos (Peso en ruedas, flaps, etc.) conmutan entre ralentí tierra/vuelo.

## Rangos de Control de Turbohélice
*   **Rango Alfa**: Rango de vuelo (Flight Idle a Max Power). Hélice gobernada por CSU (Unidad de Velocidad Constante).
*   **Rango Beta**: Rango de tierra (Debajo de Flight Idle).
    *   **Control**: El piloto controla directamente el **paso de la pala** vía la palanca de potencia.
    *   **Ralentí de Tierra**: Empuje justo para rodar.
    *   **Reversa**: Máximo empuje negativo para deceleración.

## Anomalías en el Arranque del Motor
*   **Arranque Colgado (Hung Start)**: El motor enciende pero falla en acelerar a velocidad de auto-sustentación.
    *   **Causa**: Baja presión del starter, ¿flujo de combustible insuficiente?
    *   **Acción**: Apagar, ventilar (dry motor) para limpiar combustible.
*   **Arranque Caliente (Hot Start)**: EGT excede límites.
    *   **Síntomas**: Bajas RPM + **Subida repentina/rápida de EGT**.
    *   **Causa**: Exceso de combustible, viento de cola, corte prematuro del starter.
    *   **Acción**: **Abortar inmediatamente** (Cortar combustible).
*   **Arranque Húmedo (Wet Start)**: No hay encendido (fallo de ignición). Combustible no quemado drena de la cámara.
*   **Fuego en Tobera (Tailpipe Fire)**: Fuego en la tobera de escape (interno) debido a exceso de combustible que se enciende tras el apagado o arranque fallido.
    *   **Acción**: Cortar combustible, **ventilar** (crank) el motor.

## Conceptos Operacionales
*   **Tiempo de Aceleración (Spool-up)**: Tiempo de ralentí a empuje máx. Las turbinas sufren de "inercia" (respuesta lenta). El 'Flight Idle' ayuda a reducir este tiempo.
*   **Reencendido en Vuelo (Relight)**:
    *   Usa el **molinete** (windmilling/velocidad aire) para rotar el compresor.
    *   La envolvente depende de **Altitud** y **Velocidad**.
*   **Encendido Continuo**: Seleccionado cuando hay riesgo de apagado de llama (Turbulencia, Lluvia fuerte, Hielo, Aproximación).
