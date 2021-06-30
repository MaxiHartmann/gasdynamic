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
# Ma = 2.0
Ma = float(input("Enter Machnumber: "))

# CALCULATION
MaStar = np.sqrt( ( gamma+1.)/ (2. / (Ma*Ma) + gamma -1.))
TRatio = (1 + (gamma - 1) / 2 * Ma**2)**(-1)
pRatio = (1 + (gamma - 1) / 2 * Ma**2)**(-gamma / (gamma - 1))
rhoRatio = (1 + (gamma - 1) / 2 * Ma**2)**(-1 / (gamma - 1))
A_Astar = 1. / (Ma * (2/(gamma + 1) * (1 + (gamma-1)/2 * Ma**2))**(-(gamma+1)/(2*(gamma-1))))
MachAngle = np.arcsin( 1. / Ma) * 180. / np.pi
PM_angle = (np.sqrt((gamma + 1.) / (gamma - 1.)) 
        * np.arctan(np.sqrt((gamma - 1.)/(gamma + 1.) 
            * (Ma * Ma - 1.))) - np.arctan(np.sqrt(Ma*Ma - 1.))) * 180. / np.pi
T_Tstar = 1. / (Ma / MaStar)**2
rho_rhoStar = 1. / A_Astar * (1./MaStar)
p_pstar = rho_rhoStar * T_Tstar

# OUTPUT
print("Ma       = {:.04f}".format(Ma))
print("Ma*      = {:.04f}".format(MaStar))
print("Mach-angle = {:.05f}".format(MachAngle))
print("PM-angle = {:.05f}".format(PM_angle))
print("p/pt     = {:.05f}".format(pRatio))
print("rho/rhot = {:.05f}".format(rhoRatio))
print("T/Tt     = {:.05f}".format(TRatio))

print("p/p*     = {:.05f}".format(p_pstar))
print("rho/rho* = {:.05f}".format(rho_rhoStar))
print("T/T*     = {:.05f}".format(T_Tstar))
print("A/A*     = {:.05f}".format(A_Astar))

