import myfunctions as myFunc
import numpy as np
import matplotlib.pyplot as plt

Ma = np.linspace(1e-5,4.,100)

fig, ax = plt.subplots()
ax.plot(Ma, myFunc.calc_pdp0(Ma), label='p/p0')
ax.plot(Ma, myFunc.calc_TdT0(Ma), label='T/T0')
ax.plot(Ma, myFunc.calc_rhodrho0(Ma), label=r'$\rho/\rho_0$')
ax.plot(Ma, 1/myFunc.calc_AdAstar(Ma), label=r'$A^*/A$')
ax.set_xlim(xmin=0)
ax.set_ylim(ymin=0)
ax.set_xlabel('Ma')
ax.set_ylabel('-')
ax.legend()
plt.show()


