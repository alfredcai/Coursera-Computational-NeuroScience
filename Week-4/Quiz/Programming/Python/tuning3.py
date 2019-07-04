import pickle

import matplotlib.pyplot as plt
import numpy as np


def load_data(path):
    with open(path, 'rb') as f:
        data = pickle.load(f)
    return data


data_path = "tuning_3.4.pickle"
data = load_data(data_path)
print(f"data.key:{data.keys()}")
# ['neuron4', 'stim', 'neuron3', 'neuron2', 'neuron1']
stim = data['stim']
n1 = np.array(data['neuron1'])
n2 = np.array(data['neuron2'])
n3 = np.array(data['neuron3'])
n4 = np.array(data['neuron4'])

ave_n1 = np.average(n1, axis=0)
ave_n2 = np.average(n2, axis=0)
ave_n3 = np.average(n3, axis=0)
ave_n4 = np.average(n4, axis=0)

# Question 7
plt.figure(1)
plt.subplot(221)
plt.title("n1")
plt.plot(stim, ave_n1)

plt.subplot(222)
plt.title("n2")
plt.plot(stim, ave_n2)

plt.subplot(223)
plt.title("n3")
plt.plot(stim, ave_n3)

plt.subplot(224)
plt.title("n4")
plt.plot(stim, ave_n4)

# question 8
delta1 = 10 * np.var(n1, axis=0) - np.average(n1, axis=0)
delta2 = 10 * np.var(n2, axis=0) - np.average(n2, axis=0)
delta3 = 10 * np.var(n3, axis=0) - np.average(n3, axis=0)
delta4 = 10 * np.var(n4, axis=0) - np.average(n4, axis=0)

plt.figure(2)
plt.plot(stim, delta1, label="n1")
plt.plot(stim, delta2, label="n2")
plt.plot(stim, delta3, label="n3")
plt.plot(stim, delta4, label="n4")
plt.legend()
plt.show()
