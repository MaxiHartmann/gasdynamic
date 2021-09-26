import numpy as np
import matplotlib.pyplot as plt

r=0.5
T_w=350
T_inf=300
V_inf=50
delta_T=0.1
delta=0.1

y=np.linspace(0, delta_T, 20)

order_T=4
order_V=2

T=((delta_T - y) / delta_T)**order_T * (T_w - T_inf) + T_inf
V=((delta - y) / delta)**order_V * (0. - V_inf) + V_inf
T=T/T_inf
V=V/V_inf

fig, ax = plt.subplots()
plt.plot(T,y, color='red', label=r'$T(y)/T_\infty$')
plt.plot(V,y, color='blue', label=r'$u_x(y)/U$')

ax.plot([0, 2], [0, 0], color='black', linewidth=3)

textstr = '\n'.join((
    r'$\delta=%.2f$' % (delta, ),
    r'$\delta_T=%.2f$' % (delta_T, ),
    r'$T_w/T_\infty =%.2f$' % (T_w/T_inf, ),
    r'$u_x(y)\propto y^%1.f $' % (order_V, ),
    r'$T(y)\propto y^%1.f $' % (order_T, )))
props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
ax.text(0.70, 0.7, textstr, transform=ax.transAxes, fontsize=14,
        verticalalignment='top', bbox=props)

ax.set_ylabel(r'$y$')
ax.legend()
plt.show()
