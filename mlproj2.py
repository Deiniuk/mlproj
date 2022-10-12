import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


N = 30
x = np.linspace(0, 1, num=N)
print(x.shape)
# Графік синусоїдальної функції
t = np.sin(2*np.pi*x)
print(t.shape)
plt.plot(x, t)
plt.plot(x, t, 'ro')
plt.show()
# Графік синусоїдальної функції з нормальним шумом
t1 = t + 0.2 * np.random.randn(N)
plt.plot(x, t1)
plt.plot(x, t1, 'ro')
plt.show()
# Графік синусоїдальної функції з нормальним шумом та прогнозовані дані
y_pred = []
for i in range(N):
    tra = -0.1+11.05*x[i]-33.03*x[i]**2+22.13*x[i]**3
    y_pred.append(tra)
print(y_pred)
plt.scatter(x, t1)
plt.plot(x, y_pred)
plt.show()
