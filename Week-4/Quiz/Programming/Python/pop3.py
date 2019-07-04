import pickle

import numpy as np


def load_data(path):
    with open(path, 'rb') as f:
        data = pickle.load(f)
    return data


# question 9
data = load_data("pop_coding_3.4.pickle")

c = [data['c1'], data['c2'], data['c3'], data['c4']]
r = [data['r1'], data['r2'], data['r3'], data['r4']]

data = load_data("tuning_3.4.pickle")

stim = data['stim']
n = [data['neuron1'], data['neuron2'], data['neuron3'], data['neuron4']]

n_max = [np.max(np.mean(ni, axis=0)) for ni in n]

arg = np.divide([rr.mean() for rr in r], n_max)

popultion = np.multiply(c, arg.T)
popultion = popultion.sum(axis=1)
angle = np.arctan(-popultion[0] / popultion[1])
answer = 180 - angle * 180.0 / np.pi
print(answer)
