"""
http://www.i-asem.org/publication_conf/anbre15/T2I.5.AS502_1358F1.pdf
"""
# M1: inflow-Machnumber
# beta: Deflection-Angle
# sigma: Shock-Angle

import math
pi = math.pi

# Analytical Solution

M1 = 2.0
beta = 10 * pi/180
gamma = 1.4

# eq. 2
b = -((M1 * M1 + 2)/(M1 * M1) + gamma * math.sin(beta) * math.sin(beta))
c = (2 * M1 * M1 + 1) / M1**4 + ((gamma + 1)**2 / 4 + (gamma - 1) / M1**2) * math.sin(beta)**2
d = - math.cos(beta)**2 / M1**4


v = (3 * d - b*b) / 9
w = (9 * b * c - 27 * d - 2 * b * b) / 54
D = v * v * v + w * w

print("v = {}, w = {}, D = {}".format(v, w, D))

delta = 0

# error -D is negativ and phi is complex
phi = 1/3 * (math.atan(math.sqrt(-D) / w + delta))
xs = -b / 3 + 2 * math.sqrt(-v) * math.cos(phi)
xw = -b / 3 - math.sqrt(-v) * (math.cos(phi) * - math.sqrt(3) * math.sin(phi))

# eq. 3a
beta_s = math.atan(math.sqrt(xs / (1 - xs)))

# eq. 3b
beta_w = math.atan(math.sqrt(xw / (1 - xw)))


#================================================================================#
# Wellmann 1972
#================================================================================#


