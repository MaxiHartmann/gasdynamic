import numpy as np
import matplotlib.pyplot as plt

pi = np.pi

def calc_beta(Ma1, sigma, gamma=1.4):
    tan_beta=2.*(Ma1*Ma1* np.sin(sigma)*np.sin(sigma) - 1.) / (np.tan(sigma) *(Ma1*Ma1 * (gamma + np.cos(2*sigma)) + 2))
    beta = np.arctan(tan_beta)
    return beta

def calc_Ma2(Ma1, sigma, beta, gamma=1.4):
    Ma2 = 1 / np.sin(sigma - beta) * np.sqrt(
            (2+(gamma-1)*Ma1*Ma1*np.sin(sigma)**2) /
            (2*gamma*Ma1*Ma1*np.sin(sigma)**2 - (gamma - 1)))
    return Ma2

Mach = range(1,10,1)
sigma = np.linspace(1e-3,90,100) * pi/180.

fig, ax = plt.subplots()
for Ma in Mach:
    ax.plot(sigma*180/pi, calc_beta(Ma,sigma)*180/pi, label='$Ma=$' + str(Ma))

ax.set_xlim(0, 90)
ax.set_ylim(0, 56)
ax.set_xlabel(r'shock angle, $\beta$')
ax.set_ylabel('Flow Deflection angle, $\sigma$')
ax.legend()
plt.show()
