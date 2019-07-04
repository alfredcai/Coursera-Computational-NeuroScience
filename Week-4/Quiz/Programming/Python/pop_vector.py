"""
Finally, we ran an additional set of experiments in which we exposed each of the
neurons to a single stimulus of unknown direction for 10 trials of 10 seconds
each. We have placed the results of this experiment in the following file:

pop_coding contains four vectors named r1, r2, r3, and r4 that contain the
responses (firing rate in Hz) of the four neurons to this mystery stimulus.
It also contains four vectors named c1, c2, c3, and c4. These are the basis
vectors corresponding to neuron 1, neuron 2, neuron 3, and neuron 4.

Decode the neural responses and recover the mystery stimulus vector by computing
the population vector for these neurons. You should use the maximum average
firing rate (over any of the stimulus values in 'tuning.mat') for a neuron as
the value of rmax for that neuron. That is, rmax should be the maximum value in
the tuning curve for that neuron.

What is the direction, in degrees, of the population vector? You should round
your answer to the nearest degree. Your answer should contain the value only (no
units!) and should be between 0∘ and 360∘. If your calculations give a negative
number or a number greater than or equal to 360, convert it to a number in the
proper range (you may use the mod function to do this).

You may need to convert your resulting vector from Cartesian coordinates to
polar coordinates to find the angle. You may use the atan() function in MATLAB
to do this. Note that the the convention we're using defines 0∘ to point in the
direction of the positive y-axis and 90∘ to point in the direction of the
positive x-axis (i.e., 0 degrees is north, 90 degrees is east).
"""

import numpy as np
import pickle

FILENAME = 'pop_coding_3.4.pickle'

with open(FILENAME, 'rb') as f:
    data = pickle.load(f)

c = [data['c1'], data['c2'], data['c3'], data['c4']]
r = [data['r1'], data['r2'], data['r3'], data['r4']]

basis_vector = []
for rr, cc in zip(r, c):
    # Calculate the weighted basis vector
    nr = rr / rr.max()
    mean_vector = np.outer(nr, cc).mean(axis=0)

    # Normalize the vector
    mean_vector /= np.sqrt(np.inner(mean_vector, mean_vector))

    basis_vector.append(mean_vector)

print('Weighted basis vectors: %s' % basis_vector)

# Only take the first two, because the rest are nan
pop_vector = np.nansum(basis_vector, axis=0)
pop_vector /= np.sqrt(np.inner(pop_vector, pop_vector))

print('Population Vector (X, Y): %s' % pop_vector)
print('Population vector in polar coordinates: %f' % np.arctan(pop_vector[1]/pop_vector[0]))