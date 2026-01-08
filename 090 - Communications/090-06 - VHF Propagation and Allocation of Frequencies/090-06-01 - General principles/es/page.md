## Bandas de Frecuencia
El espectro radioeléctrico se divide en bandas específicas según la frecuencia. La aviación utiliza varias de ellas:

| Banda | Nombre | Rango de Frecuencia | Uso en Aviación |
| :--- | :--- | :--- | :--- |
| **VLF** | Very Low Frequency | 3 – 30 kHz | Nav de largo alcance |
| **LF** | Low Frequency | 30 – 300 kHz | **NDB** |
| **MF** | Medium Frequency | 300 – 3,000 kHz | **NDB**, Radio comercial AM |
| **HF** | High Frequency | 3 – 30 MHz | **Coms de Largo Alcance** (Oceánico) |
| **VHF** | **Very High Frequency** | **30 – 300 MHz** | **Coms Estándar y Nav** |
| **UHF** | Ultra High Frequency | 300 – 3,000 MHz | Militar, ILS Glideslope, DME |
| **SHF** | Super High Frequency | 3 – 30 GHz | Radar, Radalt |
| **EHF** | Extremely High Frequency | 30 – 300 GHz | - |

## La Banda Aérea (Airband - VHF)
La "banda aérea" es el espectro VHF asignado para la aviación civil, que va de **108.000 MHz a 137.000 MHz**.

### Asignación
1.  **Navegación (NAV)**: **108.000 – 117.975 MHz**.
    *   Usado para: **VOR**, **ILS** (Localizador), **ATIS** (a veces en voz VOR).
    *   *Nota*: Frecuencias como 116.30 MHz son de navegación y no se pueden seleccionar en una radio COM estándar para transmisión de voz.
2.  **Comunicación (COM)**: **118.000 – 136.975 MHz**.
    *   Usado para: **ATC**, **Aire-Aire**, **Operaciones**.
    *   *Nota*: **121.500 MHz** es la Frecuencia Internacional de Emergencia Aérea.

### Espaciado de Canales (8.33 kHz)
Tradicionalmente, los canales estaban separados por **25 kHz**. Para combatir la congestión de frecuencias en Europa, los canales se subdividieron en un espaciado de **8.33 kHz**.
*   Esto crea 2 canales extra por cada bloque de 25 kHz.
*   El equipamiento de radios compatibles con 8.33 kHz es obligatorio en la región europea de la OACI (por ejemplo, por encima de FL195).

## Características de Propagación VHF
Las ondas de radio VHF se propagan como **Ondas Espaciales** (Directas).

### Línea de Visión (Line of Sight)
*   La transmisión es "cuasi-óptica" o de **Línea de Visión**.
*   Las ondas viajan en línea recta y **no** rebotan en la ionosfera (a diferencia de HF).
*   El **alcance** está limitado por la curvatura de la Tierra y el terreno/obstáculos.

### Cálculo de Alcance
El alcance teórico máximo depende de la altura del transmisor ($h_{TX}$) y del receptor ($h_{RX}$).
$$ Alcance (NM) \approx 1.23 \times (\sqrt{h_{TX}} + \sqrt{h_{RX}}) $$
*(Donde las alturas están en pies)*.
*   **Conclusión**: Ascender a una mayor altitud aumenta significativamente el alcance y la recepción VHF.

### Factores que Afectan la Recepción
1.  **Altitud**: Mayor altura es mejor.
2.  **Obstáculos**: Montañas/terreno bloquean las señales (Sombreado).
3.  **Ductos Atmosféricos (Ducting)**: Bajo ciertas condiciones (Inversión Térmica), las señales VHF pueden quedar atrapadas en un "ducto" y viajar **más lejos** que la línea de visión normal.
4.  **Atenuación**: La fuerza de la señal se debilita con la distancia debido a la absorción atmosférica.
