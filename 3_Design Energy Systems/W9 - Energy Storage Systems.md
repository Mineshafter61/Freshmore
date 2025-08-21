# W9 - Energy Storage Systems
## Terminology
- Energy is stored in **Wh** (watt-hours) but batteries are rated in **Ah** (ampere-hours, unit of charge = 3600 coulombs)
- **Depth of discharge (DOD)**: percentage of the battery that has been discharged relative to the overall capacity of the battery, **capacity discharged / total battery capacity**
- Maximum DOD recommendations: 50% for lead acid, 80% for lithium ion
- Theoretical cell voltage ($E^0_{cell}$)
- **Nominal voltage**: voltage when 50 percent of the available capacity is discharged
- **Cut-off Voltage**: minimum allowable voltage to prevent damaging the battery. It is this voltage that generally defines the “empty” state of the battery.
- **Specific energy**: energy stored per unit mass
- **Energy density**: energy stored per unit volume
- **Specific power**: maximum amount of power per unit mass
- **Power density**: maximum amoutnt of power per unit volume
- **Self-discharge rate**: Loss of capacity through reactions during the battery storage and when battery is not connected to a load
- **End-of-life**: Batteries that have reached the end of their usefulness and/or lifespan and no longer operate at sufficient capacity. Percent of capacity at EOL of battery is usually defined as 80% of original capacity.
- **Days of autonomy**: duration the battery can supply the site’s loads without any support from generation sources (e.g., cloudy days)
## Components in a Standalone PV System
1. Energy source (sun)
2. Solar Panel
3. Solar Charge Controller
4. Battery
5. Load
## Determining the Load Energy Requirement
- Li-ion batteries have higher capacity and DOD, but lead acid batteries do not need BMS and work in a wider range of temperatures (-20 to 50˚C)
- **Battery management system** (BMS) should be used for Li-ion batteries to prevent thermal runaway.
- Optimal temperature for Li-ion batteries are between **10 and 25˚C**.
- Voltage times current times time; $E=IVt$ and $P=IV$
## Battery sizing chart reference
1. Nominal system voltage:
2. Days of autonomy:
3. Total daily load (A x hour of operation/day):
4. Unadjusted battery capacity (Days of autonomy x total daily load):
5. Maximum allowable depth of discharge (MDOD): % (50% normally for Lead-acid)
6. Capacity adjusted for MDOD (Step 4 ÷ Step 5):
7. Maximum daily depth of discharge (MDDOD):
8. Capacity adjusted for MDDOD (Step 3 ÷ Step 7):
9. Percent of capacity at end of life (EOL): %
10. Capacity adjusted for EOL (Step 4 ÷ Step 9):
11. Capacity adjusted for depths of discharge or end of life (greatest of 6, 8, or 10):
12. Design margin factor (≥1): 1.1
13. Capacity adjusted for design margin (Step 11 × Step 12):
14. Determine the smallest practical capacity to meet the capacity adjusted for design margin value calculated in xiii (= Step 13):
## Solar panel sizing chart reference