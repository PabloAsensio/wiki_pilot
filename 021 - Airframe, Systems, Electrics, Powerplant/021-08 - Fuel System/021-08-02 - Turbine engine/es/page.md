---
title: "Fundamentos del Sistema de Combustible en Motores de Turbina"
description: "Propiedades del combustible Jet, bombas booster y HP, gestión de crossfeed y arquitectura del sistema de combustible en turbinas."
---

# Fundamentos del Sistema de Combustible en Motores de Turbina

Los sistemas de combustible de aeronaves de turbina están diseñados para manejar caudales altos, temperaturas muy variadas y una gestión crítica del peso. Utilizan tipos específicos de combustibles a base de queroseno.

## Características del Combustible Jet

- **Jet A:**
    - Punto de congelación: **-40°C**
    - Punto de inflamación: **+38°C**
    - Común en los EE. UU.
- **Jet A-1:**
    - Punto de congelación: **-47°C**
    - Punto de inflamación: **+38°C**
    - Densidad: Aprox. **0.8 kg/l** (Gravedad Específica ~0.8).
    - El combustible estándar para la aviación comercial internacional.
- **Jet B:**
    - Combustible "Wide-cut" (mezcla de gasolina y queroseno).
    - Punto de congelación: **-60°C** (Ideal para climas extremadamente fríos).
    - Punto de inflamación: **-20°C** (Altamente inflamable/volátil).
    - **Comparación:** El Jet A tiene un punto de congelación más alto y un punto de inflamación más alto que el Jet B.
- **Aditivos:**
    - **FSII (Inhibidores de Hielo del Sistema de Combustible):** Previenen la congelación del agua/formación de cristales de hielo. Obligatorio en aviones militares; los jets civiles suelen utilizar calentadores de combustible en su lugar.

## Componentes del Sistema

- **Bombas:**
    - **Bombas Booster de Baja Presión (AC):** Bombas centrífugas ubicadas en los tanques. Presurizan las líneas de combustible para prevenir el **vapor lock** y la **cavitación** en la entrada de la bomba de alta presión accionada por el motor.
    - **Bomba de Alta Presión (HP):** Accionada por el motor. Si fallan las bombas booster, la bomba HP a menudo puede "succionar" combustible (alimentación por gravedad), pero las operaciones están restringidas.
    - **Bomba DC:** Utilizada principalmente para suministrar combustible a la **APU** para el arranque.
- **Válvula de Alimentación Cruzada (Crossfeed):**
    - **Propósito:** Permite que **cualquier tanque de combustible alimente a cualquier motor**. Mantiene la estabilidad y el equilibrio de la aeronave.
    - **Operación para Equilibrar:** Para corregir un desequilibrio (por ejemplo, poco combustible en el tanque izquierdo), el piloto **abre la válvula de alimentación cruzada** y apaga (**OFF**) las bombas en el tanque bajo (izquierdo). Los motores se alimentarán entonces de las bombas del tanque alto (derecho).
- **Respiraderos (Vents):**
    - Permiten que entre aire para reemplazar el combustible consumido y evitar el vacío.
    - A menudo utilizan **aire ram** para proporcionar una pequeña presión positiva a las bombas.
- **Deflectores (Baffles):**
    - Barreras internas para evitar que el combustible se "agite" (sloshing) durante las maniobras, lo que podría causar cambios rápidos en el CG o dejar las bombas sin suministro.

## Características Avanzadas

- **Tanques de Compensación (Trim Tanks):**
    - Ubicados en la **cola** (estabilizador horizontal).
    - El combustible se transfiere hacia atrás para mover el CG hacia atrás durante el crucero.
    - **Beneficio:** Reduce la fuerza aerodinámica hacia abajo requerida de la cola, reduciendo así la **resistencia de compensación** (trim drag) y el consumo de combustible.
- **Descarga de Combustible (Jettison):**
    - Permite a la tripulación reducir el peso de la aeronave al **Peso Máximo de Aterrizaje** rápidamente en una emergencia (por ejemplo, fallo del motor poco después del despegue).
