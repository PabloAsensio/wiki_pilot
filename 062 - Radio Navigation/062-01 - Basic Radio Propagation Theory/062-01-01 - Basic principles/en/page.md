Radio navigation is based on the transmission and reception of electromagnetic waves. To understand these systems, it is crucial to master concepts such as the frequency spectrum, wave properties, and modulation methods.

## Frequency Spectrum

The electromagnetic spectrum is divided into logarithmic bands, where each band covers a frequency range starting with a value and ending at one ten times higher. All bands start with the number 3.

| Band | Frequency | Main Applications |
| :--- | :--- | :--- |
| **VLF** (Very Low Frequency) | 3 - 30 kHz | Long-range navigation (little current use). |
| **LF** (Low Frequency) | 30 - 300 kHz | **NDB / ADF**. |
| **MF** (Medium Frequency) | 300 - 3,000 kHz | **NDB / ADF**, commercial broadcasting. |
| **HF** (High Frequency) | 3 - 30 MHz | **Long-range communications** (transoceanic). |
| **VHF** (Very High Frequency) | 30 - 300 MHz | **ATC Communications**, VOR, ILS Localizer, VDF. |
| **UHF** (Ultra High Frequency) | 300 - 3,000 MHz | ILS Glide Path, DME, SSR, GNSS. |
| **SHF** (Super High Frequency) | 3 - 30 GHz | Radio Altimeter, Weather Radar, MLS. |
| **EHF** (Extremely High Frequency) | 30 - 300 GHz | Advanced satellite communications. |

**Mnemonic:** *"**V**ery **L**ovely **M**aidens **H**ave **V**ery **U**seful **S**ewing **E**quipment"*.

## Wave Properties

*   **Frequency (f):** Number of cycles per second. Measured in **Hertz (Hz)**.
*   **Wavelength ($\lambda$):** Physical distance of a complete cycle. Calculated as $\lambda = c / f$, where $c$ is the speed of light ($300,000,000$ m/s).
    *   Example: A frequency of 100 MHz has a wavelength of 3 meters.
*   **Phase Angle:** Describes the exact position within a wave cycle, measured in degrees (0° to 360°). Phase comparison is the basis for the operation of the **VOR**.

## Modulation

Modulation is the process of impressing information (modulating signal) onto a carrier wave.

1.  **Amplitude Modulation (AM):** Varies the intensity (amplitude) of the signal. Two sidebands (upper and lower) are generated.
    *   **Single Sideband (SSB):** In **HF** communications, one of the sidebands and sometimes the carrier are suppressed to save power and bandwidth.
2.  **Frequency Modulation (FM):** Varies the frequency of the carrier.
3.  **Phase Modulation (PM):** Inverts or shifts the phase of the wave. Used in systems like **MLS** and **GNSS**.

## ITU Classification

The International Telecommunication Union (ITU) uses three-character codes to classify emissions:

1.  **First character:** Type of modulation (N=None, A=Amplitude, etc.).
2.  **Second character:** Type of modulating signal (0=None, 1=Digital without subcarrier, 2=Digital with subcarrier, 3=Analog).
3.  **Third character:** Type of information (N=None, A=Aural telegraphy, E=Telephony/Voice).

**Essential codes:**
*   **N0N:** Unmodulated carrier (base signal of an NDB).
*   **A1A:** Telegraphy (Morse) by carrier interruption (old NDBs).
*   **A2A:** Telegraphy (Morse) amplitude modulated (modern NDBs, audible without BFO).
*   **A3E:** Telephony (Voice) amplitude modulated (Standard for **VHF communications**).

## Interference Phenomena

*   **Multipath Effect:** Occurs when a signal reaches the receiver via multiple paths (direct and reflected), causing confusion or errors. Affects systems like VOR, ILS, and GNSS.
*   **Fading:** Variation in the received signal strength, caused by interference, atmospheric conditions, or the multipath effect.
