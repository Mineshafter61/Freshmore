# W6 - Photovoltaic Systems

## Solar Radiation Spectrum

- Velocity, wavelength, frequency: $c=\lambda f$
- Photon energy $E=hf=\frac{hc}{\lambda}$
- Wien's displacement law $\lambda_{peak}=\frac bT$
![image](ref/solar%20irradiance.png)
- The sun emits EM radiation across most of the electromagnetic spectrum.
    - Yellow is for solar irradiance spectrum above atmosphere
    - Red is for solar irradiance spectrum on earth surface
- **Spectral irradiance** is the irradiance of a surface at a given wavelength.
- **Irradiance** is the power received per unit area.
- The **solar radiation that passes through the atmosphere** ($G_0$) is reduced to a **peak value of approximately 1 kW/m²**.

### Irradiation

- **Irradiance** is a measure of solar power per unit area at any moment in time
- **Irradiation** (Wh/m²) is the total amount of solar energy per unit area received over a given period (day, month, year) (integral of irradiance)
- **Peak sun hour (PSH)** is equivalent to the total irradiation received at the site during the day.
    - 1 peak sun hour is equivalen to 1 kWh/m²

## Solar Irradiation Variation

- Solar irradiation varies by
    - Location on globe
    - Position of sun throughout the day and year
- Considerations for the Energy/Power available for consumption
    - Weather and Climate
        - Weather affects daily short term energy collection.
        - Climate is of the average weather in a reason.
    - Tilt angle and Orientation (dependent on relative Sun's position at specific time and day in the year.)
    - Shadowing (due to surrounding buildings, vegetations, terrain etc.)

## Solar Module

- The solar irradiation provides energy in the form of photon
- The solar module (photovoltaic panel, solar panel) absorbed the photon to produce electron-hole pair that conduct electricity

### Formation of Electron-Hole Pairs with Solar Energy

- Semiconductors (p and n) have bandgap < ~5 eV.
- In the presence of light with energy greater or equal to the bandgap, electrons (e-) and holes (h+) pair form due to the absorption of photons, and electron moves into conduction band and leaves a hole in the valence band.
- Photons with energy larger than the bandgap of the semiconductor will be absorbed to create an electron-hole pair. 1 photon will generate 1 pair of electron (e-) and hole (h+).
- Electron (e-) gets excited into the conduction and leaves a hole (h+).

### Recombination

- Electrons in conduction band move in to occupy vacant sites in the valence band, i.e. electron recombines with a hole. Electron loses its energy in the form of light, or thermal energy

### Creating the Driving Force

- At 0K, all electrons are occupied in covalent bonds and are not free to move in the lattice structure.
- At T > 0K, Thermal energy can create few electron-hole pairs resulting in some electrical conduction.

## Semiconductors

- Number of electrons (n) = number of holes (p)
    - For every electron excited into conduction band, a missing electron is left behind
        - vacant electron state in valence band
    - Missing electron considered as positively charged particle called a hole, which has same magnitude of charge as an electron.

### Doping

Doping is the process of adding impurities or dopants to a pure semiconductor to generate either a surplus or a deficiency in valence electrons.

- Surplus: n type (5 valence electrons, e.g. phosporous): introduces extra electrons
    - Creates a new energy level in the energy band near the conduction band called the Donor Level
    - ![image](ref/n-doped%20semiconductor.png)
- Deficiency: p type (3 valence electrons, e.g. boron): introduces extra holes
    - Only done in the acceptor level
    - ![image](ref/p-doped%20semiconductor.png)

## p-n junction

|                          | **p-doped** | **n-doped** |
|--------------------------|-------------|-------------|
| Major charge carrier     | holes       | electrons   |
| Minor charge carrier     | electrons   | holes       |
| Overall charge           | neutral     | neutral     |

- When both p and n junctions are combined, there will be "diffusion" of electrons from n to p
- This leads to an electric field due to the separation of charges which opposes this process
    - The location containing the positive and negative ions is known as the **depletion region**
    - Re-combination of electron-hole pairs mainly happen at the depletion region
- Steady state is achieved
![image](ref/depletion%20region.png)

### The Sun

- A current can only be obtained with **mobile charge carriers** and a **driving force** (potential difference)
- At steady state, there is a PD but no longer any mobile charge carriers at the depletion region
- The sun is required to provide energy to excite more electrons from valance band to conduction band
    - This leads to electrons at the depletion region that can recombine with holes
