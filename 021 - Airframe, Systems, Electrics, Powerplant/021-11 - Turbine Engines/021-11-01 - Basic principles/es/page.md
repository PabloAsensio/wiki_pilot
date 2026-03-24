# Motores de Turbina: Principios Básicos

Un motor de turbina de gas es un motor térmico que usa aire como fluido de trabajo para producir empuje. Opera bajo el **Ciclo Brayton**.

## Principio de Funcionamiento (Ciclo Brayton)
Al igual que un motor de pistón (Ciclo Otto), una turbina de gas tiene cuatro fases: Admisión, Compresión, Combustión y Escape.
*   **Proceso Continuo**: A diferencia del motor de pistón intermitente, el proceso de la turbina de gas es **continuo**.
*   **Presión Constante**: La combustión ocurre a **presión constante** (el volumen y la temperatura aumentan), mientras que en un motor de pistón, ocurre a volumen constante.

## Componentes Principales
El aire fluye axialmente de adelante hacia atrás:
1.  **Toma de Admisión**: Diseñada para reducir la velocidad del aire (presión dinámica) y **aumentar la presión estática y temperatura** (conducto divergente) antes del compresor.
2.  **Compresor**: Aumenta la presión del aire. Puede ser axial o centrífugo.
3.  **Cámara de Combustión**: Mezcla combustible con aire comprimido y lo quema a **presión constante**.
4.  **Turbina**: Extrae energía de los gases calientes en expansión para mover el compresor (y el fan/hélice).
5.  **Tobera de Escape**: Acelera los gases de escape para producir empuje (conducto convergente aumenta velocidad, disminuye presión).

## Tipos de Motor

### Turborreactor / Turbofan
*   **Eje Simple (Single Spool)**: Un eje conecta compresor y turbina.
*   **Eje Múltiple (Twin Spool)**:
    *   **N1 (Baja Presión)**: Fan + Compresor de Baja (LP) movidos por Turbina de Baja (LP).
    *   **N2 (Alta Presión)**: Compresor de Alta (HP) movido por Turbina de Alta (HP).
    *   Los ejes rotan mecánicamente independientes.
*   **Índice de Derivación (Bypass Ratio)**: Relación entre el aire que evita el núcleo y el aire que pasa por el núcleo (compresor de alta).
    *   **Fórmula**: `Bypass Ratio = (Flujo Total Entrada - Flujo Núcleo HP) / Flujo Núcleo HP`
    *   Los motores de alto índice de derivación son más eficientes (menor SFC) y silenciosos.

### Turbohélice / Turboeje (Turbina Libre)
*   **Generador de Gas**: El motor núcleo (Compresor + Combustión + Turbina del Compresor) crea gas de alta energía.
*   **Turbina Libre**: Una turbina separada (mecánicamente independiente del núcleo) extrae energía para mover una hélice o rotor vía una caja reductora.
*   **Control**:
    *   **Palanca de Potencia**: Controla el flujo de combustible (velocidad del Generador de Gas/N1).
    *   **Palanca de Hélice / CSU**: Ajusta el ángulo de pala para mantener constantes las RPM de la hélice/turbina libre (N2/Np).

## Conceptos de Rendimiento

### Empuje (Thrust)
*   **Empuje Estático**: Cuando el avión está estacionario.
    *   Produce **Fuerza**, pero **Cero Potencia Mecánica** (Potencia = Fuerza x Velocidad; si Velocidad es 0, Potencia es 0).
    *   Igual al producto del flujo másico y la velocidad de escape (más el término de presión).

### Consumo Específico de Combustible (SFC)
*   **Turborreactor/Turbofan**: Flujo de combustible por unidad de **Empuje**. Unidad: `kg/hora/Newton` (o lb/hr/lbf).
*   **Turbohélice/Pistón**: Flujo de combustible por unidad de **Potencia**. Unidad: `kg/hora/Watt` (o lb/hr/shp).
*   Un menor SFC indica mejor eficiencia.

## Secuencia de Arranque
1.  **Arranque Seleccionado**: El starter rota el compresor de alta (N2).
2.  **Ignición ON**: Ignitores activados.
3.  **Combustible ON**: Combustible inyectado en la cámara.
4.  **Encendido (Light-up)**: La mezcla se enciende.
5.  **Auto-sustentación**: El motor acelera a ralentí (idle); el starter se desconecta.
