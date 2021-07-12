import math
import matplotlib.pyplot as plt
import numpy as np


def regula_falsi(func, a, b, max_steps=100, tolerance=1e-5):
    '''Calculate the zero crossings of a function:
    Inputs:
        func: Function(x)
        a,b :  Boundaries of search interval
        max_steps: limit for number of iterations
        tolerance: Convergence Criteria
    RETURN:
        p: Position x of func(x)=0
    HINT: 
    - Finds only one position
    - Position must be in given interval
    '''
    p = 0.0
    for loopCount in range(max_steps):
        p = b - (func(b) * ((a-b)/(func(a)-func(b))))
        print("Current approximation is {:.05f}".format(p))
        if math.copysign(func(a), func(b)) != func(a):
            b = p
        else:
            a = p
        if abs(func(p)) < tolerance:
            print ("Root is {:.05f} ({} iterations)".format(p, loopCount))
            return p
    print("Root find cancelled at {:.05f} ({} iterations)".format(p, loopCount))
    return p

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
        print("Current approximation is {:.05f}".format(x))
        if math.copysign(func_a, func_b) != func_a:
            b = x
        else:
            a = x
        if abs(func(x)-target) < tolerance:
            print ("Root is {:.05f} ({} iterations)".format(x, loopCount))
            return x
    print("Root find cancelled at {:.05f} ({} iterations)".format(x, loopCount))
    return x

def calc_PM_Angle(Ma):
    gamma=1.4
    result = (np.sqrt((gamma + 1.) / (gamma - 1.))
            * np.arctan(np.sqrt((gamma - 1.)/(gamma + 1.)
                * (Ma * Ma - 1.))) - np.arctan(np.sqrt(Ma*Ma - 1.))) * 180. / np.pi
    return result

def findMaFromPM_Angle2(PM_Angle):
    Ma_min=1.0
    Ma_max=50.0
    Ma = regula_falsi(calc_PM_Angle, Ma_min, Ma_max,30, 1e-6,PM_Angle)
    return Ma

Mach = findMaFromPM_Angle2(26.3797608)
print("Mach = ", Mach)


# TEST:
# def sinusFunction(x):
#     result = np.sin(x-1.5*np.pi)
#     return result
#
# result = regula_falsi(sinusFunction, 0., 2., 10, 1e-10)
# print("Result = {}".format(result))
#
# print(regula_falsi.__doc__)
#
# x = np.linspace(-2,3,100)
# y = sinusFunction(x)
# plt.plot(x,y)
# plt.grid()
# plt.show()
