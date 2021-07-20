import numpy as np
import math
# import matplotlib.pyplot as plt
# import isentropicFlow as isenFlow
# import normalShock as ns

"""
IMPORTANT: Here

BETA := deflection angle (turn angle)
SIGMA := shock angle (wave angle)

"""
pi=math.pi


def mdb(g,m1,d,i):
    p=-(m1*m1+2.)/m1/m1-g*math.sin(d)*math.sin(d)
    q=(2.*m1*m1+1.)/math.pow(m1,4.)+((g+1.)*(g+1.)/4.+(g-1.)/m1/m1)*math.sin(d)*math.sin(d)
    r=-math.cos(d)*math.cos(d)/math.pow(m1,4.)

    a=(3.*q-p*p)/3.
    b=(2.*p*p*p-9.*p*q+27.*r)/27.

    test=b*b/4.+a*a*a/27.
    
    if (test>0.0): 
        print("test>0.0")
        return -1

    else:
        if (test==0.0):
            x1=math.sqrt(-a/3.)
            x2=x1
            x3=2.*x1
            if (b>0.0):
                x1*=-1
                x2*=-1
                x3*=-1
        if (test<0.0):
            phi=math.acos(math.sqrt(-27.*b*b/4./a/a/a))
            x1=2.*math.sqrt(-a/3.)*math.cos(phi/3.)
            x2=2.*math.sqrt(-a/3.)*math.cos(phi/3.+pi*2./3.)
            x3=2.*math.sqrt(-a/3.)*math.cos(phi/3.+pi*4./3.) 
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

        b1=math.asin(math.sqrt(t1))
        b2=math.asin(math.sqrt(t2))

        betas=b1
        betaw=b2
        if (b2>b1):
            betas=b2
            betaw=b1

        if (i==0): return betaw
        if (i==1): return betas


def mbd(g,m1,b):
   return math.atan((m1*m1*math.sin(2.*b)-2./math.tan(b))/(2.+m1*m1*(g+math.cos(2.*b))))

def pp0(g,m):
   return math.pow((1.+(g-1.)/2.*m*m),-g/(g-1.))

def rr0(g,m):
   return math.pow((1.+(g-1.)/2.*m*m),-1./(g-1.))

def calc_m2(g,m1):
   return math.sqrt((1. + .5 * (g - 1.) * m1 * m1) / (g * m1 * m1 - .5 * (g - 1.)))

def tt0(g,m):
   return math.pow((1.+(g-1.)/2.*m*m),-1.)




def osr(i,g,m1,v):
    g=g
    if(g<=1.0):
        print("Gamma must be greater than 1")
        return -1
    if (m1<=1.0):
        print("m1 must be greater than 1")
        return -1
    if (i==0 or i==1):
        delta=v*pi/180.
        if (delta>=pi/2):
            print("Turning angle too large")
            return -1
        if (delta<=0.0):
            print("Turning angle must be greater than zero")
            return -1
        beta=mdb(g,m1,delta,i)
        if(beta<0.0):
            print("Shock Detached")
            return -1
    elif (i==2):
        beta=v*pi/180.
        if (beta>=pi/2.):
            print("Wave angle must be less than 90 deg.")
            return -1
        if (beta-math.asin(1./m1)<=0.0):
            print("Wave angle must be greater than Mach angle ({:.03f})".format(math.asin(1./m1)*180./pi))
            return -1
        delta=mbd(g,m1,beta)
    elif (i==3):
        m1n=v
        if (m1n<=1.0 or m1n>=m1):
            print("M1n must be between 1 and M1")
            return -1
        beta=math.asin(m1n/m1)
        delta=mbd(g,m1,beta)


    m1n=m1*math.sin(beta)
    p2p1=1.+2.*g/(g+1.)*(m1n*m1n-1.)
    m2n=calc_m2(g,m1n)
    m2=m2n/math.sin(beta-delta)
    p02p01=pp0(g,m1n)/pp0(g,m2n)*p2p1
    r2r1=rr0(g,m2n) / rr0(g,m1n) * p02p01
    t2t1=tt0(g,m2n)/tt0(g,m1n)

    print("OUTPUT:")
    print("beta = {:.05f}".format(beta*180./pi))
    print("delta = {:.05f}".format(delta*180./pi))
    print("m1n = {:.05f}".format(m1n))
    print("m2n = {:.05f}".format(m2n))
    print("m2 = {:.05f}".format(m2))
    print("p02/p01 = {:.05f}".format(p02p01))
    print("p2/p1 = {:.05f}".format(p2p1))
    print("rho2/rho1 = {:.05f}".format(r2r1))
    print("T2/T1 = {:.05f}".format(t2t1))

if __name__ == "__main__":
    # INPUTS
    i=1
    g=1.4
    m1=2.0
    v=1.1
    print("INPUT:")
    print("i={}, g={}, m1={}, v={}".format(i, g, m1, v))
    osr(i,g,m1,v)
