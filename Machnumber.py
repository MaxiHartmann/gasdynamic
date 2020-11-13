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
Ma = 2.0

# CALCULATION
MaStar = np.sqrt(((gamma + 1)/2 * Ma**2)/(1 + (gamma - 1)/2 * Ma**2))
tRatio = (1 + (gamma - 1) / 2 * Ma**2)**(-1)
pRatio = (1 + (gamma - 1) / 2 * Ma**2)**(-gamma / (gamma - 1))
rhoRatio = (1 + (gamma - 1) / 2 * Ma**2)**(-1 / (gamma - 1))
Aratio = Ma * (2/(gamma + 1) * (1 + (gamma-1)/2 * Ma**2))**(-(gamma+1)/(2*(gamma-1)))

# OUTPUT
print("Ma       = {:.04f}".format(Ma))
print("Ma*      = {:.04f}".format(MaStar))
print("T/Tt     = {:.05f}".format(tRatio))
print("p/pt     = {:.05f}".format(pRatio))
print("rho/rhot = {:.05f}".format(rhoRatio))
print("A/A*     = {:.05f}".format(Aratio))

