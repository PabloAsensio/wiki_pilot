## Reglas de Notificación del Viento
Existe una distinción crucial en cómo se notifica la dirección del viento en aviación:

*   **Información Escrita (Mapas, METAR, TAF)**: La dirección del viento se referencia al **Norte VERDADERO (Geográfico)**.
    *   *Regla general*: "Si lo **lees**, es **Verdadero**."
*   **Información Hablada (ATC, ATIS)**: La dirección del viento se referencia al **Norte MAGNÉTICO**.
    *   *Regla general*: "Si lo **escuchas**, es **Magnético**."
    *   *Razón*: Los pilotos utilizan brújulas/rumbos magnéticos para el despegue y aterrizaje, por lo que el ATC convierte el viento a magnético para alinearlo con la pista (que tambien está orientada magnéticamente).

## ATIS (Servicio Automático de Información Terminal)
El ATIS es el suministro automático de información actual y rutinaria a las aeronaves que llegan y salen.

*   **Voice-ATIS (Voz)**: Transmisión de voz continua, generalmente en una frecuencia **VHF** discreta (o canal de voz VOR).
*   **D-ATIS (Datos)**: Suministro del ATIS mediante enlace de datos (ej. ACARS).

### Contenido
Los mensajes ATIS siguen una estructura específica (Aeródromo, Designador, Hora, Pista, Meteorología, etc.).
*   **Ejemplo**: "TWY E3 Southbound CLSD due WIP" $\rightarrow$ Calle de rodaje E3 dirección sur cerrada debido a trabajos en curso.

## VOLMET
**VOLMET** proporciona información meteorológica (METAR, SPECI, TAF, SIGMET) de múltiples aeródromos a las aeronaves en vuelo.
*   **VHF VOLMET**: Normalmente transmisiones continuas.
*   **HF VOLMET**: Transmisiones programadas (usadas para cobertura de largo alcance/oceánica).
*   **D-VOLMET**: Suministro vía enlace de datos.

## Códigos Meteorológicos (METAR/SPECI)
### CAVOK (Ceiling And Visibility OK)
Se utiliza cuando ocurren simultáneamente estas condiciones:
*   **Visibilidad**: 10 km o más.
*   **Nubes**: Sin nubes de importancia operativa (Sin nubes por debajo de 5000 ft o MSA, sin CB/TCU).
*   **Tiempo**: Sin fenómenos meteorológicos significativos.

### RVR (Alcance Visual en la Pista)
Formato: `R(Pista)/(Valor)(Tendencia)`
*   **P**: Plus (Más de). Ej. `P2000` > 2000m.
*   **M**: Minus (Menos de). Ej. `M0150` < 150m.
*   **U**: Upward (Tendencia ascendente/mejorando).
*   **D**: Downward (Tendencia descendente/empeorando).
*   **N**: No hay tendencia distinta (Nil).
*   **V**: Variable (ej. `1100V1500`).

### Otras Definiciones
*   **Techo de Nubes (Ceiling)**: La altura de la base de la capa de nubes más baja que cubre **más de la mitad del cielo** (BKN u OVC).
*   **Cizalladura (Wind Shear - WS)**: Se notifica si afecta a las trayectorias de despegue/aproximación (ej. `WS TKOF RWY20` o `WS ALL RWY`).

## Aeronotificaciones (AIREP)
### Aeronotificaciones Especiales (AIREP SPECIAL)
Los pilotos **deben** hacer una aeronotificación especial siempre que encuentren las siguientes condiciones:
1.  **Turbulencia Moderada o Severa**.
2.  **Engelamiento (Hielo) Moderado o Severo**.
3.  **Onda de Montaña Severa**.
4.  **Tormentas** (con/sin granizo, oscurecidas, inmersas, generalizadas o en líneas de turbonada).
5.  **Tormenta de polvo/arena Fuerte**.
6.  **Ceniza Volcánica** o actividad pre-erupción.
7.  **Eficacia de Frenado**: Si la eficacia de frenado encontrada es **diferente** (mejor o peor) a la notificada.

### Aeronotificaciones Rutinarias
*   **Enlace de Datos (ADS-C)**: Las aeronaves equipadas con ADS-C están **exentas** de realizar informes meteorológicos rutinarios por voz (la automatización se encarga).
*   **Intervalos de notificación (si se requieren)**:
    *   **En ruta**: Cada 15 minutos.
    *   **Ascenso inicial**: Cada 30 segundos durante los primeros 10 minutos.
