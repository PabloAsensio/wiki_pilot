---
title: "Baterías Eléctricas de Aeronave y Protección ante Fuga Térmica"
description: "Tipos de baterías de aeronaves, propiedades, peligros (fuga térmica) y métodos de carga."
---

# Baterías Eléctricas de Aeronave y Protección ante Fuga Térmica

## Conceptos Básicos de Baterías

Las baterías convierten energía química en energía eléctrica.

*   **Capacidad**: Medida en **Amperios-hora (Ah)**. Representa la cantidad de carga que una batería completamente cargada puede suministrar.
    *   Ejemplo: Una batería de 5 Ah puede suministrar 5A durante 1 hora, o 2.5A durante 2 horas.
    *   La capacidad depende del tamaño físico de las placas de la batería (no del voltaje).
    *   **Conexión en Serie**: El voltaje se duplica, la capacidad permanece igual.
    *   **Conexión en Paralelo**: La capacidad se duplica, el voltaje permanece igual.

### Comprobación de Estado

*   **Comprobación con Carga (On-Load Check)**: Una prueba aplicada para dar una mejor indicación del estado de la batería usando el voltímetro de la aeronave.
    *   Requiere aplicar una carga (por ejemplo, luces, calefacción del pitot) durante un tiempo específico (10-20 segundos).
    *   El voltaje debe permanecer estable y no caer por debajo de un valor específico.
    *   Implica comparar voltajes con carga y sin carga.

### Tipos de Baterías

#### Baterías de Plomo-Ácido
*   **Composición**: Ánodo (Peróxido de Plomo), Cátodo (Plomo Esponjoso), Electrolito (Agua y Ácido Sulfúrico).
*   **Voltaje**: 2V por celda con carga, **2.2V sin carga**.
*   **Características**:
    *   Buen almacenamiento de energía pero pesadas.
    *   Menor densidad energética.
    *   La tasa de descarga disminuye con menor temperatura (la resistencia interna aumenta).
*   **Peligros**: La sobrecarga hierve el electrolito, dañando las placas.

#### Baterías de Níquel-Cadmio (NiCd)
*   **Composición**: Placas de Óxido de Níquel y Cadmio, Electrolito (Hidróxido de Potasio).
*   **Voltaje**: ~1.2V por celda (permanece relativamente constante durante la descarga).
*   **Características**:
    *   Baja resistencia interna.
    *   Amplio rango de temperatura de funcionamiento.
    *   **Riesgo de Fuga Térmica**: Alto.
    *   **Ventilación**: Requerida.

#### Iones de Litio (Li-ion) / Polímero de Litio (LiPo)
*   **Características**: Alta densidad de energía.
*   **Peligros**: Extremadamente susceptibles a **Fuga Térmica** (Thermal Runaway).
*   **Desgaste**: El rendimiento se degrada con el tiempo; la resistencia interna aumenta, causando peor rendimiento bajo carga.

### Fuga Térmica (Thermal Runaway)

Una reacción en cadena rápida e imparable donde un aumento en la temperatura cambia la resistencia interna, causando más generación de calor, lo que aumenta aún más la temperatura (bucle de retroalimentación positiva).

*   **Causas**:
    *   **Cortocircuito Interno**: Formación de dendritas, choque/impacto compresivo (daño físico), deformación.
    *   **Cortocircuito Externo**.
    *   **Sobrecarga**: Más allá del voltaje máximo.
    *   **Sobrecalentamiento**: Durante la carga o debido a altas corrientes.
*   **Proceso**: Descomposición del electrolito (reacción exotérmica) -> Aumento rápido de temperatura -> Liberación de energía almacenada -> Fuego/Explosión.
*   **Riesgo**: Los incendios de Li-ion arden a miles de grados y son muy difíciles de extinguir. El fuego puede propagarse a celdas vecinas.
*   **Protección/Contención**:
    *   **Cajas de Metal**: Las baterías de Li-ion a menudo se alojan en cajas ventiladas hechas de acero galvanizado/inoxidable con aislamiento contra incendios para contener la fuga térmica.
    *   **Ventilación**: Permite la disipación de calor y la liberación de gases inflamables.

### Operaciones y Carga

*   **Método de Carga**: La mayoría de las aeronaves usan **Carga de Voltaje Constante**.
    *   El voltaje del generador excede el voltaje de la batería (por ejemplo, generador de 28V para una batería de 24V).
*   **Amperímetro**: Conectado en serie. Una lectura positiva (por ejemplo, +24A) indica que la batería se está **cargando**.
*   **Pérdida de Potencia Generada**: Si todos los generadores fallan, la energía eléctrica restante de la batería es **limitada en el tiempo** (típicamente 30 minutos para sistemas esenciales).
*   **Mercancías Peligrosas**: Las baterías de litio de repuesto están restringidas/prohibidas en carga debido al riesgo de incendio.
