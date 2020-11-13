#!/usr/bin/python3

"""
Machnumber-relation:

"""

import numpy as np

# constants: ideal Gas
gamma = 1.4
gasConst = 287.058
Cp = gamma * gasConst / (gamma - 1)

# INPUT
Ma1 = 2.0

# CALCULATION
# shock
Ma1Star = np.sqrt(((gamma + 1)/2 * Ma1**2)/(1 + (gamma - 1)/2 * Ma1**2))
Ma2Star = 1 / Ma1Star
Ma2 = Ma1 * np.sqrt((2/Ma1**2 + (gamma - 1)) / (2 * gamma * Ma1**2 - (gamma - 1)))
p2_p1 = (1 + 2*gamma / (gamma + 1) * (Ma1**2 - 1))
u2_u1 = (1 - 2 / (gamma + 1) * (1 - 1/Ma1**2))
rho2_rho1 = 1 / u2_u1
T2_T1 = p2_p1 / rho2_rho1
entropy = np.log10((1.0 + 2.0 * gamma / (gamma + 1) * (Ma1*Ma1 - 1)) * (1 - 2/(gamma - 1) * (1 - 1/Ma1**2))**gamma) # * gasConst / (gamma-1)

# OUTPUT
print("Ma1          = {:.04f}".format(Ma1))
print("Ma2          = {:.04f}".format(Ma2))
print("Ma1*         = {:.04f}".format(Ma1Star))
print("Ma2*         = {:.04f}".format(Ma2Star))
print("p2/p1        = {:.05f}".format(p2_p1))
print("u2/u1        = {:.05f}".format(u2_u1))
print("rho2/rho1    = {:.05f}".format(rho2_rho1))
print("T2/T1        = {:.05f}".format(T2_T1))
print("s2-s1        = {:.05f}".format(entropy))

