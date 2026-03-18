El **Indicador de Velocidad del Aire (ASI)** mide la velocidad de la aeronave a través del aire comparando la presión total y la presión estática.

## Principio
*   **Fórmula:** $\text{Presión Dinámica} (q) = \text{Presión Total} (P_t) - \text{Presión Estática} (P_s)$.
*   **Mecanismo:** La presión de Pitot ($P_t$) alimenta la cápsula; la presión estática ($P_s$) alimenta la caja. La expansión de la cápsula representa la presión dinámica ($1/2 \rho V^2$), que se calibra a velocidad del aire.

## Definiciones de Velocidad
1.  **IAS (Indicada):** La lectura directa del dial.
2.  **CAS (Calibrada):** IAS corregida por errores de **Instrumento** y **Posición**.
3.  **EAS (Equivalente):** CAS corregida por error de **Compresibilidad** (significativo > 300 kts / Mach 0.4).
4.  **TAS (Verdadera):** EAS corregida por error de **Densidad** (Altitud/Temperatura). TAS es la velocidad real a través del aire.
    *   *Regla general:* La TAS aumenta con la altitud para una IAS constante. ($TAS \approx EAS \times \sqrt{\rho_0 / \rho}$).

## Bloqueos (PUDSOD)
Los errores dependen de qué puerto esté bloqueado y la fase de vuelo:
*   **P**itot Bloqueado:
    *   **U**nder-reads (Indica menos) en **D**escenso (y más en ascenso). Actúa como un altímetro.
*   **S**tática Bloqueada:
    *   **O**ver-reads (Indica más) en **D**escenso (y menos en ascenso).

## Código de Colores
*   **Arco Blanco:** Rango de operación de flaps ($V_{SO}$ a $V_{FE}$).
*   **Arco Verde:** Rango de operación normal ($V_{S1}$ a $V_{NO}$).
*   **Arco Amarillo:** Rango de precaución ($V_{NO}$ a $V_{NE}$).
*   **Línea Roja:** Velocidad de nunca exceder ($V_{NE}$).
*   **Línea Azul:** Mejor régimen de ascenso con un motor inoperativo ($V_{YSE}$) en bimotores ligeros.

## Velocidad No Fiable
Se reconoce por lecturas de ASI no coincidentes, alertas de "IAS disagree", o relaciones anormales de cabeceo/potencia. Los pilotos deben verificar con **Ground Speed** (GNSS/INS) y tablas de cabeceo/potencia.
