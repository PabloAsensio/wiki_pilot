---
title: "Sistemas Hidráulicos en Aeronaves: Fluidos, Bombas, Válvulas y Monitorización"
description: "Tipos de fluido hidráulico, arquitecturas de bombas, función de acumuladores y depósitos, lógica de válvulas y monitorización de presión en aeronaves modernas."
---

# Sistemas Hidráulicos en Aeronaves: Fluidos, Bombas, Válvulas y Monitorización

Los sistemas hidráulicos en aeronaves modernas son redes complejas diseñadas para transmitir fuerzas altas de manera confiable. Esta sección detalla los fluidos, componentes y principios operativos que aseguran que estos sistemas funcionen correctamente bajo todas las condiciones de vuelo.

## Fluidos Hidráulicos

Los fluidos hidráulicos son el medio para transmitir presión y energía. Su correcta selección y manejo son vitales.

- **Propiedades Ideales:**
    - **Baja Compresibilidad:** Permite una operación instantánea.
    - **Alto Punto de Inflamación / Baja Inflamabilidad:** Esencial para la seguridad contra incendios.
    - **Viscosidad:** Debe fluir fácilmente a bajas temperaturas mientras mantiene una viscosidad adecuada a altas temperaturas.
    - **Protección:** Debe proporcionar propiedades de **lubricación** y **anticorrosión** para proteger bombas y actuadores.
- **Tipos:**
    - **Base Mineral (ej. DTD 585):** Típicamente rojo. Usa sellos de goma sintética.
    - **Sintético (ej. Skydrol):** Típicamente púrpura o verde. Resistente al fuego.
    - **Advertencia:** Los diferentes tipos de fluidos **nunca deben mezclarse**, ya que esto lleva a la degradación de sellos y fugas. Los fluidos también son **corrosivos para la pintura** e irritantes para la piel/ojos.

## Bombas Hidráulicas

Las bombas generan el flujo de fluido requerido para presurizar el sistema.

- **Bomba de Presión Constante (De Demanda):** Usa un plato oscilante variable (pistón axial) para modular el volumen de salida basado en la demanda, manteniendo una presión constante del sistema. Este es el estándar para aeronaves modernas.
- **Bomba de Caudal Constante (Volumen Fijo):** Entrega un volumen fijo por giro. Requiere una **Válvula de Corte Automático (ACOV)** para regular la presión y devolver el exceso de fluido al depósito (ralentí) cuando los servicios no están en uso.
- **Bomba Manual:** A menudo usada en tierra para tareas específicas (ej. abrir puertas de carga) cuando la energía eléctrica o del motor no está disponible.
- **Turbina de Aire de Impacto (RAT):** Una bomba de emergencia que actúa como último recurso. Desplegada en vuelo, alimenta sistemas vitales (controles de vuelo) si fallan las fuentes de energía principales.

## Acumuladores

Los acumuladores son dispositivos de almacenamiento que contienen fluido hidráulico bajo presión, separados de un gas comprimido (nitrógeno) por un pistón o diafragma.

- **Funciones:**
    - **Almacenar Energía:** Proporciona un suministro limitado de fluido presurizado para operación de emergencia (ej. frenado) si falla la bomba.
    - **Amortiguar Fluctuaciones:** Suaviza los picos de presión transitorios en el sistema.
    - **Expansión Térmica:** Absorbe la expansión del fluido en sistemas cerrados.
- **Operación:** El gas está precargado. A medida que aumenta la presión del sistema, el fluido entra en el acumulador y comprime el gas hasta que las presiones se igualan.

## Depósitos y Filtros

- **Depósito:** Almacena el fluido del sistema. Usualmente está **presurizado** (a menudo por aire de purga neumático) para prevenir la **cavitación** (formación de burbujas de aire) a gran altitud y asegurar una alimentación positiva a las bombas.
    - **Tubo Vertical (Stack Pipe):** Un diseño de tubo vertical asegura que si ocurre una fuga en la línea de suministro principal, quede una reserva de fluido en el fondo del depósito específicamente para **sistemas de emergencia**.
- **Filtros:** Eliminan contaminantes. A menudo cuentan con indicadores emergentes para señalar un **bypass inminente**, advirtiendo que el filtro se está obstruyendo.

## Válvulas y Lógica de Control

- **Válvula de Alivio de Presión (PRV):** Una válvula de seguridad que limita la presión máxima del sistema ventilando el exceso de fluido de vuelta al tanque.
- **Válvula Antirretorno (NRV):** Asegura que el fluido fluya en una sola dirección (check valve).
- **Válvula Selectora:** Dirige el fluido a un lado u otro de un actuador. Atrapar fluido entre una selectora cerrada y un pistón puede causar un **Bloqueo Hidráulico**.
- **Válvula Lanzadera (Shuttle Valve):** Selecciona automáticamente la fuente de mayor presión, permitiendo que un sistema alternativo tome el control (ej. para frenos) si falla la presión primaria.
- **Fusibles:** Dispositivos de seguridad que cortan el flujo si se detecta una fuga repentina de alto volumen (caída de presión), previniendo la pérdida total de fluido del sistema.

## Monitoreo del Sistema

- **Presión Típica:** La mayoría de las aerolíneas comerciales operan a **3000 psi**.
- **Indicaciones:** Una pérdida de presión hidráulica típicamente activa una **Precaución Ámbar** (Luz Master Caution + Anunciación Low Press), requiriendo la atención de la tripulación.
- **Sobrecalentamiento:** Puede ser causado por un flujo de enfriamiento bloqueado, requiriendo que el sistema sea desenergizado.
