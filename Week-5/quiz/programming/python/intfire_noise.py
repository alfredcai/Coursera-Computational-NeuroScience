from __future__ import print_function
"""
Created on Wed Apr 22 16:02:53 2015

Basic integrate-and-fire neuron 
R Rao 2007

translated to Python by rkp 2015
"""

import numpy as np
import matplotlib.pyplot as plt


# input current
I = 1  # nA

# capacitance and leak resistance
C = 1  # nF
R = 40  # M ohms

# I & F implementation dV/dt = - V/RC + I/C
# Using h = 1 ms step size, Euler method
# input current
nosiserange = np.arange(0, 5, 1)
for index, noiseamp in enumerate(nosiserange):
    V = 0
    tstop = 200*3
    abs_ref = 5  # absolute refractory period
    ref = 0  # absolute refractory period counter
    V_trace = []  # voltage trace for plotting
    V_th = 10  # spike threshold
    spiketimes = []  # list of spike times
    I += noiseamp*np.random.normal(0, 1, (tstop,))  # nA; Gaussian noise

    for t in range(tstop):

        if not ref:
            V = V - (V/(R*C)) + (I[t]/C)
        else:
            ref -= 1
            V = 0.2 * V_th  # reset voltage

        if V > V_th:
            V = 50  # emit spike
            ref = abs_ref  # set refractory counter
            spiketimes += [t]
        V_trace += [V]
    plt.figure(1)
    plt.subplot(len(nosiserange), 1, index + 1)
    plt.plot(V_trace)
# print(spiketimes)
# plt.plot(V_trace)
# plt.show()
    plt.figure(2)
    plt.subplot(len(nosiserange), 1, index+1)
    z = 0
    x = 0
    interval = []
    for x in range(len(spiketimes)):
        if x+1 < len(spiketimes):
            z = spiketimes[x+1]-spiketimes[x]
            interval.append(z)
        else:
            # print (interval)
            break
    plt.hist(interval, bins=50)
plt.show()
