# analytic equation: p02 / p01 = f(Ma1)  
# and polynomial fitting (numpy)
import matplotlib.pyplot as plt
import numpy as np

Ma1 = np.linspace(1., 2., 40)
gamma =1.4
p02d01 = (1+2*gamma/(gamma+1)*(Ma1*Ma1-1))**(-1/(gamma-1))*( (gamma+1)*Ma1*Ma1 / ((gamma-1)*Ma1*Ma1+2))**(gamma/(gamma-1))

new = np.polyfit(Ma1, p02d01, 3)
p = np.poly1d(new)

fig, ax = plt.subplots()
ax.plot(Ma1, p02d01, label='orig')
ax.plot(Ma1, p(Ma1), label='polyfit')
print(new)
props=dict(boxstyle='round', facecolor='wheat', alpha=0.5)

textstr='$y = {:.02f}x^3 + {:.02f}x^2 + {:.02f}x + {:.02f}$'.format(new[0], new[1], new[2], new[3])
ax.text(0.05, 0.95, textstr, transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)
plt.show()
