import math
import matplotlib.pyplot as plt
import numpy as np
pi = np.pi



# list_secant = []
# list_regula_falsi = []
# list_bisection = []


def secant(func, a, b, max_steps=100, tolerance=1e-5, target=0.):
    func_a = func(a) - target
    func_b = func(b) - target
    if(abs(func_a-func_b) < 1e-4):
        print("Error: Secant-Method, f(a)=f(b)")

    iteration_counter = 0
    list_secant = []
    while abs(func_b) > tolerance and iteration_counter < max_steps:
        try:
            x = b - float(func_b) * (b-a) / (func_b - func_a)
        except ZeroDivisionError:
            print("Error! - denominator zero for x = ", x)
            sys.exit(1)     # Abort with error
        a = b
        b = x
        func_a = func_b
        func_b = func(b)-target
        iteration_counter += 1
        
        list_secant = np.append(list_secant, x)
    # Here, either a solution is found, or too many iterations
    if abs(func_b) > tolerance:
        iteration_counter = -1
    return x, iteration_counter, list_secant

def calc_beta(sigma):
    Ma1 = 2.0
    gamma = 1.4
    sigma = sigma * pi/180
    tan_beta=2.*(Ma1*Ma1* np.sin(sigma)*np.sin(sigma) - 1.) / (np.tan(sigma) *(Ma1*Ma1 * (gamma + np.cos(2*sigma)) + 2))
    beta = np.arctan(tan_beta)
    return beta * 180/pi

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
    list_regula_falsi = []
    x = 0.0
    i = 0
    for loopCount in range(max_steps):
        func_a = func(a) - target
        func_b = func(b) - target
        x = b - func_b * (a-b) / (func_a-func_b)
        x = b - func_b * (b-a) / (func_b-func_a)
        # print("Current approximation is {:.05f}".format(x))
        i += 1
        list_regula_falsi.append(x)
        if math.copysign(func_a, func_b) != func_a:
            b = x
        else:
            a = x
        if abs(func(x)-target) < tolerance:
            # print ("Root is {:.05f} ({} iterations)".format(x, loopCount))
            return x, i, list_regula_falsi
        # print("Root find cancelled at {:.05f} ({} iterations)".format(x, loopCount))
    return x, i, list_regula_falsi

def samesign(a, b):
    return a * b > 0

def bisection(func, a, b, max_steps=100, tolerance=1e-5, target=0.):
    'Find root of continuous function where f(low) and f(high) have opposite signs'
    list_bisection = []

    # assert not samesign(func(a)-target, func(b)-target)

    for i in range(max_steps):
        midpoint = (a + b) / 2.0
        list_bisection.append(midpoint)
        if samesign(func(a)-target, func(midpoint)-target):
            a = midpoint
        else:
            b = midpoint

        if (abs(func(midpoint)-target) < tolerance):
            return midpoint, i, list_bisection

    return midpoint, i, list_bisection
# TEST:
#
aim=22
Ma1=2
sigMin = np.arcsin(1/Ma1)*180/pi

print("regula-Falsi-Method:")
m1, i1, listRegula = regula_falsi(calc_beta, a=sigMin, b=65, max_steps=100, tolerance=1e-8, target=aim)
print(m1, i1)

print("Secant-Method:")
m2, i2, listSecant = secant(calc_beta, a=sigMin, b=65, max_steps=100, tolerance=1e-8, target=aim)
print(m2, i2)

print("Bisection-Method:")
m3, i3, listBisection = bisection(calc_beta, a=sigMin, b=65, max_steps=100, tolerance=1e-8, target=aim)
print(m3, i3)


# PLOT
import matplotlib.pyplot as plt

x = np.linspace(sigMin, 90, 100)
plt.plot(x, calc_beta(x)) 


listBisection = np.array(listBisection)
listSecant = np.array(listBisection)
listRegula = np.array(listRegula)



plt.plot(listBisection, calc_beta(listBisection),'rx', label='bisection ({} iter.)'.format(i1))
plt.plot(listSecant, calc_beta(listSecant),'gx', label='secant ({} iter.)'.format(i2))
plt.plot(listRegula, calc_beta(listRegula),'bx', label='Regula-Falsi ({} iter.)'.format(i3))
plt.legend()
plt.xlim(30, 70)
plt.ylim(10, 30)
plt.show()
