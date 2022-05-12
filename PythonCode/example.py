import matplotlib.pyplot as plt
import os
import pandas as pd
import matplotlib.ticker as ticker
import numpy as np
from scipy.optimize import curve_fit

fig_dir = os.path.join(os.getcwd(), '..', 'src', 'figures')
data = pd.read_csv('../Data/Data1.csv', sep=';')
x = data['delta x, мм']
print(data)
phi = data['phi']
rho = data['rho']
print(x)
# plot

for i in range(rho.shape[0]):
    rho[i] = rho[i].replace(",", ".")
    rho[i] = float(rho[i])
fig, ax = plt.subplots()

plt.plot(x, rho, 'r--',
         label='')
degree_sign = u'\N{DEGREE SIGN}'
plt.legend()
plt.xlabel('x, мм')
plt.ylabel(r'$\rho$')

#  Устанавливаем интервал основных делений:
ax.xaxis.set_major_locator(ticker.MultipleLocator(5))
#  Устанавливаем интервал вспомогательных делений:
ax.xaxis.set_minor_locator(ticker.MultipleLocator(5))

#  Тоже самое проделываем с делениями на оси "y":
ax.yaxis.set_major_locator(ticker.MultipleLocator(0.5))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.5))

# включаем дополнительные отметки на осях
ax.minorticks_on()
# включаем основную сетку
ax.grid(which='major')
# включаем дополнительную сетку
ax.grid(which='minor', linestyle=':')
fig.show()

fig.savefig(os.path.join(fig_dir, 'rhox.png'))
