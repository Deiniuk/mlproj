import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


N = 30
x = np.linspace(0, 1, num=N)
t = np.sin(2*np.pi*x)
plt.plot(x, t)
plt.plot(x, t, 'ro')
plt.show()
t1 = t + 0.2 * np.random.randn(N)
plt.plot(x, t1)
plt.plot(x, t1, 'ro')
plt.show()


def poly(x, t1, M, N):
    y_pred = np.poly1d(np.polyfit(x, t1, M))
    E = sum((y_pred(x)[i]-t1[i])**2 for i in range(0, N))/2
    plt.scatter(x, t1)
    plt.title(f"E = {E} M = {M}")
    plt.plot(x, y_pred(x))
    plt.show()


for M in [0, 1, 3, 9]:
    poly(x, t1, M, N)

Ntest = 8
n = np.arange(Ntest)
std_deviation = 0.3
xtest = np.random.random_sample(Ntest)
ytest = np.sin(2*np.pi*xtest) + np.random.randn(Ntest) * std_deviation
plt.plot(xtest, ytest)
plt.plot(xtest, ytest, 'ro')
plt.show()

for M in [0, 1, 3, 9]:
    poly(xtest, ytest, M, Ntest)
