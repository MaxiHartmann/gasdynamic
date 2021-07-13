# myfunctions_normalShock.py
import numpy as np
import math

#================================Functions========================================== 
#
def calc_Ma2(Ma1, gamma=1.4):
    Ma2 = np.sqrt((1+(gamma-1.)/2.*Ma1 * Ma1) / (gamma * Ma1 * Ma1 - (gamma-1)/2.))
    return Ma2

def calc_p2dp1(Ma1, gamma=1.4):
    result = 1. + 2 * gamma / (gamma + 1.) * (Ma1 * Ma1 - 1.)
    return result

def calc_rho2drho1(Ma1, gamma=1.4):
    result = (gamma + 1.) / ((gamma - 1.) + 2. / (Ma1 * Ma1))
    return result

def calc_T2dT1(Ma1, gamma=1.4):
    result = 1. + (2. * (gamma - 1.)) / ((gamma + 1.)**2) * (gamma * Ma1 * Ma1
            + 1.) / (Ma1 * Ma1) * (Ma1 * Ma1 - 1.)
    return result

def calc_p02dp01(Ma1n, gamma=1.4):
    p02d01 = (1+2*gamma/(gamma+1)*(Ma1n*Ma1n-1))**(-1/(gamma-1))*(
            (gamma+1) * Ma1n * Ma1n / ((gamma-1)*Ma1n*Ma1n+2))**(gamma/(gamma-1))
    return p02d01

def calc_p1dp02(Ma1, gamma=1.4):
    p2dp1 = calc_p2dp1(Ma1,gamma)
    Ma2 = calc_Ma2(Ma1,gamma)
    p02dp1 = p2dp1 * (1. + (gamma - 1.) / 2. * Ma2 * Ma2)**(gamma/(gamma-1.))
    result = 1. / p02dp1
    return result

def calc_MaStar(Ma, gamma=1.4):
    result = np.sqrt(( gamma + 1.)/ (2. / (Ma*Ma) + gamma -1.))
    return result

def calc_MaFromMaStar(MaStar, gamma=1.4):
    result = np.sqrt(2. / ((gamma + 1.) / MaStar**2. - ( gamma -1.)))
    return result

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

def bisection(func, a, b, max_steps=100, tolerance=1e-5, target=0.):
    func_a = func(a) - target
    func_b = func(b) - target
 
    if (func_a * func_b >= 0):
        print("You have not assumed right a and b\n")
        return
  
    c = a
    counter = 0
    while ((b-a) >= tolerance):
 
        # Find middle point
        c = (a+b)/2
  
        func_a = func(a) - target
        func_c = func(c) - target
        # Check if middle point is root
        if (func_c == 0.0):
            break
  
        # Decide the side to repeat the steps
        if (func_c*func_a < 0):
            b = c
        else:
            a = c
        counter+=1
             
    print("The value of root is : {:.06f} ({} iter)".format(c, counter))
    return c

# ===================== different ways to get Machnumber =======================================
def calcInflowMachnumber(Type, value):
    if (Type==0):
        mach_1 = value;
        if (mach_1 < 1.):
                print("M1 must be greater than 1")
                return np.nan
    elif (Type==1):
        mach_2 = value;
        if (mach_2 < 0.37796447 or mach_2 > 1.):
                print("M2 must be between  0.37796447 and 1!")
                return np.nan
        mach_2_star = calc_MaStar(mach_2)
        mach_1_star = 1. / mach_2_star 
        mach_1 = calc_MaFromMaStar(mach_1_star)
    elif (Type==2):
        p2dp1 = value;
        if (p2dp1 <= 1.):
                print("p2/p1 must be greater than 1")
                return np.nan
        mach_1 = np.sqrt((p2dp1 - 1.) * (gamma + 1.) / (2. * gamma) + 1.)
    elif (Type==3):
        rho2drho1 = value;
        if (rho2drho1 <= 1.):
                print("rho2/rho1 must be greater than 1")
                return np.nan
        mach_1 = np.sqrt(2. / ((gamma + 1.) / rho2drho1 - (gamma - 1.)))
    elif (Type==4):
        T2dT1 = value;
        if (T2dT1 <= 1.):
                print("T2/T1 must be greater than 1")
                return np.nan
        # Solve Iterative
        mach_1 = bisection(calc_T2dT1, 1., 20., 20, 1e-6, T2dT1)
    elif (Type==5):
        p02dp01 = value;
        if (p02dp01 > 1.):
                print("p02/p01 must be between 0 and 1")
                return np.nan
        # Solve Iterative
        mach_1 = bisection(calc_p02dp01, 1., 20., 100, 1e-6, p02dp01)
    elif (Type==6):
        p1dp02 = value;
        if (p1dp02 < 0. or p1dp02 > 0.52828178):
                print("p1/p02 must be between 0 and  0.52828178")
                return np.nan
        # Solve Iterative
        mach_1 = bisection(calc_p1dp02, 1., 20., 100, 1e-6, p1dp02)
    else:
        print("Using default: Ma1 = 2.0")
        mach_1 = 2.0

    return mach_1

# ==============================================================================
# Test Programm:
# ==============================================================================

gamma = 1.4
inputType = 0
inputValue = 5.0

Ma1 = inputValue
Ma2 = calc_Ma2(inputValue)
p2dp1 = calc_p2dp1(inputValue)
rho2drho1 = calc_rho2drho1(inputValue)
T2dT1 = calc_T2dT1(inputValue)
p02dp01 = calc_p02dp01(inputValue)
p1dp02 = calc_p1dp02(inputValue)
inputValuestar = calc_MaStar(inputValue)
Ma1star = calc_MaStar(inputValue)
Ma2star = calc_MaStar(Ma2)

print("Ma2 = {:.05f}".format(Ma2))
print("p2/p1 = {:.05f}".format(p2dp1))
print("rho2/rho1 = {:.05f}".format(rho2drho1))
print("T2/T1 = {:.05f}".format(T2dT1))
print("p02/p01 = {:.05f}".format(p02dp01))
print("p1/p02 = {:.05f}".format(p1dp02))
print("Ma1* = {:.05f}".format(Ma1star))
print("Ma2* = {:.05f}".format(Ma2star))

inputType = 0
inputValue = Ma1
print("Ma1 = {:.05f}".format(calcInflowMachnumber(inputType, inputValue)))

inputType = 1
inputValue = Ma2
print("Ma1 = f(Ma2) = {:.05f}".format(calcInflowMachnumber(inputType, inputValue)))

inputType = 2
inputValue = p2dp1
print("Ma1 = f(p2/p1) = {:.05f}".format(calcInflowMachnumber(inputType, inputValue)))

inputType = 3
inputValue = rho2drho1
print("Ma1 = f(rho2/rho1) = {:.05f}".format(calcInflowMachnumber(inputType, inputValue)))

inputType = 4
inputValue = T2dT1
print("Ma1 = f(T2/T1) = {:.05f}".format(calcInflowMachnumber(inputType, inputValue)))

inputType = 5
inputValue = p02dp01
print("Ma1 = f(p02/p01) = {:.05f}".format(calcInflowMachnumber(inputType, inputValue)))

inputType = 6
inputValue = p1dp02
print("Ma1 = f(p1/p02) = {:.05f}".format(calcInflowMachnumber(inputType, inputValue)))
