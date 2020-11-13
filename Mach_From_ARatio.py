"""
Created on Tue Oct  6 12:39:49 2020

@author: max
"""

# import matplotlib
# import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# from calcMachnumberFromAreaRatio import findMforARatio

###########################################################################
# geometry:

A_star = 0.965066
# A_star = 1.0

x = np.linspace(0.0, 10.0, 101)

area = []
for i in x:
    if i < 5.0:
        area.append(1.75 - 0.75 * np.cos( ( 0.2 * i - 1.0 ) * np.pi ))
    else:
        area.append(1.25 - 0.25 * np.cos( ( 0.2 * i - 1.0 ) * np.pi ))

area = np.array(area)

ARatio = area / A_star

# plt.plot(x, Aratio)
# plt.show()


#################################################################################
###############
#  FUNCTIONS: AM_EQN findMforARatio
###############
#################################################################################

def AM_EQN(M, ARatio):
    # constants
    g   = 1.4
    gm1 = g - 1
    gp1 = g + 1
    return np.sqrt((1/M**2)*(((2 + gm1 * M**2) / gp1)**(gp1 / gm1))) - ARatio

def findMforARatio(ARatio):
    
    if (ARatio == 1.0):
        ARatio = 1.0
        Msub = 1.0
        Msup = 1.0
        return ARatio, Msub, Msup
    
    # A_Ratio = ARatio
    errTol = 1e-5
    
    # Initial values
    dM       = 0.1
    M        = 1e-6
    
    #  Iterate to solve for root
    iterMax = 100
    stepMax = 100
    
    for i in range(1, iterMax, 1):
        for j in range(1, stepMax, 1):
            fj = AM_EQN(M, ARatio)
            fjp1 = AM_EQN(M + dM, ARatio)
                
            # Update M depending on sign change or not
            # - If no sign change, then we are not bounding root yet
            # - If sign change, then we are bounding the root, update dM
            if (fj * fjp1 > 0):
                M = M + dM
            else:
                dM = dM * 0.1
                break
            # END: j Loop
        
        if (abs(fj-fjp1) <= errTol):
            break
    # END: i Loop
    
    Msub = M
    
    ## SUPERSONIC INCREMENTAL SEARCH
    
    # Initial values
    dM       = 1
    M        = 1 + 1e-6
    
    #  Iterate to solve for root
    iterMax = 100
    stepMax = 100
    
    for i in range(1, iterMax, 1):
        for j in range(1, stepMax, 1):
            fj = AM_EQN(M, ARatio)
            fjp1 = AM_EQN(M + dM, ARatio)
            
            # Update M depending on sign change or not
            # - If no sign change, then we are not bounding root yet
            # - If sign change, then we are bounding the root, update dM
            if (fj * fjp1 > 0):
                M = M + dM
            else:
                dM = dM * 0.1
                break
            
            # END: j Loop
        
        if (abs(fj - fjp1) <= errTol):
            # iConvSub = i
            break
        
    # END: i Loop
    
    Msup = M
    
    # result = np.array([ARatio, Msub, Msup])
    return ARatio, Msub, Msup


###########################################################################


data = np.empty((0,3), float)
for i in ARatio:
    ARatio, Msub, Msup = findMforARatio(i)
    data = np.append(data, np.array([[ARatio,Msub,Msup]]), axis=0)

dataset = pd.DataFrame({'x': x, 'area': data[:,0], 'Mach_subsonic' : data[:,1], 'Mach_supersonic' : data[:,2]})
# print(dataset)
dataset.to_csv(r'points.csv', index = False, header=True)
