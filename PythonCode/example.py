import matplotlib.pyplot as plt
import os
import pandas as pd
import matplotlib.ticker as ticker
import numpy as np
from scipy.optimize import curve_fit

fig_dir = os.path.join(os.getcwd(), '..', 'src', 'figures')
data = pd.read_csv('../Data/Data.csv', sep=';')
t = data['t']
print(data)
I_340 = data['I_340']
I_342 = data['I_342']
I_343 = data['I_343']
I_344 = data['I_344']
I_345 = data['I_345']
I_346 = data['I_346']
I_347 = data['I_347']
# plot

fig, ax = plt.subplots()
seria = I_347
seria = seria - seria[seria.__len__() - 1]

y = seria / seria.max()
last = y.nlargest(n=20, keep='last')

maxIndex = last.index[1]
for i in range(0, t.shape[0]):
    t[i] = t[i].replace(",", ".")
maxTime = t[maxIndex]

for i in range(0, t.shape[0]):
    t[i] = float(t[i]) - float(maxTime)

ax.plot(t[maxIndex:], y[maxIndex:])

def func(x, a, b, c):
    return 1 * np.exp(-b * x) + 0

popt, pcov = curve_fit(func, np.array(t[maxIndex:]), np.array(y[maxIndex:]))
q = []
for i in t[maxIndex:]:
    q.append(i)
q = np.array(q)
plt.plot(q, func(q, *popt), 'r--',
         label='Оптимизированная функция: a=%5.3f, b=%5.3f, c=%5.3f' % tuple(popt))

summ = 0
for i in range(1, func(q, *popt).shape[0]):
    summ = summ + func(q, *popt)[i] * (q[i] - q[i - 1])
print(summ)
plt.legend()
plt.xlabel('Время, мс')
plt.ylabel('Нормированная интенсивность люминесценции, от. ед.')

#  Устанавливаем интервал основных делений:
ax.xaxis.set_major_locator(ticker.MultipleLocator(10))
#  Устанавливаем интервал вспомогательных делений:
ax.xaxis.set_minor_locator(ticker.MultipleLocator(5))

#  Тоже самое проделываем с делениями на оси "y":
ax.yaxis.set_major_locator(ticker.MultipleLocator(0.2))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))

# включаем дополнительные отметки на осях
ax.minorticks_on()
# включаем основную сетку
ax.grid(which='major')
# включаем дополнительную сетку
ax.grid(which='minor', linestyle=':')
fig.show()
# fig.savefig(os.path.join(fig_dir, 'I_341239.png'))
