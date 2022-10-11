import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


N = 30
x = np.linspace(0, 1, num=N)
x1 = x.reshape(-1, 1)
print(x1.shape)
# Графік синусоїдальної функції
t = np.array([np.sin(2*np.pi*x)]).reshape(-1, 1)
print(t.shape)
plt.plot(x1, t)
plt.plot(x1, t, 'ro')
plt.show()
# Графік синусоїдальної функції з нормальним шумом
t1 = (np.array([np.sin(2*np.pi*x)])+np.random.normal(scale=0.2, size=N)).reshape(-1, 1)
plt.plot(x1, t1)
plt.plot(x1, t1, 'ro')
plt.show()
# Графік синусоїдальної функції з нормальним шумом та прогнозовані дані
x_ = PolynomialFeatures(degree=8, include_bias=False).fit_transform(x1)
model = LinearRegression()
model.fit(x_, t1)
r_sq = model.score(x_, t1)
print(f"Кф. детермінації: {r_sq}")
print(f"b0: {model.intercept_}")
print(f"b1: {model.coef_}")
t1_pred = model.predict(x_)
plt.plot(x, t1_pred)
plt.plot(x1, t1, 'ro')
plt.show()
