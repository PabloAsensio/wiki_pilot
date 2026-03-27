---
title: "Componentes Principales del Motor de Turbina de Gas: Compresor, Combustión, Turbina y Escape"
description: "Repasa los componentes principales del motor de turbina de gas: comportamiento del compresor, combustión, extracción de energía en turbina y sección de escape."
---
# Componentes Principales del Motor de Turbina de Gas: Compresor, Combustión, Turbina y Escape

Los componentes centrales de un motor de turbina de gas están diseñados para procesar el aire a través del ciclo Brayton: Admisión, Compresión, Combustión, Expansión (Turbina) y Escape.

## Sección del Compresor
El compresor aumenta la presión del flujo másico de aire para alimentar la cámara de combustión.
*   **Tipos**:
    *   **Centrífugo**: Acelera el aire radialmente. Robusto, simple, relación de presión máx ~4.5:1 por etapa.
    *   **Axial**: El aire fluye paralelo al eje. Compuesto por filas alternas de **Rotores** y **Estatores**.
        *   **Rotor**: Gira, reduce volumen, añade energía cinética (Velocidad aumenta, Presión aumenta).
        *   **Estator**: Álabes fijos. Convierte energía cinética en presión (Velocidad disminuye, Presión aumenta). También endereza el flujo de aire.
*   **Efecto Global**: A través del compresor, **Presión y Temperatura aumentan**, mientras que la **Velocidad Axial disminuye**.
*   **Entrada en Pérdida del Compresor (Stall/Surge)**: Puede ocurrir si el flujo se interrumpe (ej. desajuste entre RPM y flujo).
    *   **Síntomas**: Alta EGT, Vibración, pérdida de empuje, ruidos fuertes de explosión (surge).
    *   **Prevención**:
        *   **Álabes Guía de Entrada Variables (VIGVs)**: Antes de la 1ª etapa, ajustan el ángulo del aire.
        *   **Álabes Estatores Variables (VSVs)**: Entre etapas.
        *   **Válvulas de Sangrado (Bleed Valves)**: Liberan presión para prevenir flujo inverso.

## Difusor
Situado entre la salida del compresor y la cámara de combustión.
*   **Función**: Un conducto divergente que **disminuye la velocidad del aire** y **aumenta la presión estática**.
*   **Propósito**: Frenar el aire a una velocidad compatible con la propagación de la llama, asegurando que la **llama arda continuamente** y no se apague.

## Cámara de Combustión
Mezcla el aire comprimido con combustible y lo quema.
*   **Proceso**: Combustión a presión constante.
*   **Inyectores de Combustible**: Atomizan el combustible en un spray con componentes de velocidad axial y tangencial.
*   **Válvulas de Drenaje**: Situadas en la parte inferior para eliminar combustible no quemado tras un arranque fallido (wet start).

## Sección de Turbina
Extrae energía de los gases calientes para mover el compresor y accesorios.
*   **Tipos**:
    *   **Turbina de Impulso (Acción)**:
        *   **Estatores (NGV)**: Conducto convergente -> Velocidad Aumenta, Presión Disminuye.
        *   **Rotores**: Forma de cuchara -> Velocidad Disminuye, **Presión Constante**.
    *   **Turbina de Reacción**:
        *   **NGV**: Dirige el aire (Presión constante).
        *   **Rotores**: Forma convergente -> Velocidad Aumenta, **Presión Disminuye** (creando fuerza de reacción).
*   **Limitaciones**: La turbina es el componente **más estresado** (Calor + Fuerza centrífuga).
    *   **Creep (Fluencia)**: Los álabes se estiran con el tiempo debido al estrés/calor. Limita la vida del motor y la temperatura máx (TGT/EGT).
    *   **Control Activo de Holgura (ACC)**: Enfría la carcasa para mantener la holgura óptima con las puntas de los álabes.

## Sección de Escape
Dirige los gases fuera del motor para producir empuje.
*   **Tubo de Chorro (Jet Pipe)**: Conduce el gas.
*   **Cono de Escape**: Suaviza el flujo que sale de la turbina.
*   **Tobera Propulsora**: Generalmente **convergente**.
    *   **Función**: Aumenta la **velocidad** de los gases de escape y disminuye la presión para maximizar el momento y el empuje.

## Daño por Objetos Extraños (FOD)
Ingestión de escombros/objetos.
*   **Indicaciones**: Alta Vibración, Alta EGT, fluctuación de RPM o parámetros.
