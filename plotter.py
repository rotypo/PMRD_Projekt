#!/usr/bin/env python3

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import locale
import platform

matplotlib.use("pgf")

if platform.system() == 'Windows':
    locale.setlocale(locale.LC_NUMERIC, 'Polish')
else:
    locale.setlocale(locale.LC_NUMERIC, ('pl_PL', 'UTF-8'))


mody = np.loadtxt("./data/mody.txt", skiprows=1).transpose()

plt.figure()
plt.plot(mody[0], mody[1], mody[2], mody[3])

plt.xlabel(r"Częstotliwość [\si{\hertz}]")
plt.ylabel(r"Amplituda [\si{\volt}]")

plt.legend(["$S1$", "$S2$"])

plt.savefig("plots/mody.pgf")
