"""
Created on Wed Apr 22 15:15:16 2015

Quiz 2 code.
This exercise is based on a set of artificial "experiments" that we've run on
four simulated neurons that emulate the behavior found in the cercal organs of a
cricket. Please note that all the supplied data is synthetic. Any resemblance to
a real cricket is purely coincidental.

In the first set of experiments, we probed each neuron with a range of air
velocity stimuli of uniform intensity and differing direction. We recorded the
firing rate of each of the neurons in response to each of the stimulus values.
Each of these recordings lasted 10 seconds and we repeated this process 100
times for each neuron-stimulus combination.

We've supplied you with a .mat file for each of the neurons that contains the
recorded firing rates (in Hz). These are named neuron1, neuron2, neuron3, and
neuron4. The stimulus, that is, the direction of the air velocity, is in the
vector named stim.

Plot the tuning curve-- the mean firing rate of the neuron as a function of the
stimulus-- for each of the neurons.
"""

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

import pickle

FILENAME = 'tuning_3.4.pickle'

with open(FILENAME, 'rb') as f:
    data = pickle.load(f)

stim = data['stim']
neurons = ['neuron1', 'neuron2', 'neuron3', 'neuron4']

f, ax = plt.subplots(len(neurons), 1, sharex=True, sharey=True)
for i, n in enumerate(neurons):
    ax[i].plot(stim, data[n].mean(axis=0))
    ax[i].set_title(n)

plt.xlabel('Air direction [degree]')
plt.ylabel('Spike Rate [Hz]')
f.subplots_adjust(hspace=0.5)
plt.show()


"""
We have reason to suspect that one of the neurons is not like the others. Three
of the neurons are Poisson neurons (they are accurately modeling using a Poisson
process), but we believe that the remaining one might not be.

Which of the neurons (if any) is NOT Poisson?

Hint: Think carefully about what it means for a neuron to be Poisson. You may
find it useful to review the last lecture of week 2. Note that we give you the
firing rate of each of the neurons, not the spike count. You may find it useful
to convert the firing rates to spike counts in order to test for "Poisson-ness",
however this is not necessary.

In order to realize why this might be helpful, consider the fact that, for a
constant a and a random variable X, 𝔼[aX]=a𝔼[X] but Var(aX)=a2Var(X). What might
this imply about the Poisson statistics (like the Fano factor) when we convert
the spike counts (the raw output of the Poisson spike generator) into a firing
rate (what we gave you)?
"""

a = 10.0 # 10Hz
# As mentioned in the hint above
# a E[X] = a**2 Var(X) -> E[x] = a Var(X)
# So test for diversions from the similarity
f, ax = plt.subplots(len(neurons), 1, sharex=True, sharey=True)
for i, n in enumerate(neurons):
    y = data[n].mean(axis=0) - a * data[n].var(axis=0)
    ax[i].plot(stim, y)
    ax[i].set_title(n)

plt.xlabel('Air direction [degree]')
plt.ylabel('E[X] - 10.0 * Var(X)')
f.subplots_adjust(hspace=0.5)
plt.show()

