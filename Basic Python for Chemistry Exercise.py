#!/usr/bin/env python
# coding: utf-8

# # Basic Phyton Usage for Chemistry Exercise
# 

# ## P2.1 
# The rate of the reaction between $H_{2}$ and $F_{2}$ to form HF increases by a factor of 10 when the temperature is increased from $25 ^oC$ to $47 ^oC$. What is the reaction activation energy? Assume the Arhenius equation applies.

# In[7]:


import numpy as np
# The gas constant in J.K.mol-1 (4 s.f).
R = 8.314

# Convert the second temperature from degC to K.
T1, T2 = 25 + 273, 47 + 273

# Calculation the activation energy in J.mol-1.
Ea = R * np.log(10) / (1/T1 - 1/T2)
Ea


# ## P2.2 
# Calculate the energy (in eV) of a photon with wavelength of 450 nm. One eV is equivalent to $1.6 $ x $ 10^{-19}$ Joules.

# In[12]:


# Planck's constant, in J.s.
h = 6.626 * 10 ** -34

# Constant J_per_eV
J_per_eV = 1.6 * 10 ** -19

# Convert wavelengths nm to m.
Lambda = 450 * 10 ** -9

# Speed of light, in m.s-1.
c = 3.0 * 10 ** 8

# Calculate energy of photon in J.
Energy_J = h * c / Lambda
Energy_J


# In[13]:


# Convert energy of photon from J to eV 
Energy_eV = Energy_J /J_per_eV
Energy_eV


# ## P2.3 
# From back-scattering experimental data, the radius of an aluminum nucleus can be calculated to be approximately 5 x 10 meters. The radius of an aluminum atom is known to be 1.43 x 10 meters. Using atomic weight data from your periodic table, calculate the density of an aluminum nucleus. Express your answer in units of g/m.

# In[14]:


# Constant radius of alumunium nucleus 
R = 5 * 10 ** -15
# The mass of alumunium, in amu
m_amu = 26.98

# Constant atomic mass units to kg.
m_kg = 1.66 * 10 ** -27

# Convert mass of alumunium from amu to kg.
m = m_amu * m_kg
m


# In[15]:


# Calculate the volume of the alumunium nucleaus, in m3
V = 4 / 3 * 3.14 * (R ** 3)
V


# In[16]:


# Calculate the density of the alumunium nucleus, in g.m-1.
Rho = m / V
Rho


# ## P2.4 
# Body fat (triglyceride) has the average chemical formula $C_{55}H_{104}O_{6}$. In the absence of other mechanism (such as ketosis), its metaboilsm is essentially a low temperature combustion to form carbon dioxide and water.
# 
# Calculate the mass of $CO_{2}$ and $H_{2}O$ produced when 1 kg of fat is "burned off". Take the molar masses to be M(C) = 12 g $mol^{-1}$ and M (H) = 1 g $mol^{-1}$ and M(O) = 16 g $mol^{-1}$.
# What percentage of the original mass of fat is exhaled as $CO_{2}$?.

# The balanced chemical reaction for the metabolism of the fat $C_{55}H_{104}O_{6}$ is:
# 
# $C_{55}H_{104}O_{6}$ + $78O_{2}$ $\rightarrow$ $55CO_{2}$ + $52H_{2}O$

# In[21]:


# The molar masses of C, H and O, in g.mol-1.
M_C = 12
M_H = 1
M_O = 16

# Calculate molar masses of fatt, CO2 and H2O, in g.mol-1
M_fat = (55 * M_C) + (104 * M_H) + (6 * M_O)
M_CO2 = (1 * M_C) + (2 * M_O)
M_H2O = (2 * M_H) + (1 * M_O)

# Calculate ratio mass ratios (stoichiometry), in g.
M_fat_per_mole = 1 * M_fat
M_CO2_per_mole = 55 * M_CO2
M_H2O_per_mole = 52 * M_H2O

# Calculate mass CO2 and H2O from 1000 g of fat, in g.
M_CO2_fat = 1000 * (M_CO2_per_mole / M_fat_per_mole)
M_H2O_fat = 1000 * (M_H2O_per_mole / M_fat_per_mole)
M_CO2_fat, M_H2O_fat


# In[24]:


# Calculate percentage of original mass exhaled CO2 and H2O, in %.
Percen_CO2 = ((55 * M_C + 2/3 * 6 * M_O) / M_fat) * 100
Percen_H2O = ((104 * M_H + 1/3 * 6 * M_O) / M_fat) * 100
Percen_CO2, Percen_H2O


