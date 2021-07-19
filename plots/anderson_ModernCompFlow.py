import math as m
import numpy as np

pi = m.pi
M1=2.0
beta=10*pi/180
gamma=1.4

# weak Shock (1); strong shock (0)
alpha = 1

lam=m.sqrt((M1*M1-1.)**2-3*(1.+(gamma-1)/2.*M1*M1)*\
        (1+(gamma+1)/2.*M1*M1)*m.tan(beta)**2)
X = 1./lam**3 * ((M1*M1-1)**3 - 9*(1+(gamma-1)/2.*M1*M1)*\
        (1.+(gamma-1)/2.*M1*M1+(gamma+1)/4.*M1**4)*np.tan(beta)**2)

# CORRECT:
sigma=m.atan((M1**2-1+2*lam*np.cos((4*pi*alpha+np.arccos(X))/3.))/\
        (3*(1.+(gamma-1.)/2.*M1*M1)*m.tan(beta)))

print(sigma*180/pi)
