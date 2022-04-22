import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import os

fig_dir = os.path.join(os.getcwd(), '..', 'src', 'figures')

time_340 = 73.00
N_340 = 0.5 * 10 ** (-20)
# концентрации ионов эрбия %cm^3
time_342 = 65.58
N_342 = 0.15 * 10 ** (-20)

time_343 = 20.66
N_343 = 8.5 * 10 ** (-20)

time_344 = 62.39
N_344 = 0.26 * 10 ** (-20)

time_345 = 64.91
N_345 = 0.56 * 10 ** (-20)

time_346 = 60.74
N_346 = 1.12 * 10 ** (-20)

time_347 = 60.68
N_347 = 2.26 * 10 ** (-20)

liveTimeSeria1 = np.array([time_342, time_340, time_343])
concentrationSeria1 = np.array([N_342, N_340, N_343])

liveTimeSeria2 = np.array([time_344, time_345, time_346, time_347])
concentrationSeria2 = np.array([N_344, N_345, N_346, N_347])

fig, ax = plt.subplots()

ax.plot(concentrationSeria1, liveTimeSeria1, label="Серия 1")
plt.legend()
plt.xlabel('Концентрации ионов эрбия, см^-3')
plt.ylabel('Квантовый выход люминисценции, %')

ax.plot(concentrationSeria2, liveTimeSeria2, label="Серия 2")
plt.legend()
#  Устанавливаем интервал основных делений:
ax.yaxis.set_major_locator(ticker.MultipleLocator(10))
#  Устанавливаем интервал вспомогательных делений:
ax.yaxis.set_minor_locator(ticker.MultipleLocator(5))

#  Тоже самое проделываем с делениями на оси "y":
ax.xaxis.set_major_locator(ticker.MultipleLocator(10 ** (-20)))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(10 ** (-21)))

# включаем дополнительные отметки на осях
ax.minorticks_on()
# включаем основную сетку
ax.grid(which='major')
# включаем дополнительную сетку
ax.grid(which='minor', linestyle=':')
fig.show()
fig.savefig(os.path.join(fig_dir, 'ContcentrationTheory.png'))
