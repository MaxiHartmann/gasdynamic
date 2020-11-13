#!/usr/bin/python3

"""
Transsonic airfoil
RAE2822
Case-Information for: 

"""

import numpy as np

# constants: ideal Gas
T_ref = 273.15
S = 110.4
mu_ref = 1.716e-5
gamma = 1.4
gasConst = 287.058
Cp = gamma * gasConst / (gamma - 1)

# INPUT
Ma = 0.729
Re = 6.5e6
Length = 1.0 * 0.3048
T = 460.0 * 5.0/9.0
aoa = 2.92

# CALCULATION
sonicSpeed = np.sqrt(gamma * gasConst * T)
U_inf = Ma * sonicSpeed
nu = U_inf * Length / Re
mu = mu_ref * (T / T_ref)**(1.5) * (T_ref + S) / (T + S)
rho = mu / nu
p = rho * gasConst * T
Tt = T * (1 + (gamma - 1) / 2 * Ma**2)
pt = p * (1 + (gamma - 1) / 2 * Ma**2)**(gamma / (gamma - 1))

vx = np.cos(aoa * np.pi/180.0)
vy = np.sin(aoa * np.pi/180.0)
vz = 0.0

# OUTPUT
print("gamma    \t= {:02.3f}".format(gamma))
print("Cp       \t= {:02.3f}".format(Cp))
print("R       \t= {:02.3f}".format(gasConst))
print("Temperature   \t= {:02.3f}".format(T))
print("sonicSpeed   \t= {:02.3f}".format(sonicSpeed))
print("Machnumber   \t= {:02.3f}".format(Ma))
print("U_inf        \t= {:02.3f}".format(U_inf))
print("Reynoldsnumber\t= {:e}".format(Re))
print("nu           \t= {:e}".format(nu))
print("mu(T={:06.2f}K) \t= {:e}".format(T, mu))
print("density      \t= {:e}".format(rho))
print("pressure \t= {:e}".format(p))
print("Total Temperature   \t= {:02.3f}".format(Tt))
print("Total pressure   \t= {:e}".format(pt))

print("vx    \t= {:02.6f} \t {:02.6f}".format(vx, vx * U_inf))
print("vy    \t= {:02.6f} \t {:02.6f}".format(vy, vy * U_inf))
print("vz    \t= {:02.6f} \t {:02.6f}".format(vz, vz * U_inf))
