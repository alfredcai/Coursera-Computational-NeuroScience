import pickle
import numpy as np
import matplotlib.pyplot as plt

with open('c10p1.pickle', 'rb') as f:
    data = pickle.load(f)

c10p1 = data['c10p1']


def normailze(raw_data):
    mean = np.mean(raw_data, axis=0)
    data = raw_data - mean
    return data


data = normailze(c10p1)

plt.figure(1)
plt.scatter(data[:, 0], data[:, 1], marker='o',  c='r')
plt.title('Oja`s rule, data cloud')
plt.xlabel('u1')
plt.ylabel('u2')

eta = 1
alpha = 1
t_step = 0.01
max_iter = 500
w0 = w = np.random.rand(2)
print(f'W0:{w}')

for step in np.arange(0, max_iter, 1):
    plt.figure(1)
    u = data[np.remainder(step, data.shape[0]), :]
    v = u @ w
    plt.plot(v, marker='^',  c='b')
    w = w+t_step*eta*(v*u-alpha*v*v*w)
    plt.plot(w[0], w[1], marker='*',  c='g')

print('Question 7:')
c = np.dot(data.T, data) / data.shape[0]
ev, e = np.linalg.eig(c)
print(ev)
print(e)

print('Question 8:')
w1 = w0
offset = [2, 2]
data1 = data + np.tile(offset, (data.shape[0], 1))
plt.figure(2)
plt.scatter(data1[:, 0], data1[:, 1], marker='o',  c='r')
plt.title('Oja`s rule, data1 cloud')
plt.xlabel('u1')
plt.ylabel('u2')

for step in np.arange(0, max_iter, 1):
    plt.figure(2)
    u = data1[np.remainder(step, data1.shape[0]), :]
    v = u @ w1
    plt.plot(v, marker='^',  c='b')
    w1 = w1+t_step*eta*(v*u-alpha*v*v*w1)
    plt.plot(w1[0], w1[1], marker='*',  c='g')

print('Question 9:')
w2 = w0
plt.figure(3)
plt.scatter(data[:, 0], data[:, 1], marker='o',  c='r')
plt.title('Hebb rule, data cloud')
plt.xlabel('u1')
plt.ylabel('u2')
for step in np.arange(0, max_iter, 1):
    plt.figure(3)
    u = data[np.remainder(step, data.shape[0]), :]
    v = u @ w2
    plt.plot(v, marker='^',  c='b')
    w2 = w2+t_step*eta*(v*u)
    plt.plot(w2[0], w2[1], marker='*',  c='g')

plt.show()
