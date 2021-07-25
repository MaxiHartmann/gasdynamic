import math as m

# INPUTs

u_inf = 1.0
rho_inf = 1.205
mu_inf = 1.82e-5
L = 1.0
yPlus = 1.0

# Re = 6.6e+4
# y = 2.7e-4

Re_L = rho_inf * u_inf * L / mu_inf
C_f = (2 * m.log(Re_L) - 0.65)**(-2.3)

tau_w = C_f * rho_inf * u_inf * u_inf

u_star = m.sqrt(tau_w / rho_inf)

y = yPlus * mu_inf / (rho_inf * u_star)

print("\nINPUT:")
print("U_inf    = {:.04f} \t [m/s]".format(u_inf))
print("rho_inf  = {:.04f} \t [kg/m3]".format(rho_inf))
print("mu_inf   = {:.04f} \t [kg/ms]".format(mu_inf))
print("L        = {:.04f} \t [m]".format(L))
print("yPlus    = {:.04f} \t [-]".format(yPlus))

print("\nOUTPUT:")
print("Re_L     = {:.03e} \t [-]".format(Re_L))
print("y        = {:.03e} \t [m]".format(y))
