#!/usr/bin/python3

"""

Case-Information for: 
https://turbmodels.larc.nasa.gov/flatplate.html

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
Ma = 0.2
Re = 5.0e6
Length = 1.0
T = 540.0 * 5.0/9.0

intensity = 0.039
muratio = 0.009

# CALCULATION
sonicSpeed = np.sqrt(gamma * gasConst * T)
U_inf = Ma * sonicSpeed
I_inf = intensity / 100.0
nu = U_inf * Length / Re
mu = mu_ref * (T / T_ref)**(1.5) * (T_ref + S) / (T + S)
rho = mu / nu
p = rho * gasConst * T
Tt = T * (1 + (gamma - 1) / 2 * Ma**2)
pt = p * (1 + (gamma - 1) / 2 * Ma**2)**(gamma / (gamma - 1))
k_inf = 3.0 / 2.0 * U_inf**2 * I_inf**2
ep_inf = Cmu * rho * k_inf**2 / mu / muratio
om_inf = rho * k_inf / mu / muratio
turbLengthscale = Cmu**(0.75) * k_inf**(1.5) / ep_inf

# OUTPUT
table = []
table.append(['gamma', gamma, '[-]'])
table.append(['Cp', Cp, '[J/kgK]'])
table.append(['R', gasConst, '[J/kgK]'])
table.append(['Temperature', T, '[K]'])
table.append(['speed of sound', sonicSpeed, '[m/s]'])
table.append(['Machnumber', Ma, '[-]'])
table.append(['U_inf', U_inf, '[m/s]'])
table.append(['Reynoldsnumber', Re, '[-]'])
table.append(['kin. Viscosity', nu, '[m2/s]'])
table.append(['dyn. Viscosity', mu, '[kg/ms]'])
table.append(['density', rho, '[kg/m3]'])
table.append(['pressure', p, '[Pa]'])
table.append(['total pressure', pt, '[Pa]'])
table.append(['total temperature', Tt, '[K]'])

table.append(['turbulent Intensity', intensity, '[%]'])
table.append(['mut/mu', muratio, '[-]'])
table.append(['turbulent length', turbLengthscale, '[m]'])
table.append(['k_inf', k_inf, '[m2/s2]'])
table.append(['epsilon_inf', ep_inf, '[m2/s3]'])
table.append(['omega_inf', om_inf, '[1/s]'])

headers = ['quantity', 'value', 'unit']
print(tabulate(table, headers, tablefmt="github", floatfmt=".10f"))

