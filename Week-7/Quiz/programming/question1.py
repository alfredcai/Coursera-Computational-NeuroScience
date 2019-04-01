import numpy as np

Q = np.array([
    [0.2, 0.1],
    [0.1, 0.3]
])

ev, e = np.linalg.eig(Q)
print(ev)
print(e)

# for a long period of time, W equal eigenvector where eigenvalue is maximum
# w(t)=e_1/sqrt(a)
max_index = ev.argmax()
print("W=")
print(2 * e[:, max_index])

w1 = np.array([0.8944, 1.7889]).T
w2 = np.array([-1.5155, -1.3051]).T
w3 = np.array([-1.5764, -1.2308]).T
w4 = np.array([1.0514, 1.7013]).T

print(w1/e[:, max_index])
print(w2/e[:, max_index])
print(w3/e[:, max_index])
print(w4/e[:, max_index])

print(w1[0]/w1[1])
print(w2[0]/w2[1])
print(w3[0]/w3[1])
print(w4[0]/w4[1])