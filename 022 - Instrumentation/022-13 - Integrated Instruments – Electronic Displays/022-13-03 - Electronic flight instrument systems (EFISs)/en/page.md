---
title: Electronic Flight Instrument Systems (EFIS)
---

**EFIS** replaces electromechanical instruments with CRT or LCD screens. The system typically consists of two main displays for each pilot: the **PFD** (Primary Flight Display) and the **ND** (Navigation Display).

### Primary Flight Display (PFD)
Combines the "Basic T" flight instruments into a single dynamic display.
*   **Layout**:
    *   **Center**: Attitude Indicator (AI) with Flight Director (FD) bars.
    *   **Left**: Airspeed Indicator (Speed Tape). Includes speed bugs ($V_1$, $V_R$, $V_2$), trend vectors, and Mach number.
    *   **Right**: Altimeter (Altitude Tape) and Vertical Speed Indicator (VSI).
    *   **Bottom Center**: Heading/Track indication (Compass Rose segment).
    *   **Top**: **FMA** (Flight Mode Annunciator) - Displays Autopilot/Autothrust status.
*   **Radio Altimeter**: Displayed below 2500 ft AGL.

### Navigation Display (ND) / EHSI
The ND displays navigation data and can be operated in various modes selected via the **EFIS Control Panel**.

#### Common Display Modes
| Mode | Description | Orientation | Features |
|---|---|---|---|
| **MAP / ARC** | Expanded view (~90° arc). Moving map. | Heading or Track Up | Waypoints, Flight Plan, **Weather**, **Terrain**, **Traffic**. Most common flight mode. |
| **VOR / ROSE** | Full 360° compass rose. | Heading Up | VOR deviation bar (RMI style). Aircraft in center. |
| **APP / ILS** | Full 360° or Expanded. | Heading Up | ILS (Loc/GS) deviation. |
| **PLAN** | Static map. | **True North Up** | Used to review the flight plan (step through waypoints). **No Weather/Terrain**. |

#### Centre (CTR) vs Expanded (EXP)
*   **CTR (Full Rose)**: Aircraft symbol in the center. 360° view.
*   **EXP (Expanded/Arc)**: Aircraft at bottom. Forward view sector. Use for better forward resolution.
*   **Weather Radar (WXR)**: Typically **cannot** be displayed in Full Rose VOR/ILS or PLAN modes. Requires an Expanded/Map mode.

### EFIS Control Panel
Allows the pilot to select:
*   **Mode**: MAP, VOR, APP, PLAN.
*   **Range**: e.g., 10, 20, 40, ... 640 NM.
*   **Overlays**: WXR (Weather), TERR (Terrain), TFC (Traffic), WPT (Waypoints), ARPT (Airports), STA (Navaids).
*   **Baro Setting**: QNH/STD.

### Standby Instruments (ISIS)
In case of total EFIS failure, **Standby Instruments** are required.
*   **ISIS** (Integrated Standby Instrument System): A single small electronic display combining Attitude, Altitude, and Airspeed.
*   **Independence**: Operates from independent pitot/static sources, gyros, and power supplies.
*   **Challenges**: Often larger parallax errors, smaller size, and harder to read than main displays.
