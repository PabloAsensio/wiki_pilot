**Introducción**
Los sistemas de presurización y aire acondicionado mantienen un ambiente cómodo y seguro para los pasajeros y la tripulación. Esto implica regular la presión y la temperatura de la cabina utilizando aire suministrado por los motores o la APU.

## Aire Acondicionado (Máquina de Ciclo de Aire)

Comúnmente llamada **"Packs de Aire Acondicionado"** o **"Sistema Bootstrap"**, la Máquina de Ciclo de Aire (ACM) enfría el aire de purga caliente para su uso en la cabina.

- **Ciclo de Operación:**
    1.  **Intercambiador de Calor Primario:** El aire de purga de alta presión se enfría previamente utilizando aire ram.
    2.  **Compresor:** El aire se comprime (calentándolo nuevamente).
    3.  **Intercambiador de Calor Secundario:** Elimina el calor del aire comprimido utilizando aire ram.
    4.  **Turbina:** El aire se expande a través de la turbina, que **impulsa el compresor** y **enfría significativamente el aire**.
    5.  **Separador de Agua:** Elimina el exceso de humedad.
    6.  **Humidificador:** Puede agregar humedad para mayor comodidad antes de ingresar a la cabina.
- **Medio de Enfriamiento:** Los intercambiadores de calor utilizan **aire ram** (aire de impacto). En tierra o durante el vuelo lento, un **ventilador de enfriamiento en tierra** extrae aire a través de los conductos de aire ram para asegurar el intercambio de calor.
- **Función Principal:** Aunque tanto la presión como la temperatura descienden a través de la ACM, su propósito principal es **enfriar el aire de purga**.

## Control de Presurización

La presurización se logra suministrando una masa constante de aire a la cabina y regulando la cantidad de aire que se permite escapar.

- **Válvulas de Salida (Outflow Valves):** Son los dispositivos de control primarios.
    - **Cerrar** las válvulas reduce el flujo de salida, **aumentando la presión de la cabina** (disminuyendo la altitud de la cabina).
    - **Abrir** las válvulas aumenta el flujo de salida, **disminuyendo la presión de la cabina** (aumentando la altitud de la cabina).
- **Modos de Control:**
    - **Automático:** Un controlador electrónico envía señales a **motores AC** para posicionar las válvulas. Teóricamente, la presión de la cabina disminuye más lentamente que la presión atmosférica durante el ascenso para mantener la programación.
    - **Manual:** El piloto utiliza un circuito separado con un **motor DC** para posicionar las válvulas.
    - **Amerizaje (Ditching):** Cierra todas las válvulas para evitar la entrada de agua durante un aterrizaje en agua.
    - **Pre-Presurización:** El sistema presuriza ligeramente la cabina **en tierra** para evitar un "golpe" de presión en la rotación/despegue.

## Seguridad y Mal funcionamiento

- **Válvula de Seguridad (Alivio de Presión Positiva):** Se abre si la presión de la cabina sube demasiado en relación con el exterior (Dif. máx. + ~0.25 psi).
- **Válvula de Alivio Interior (Alivio de Presión Negativa):** Se abre si la presión exterior es mayor que la interior (por ejemplo, durante un descenso rápido), evitando daños al fuselaje por compresión.
- **Escenarios de Mal funcionamiento:**
    - **Válvula de Salida atascada en CERRADO:** La presión aumenta hasta que la **válvula de seguridad** se abre.
    - **Válvula de Salida atascada en ABIERTO en crucero:**
        - **Régimen de Ascenso de Cabina:** Aumenta.
        - **Altitud de Cabina:** Aumenta (la cabina se despresuriza).
        - **Presión Diferencial:** Disminuye (eventualmente a 0).

## Instrumentación

- **Altímetro de Cabina:** Indica la presión de la cabina como una altitud equivalente.
- **Variómetro de Cabina:** Indica la tasa de cambio de la altitud de la cabina.
- **Medidor de Presión Diferencial:** Muestra la diferencia entre la presión interna y externa.
- **Advertencias:** Las advertencias visuales y auditivas se activan si la altitud de la cabina excede **10,000 ft**.
