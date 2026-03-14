---
title: "Distribución"
description: "Barras colectoras, sistemas de bus dividido frente a paralelo, conversión DC/AC y escenarios de fallo."
---

### Barras Colectoras (Bus Bars)

*   **Definición**: Barras de cobre gruesas que actúan como punto de distribución central para la energía eléctrica.
*   **Función**: Simplifica el cableado (más ligero que cables individuales a cada consumidor). Recolecta energía de fuentes y la distribuye a consumidores.
*   **Consumidores**: Conectados en **paralelo** (aislar uno no afecta a otros).
*   **Protección**: Protegida por disyuntores.
    *   **Cortocircuito en Barra Colectora**: Si una barra colectora falla (cortocircuito), su protección la aísla. **Todos los consumidores en esa barra pierden energía por el resto del vuelo.**

### Sistemas de Distribución

#### Sistema de Bus Dividido (Split Bus)
*   **Operación Normal**: Cada generador alimenta su **propia** barra de AC dedicada. Las fuentes están **aisladas** (nunca en paralelo).
*   **Configuración Típica**: Aeronaves modernas bimotores.
*   **Fallo de Generador**:
    1.  Se abre el GCB (Disyuntor del Generador) del generador fallido.
    2.  Se cierra el BTB (Disyuntor de Enlace de Bus).
    3.  **Resultado**: El generador restante que funciona alimenta **AMBAS** barras colectoras. (O la APU se hace cargo del lado fallido).
    4.  Puede ocurrir desconexión de carga debido a la capacidad de una sola fuente.

#### Sistema de Bus Paralelo
*   **Operación Normal**: Todos los generadores alimentan una red de distribución común (bus de sincronización).
*   **Requisito**: Los generadores deben estar **en paralelo** (Sincronizados).
*   **Condiciones para el Paralelismo**:
    *   Igual **Voltaje**.
    *   Igual **Frecuencia**.
    *   Igual **Secuencia de Fase**.
*   **Fallo de Generador**: Se abre el GCB del generador fallido. Los generadores restantes continúan alimentando todos los buses (la carga se comparte entre las fuentes restantes).

### Tipos de Buses

*   **AC BUS**: Distribución principal para cargas AC.
*   **DC BUS**: Distribución principal para cargas DC (alimentadas por TRUs).
*   **ESSENTIAL BUS**: Alimenta sistemas críticos. Puede ser alimentado por fuentes de emergencia (por ejemplo, baterías/inversor) si falla la alimentación principal.
*   **HOT BATTERY BUS (Bus Directo)**:
    *   **Directamente** conectado a la batería.
    *   **Siempre** alimentado (incluso cuando la aeronave está sin energía).
    *   Alimenta elementos vitales (por ejemplo, extintores de incendios, relojes).

### Conversión de Energía

*   **TRU (Unidad Transformadora Rectificadora)**:
    *   **AC $\rightarrow$ DC**.
    *   Reduce el voltaje (115V $\rightarrow$ 28V).
*   **Inversor (Inversor Estático)**:
    *   **DC $\rightarrow$ AC**.
    *   Usado para alimentar cargas *AC Esenciales* desde baterías en una emergencia (Fallo total de AC).
*   **Carga de Baterías**: Las baterías (DC) se cargan mediante el Bus DC (alimentado por TRUs).

### Contactores y Reconfiguración (Lógica)

*   **Energía Externa**: Puede alimentar buses principales en tierra a través de Contactores de Energía Externa.
*   **APU**: Puede alimentar buses principales (reemplaza a los generadores principales).
*   **Cross-Tie (X-TIE)**: Permite que el bus DC de un lado alimente el bus DC del otro lado (si falla un TRU).
*   **Configuración de Emergencia**:
    *   Pérdida de todos los generadores $\rightarrow$ Baterías alimentan **DC ESS BUS** $\rightarrow$ Inversor Estático alimenta **AC ESS BUS**.

### Sistemas de Protección

Los sistemas eléctricos monitorean y protegen contra:
*   Sobrevoltaje
*   Subvoltaje
*   Sobrecorriente
*   Sobrevelocidad (IDG/CSD)
*   Subfrecuencia
