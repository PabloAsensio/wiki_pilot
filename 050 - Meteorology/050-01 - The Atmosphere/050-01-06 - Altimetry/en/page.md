## Key Definitions

![Altimeter Settings (QNH, QFE, QNE)](https://upload.wikimedia.org/wikipedia/commons/b/bb/FL_QNE_QNH_QFE.png)

*   **True Altitude**: The actual height of the aircraft above mean sea level (MSL).
*   **Indicated Altitude**: The altimeter reading when set to the local **QNH**.
*   **Pressure Altitude**: The altimeter reading when set to standard pressure (**1013.2 hPa**). Used for flying at **Flight Levels (FL)**.
*   **QNH**: Atmospheric pressure reduced to sea level according to the standard atmosphere. When setting QNH on the ground, the altimeter indicates the **aerodrome elevation**.
*   **QFE**: Atmospheric pressure measured at the aerodrome. When setting QFE on the ground, the altimeter indicates **zero**.
*   **QFF**: Atmospheric pressure reduced to sea level considering the actual temperature.

## Altimeter Errors

The altimeter is essentially a barometer that measures pressure and converts it to altitude assuming standard conditions (ISA). If conditions are not standard, the indication will be erroneous.

![Temperature's influence on aircraft altimeters](https://upload.wikimedia.org/wikipedia/commons/2/25/Temperature%27s_influence_on_aircraft_altimeters.png)

### Pressure Error
*   **High to Low**: If you fly towards an area of lower pressure without adjusting the altimeter (keeping the previous higher setting), the altimeter will indicate a higher altitude than you actually have.
    *   *"High to Low, Look out below"* -> **True Altitude < Indicated Altitude**. (Dangerous).
*   **Low to High**: If you fly towards an area of higher pressure, the altimeter will indicate a lower altitude than actual.
    *   **True Altitude > Indicated Altitude**.

### Temperature Error
*   **Cold Air (Colder than ISA)**: The air column contracts. For the same pressure, the actual altitude is lower.
    *   *"Warm to Cold, Don't be bold"* -> **True Altitude < Indicated Altitude**. (Dangerous).
*   **Warm Air (Warmer than ISA)**: The air column expands.
    *   **True Altitude > Indicated Altitude**.

## How to Solve Altimetry Exercises

### 1. Pressure Correction
A barometric gradient of **30 ft per hPa** (or 27 ft/hPa if specified) is assumed.

$$Correction = (QNH - 1013) \times 30$$

*   If QNH > 1013: Indicated Altitude > Pressure Altitude.
*   If QNH < 1013: Indicated Altitude < Pressure Altitude.

### 2. Temperature Correction (4% Rule)
True altitude changes approximately **4% for every 10°C of ISA deviation**.

$$Temp\_Correction = 4 \times (ISA\_Deviation) \times \frac{Indicated\_Altitude}{1000}$$

*   **Warmer than ISA**: Add correction (True Alt > Indicated Alt).
*   **Colder than ISA**: Subtract correction (True Alt < Indicated Alt).

*Note: The temperature correction applies to the air column between the station (aerodrome) and the aircraft. If calculating true altitude above the ground, use (Indicated Altitude - Station Elevation) in the formula.*

### Pilot Perspective in the Aircraft: Worked Example

Here is how these corrections play out in the cockpit. Let's go through a complete exercise:

**Situation**: You are on approach to an aerodrome on a cold winter day. You have the following information:
*   Destination QNH: **1003 hPa**
*   Current Indicated Altitude: **5,000 ft** (altimeter set to QNH)
*   OAT (Outside Air Temperature): **-5°C**
*   Aerodrome elevation: **500 ft**

**Step 1 – Pressure Correction** (converting Indicated Altitude to Pressure Altitude):

$$Correction = (1003 - 1013) \times 30 = -10 \times 30 = -300 \text{ ft}$$

The QNH is below 1013, so your Pressure Altitude (with 1013 set) would be **5,300 ft**. In other words, your altimeter is *understating* how high you are in standard pressure terms.

**Step 2 – Temperature Correction** (finding True Altitude):

ISA temperature at 5,000 ft = 15 − (5 × 2) = **+5°C**  
ISA deviation = OAT − ISA = −5 − 5 = **−10°C** (colder than ISA)

$$Temp\_Correction = 4 \times (-10) \times \frac{5{,}000}{1{,}000} = -200 \text{ ft}$$

True Altitude = 5,000 − 200 = **4,800 ft**

**Cockpit interpretation**: Your altimeter reads 5,000 ft with QNH set, but you are actually at **4,800 ft** above sea level. The aerodrome is at 500 ft, so your actual clearance above terrain is only 4,300 ft — **200 ft less** than the altimeter shows. On cold days like this, always add extra safety margins above terrain.

> 💡 **Practical rule**: In low pressure and/or very cold conditions, your actual altitude is always **lower** than the indicated altitude. The altimeter "lies in your favour" on the exam, but can be dangerous in real flight.

## Transition Procedures

*   **Transition Altitude (TA)**: The altitude at or below which vertical position is controlled by reference to altitudes (QNH). When climbing and crossing the TA, change to 1013 hPa.
*   **Transition Level (TL)**: The lowest flight level available for use above the transition altitude. When descending and crossing the TL, change to QNH.
*   **Transition Layer**: The airspace between the TA and the TL.
