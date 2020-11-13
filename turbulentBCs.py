#!/usr/bin/python3

"""

"""

import numpy as np
from tabulate import tabulate

# constants: ideal Gas
T_ref = 273.15
S = 110.4
mu_ref = 1.716e-5
gamma = 1.4
gasConst = 287.058
Cp = gamma * gasConst / (gamma - 1)

Cmu = 0.09

# INPUT
T = 300.0
U_inf = 70.0
rho = 1.329054

intensity = 0.039 
muratio = 0.009

# CALCULATION
I_inf = intensity / 100.0
mu = mu_ref * (T / T_ref)**(1.5) * (T_ref + S) / (T + S)
nu = mu / rho

k_inf = 3.0 / 2.0 * U_inf**2 * I_inf**2
ep_inf = Cmu * rho * k_inf**2 / mu / muratio
om_inf = rho * k_inf / mu / muratio
turbLengthscale = Cmu**(0.75) * k_inf**(1.5) / ep_inf

# OUTPUT
content = []
content.append(['turbulent Intensity', intensity, '[%]'])
content.append(['mut/mu', muratio, '[-]'])
content.append(['turbulent length', turbLengthscale, '[m]'])
content.append(['k_inf', k_inf, '[m2/s2]'])
content.append(['epsilon_inf', ep_inf, '[m2/s3]'])
content.append(['omega_inf', om_inf, '[1/s]'])

print(tabulate(content, headers=['quantity', 'value', 'unit']))

