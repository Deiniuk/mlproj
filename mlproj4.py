import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


N = 15
my_range = list(range(1, N*2))
x = my_range[::2]
y = my_range[:len(x)]

x_n = x + 0.4 * np.random.randn(N)
y_n = y + 0.4 * np.random.randn(N)

plt.plot(x_n, color='pink', label='x_n')
plt.plot(y_n, color='blue', label='y_n')
plt.plot(x, color='red', label='x')
plt.plot(y, color='black', label='y')
plt.plot(x_n, y_n, color='yellow', label='x_n with y_n')
plt.legend()
plt.show()

x = x_n
y = y_n

a1 = sum(x[i] * y[i] for i in range(0, N))/N
a2 = sum(x[i]**2 for i in range(0, N))/N
Mx = sum(x)/N
My = sum(y)/N
print("a1 = ", a1, "\na2 = ", a2, "\nMx = ", Mx, "\nMy = ", My)
k = (a1-Mx*My)/(a2-Mx**2)
b = My-k*Mx
print("k = ", k, "\nb = ", b)
f = [k*x[i]+b for i in range(0, N)]
print("f(x) = ", f)
E = sum(y[i]**2-f[i]**2 for i in range(0, N))
print("E = ", E)