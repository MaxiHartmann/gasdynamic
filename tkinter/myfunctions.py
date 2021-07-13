# myfunctions.py
import numpy as np
import math

def calcMachnumber(Type, value, gamma=1.4):
    if (Type==0):
        machnumber = value;
    elif (Type==1):
        TdT0 = value;
        if (TdT0 > 1.0):
            print('T/T0 must be between 0 and 1')
            return np.nan
        machnumber = np.sqrt(2. / (gamma - 1.) * (1. / TdT0 - 1.));
    elif (Type==2):
        pdp0 = value;
        if (pdp0 > 1.0):
            print('p/p0 must be between 0 and 1')
            return np.nan
        machnumber = np.sqrt(2. / (gamma - 1.) *
            (np.power(pdp0, (1. - gamma) / gamma) - 1.));
    elif (Type==3):
        rhodrho0 = value;
        if (rhodrho0 > 1.0):
            print('rho/rho0 must be between 0 and 1')
            return np.nan
        machnumber = np.sqrt(2. / (gamma - 1.) *
            (np.power(rhodrho0, (1. - gamma) / 1.) - 1.));
    elif (Type==4):
        AdAstar = value;
        if (AdAstar < 1.0):
            print('A/A* must be greater than 1')
            return np.nan
        machnumber = findMaFromAratio(AdAstar, "sub");
    elif (Type==5):
        AdAstar = value;
        if (AdAstar < 1.0):
            print('A/A* must be greater than 1')
            return np.nan
        machnumber = findMaFromAratio(AdAstar, "sup");
    elif (Type==6):
        MachAngle = value;
        if (MachAngle >= 90.0):
            print('Mach angle must be between 0 and 90')
            return np.nan
        machnumber = 1. / np.sin(MachAngle * np.pi / 180.)
    elif (Type==7):
        PM_Angle = value;
        if (PM_Angle >= 130.454076):
            print('Prandtl-Meyer angle must be between 0 and 130.454076')
            return np.nan
        # with regula_falsi:
        machnumber = findMaFromPM_Angle2(PM_Angle)
    else:
        print("Using default: Ma = 2.0")
        # print("Type = {0}, value = {1}".format(Type, value))
        machnumber = 2.0

    return machnumber

def findMaFromAratio(Aratio, flowType):
    dM = 0.1
    M = 1e-6

    if (flowType == "sub"):
        M = 1e-6;
        # print("Choose Ma = 1e-6 for subsonic")
    if (flowType == "sup"):
        M = 1.0;
        # print("Choose Ma = 1.0 for supersonic")

    # iterate to solve root
    iterMax = 100;
    stepMax = 100;
    errTol = 1e-5;

    for i in range(1, iterMax):
        for j in range(1, stepMax):
            fj = calc_AdAstar(M) - Aratio
            fjp1 = calc_AdAstar(M + dM) - Aratio

            # updating: depending on sign
            if (fj * fjp1 > 0):
                M = M + dM;
            else:
                dM = dM * 0.1
                break

        # checking convergence
        if (abs(fj - fjp1) <= errTol):
            break

    return M

def findMaFromPM_Angle(PM_Angle):
    dM = 0.1
    M = 1.0

    # iterate to solve root
    iterMax = 100;
    stepMax = 100;
    errTol = 1e-5;

    for i in range(1, iterMax):
        for j in range(1, stepMax):
            fj = calc_PM_Angle(M) - PM_Angle
            fjp1 = calc_PM_Angle(M + dM) - PM_Angle

            # updating: depending on sign
            if (fj * fjp1 > 0):
                M = M + dM;
            else:
                dM = dM * 0.1
                # break j-loop
                break

        # checking convergence
        if (abs(fj - fjp1) <= errTol):
            # break i-loop
            break

    return M

def findMaFromPM_Angle2(PM_Angle):
    Ma_min=1.0
    Ma_max=50.0
    Ma = regula_falsi(calc_PM_Angle, Ma_min, Ma_max,30, 1e-8, PM_Angle)
    return Ma

def calc_AdAstar(Ma, gamma=1.4):
    result = 1. / (Ma * np.power((2. / (gamma + 1.) *
        (1. + (gamma - 1.) / 2. * Ma * Ma)),
        (-(gamma + 1.) / (2. * gamma -2.))))
    return result

def calc_TdT0(Ma, gamma=1.4):
    result = (1 + (gamma - 1) / 2 * Ma**2)**(-1)
    return result

def calc_MaStar(Ma, gamma=1.4):
    result = np.sqrt(( gamma + 1.)/ (2. / (Ma*Ma) + gamma -1.))
    return result

def calc_pdp0(Ma, gamma=1.4):
    result = (1 + (gamma - 1) / 2 * Ma**2)**(-gamma / (gamma - 1))
    return result

def calc_rhodrho0(Ma, gamma=1.4):
    result = (1 + (gamma - 1) / 2 * Ma**2)**(-1 / (gamma - 1))
    return result

def calc_MachAngle(Ma):
    if(Ma < 1.0):
        print("Ma < 1.0: no P-M angle in subsonic flow")
        return np.nan
    result = np.arcsin( 1. / Ma) * 180. / np.pi
    return result

def calc_PM_Angle(Ma, gamma=1.4):
    if(Ma < 1.0):
        print("Ma < 1.0: no Mach angle in subsonic flow")
        return np.nan
    result = (np.sqrt((gamma + 1.) / (gamma - 1.))
            * np.arctan(np.sqrt((gamma - 1.)/(gamma + 1.)
                * (Ma * Ma - 1.))) - np.arctan(np.sqrt(Ma*Ma - 1.))) * 180. / np.pi
    return result


def regula_falsi(func, a, b, max_steps=100, tolerance=1e-6, target=0.):
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
        # print("Current approximation is {:.08f}".format(x))
        if math.copysign(func_a, func_b) != func_a:
            b = x
        else:
            a = x
        if abs(func(x)-target) < tolerance:
            print ("Root is {:.08f} ({} iterations)".format(x, loopCount))
            return x
    print("Root find cancelled at {:.08f} ({} iterations)".format(x, loopCount))
    return x
