---
title: "Sistemas de Frenado en Aeronaves: Auto-Brake, RTO y Lógica Anti-Skid"
description: "Modos de auto-brake en aterrizaje y RTO, interacción con anti-skid, condiciones de desarmado e impacto en rendimiento de frenado según pista."
---

# Sistemas de Frenado en Aeronaves: Auto-Brake, RTO y Lógica Anti-Skid

El sistema de frenos proporciona los medios para detener la aeronave durante el aterrizaje y un despegue abortado (RTO). Las aeronaves modernas emplean sistemas avanzados como Anti-Skid y Auto-Brake para optimizar el rendimiento de frenado y la seguridad.

## Operación del Sistema Auto-Brake

El sistema de frenado automático (auto-brake) asiste a los pilotos aplicando automáticamente los frenos de las ruedas durante el aterrizaje y RTO.

- **Modo de Aterrizaje:**
    - Proporciona una **tasa de desaceleración predeterminada y constante**.
    - El sistema modula la **presión de frenado** para lograr esta desaceleración objetivo.
    - **Efecto del Empuje Inverso:** Si se utiliza el empuje inverso, este contribuye a la desaceleración. El sistema auto-brake compensa **reduciendo la presión de frenado** para mantener la misma tasa de desaceleración total. Esto resulta en **frenos más fríos**, pero **no cambia la tasa de desaceleración**.
    - **Independencia del peso:** El objetivo de desaceleración constante se mantiene independientemente del peso de la aeronave (suponiendo que existe suficiente fricción).

- **Modo de Despegue Abortado (RTO):**
    - Aplica la **máxima presión de frenado** inmediatamente cuando se activa el sistema.
    - A diferencia del modo de aterrizaje, **no** apunta a una tasa de desaceleración específica; busca la máxima potencia de frenado. La desaceleración real puede variar debido a las condiciones de la pista (por ejemplo, parches resbaladizos).
    - **Rendimiento vs. Frenado Manual:** El modo RTO y el frenado manual máximo pueden lograr la misma tasa de desaceleración. Sin embargo, el RTO ofrece un beneficio de seguridad porque **reacciona inmediatamente**, mientras que el frenado manual implica tiempo de reacción del piloto, lo que lleva a una distancia de frenado más larga.

- **Condiciones de Desarmado:**
    El sistema auto-brake se desarmará inmediatamente si:
    - El piloto aplica **frenado manual**.
    - Se avanza cualquier **palanca de empuje** después del aterrizaje.
    - La palanca de freno de velocidad (aerofrenos) se mueve a la posición DOWN (abajo).
    - El sistema se cambia a OFF o DISARM.

## Sistema Anti-Skid

El sistema anti-skid (antideslizante) determina si una rueda está a punto de bloquearse y reduce la presión de frenado para mantener la rotación del neumático y la máxima eficiencia de frenado.

- **Interacción con Auto-Brake:** El sistema auto-brake depende del sistema anti-skid. Si el sistema anti-skid está **inoperativo**, el **sistema auto-brake no funcionará**.
- **Impacto en el Rendimiento:** La falla del sistema anti-skid aumenta la distancia requerida para detenerse tanto en **pistas mojadas como secas**.
- **En Modo RTO:** Aunque el RTO ordena la presión máxima, el sistema anti-skid aún puede modular (reducir) esta presión para evitar el bloqueo de las ruedas en superficies resbaladizas.
