import numpy as np
import math
import matplotlib.pyplot as plt
import isentropicFlow as isenFlow
import normalShock as ns

"""
IMPORTANT: Here

BETA := deflection angle (turn angle)
SIGMA := shock angle (wave angle)

"""


def regula_falsi(func, a, b, max_steps=100, tolerance=1e-5, target=0.):
    '''Calculate x for (f(x)-target)=0 of a function:
    Inputs:
        func: Function(x)
        a,b :  Boundaries of search interval
        max_steps: limit for number of iterations
        tolerance: Convergence Criteria
        target: target Value: f(x)-target = 0
    Returns:
        p: Position x of (func(x)-target)=0
    HINT:
    - Finds only one position
    - Position must be in given interval a,b
    '''
    x = 0.0
    for loopCount in range(max_steps):
        func_a = func(a) - target
        func_b = func(b) - target
        x = b - (func_b * ((a-b)/(func_a-func_b)))
        # print("Current approximation is {:.05f}".format(x))
        if math.copysign(func_a, func_b) != func_a:
            b = x
        else:
            a = x
        if abs(func(x)-target) < tolerance:
            # print ("Root is {:.05f} ({} iterations)".format(x, loopCount))
            return x
    # print("Root find cancelled at {:.05f} ({} iterations)".format(x, loopCount))
    return x

pi = np.pi

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

def find_sigma_12(Ma1, beta, gamma=1.4):
    ls_sigma = np.linspace(calc_sigMin(Ma1), 90, 100)
    ls_beta = calc_beta(Ma1, sigma, 1.4)





def calc_sigma(Ma1, inputType, inputValue, gamma=1.4):
    a = 0
    b = 0
    beta = inputValue
    if (inputType == 0): 
        # (beta = beta_weak)
        a = 1e-5
        b = calc_betaMax(Ma1, gamma)[1]
    elif (inputType == 1):
        # (beta = beta_strong)
        a = calc_betaMax(Ma1, gamma)[1]
        b = 90.0

    max_steps=100
    tolerance=1e-6
    target=beta
    sigma = 0.0
    for loopCount in range(max_steps):
        func_a = calc_beta(Ma1, a, gamma) - target
        func_b = calc_beta(Ma1, b, gamma) - target
        sigma = b - (func_b * ((a-b)/(func_a-func_b)))
        # print("Current approximation is {:.05f}".format(sigma))
        if math.copysign(func_a, func_b) != func_a:
            b = sigma
        else:
            a = sigma
        if abs(calc_beta(Ma1, sigma, gamma) - target) < tolerance:
            # print ("Root is {:.05f} ({} iterations)".format(sigma, loopCount))
            return sigma
    # print("Root find cancelled at {:.05f} ({} iterations)".format(sigma, loopCount))

    return sigma

def calc_betaMax(Ma1, gamma):
    error = 1e-7
    iterMax = 80
    dSig = 2
    betaMin = 0.
    betaMax = 50.
    sigMin = np.arcsin(1./Ma1)*180./pi
    sigMax = 90.

    # first estimate:
    # betaMax = max(calc_beta(Ma1, np.linspace(sigMin,sigMax, 10)))
    # sigma_betaMax = calc_sigma(betaMax)

    sigma_i = sigMin
    for i in range(1,iterMax):
        beta_i = calc_beta(Ma1, sigma_i)
        beta_ip1 = calc_beta(Ma1, sigma_i + dSig)

        if (beta_ip1 < beta_i):
            betaMax = beta_i
            dSig = dSig * 0.5
            # print("betaMax = {}, Sigma-Schritt = {}".format(betaMax, dSig))
            if (dSig < error): 
                #print("({} iter)".format(i))
                break
        else:
            sigma_i = sigma_i + dSig
            dSig = dSig * 1.5

    return betaMax, sigma_i

def calc_sigMin(Ma1):
    result = np.arcsin(1/Ma1)*180/pi
    return result

def plot():
    # Figure 1
    fix, ax = plt.subplots(figsize=(8,8))

    Mach = np.linspace(1., 2.0,11)

    for Ma1 in Mach:
        list_betaStrong = []
        list_betaWeak = []

        sigMin = calc_sigMin(Ma1)
        sigma = np.linspace(sigMin, 90, 100)

        # calc_betaMax does not work correct
        # betaMax, sigma_betaMax = calc_betaMax(Ma1, gamma)

        beta = calc_beta(Ma1, sigma, gamma)
        betaMax = max(beta)

        X = sigma
        Y = beta
        ax.plot(X, Y, label='M={}'.format(Ma1))

        ax.plot(sigma_betaMax, betaMax, 'rx')

    
    ax.set_xlim(25, 90)
    ax.set_ylim(0, 26)
    ax.set_xlabel(r"shock angle $\sigma$")
    ax.set_ylabel(r"deflection angle $\beta$")
    plt.legend()
    plt.show()


# INPUT
Ma1 = 2.0
# inputType = 0  # Ma1 and beta (weak shock)
# inputType = 1  # Ma1 and beta (strong shock)
inputType = 2    # Ma1 and sigma
# inputType = 3  # Ma1 and M1n

inputValue = 40 # sigma (shock-Angle)
gamma = 1.4
sigma=40
# print("INPUT: Ma1 = {:.02f}, sigma = {:.02f}, gamma = {:.02f}".format(Ma1, sigma, gamma))

#TEST:

# print(" Test: calc_sigma(Ma1=2, beta_weak=15)")
# print(calc_sigma(2.0, 0, 15, 1.4))
# print(" Test: calc_sigma(Ma1=2, beta_strong=15)")
# print(calc_sigma(2.0, 1, 15, 1.4))

print(" Test: calc_betaMax(Ma1=2)")
print(calc_betaMax(2.0, 1.4))
# ----------------Calculation--------------------------------
# shock
# F(Ma1, sigma) = F(2.0, 40)
beta = calc_beta(Ma1, sigma, gamma)
Ma2 = calc_Ma2(Ma1, sigma, beta, gamma)
Ma1n = Ma1*np.sin(sigma*pi/180)
Ma2n = Ma2*np.sin((sigma-beta)*pi/180)
p02dp01 = ns.calc_p02dp01(Ma1n, gamma)
T2dT1 = ns.calc_T2dT1(Ma1n, gamma)
rho2drho1 = ns.calc_rho2drho1(Ma1n, gamma)
p2dp1 = ns.calc_p2dp1(Ma1n, gamma)

# print("beta = ", beta)
# print("Ma2 = ", Ma2)
# print("Ma1n = ", Ma1n)
# print("Ma2n = ", Ma2n)
# print("p02/p01 = ", p02dp01)
# print("T2/T1 = ", T2dT1)
# print("rho2/rho1 = ", rho2drho1)
# print("p2/p1 = ", p2dp1)



# plot()
find_sigma_12(2.0, 10)
# ----------------- PLOTTING ----------------------------------

