Las aeronaves modernas utilizan tecnología de estado sólido para reemplazar los giroscopios mecánicos giratorios, aumentando la fiabilidad y precisión.

## AHRS (Sistema de Referencia de Actitud y Rumbo)
Una unidad única que calcula la actitud de la aeronave (Cabeceo/Alabeo) y el Rumbo (Guiñada). Típicamente reemplaza el Horizonte Artificial y el Giro Direccional separados.
*   **Componentes:**
    *   **Giroscopios MEMS (Sensores de Tasa):** Miden la **tasa** angular (no la posición) alrededor de 3 ejes.
    *   **Acelerómetros:** Miden la aceleración (gravedad) para determinar la vertical (referencia de Cabeceo/Alabeo).
    *   **Magnetómetros:** Miden el campo magnético para determinar el Rumbo (referencia de Guiñada, como una Válvula de Flujo).
*   **Integración:** Un ordenador integra los datos de tasa para calcular la actitud y usa datos de gravedad/magnéticos para corregir la deriva.

## Giroscopio Láser de Anillo (RLG)
Usado en Sistemas de Referencia Inercial (IRS/INS) de alta gama.
*   **Principio:** Utiliza dos rayos láser contrarrotatorios en una trayectoria triangular.
*   **Efecto Sagnac:** Cuando la unidad gira, un rayo tiene un camino más corto y el otro más largo, creando un cambio de frecuencia.
*   **Características:** Sin partes móviles, extremadamente preciso, mide la tasa angular directamente.

## Ventajas sobre Giroscopios Mecánicos
*   **Fiabilidad:** Sin partes móviles (Estado sólido).
*   **Mantenimiento:** Significativamente reducido.
*   **Arranque:** Alineación más rápida.
*   **Salida:** Datos digitales alimentados fácilmente a pantallas de cabina de cristal (PFD/ND).
