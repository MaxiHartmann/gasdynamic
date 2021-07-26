Cmu = 0.09
betaStar = Cmu

# different ways:
#
# --------- case 1: ----------------
k = 5
epsilon = 40
print("--- INPUT ---")
print("k        = {:.04f} \t [m2/s2]".format(k))
print("epsilon  = {:.04f} \t [m2/s3]".format(epsilon))

omega = epsilon / k / betaStar
print("--- OUTPUT ---")
print("Omega    = {:.04f} \t [1/s]".format(omega))


# --------- case 2: ----------------
k = 5
omega = 88.89
print("--- INPUT ---")
print("k        = {:.04f} \t [m2/s2]".format(k))
print("Omega    = {:.04f} \t [1/s]".format(omega))

epsilon = betaStar * omega * k
print("--- OUTPUT ---")
print("epsilon  = {:.04f} \t [m2/s3]".format(epsilon))


# --------- case 3: ----------------
Tu = 5
L_turb = 0.001
U_inf = 50
print("--- INPUT ---")
print("Tu        = {:.04f} \t [%]".format(Tu))
print("L_turb    = {:.04f} \t [m]".format(L_turb))
print("U_inf     = {:.04f} \t [m/s]".format(U_inf))

Tu = Tu/100
k = 3/2. * U_inf * U_inf * Tu * Tu
epsilon = Cmu * k**(3./2.) / L_turb
omega = epsilon / k / betaStar
print("--- OUTPUT ---")
print("k        = {:.04f} \t [m2/s2]".format(k))
print("epsilon  = {:.04f} \t [m2/s3]".format(epsilon))
print("Omega    = {:.04f} \t [1/s]".format(omega))


# --------- case 4: ----------------
Tu = 5.
muratio = 3.
U_inf = 50
nu = 1.5e-5
print("--- INPUT ---")
print("Tu       = {:.04f} \t [%]".format(Tu))
print("mut/mu   = {:.04f} \t [-]".format(muratio))
print("U_inf    = {:.04f} \t [m/s]".format(U_inf))
print("nu       = {:.04e} \t [m2/s]".format(nu))

Tu = Tu/100
k = 3/2. * U_inf * U_inf * Tu * Tu
epsilon = Cmu * k * k / nu / muratio
omega = k / nu / muratio
# Different definitions:
# L_turb = Cmu**(0.75) * k**(1.5) / epsilon
L_turb = Cmu * k**(1.5) / epsilon
# omega = epsilon / k / betaStar
print("--- OUTPUT ---")
print("k        = {:.04f} \t [m2/s2]".format(k))
print("epsilon  = {:.04f} \t [m2/s3]".format(epsilon))
print("Omega    = {:.04f} \t [1/s]".format(omega))
print("L_turb   = {:.04e} \t [m]".format(L_turb))
