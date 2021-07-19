"""
Improved explicit equations for oblique shock relations
Mainly recieved through:

Wellmann, J. (1972). Vereinfachung von Rechnungen am schiefen Verdichtungsstoß.
Deutsche Forschungs-und Versuchsanstalt für Luft-und Raumfahrt.
"""
import math
pi=math.pi

M1 = 2.0
gamma = 1.4
beta = 10*pi/180

def calc_sigma(M1, beta, gamma=1.4):
    alpha=math.asin(1/M1)
    a=((gamma-1.)/2. + (gamma+1)/2. * math.tan(alpha)**2) * math.tan(beta)
    b=((gamma+1.)/2. + (gamma+3)/2. * math.tan(alpha)**2) * math.tan(beta)
    c=math.tan(alpha)**2
    d=math.sqrt((4*(1-3*a*b)**3)/(27*a*a*c+9*a*b-2)**2-1.)

    # (0) weak shock; (1) strong shock
    n=0

    # eq 5
    term1 = (b+9.*a*c)/(2.*(1.-3.*a*b))
    term2 = (d*(27.*a*a*c+9.*a*b-2.))/(6.*a*(1.-3.*a*b))
    term3 = math.tan(n/3 * pi + 1/3. * math.atan(1/d))

    tan_sigma = term1 - term2 * term3
    sigma = math.atan(tan_sigma)

    return sigma

def calc_beta(M1, sigma, gamma=1.4):
    # sigma = sigma * pi/180
    tan_beta=2.*(M1*M1* math.sin(sigma)*math.sin(sigma) - 1.) / (math.tan(sigma) *(M1*M1 * (gamma + math.cos(2*sigma)) + 2))
    beta = math.atan(tan_beta)
    return beta

def calc_sigma_betaMax(M1, gamma=1.4):
    # Wellmann: Maximum Wave Angle:
    alpha=math.asin(1/M1)
    result = 1./gamma*(((gamma+1)/2.-math.cos(2*alpha)) \
            - math.sqrt(gamma+1.)*math.sqrt(((gamma+1)/2. \
            - math.cos(2*alpha))**2 + gamma/4. * (3.-gamma)))
    result = math.acos(result)/2.
    return result

def calc_sigma_M2eq1(M1, gamma=1.4):
    # Wellmann: wave angle: sigma where M2=1
    alpha=math.asin(1/M1)
    result = 1/(2*gamma) * (((gamma-3.)/2.*math.sin(alpha)**2 + (gamma+1)/2.) \
            + math.sqrt(4*gamma*math.sin(alpha)**4 + ((gamma-3)/2. *math.sin(alpha)**2 \
            + (gamma+1)/2.)**2))
    result = math.asin(math.sqrt(result))
    return result

def calc_peakPoint(M1, gamma=1.4):
    sig = calc_sigma_betaMax(M1, gamma)
    beta = calc_beta(M1, sig, gamma)
    return sig, beta

def calc_M2eq1Point(M1, gamma=1.4):
    sig = calc_sigma_M2eq1(M1, gamma)
    beta = calc_beta(M1, sig, gamma)
    return sig, beta


if __name__ == '__main__':
    print("=====   TEST:    =====")
    M1 = 2.
    beta=10
    print("sigma(M1 = {}, beta = {}°) = {}".format(M1, beta, calc_sigma(M1, beta*pi/180, 1.4)*180/pi))
    print("=====   TEST:    =====")
    print("Find peak point:")
    sigMax=calc_sigma_betaMax(M1)
    print("sigma(M1 = {}, betaMax = {}".format(M1, sigMax*180/pi))
    print("betaMax(sigmaMax) = {}".format(calc_beta(M1, sigMax)*180/pi))
    print(calc_peakPoint(M1,gamma))
    print(calc_M2eq1Point(M1,gamma))
