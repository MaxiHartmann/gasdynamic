import numpy as np

# constants: ideal Gas
T_ref = 273.15
S = 110.4
mu_ref = 1.716e-5
gamma = 1.4
gasConst = 287.058

# INPUT
# T = float(input("Enter the Temperature: "))
# p = float(input("Enter the pressure: "))
# U_ref = float(input("Enter the Velocity: "))
# Length = float(input("Enter the char. Length: "))

T = 300
p = 1e5
U_ref = 69.444
Length = 1.0

# CALCULATION
mu = mu_ref * (T / T_ref)**(1.5) * (T_ref + S) / (T + S)
rho = p / (gasConst * T)
nu = mu / rho
sonicSpeed = np.sqrt(gamma * gasConst * T)
Ma = U_ref / sonicSpeed
Re = U_ref * Length / nu

# OUTPUT
print("mu(T={:06.2f}K) \t= {:e}".format(T, mu))
print("density      \t= {:e}".format(rho))
print("nu           \t= {:e}".format(nu))
print("sonicSpeed   \t= {:e}".format(sonicSpeed))
print("Machnumber   \t= {:02.3f}".format(Ma))
print("Reynoldsnumber\t= {:e}".format(Re))
