---
title: "Indicación de Cantidad de Combustible: Sistemas de Flotador y Capacitivos"
description: "Comprende la indicación de combustible en aeronaves, desde sistemas de flotador hasta sondas capacitivas y compensación de densidad para lectura por masa."
keywords:
	- "combustible a bordo"
	- "densidad del aire"
	- "altitud de densidad"
	- "altímetro"
---
# Indicación de Cantidad de Combustible: Sistemas de Flotador y Capacitivos

Una indicación precisa de la cantidad de combustible es vital para la seguridad y eficiencia del vuelo. Los sistemas tienen como objetivo determinar la **masa** de combustible a bordo, ya que esto determina la energía disponible, a diferencia del volumen que cambia con la temperatura.

## Verificación
Después de repostar, los pilotos deben verificar la carga de combustible:
*   Asegurar que el **Combustible a Bordo (FOB)** coincida con el plan de vuelo.
*   Comprobar que cualquier desequilibrio esté dentro de los límites.
*   **Comparar la carga planificada vs. real** (en kg o lbs) para identificar errores o fugas. Las discrepancias fuera de los límites del Manual de Vuelo de la Aeronave (AFM) requieren mantenimiento.

## Sistemas de medición de combustible

### Sistema de tipo flotador
Es el sistema más básico, encontrado típicamente en aeronaves más pequeñas.
*   **Principio:** Un flotador mecánico se asienta en la superficie del combustible. Al cambiar el nivel, mueve un brazo mecánico conectado a una resistencia variable (circuito de CC), cambiando la indicación en cabina.
*   **Limitación:** Mide **volumen**, no masa. El combustible se expande cuando está caliente y se contrae cuando está frío. A altas temperaturas, el volumen aumenta, haciendo que el indicador marque más alto aunque la **masa** permanezca igual. También es susceptible a errores durante maniobras y turbulencias.

### Sistema de tipo capacitivo
Las aeronaves modernas utilizan sistemas capacitivos para medir la cantidad de combustible con mayor precisión.
*   **Principio:** Mide la **capacitancia** entre dos placas (tubos) en el tanque. La capacitancia depende del material dieléctrico entre ellas.
*   **Dieléctrico:** El sistema distingue entre **combustible** (permitividad ~2.0) y **aire** (permitividad ~1.0). A medida que el combustible reemplaza al aire entre las placas, la capacitancia aumenta (ej. Lleno = 210pF vs Vacío = 100pF).
*   **Volumen a Masa:** Una **unidad compensadora** (o densímetro) ubicada en el fondo del tanque está siempre sumergida en combustible. Mide las propiedades específicas del combustible para tener en cuenta los cambios de densidad debidos a la temperatura. Esto permite al sistema convertir electrónicamente el volumen medido en una indicación precisa de **masa**.

## Unidades y Conversión
*   **Masa:** Kilogramos (kg), Libras (lb). ($1 \text{ kg} \approx 2,2 \text{ lb}$)
*   **Volumen:** Litros (L), Galones US (US Gal).
*   **Conversión:** $1 \text{ US Gal} \approx 3,785 \text{ Litros}$.
*   **Ejemplo:** Para verificar la carga, si el indicador requiere verificar 272 Litros contra un surtidor en Galones US: $272 / 3,785 \approx 72 \text{ US Gal}$.
