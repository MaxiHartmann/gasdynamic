import numpy as np
import matplotlib.pyplot as plt

r=0.5
T_w=200
T_air=300
delta_T=0.1

y=np.linspace(0, delta_T, 10)

T=((delta_T - y) / delta_T)**2 * (T_w - T_air) + T_air
y=r+y
plt.plot([0,r],[T_w, T_w], color='red')
plt.plot(y,T, color='red')
plt.plot([r+delta_T, r+delta_T*1.1],[T_air, T_air], color='red')

dT=abs(T_air-T_w)
plt.xlim(0, r+delta_T*1.5)
plt.ylim(min(T_w, T_air)-dT*0.1, max(T_w, T_air)+dT*0.1)
plt.show()
