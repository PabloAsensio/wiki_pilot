Una **Brújula de Indicación Remota** (a menudo llamada Brújula Giro-Magnética) combina un Giro Direccional con una Válvula de Flujo para proporcionar un rumbo estable y referenciado magnéticamente sin necesidad de reinicio manual.

## Componentes del Sistema (FEAT)
El bucle funciona de la siguiente manera:
1.  **F**lux Valve (Válvula de Flujo): Detecta el error del campo magnético terrestre.
2.  **E**rror Detector (Detector de Error): Compara el rumbo de la Válvula vs. rumbo del Giro.
3.  **A**mplifier (Amplificador): Amplifica la señal de error.
4.  **T**orque Motor (Motor de Torque): Precesa el giroscopio para alinearlo con el norte magnético.

## Modos de Operación
1.  **Modo Esclavo (Slaved):** El modo de operación normal. La Válvula de Flujo corrige continuamente el Giro (lentamente, para evitar perseguir errores magnéticos temporales). El giroscopio está "atado" al Norte Magnético.
2.  **Modo Libre (Free/DG):** La esclavitud se desconecta. El instrumento actúa como un **Giro Direccional** estándar.
    *   Usado en **Regiones Polares** (donde el campo magnético es poco fiable/débil).
    *   Usado si falla la Válvula de Flujo.
    *   Requiere sincronización manual.

## Ventajas
*   Elimina la necesidad de reinicio manual (en modo Esclavo).
*   Reduce el efecto del desvío (La válvula de flujo está en la punta del ala/cola).
*   Proporciona datos de rumbo a otros sistemas (Piloto Automático, RMI, Radar).
