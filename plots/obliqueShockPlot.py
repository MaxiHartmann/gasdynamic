import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)

import math
import numpy as np
import wolf_1992 as os

font = {'family': 'serif',
        'color':  'darkred',
        'weight': 'normal',
        'size': 16,
        }

fix, ax = plt.subplots(figsize=(14,8))
Mach = np.linspace(1.1, 2.0, 10)
gamma = 1.4
pi = math.pi

ls_betaMax = []
ls_sigmaMax = []

for Ma1 in Mach:
    alpha=math.asin(1/Ma1)

    # Find local Maxima which separates weak and strong solution
    sigma_betaMax, betaMax = os.calc_peakPoint(Ma1, gamma)
    ax.plot(sigma_betaMax*180/pi, betaMax*180/pi, 'yx')
    ls_betaMax.append(betaMax*180/pi)
    ls_sigmaMax.append(sigma_betaMax*180/pi)

    ax.text(sigma_betaMax*180/pi-7, betaMax*180/pi,'$Ma_1={:.01f}$'.format(Ma1) , 
            size=8, color='black')

    # find points where M2 = 1
    sig, beta = os.calc_M2eq1Point(Ma1, gamma)
    ax.plot(sig*180/pi, beta*180/pi, 'bx')

    # separate sub- and super-sonic solutions of M2
    sigmaSupersonic = np.linspace(alpha, sig, 50)
    sigmaSubsonic = np.linspace(sig, pi/2, 50)

    beta=[]
    for s in sigmaSupersonic:
        beta.append(os.calc_beta(Ma1, s, gamma))
    X = np.array(sigmaSupersonic)*180/pi
    Y = np.array(beta)*180/pi
    ax.plot(X, Y, color='red', label='M1={:.01f}'.format(Ma1))

    beta=[]
    for s in sigmaSubsonic:
        beta.append(os.calc_beta(Ma1, s, gamma))
    X = np.array(sigmaSubsonic)*180/pi
    Y = np.array(beta)*180/pi
    ax.plot(X, Y, color='blue', label='M1={:.01f}'.format(Ma1))


# Line through beta_max
ax.plot(ls_sigmaMax, ls_betaMax, color='darkorange', linestyle='--')

ax.set_xlim(25, 90)
ax.set_ylim(0, 26)
ax.set_xlabel(r"shock angle $\sigma$")
ax.set_ylabel(r"deflection angle $\beta$")
ax.text(40, 16, r"$Ma_2>1$", size=16, color='darkred',
        bbox=dict(facecolor='white'))
ax.text(80, 16, r"$Ma_2<1$", size=16, color='blue',
        bbox=dict(facecolor='white'))
ax.text(40, 24, r"$weak shock$", size=16, color='darkorange',
        bbox=dict(facecolor='white'))
ax.text(80, 24, r"$strong shock$", size=16, color='darkorange',
        bbox=dict(facecolor='white'))

ax.xaxis.set_major_locator(MultipleLocator(5))
ax.xaxis.set_major_formatter('{x:.0f}')
ax.yaxis.set_major_locator(MultipleLocator(2))
ax.yaxis.set_major_formatter('{x:.0f}')
plt.grid()
plt.savefig('obliqueShockPlot.pdf')
plt.show()
