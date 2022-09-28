import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np


def func(cord1, cord2):
    a = cord2[1] - cord1[1]
    b = cord1[0] - cord2[0]
    c = a * cord1[0] + b * cord1[1]
    if b < 0:
        print(f'{a}*x{b}*y={c}')
    else:
        print(f'{a}*x+{b}*y={c}')


dot1, dot2 = np.array([3, 2]), np.array([5, 7])
func(dot1, dot2)
plt.plot(dot1, dot2)
plt.plot(dot1, dot2, 'o')
plt.show()
