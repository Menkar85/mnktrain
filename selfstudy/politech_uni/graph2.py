import matplotlib.pyplot as plt
import math


def f_x(x):
    try:
        y = 1 / (x ** 2 - 1)
    except:
        y = math.inf
    return y


a = -3
b = 3
n = 100

h = abs(a - b) / (n - 1)


x_list = [a + i * h for i in range(n)]

y_list = [f_x(x) for x in x_list]

plt.plot(x_list, y_list, "r", label="y(x)")
plt.gca().spines["left"].set_position('zero')
plt.gca().spines['bottom'].set_position('zero')
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['top'].set_visible(False)

plt.legend()
plt.show()
