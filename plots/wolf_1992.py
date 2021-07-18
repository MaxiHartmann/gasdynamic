import math
pi=math.pi

M1 = 2.0
gamma = 1.4
beta = 10*pi/180

alpha=math.asin(1/M1)


a=((gamma-1.)/2. + (gamma+1)/2. * math.tan(alpha)**2) * math.tan(beta)
b=((gamma+1.)/2. + (gamma+3)/2. * math.tan(alpha)**2) * math.tan(beta)
c=math.tan(alpha)**2
d=math.sqrt((4*(1-3*a*b)**3)/(27*a*a*c+9*a*b-2)**2-1)

n=0

# eq 5
term1 = (b+9.*a*c)/(2.*(1.-3.*a*b))
term2 = (d * (27.*a*a*c+9.*a*b-2.))/(6.*a*(1.-3.*a*b))
term3 = math.tan(n/3 * pi + 1/3. * math.atan(1/d))

tan_Beta = term1 - term2 * term3

print(tan_Beta*180/pi)