# ## P2.5 
# What is the boiling point of water on the summit of Mt Everest (8,849 m)?. Assume that the ambient air pressure, p, decrease with altitude, z, according to p = p0 exp(-z/H), Where p0 = 1 atm and take scale height, H to be 8 km. The molar entalpy of vaporization of water is 
# 
# $\Delta_{vap}H{m}$ = 44 kJ $mol^{-1}$
# 
# The Clausius-Clapeyron equation is:
# 
# $\frac{dlnp}{dT}$ = $\frac{\Delta_{vap}H{m}}{RT^{2}}$
# 

# In[48]:


# Constant the normal boiling point of water T1 at p 1 atm, in K.
T1 = 100 + 273

# The moalr entalphy of vaporization, in J.mol-1.
Delta_H_vap = 44 * 1000

# The ideal gas constant, in J.mol-1.K-1.
R = 8.314

# Height of Everest, in m.
z = 8849

# The height scale, in m.
H = 8 * 1000

import numpy as np
# Calculate pressure with p0 = 1 atm, in atm.
P1 = 1
P2 = P1 * np.exp(-z / H)

# Calculate Boiling point use the Clausius-Clapeyron, in K.
Boil_per_T2= (1 / T1) - ((R / Delta_H_vap) * np.log(P2 / P1))
P2, Boil_per_T2



# In[49]:


# Calculate T2, in K and convet to degC.
Boil_T2 = (1 / (Boil_per_T2)) - 273
Boil_T2


# ## P2.6
# Calculate the ionization energy (in eV) of an electron in the excited state of n = 3 in a hydrogen atom.

# In[2]:


# Rydberg's constant, in m-1.
R = 1.097 * 10 ** 7

# Planck's constant, in J.s
h = 6.626 * 10 ** -34

# Speed of light, in m.s-1
c = 3.0 * 10 ** 8

# Constant J_per_eV
J_per_eV = 1.6 * 10 ** -19

# The number or orbit
n = 3

# Calculate energy of an electron in a particular orbit n = 3, in eV.
En = -(R * h * c) / (n ** 2)
En_eV = En / J_per_eV
En_eV


# In[6]:


# Energy final, in infinite
E_final = 0

# Calculate the ionization energy
Delta_E = E_final - En_eV
Delta_E


# ## P2.7
# The pfund series of lines in the emission spectrum of hydrogen correspond to transition from higher excited states to the n = 5 orbit. Calculate the wavelength of the second line in the Pfund series to three significant figures. In which region of the spectrum does it lie?

# In[9]:


# Rydberg's constant, in m-1.
R = 1.097 * 10 ** 7

# Orbit at the second state and initial state, in orbit.
n2 = 7 ** 2
n1 = 5 ** 2

# Calculate the wavelength use the Rydberg equation, in nm.
Lambda_m = 1 / (R * ((1 / n1) - (1 /n2)))
Lambda_nm = Lambda_m * 10 ** 9
Lambda_nm


# 4.65 x $10^{3}$ nm, this wavelength is in the infrared region of the spectrum.

# In[ ]:

# ## P2.8
Determine the wavelength of radiation (in nm) emitted by a transition from n=5 to n=3 in atomic hydrogen.

# Rydberg's constant, in m-1.
R = 1.097 * 10 ** 7

# Orbit at the second state and initial state, in orbit.
n2 = 5 ** 2
n1 = 3 ** 2

# Calculate the wavelength of radiation, in nm.
lambda_m = 1/ (R * ((1/n1) - (1/n2)))
lambda_nm = lambda_m * 10 ** 9
lambda_nm
1281.9051959890614

# In[]:


# ## P2.9
Calculate the wavelenght of neutron that is moving at 3.00 x $10^{3}$ m/s.

# the speed moving of neutron, in m/s.
v = 3.00 * 10 ** 3

# Planck's constant, in J.s
h = 6.626 * 10 ** -34

# Mass of neutron, in kg.
m = 1.674929 * 10 ** -27

# Calculate the wavelength of neutron, in Angstrong.
Lambda_m = h / (m * v)
Lambda_A = Lambda_m * 10 ** 10
Lambda_pm = Lambda_m * 10 ** 12
Lambda_A, Lambda_pm
1.3186628607341964, 131.86628607341964


