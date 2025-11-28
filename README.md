# Basic-Python-Usage-for-Chemistry-Exercises
The code aims to practice chemistry and physics exercises using Python as a calculator. There are some solutions for tasks in Python code. 
## P2.1
The rate of the reaction between $H_{2}$ and $F_{2}$ to form HF increases by a factor of 10 when the temperature is increased from $25 ^oC$ to $47 ^oC$. What is the reaction activation energy? Assume the Arhenius equation applies.
import numpy as np
import numpy as np
# The gas constant in J.K.mol-1 (4 s.f).
R = 8.314

# Convert the second temperature from degC to K.
T1, T2 = 25 + 273, 47 + 273

# Calculation the activation energy in J.mol-1.
Ea = R * np.log(10) / (1/T1 - 1/T2)
Ea
