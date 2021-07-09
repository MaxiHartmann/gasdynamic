# myfunctions.py
import numpy as np

gamma = 1.4

def calcMachnumber(Type, value):
    if (Type==0):
        machnumber = value;
    elif (Type==1):
        TdT0 = value;
        machnumber = np.sqrt(2. / (gamma - 1.) * (1. / TdT0 - 1.));
    elif (Type==2):
        pdp0 = value;
        machnumber = np.sqrt(2. / (gamma - 1.) *
            (np.power(pdp0, (1. - gamma) / gamma) - 1.));
    elif (Type==3):
        rhodrho0 = value;
        machnumber = np.sqrt(2. / (gamma - 1.) *
            (np.power(rhodrho0, (1. - gamma) / 1.) - 1.));
    elif (Type==4):
        AdAstar = value;
        machnumber = findMaFromAratio(AdAstar, "sub");
    elif (Type==5):
        AdAstar = value;
        machnumber = findMaFromAratio(AdAstar, "sup");
    elif (Type==6):
        MachAngle = value;
        machnumber = 1. / np.sin(MachAngle * np.pi / 180.)
    elif (Type==7):
        PM_Angle = value;
        machnumber = findMaFromPM_Angle(PM_Angle)
    else:
        print("Using default: Ma = 2.0")
        print("Type = {0}, value = {1}".format(Type, value))
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

    # i = 1
    # j = 1
    # while i < iterMax:
    for i in range(1, iterMax):
        # while j < stepMax:
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
        # print("i = " + str(i) + " j= " + str(j))
        # print("Error = " + str(abs(fj - fjp1)) + "   Mach = " +str(M))

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

def calc_AdAstar(Ma):
    result = 1. / (Ma * np.power((2. / (gamma + 1.) *
        (1. + (gamma - 1.) / 2. * Ma * Ma)),
        (-(gamma + 1.) / (2. * gamma -2.))))
    return result

def calc_TdT0(Ma):
    result = (1 + (gamma - 1) / 2 * Ma**2)**(-1)
    return result

def calc_MaStar(Ma):
    result = np.sqrt(( gamma + 1.)/ (2. / (Ma*Ma) + gamma -1.))
    return result

def calc_dpd0(Ma):
    result = (1 + (gamma - 1) / 2 * Ma**2)**(-gamma / (gamma - 1))
    return result

def calc_rhodrho0(Ma):
    result = (1 + (gamma - 1) / 2 * Ma**2)**(-1 / (gamma - 1))
    return result

def calc_MachAngle(Ma):
    result = np.arcsin( 1. / Ma) * 180. / np.pi
    return result

def calc_PM_Angle(Ma):
#     result = (np.sqrt((gamma + 1.) / (gamma - 1.))
#             * np.arctan(np.sqrt((gamma - 1.) / (gamma + 1.)
#                 * (Ma * Ma - 1.))) - np.arctan(np.sqrt(Ma*Ma - 1.))) *
#         180. / np.pi
    result = (np.sqrt((gamma + 1.) / (gamma - 1.))
            * np.arctan(np.sqrt((gamma - 1.)/(gamma + 1.)
                * (Ma * Ma - 1.))) - np.arctan(np.sqrt(Ma*Ma - 1.))) * 180. / np.pi
    return result
