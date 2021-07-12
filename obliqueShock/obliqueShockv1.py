import numpy as np
import matplotlib.pyplot as plt
pi = np.pi

def calc_beta(Ma1, sigma, gamma):
    tan_beta=2.*(Ma1*Ma1* np.sin(sigma)*np.sin(sigma) - 1.) / (np.tan(sigma) *(Ma1*Ma1 * (gamma + np.cos(2*sigma)) + 2))
    beta = np.arctan(tan_beta)
    return beta

def calc_Ma2(Ma1, sigma, beta, gamma):
    Ma2 = 1 / np.sin(sigma - beta) * np.sqrt(
            (2+(gamma-1)*Ma1*Ma1*np.sin(sigma)**2) /
            (2*gamma*Ma1*Ma1*np.sin(sigma)**2 - (gamma - 1)))
    return Ma2

# def sigma(Ma1, beta, weakOrStrong, gamma):
#     # finding root iterative ...
#     sigma =...
#     return sigma

def calc_p02dp01(Ma1n,gamma):
    p02d01 = (1+2*gamma/(gamma+1)*(Ma1n*Ma1n-1))**(-1/(gamma-1))*(
            (gamma+1)*Ma1n*Ma1n / ((gamma-1)*Ma1n*Ma1n+2))**(gamma/(gamma-1))
    return p02d01


# INPUT
Ma1 = 2.0
gamma = 1.4
sigma = 40*pi/180 # shock-Angle
# beta=10.6229096 # turn-angle 
# Ma2=1.61731882

# ----------------Calculation--------------------------------
# shock
beta = calc_beta(Ma1, sigma, gamma)
Ma2 = calc_Ma2(Ma1, sigma, beta, gamma)
Ma1n = Ma1*np.sin(sigma)
Ma2n = Ma2*np.sin(sigma-beta)
p02dp01 = calc_p02dp01(Ma1n, gamma)

print("beta = ", beta*180/pi)
print("Ma2 = ", Ma2)
print("Ma1n = ", Ma1n)
print("Ma2n = ", Ma2n)
print("p02/p01 = ", p02dp01)


# ----------------- PLOTTING ----------------------------------

# Figure 1
fix, ax = plt.subplots(figsize=(8,8))

# geometry
height=np.sin(beta)
pts_x=[-2, 0, 1, 2]
pts_y=[0, 0, height, height]
ax.plot(pts_x, pts_y, label='wall', color='black')

# Shock
ax.plot([0,np.cos(sigma)*3], [0, np.sin(sigma)*3], 'r-.', label='shock')

# 
pointX = 0.5
pointY = 0.5*np.sin(sigma)/np.cos(sigma)
ax.plot(pointX, pointY, 'b*', label='Point ')

X = np.array((pointX-Ma1))
Y= np.array((pointY))
U = np.array((Ma1))
V = np.array((0))

q = ax.quiver(X, Y, U, V,units='xy' ,scale=1)



# V = np.array([[1,1], [-2,2], [4,-7]])
# origin = np.array([[0, 0, 0],[0, 0, 0]]) # origin point
# 
# plt.quiver(*origin, V[:,0], V[:,1], color=['r','b','g'], scale=21)
ax.axis('equal')
ax.set_xlim(-2,2)
# ax.set_ylim(-0.1,2)
plt.show()
