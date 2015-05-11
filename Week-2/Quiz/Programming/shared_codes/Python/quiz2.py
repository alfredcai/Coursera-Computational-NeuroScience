"""
Created on Wed Apr 22 15:15:16 2015

Quiz 2 code.
"""

from __future__ import division
import numpy as np
import scipy

try:
	import matplotlib.pyplot as plt
except ImportError:
	pass

try:
	import numpy.matlib as matlib
except ImportError:
	pass

import pickle

from compute_sta import compute_sta


FILENAME = 'neuro/week2/c1p8.pickle'

with open(FILENAME, 'rb') as f:
    data = pickle.load(f)

stim = data['stim']
rho = data['rho']


# Filled in these values
sampling_period = 2 # in ms
num_timesteps = 150

sta = compute_sta(stim, rho, num_timesteps)

time = (np.arange(-num_timesteps, 0) + 1) * sampling_period

plt.plot(time, sta)
plt.xlabel('Time (ms)')
plt.ylabel('Stimulus')
plt.title('Spike-Triggered Average')

plt.show()
