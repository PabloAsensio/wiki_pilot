---
title: "Digital Circuits and Computers: CPU, Memory, Buses, and Processing Models"
description: "Study core digital-computing concepts used in avionics, including CPU architecture, memory types, bus design, and multitasking versus multiprocessing."
keywords:
    - "digital circuits"
    - "computer architecture"
    - "flight level"
    - "minimum speed"
---

# Digital Circuits and Computers: CPU, Memory, Buses, and Processing Models

## Computer Architecture
A computer consists of **Hardware** (physical components) and **Software** (programs).
*   **CPU (Central Processing Unit)**: The "brain" of the computer.
    *   **ALU (Arithmetic Logic Unit)**: Performs math and logic operations.
    *   **Control Unit**: Manages timing and sequencing.
    *   **Registers**: Small, high-speed memory for immediate processing.
*   **Memory**:
    *   **RAM** (Random Access Memory): Volatile (lost on power off), fast read/write.
    *   **ROM** (Read-Only Memory): Non-volatile (permanent).
    *   **Storage**: Magnetic tapes, Flash memory (USB/Chip circuits), Optical disks.

## Data Bus
A **Bus** is a communication system (wires, optical fibers) that transfers data between components.
*   **Function**:
    *   **Internal Bus**: Communication between internal components (CPU, Memory). Uses **Data**, **Address**, and **Control** buses.
    *   **External Bus**: Connects the computer to external **Peripherals** (Sensors, Displays, Printers, Keyboards).
*   **Transmission Types**:
    *   **Serial**: Data sent bit-by-bit sequentially (e.g., Ethernet). Save cabling weight.
    *   **Parallel**: Data sent simultaneously over multiple lines. Faster but requires more wires.

## Terminology
*   **Multitasking**: A single CPU executing multiple programs by rapidly switching between them (Time-sharing).
*   **Multiprocessing**: Using two or more CPUs (Hardware solution) to increase processing speed and handle larger amounts of data.
