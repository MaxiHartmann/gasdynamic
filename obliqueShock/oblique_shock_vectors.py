import numpy as np
import matplotlib.pyplot as plt
plt.rc('axes', axisbelow=True)
from math import sin, cos, tan, pi, atan, sqrt, acos, asin



def calc_Ma2(Ma1, gamma=1.4):
    result = np.sqrt((1+(gamma-1.)/2.*Ma1 * Ma1) / (gamma * Ma1 * Ma1 - (gamma-1)/2.))
    return result

def calc_sigma(g, m1, beta, i ):
    p=-(m1*m1+2.)/m1/m1-g*sin(beta)*sin(beta)
    q=(2.*m1*m1+1.)/pow(m1,4.)+((g+1.)*(g+1.)/4.+(g-1.)/m1/m1)*sin(beta)*sin(beta)
    r=-cos(beta)*cos(beta)/pow(m1,4.)

    a=(3.*q-p*p)/3.
    b=(2.*p*p*p-9.*p*q+27.*r)/27.

    test=b*b/4.+a*a*a/27.
    
    if (test>0.0): 
        print("test>0.0")
        return -1

    else:
        if (test==0.0):
            x1=sqrt(-a/3.)
            x2=x1
            x3=2.*x1
            if (b>0.0):
                x1*=-1
                x2*=-1
                x3*=-1
        if (test<0.0):
            phi=acos(sqrt(-27.*b*b/4./a/a/a))
            x1=2.*sqrt(-a/3.)*cos(phi/3.)
            x2=2.*sqrt(-a/3.)*cos(phi/3.+pi*2./3.)
            x3=2.*sqrt(-a/3.)*cos(phi/3.+pi*4./3.) 
            if(b>0.0):
                x1*=-1
                x2*=-1
                x3*=-1

        s1=x1-p/3.
        s2=x2-p/3.
        s3=x3-p/3.

        if (s1<s2 and s1<s3):
            t1=s2
            t2=s3
        elif (s2<s1 and s2<s3):
            t1=s1
            t2=s3
        else:
            t1=s1
            t2=s2

        b1=asin(sqrt(t1))
        b2=asin(sqrt(t2))

        sig_s=b1
        sig_w=b2
        if (b2>b1):
            sig_s=b2
            sig_w=b1

        if (i==0): return sig_w
        if (i==1): return sig_s


def plot_vectors(M1, beta, gamma):
    sigma = calc_sigma(gamma, M1, beta, 0) 
    
    M1n = M1 * sin(sigma)
    M1t = M1 * cos(sigma)
    
    M2n = sqrt((1. + .5 * (gamma - 1.) * M1n * M1n) / (gamma * M1n * M1n - .5 * (gamma - 1.)))
    M2 = M2n / sin(sigma-beta)
    M2t = M2 * cos(sigma-beta)
    
    # attention:    v1t == v2t,
    # but           M1t =! M2t, 
    # cause a1 =! a2 and T1 =! T2
    
    fig, ax = plt.subplots(figsize=(7,7))
    
    textstr = '\n'.join((
        r'INPUT:',
        r'$\mathrm{Ma}_1=%.2f$' % (M1, ),
        r'$\beta=%.2f$' % (beta*180/pi, )))
    props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
    ax.text(0.05, 0.6, textstr, transform=ax.transAxes, fontsize=10,
            verticalalignment='top', bbox=props)
    
    
    
    # plot wall boundary
    ramp_length=2
    h = tan(beta)*ramp_length
    right_bound = 10
    wall_xcoords = [-5, 0, ramp_length, right_bound]
    wall_ycoords = [0, 0, h, h]
    ax.plot(wall_xcoords, wall_ycoords, color='k') 
    
    # plot shock
    shock_xcoords = [0, 10*cos(sigma)]
    shock_ycoords = [0, 10*sin(sigma)]
    ax.plot(shock_xcoords, shock_ycoords, color='gray', linestyle='-', lw=0.5) 
    
    # origin should be on shock line
    orig_x = 2
    origin=[orig_x,orig_x*tan(sigma)]
    
    
    # plot: M1
    x_pos = origin[0] - M1
    y_pos = origin[1]
    x_direct = M1
    y_direct = 0
    ax.quiver(x_pos, y_pos, x_direct, y_direct, units='xy', color='red', scale=1, label='Ma')
    # plot: M1n
    x_direct = M1n*sin(sigma)
    y_direct = -M1n*cos(sigma)
    ax.quiver(x_pos, y_pos, x_direct, y_direct, units='xy', color='b', scale=1, label='Ma_n')
    # plot: M1t
    x_pos = x_pos + M1n*sin(sigma)
    y_pos = y_pos - M1n*cos(sigma)
    x_direct = M1t*cos(sigma)
    y_direct = M1t*sin(sigma)
    ax.quiver(x_pos, y_pos, x_direct, y_direct, units='xy', color='y', scale=1, label='Ma_t')
    
    # Mach2
    x_pos = origin[0]
    y_pos = origin[1]
    x_direct = M2*cos(beta)
    y_direct = M2*sin(beta)
    ax.quiver(x_pos, y_pos, x_direct, y_direct, units='xy', color='red', scale=1)
    # plot: M2n
    x_pos = origin[0]+M2t*cos(sigma)
    y_pos = origin[1]+M2t*sin(sigma)
    x_direct = M2n*sin(sigma)
    y_direct = -M2n*cos(sigma)
    ax.quiver(x_pos, y_pos, x_direct, y_direct, units='xy', color='b', scale=1)
    # plot: M2t
    x_pos = origin[0]
    y_pos = origin[1]
    x_direct = M2t*cos(sigma)
    y_direct = M2t*sin(sigma)
    ax.quiver(x_pos, y_pos, x_direct, y_direct, units='xy', color='y', scale=1)
    
    ax.set_title('Machnumber relations for oblique shock')
    # ax.grid(linestyle=':')
    ax.set_xlim(-2, 6)
    ax.set_ylim(0, 8)
    ax.set_aspect('equal')
    ax.legend()
    fig.savefig('vector_presentation.png')
    plt.show()

if __name__ == "__main__":
    # INPUTS
    M1 = float(input("Enter inflow-machnumber: "))
    beta = float(input("Enter wedge-angle (deg): "))
    beta =beta*pi/180
    gamma=1.4

    # plot_vectors(M1, beta, gamma)
    plot_vectors(M1, 5*pi/180, gamma)
    plot_vectors(M1, 10*pi/180, gamma)
    plot_vectors(M1, 20*pi/180, gamma)
    plot_vectors(M1, 25*pi/180, gamma)

