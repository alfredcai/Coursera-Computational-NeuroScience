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
current_list = [0.2, 0.25, 0.3, 1,8.5, 9, 10, 30, 40, 50, 60]
for index, I in enumerate(current_list):
    V = 0
    tstop = 200
    abs_ref = 5  # absolute refractory period
    ref = 0  # absolute refractory period counter
    V_trace = []  # voltage trace for plotting
    V_th = 10  # spike threshold
    numSpikes = 0   # Number of spikes in the trial period

    for t in range(tstop):

        if not ref:
            V = V - (V/(R*C)) + (I/C)
        else:
            ref -= 1
            V = 0.2 * V_th  # reset voltage

        if V > V_th:
            V = 50  # emit spike
            numSpikes += 1
            ref = abs_ref  # set refractory counter

        V_trace += [V]
    firing_rate = numSpikes/tstop*1000
    print("I:%.2f,firing_rate:%0.1f, Number of spikes = %d\n" %
          (I, firing_rate, numSpikes))
    plt.subplot(len(current_list), 1, index + 1)
    # print("I:%.2f,firing_rate:%0.1f, Number of spikes = %d\n" % (I, firing_rate, numSpikes))
    plt.plot(V_trace)


plt.show()
