import numpy as np
import matplotlib.pyplot as plt
from regula_falsi import *

pi = np.pi

"""
IMPORTANT: Here

BETA := deflection angle
SIGMA := shock angle

"""

def calc_beta(Ma1, sigma, gamma=1.4):
    sigma = sigma * pi/180
    tan_beta=2.*(Ma1*Ma1* np.sin(sigma)*np.sin(sigma) - 1.) / (np.tan(sigma) *(Ma1*Ma1 * (gamma + np.cos(2*sigma)) + 2))
    beta = np.arctan(tan_beta)
    return beta * 180/pi

def calc_Ma2(Ma1, sigma, beta, gamma=1.4):
    sigma = sigma * pi/180
    beta = beta * pi/180
    Ma2 = 1 / np.sin(sigma - beta) * np.sqrt(
            (2+(gamma-1)*Ma1*Ma1*np.sin(sigma)**2) /
            (2*gamma*Ma1*Ma1*np.sin(sigma)**2 - (gamma - 1)))
    return Ma2



# def calc_sigma(Ma1, beta, weakOrStrong, gamma=1.4):
#     beta = beta * pi / 180
#     # finding root iterative ...
# 
#     sigma = regula_falsi(calc_beta, 
#     return sigma * 180 / pi

# def calc_betaMax_sigMin(Ma1, gamma):
#     # TODO: not very efficient and accurate!
#     sigMax = 90
#     sigMin = np.arcsin(1/Ma1)*180/pi
# 
#     sigma = np.linspace(sigMin,sigMax,100)
#     list_beta = calc_beta(Ma1, sigma)
#     betaMax = max(list_beta)
#     return betaMax, sigMin

def calc_betaMax_sigMin(Ma1, gamma):
    error = 1e-4
    iterMax = 40
    dSig = 10
    betaMin = 0.
    betaMax = 46.
    sigMax = 90
    sigMin = np.arcsin(1/Ma1)*180/pi

    sigma_i = sigMin
    for i in range(1,iterMax):
        beta_i = calc_beta(Ma1, sigma_i)
        beta_ip1 = calc_beta(Ma1, sigma_i + dSig)

        if (beta_ip1 < beta_i):
            betaMax = beta_i
            dSig = dSig * 0.1
            # print("betaMax = {}, Sigma-Schritt = {}".format(betaMax, dSig))
            if (dSig < error): 
                # print("({} iter)".format(i))
                break
        else:
            sigma_i = sigma_i + dSig

    return betaMax, sigMin

def calc_p02dp01(Ma1n,gamma):
    p02d01 = (1+2*gamma/(gamma+1)*(Ma1n*Ma1n-1))**(-1/(gamma-1))*(
            (gamma+1)*Ma1n*Ma1n / ((gamma-1)*Ma1n*Ma1n+2))**(gamma/(gamma-1))
    return p02d01


# INPUT
Ma1 = 2.0
sigma = 40 # shock-Angle
gamma = 1.4
print("INPUT: Ma1 = {:.02f}, sigma = {:.02f}, gamma = {:.02f}".format(Ma1, sigma, gamma))
#TEST:
# print(calc_betaMax_sigMin(Ma1,gamma))
# print(calc_betaMax_sigMin(Ma1,gamma))
# beta=10.6229096 # turn-angle 
# Ma2=1.61731882

# ----------------Calculation--------------------------------
# shock
beta = calc_beta(Ma1, sigma, gamma)
Ma2 = calc_Ma2(Ma1, sigma, beta, gamma)
Ma1n = Ma1*np.sin(sigma*pi/180)
Ma2n = Ma2*np.sin((sigma-beta)*pi/180)
p02dp01 = calc_p02dp01(Ma1n, gamma)

print("beta = ", beta)
print("Ma2 = ", Ma2)
print("Ma1n = ", Ma1n)
print("Ma2n = ", Ma2n)
print("p02/p01 = ", p02dp01)


# # ----------------- PLOTTING ----------------------------------
# 
# # Figure 1
# fix, ax = plt.subplots(figsize=(8,8))
# 
# # geometry
# height=np.sin(beta)
# pts_x=[-2, 0, 1, 2]
# pts_y=[0, 0, height, height]
# ax.plot(pts_x, pts_y, label='wall', color='black')
# 
# # Shock
# ax.plot([0,np.cos(sigma)*3], [0, np.sin(sigma)*3], 'r-.', label='shock')
# 
# # 
# pointX = 0.5
# pointY = 0.5*np.sin(sigma)/np.cos(sigma)
# ax.plot(pointX, pointY, 'b*', label='Point ')
# 
# X = np.array((pointX-Ma1))
# Y= np.array((pointY))
# U = np.array((Ma1))
# V = np.array((0))
# 
# q = ax.quiver(X, Y, U, V,units='xy' ,scale=1)
# 
# 
# 
# # V = np.array([[1,1], [-2,2], [4,-7]])
# # origin = np.array([[0, 0, 0],[0, 0, 0]]) # origin point
# # 
# # plt.quiver(*origin, V[:,0], V[:,1], color=['r','b','g'], scale=21)
# ax.axis('equal')
# ax.set_xlim(-2,2)
# # ax.set_ylim(-0.1,2)
# plt.show()
