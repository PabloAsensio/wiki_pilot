La radiogoniometría terrestre **VDF (VHF Direction Finding)** es un sistema que permite a una estación terrestre determinar la dirección de una aeronave basándose únicamente en sus transmisiones de radio VHF estándar. Es una ayuda valiosa ya que no requiere equipo adicional a bordo más allá de una radio VHF.

## Principio de Funcionamiento

Cuando una aeronave transmite, la estación terrestre utiliza una antena especial (como la **antena Adcock**, compuesta por dipolos verticales) para detectar la fase de la señal entrante. Al comparar las diferencias de fase entre los elementos de la antena, el sistema calcula la dirección desde la que proviene la señal.

## Códigos Q y Tipos de Marcaciones

Los resultados se proporcionan al piloto utilizando **Códigos Q**:

- **QDM:** Marcación magnética **hacia** la estación (rumbo a seguir sin viento).
- **QDR:** Marcación magnética **desde** la estación (radial magnético).
- **QUJ:** Marcación verdadera **hacia** la estación.
- **QTE:** Marcación verdadera **desde** la estación.

## Precisión y Clasificación

La precisión de las marcaciones VDF se clasifica según el ICAO en cuatro clases:

- **Clase A:** Precisión de **±2°**.
- **Clase B:** Precisión de **±5°**.
- **Clase C:** Precisión de **±10°**.
- **Clase D:** Precisión inferior a la Clase C.

## Aplicaciones y Limitaciones

- **Triangulación:** Si se utilizan dos o más estaciones terrestres, se puede determinar la **posición (fix)** de la aeronave mediante la intersección de las líneas de posición (**QTE**). El ángulo óptimo de intersección es de **90°**.
- **Auto-triangulación:** Utilizada por servicios de emergencia (como en 121.5 MHz) para obtener la posición inmediata de una aeronave que transmite.
- **Viento:** El operador VDF no conoce las condiciones de viento de la aeronave, por lo que las marcaciones se dan **sin corrección de deriva**. El piloto debe calcular la corrección necesaria.
- **Alcance:** Al ser señales VHF, están limitadas por la **línea de vista (Line-of-Sight)**. El alcance aumenta con la altitud de la aeronave y la potencia del transmisor.
