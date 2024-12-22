import sympy as sp
import matplotlib.pyplot as plt
from math import log


def f(x):
    z = sp.ln(x ** 2 + 1) - 1
    return z

a = -4
b = 4
n = 50
h = (b - a) / (n - 1)

x_list = [a + i * h for i in range(n)]
y_list = [log(x ** 2 + 1) - 1 for x in x_list]

plt.plot(x_list, y_list, "b-", label="f(x)=ln(x**2+1)-1")
plt.gca().spines["left"].set_position('zero')
plt.gca().spines['bottom'].set_position('zero')
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['top'].set_visible(False)

plt.legend()


x = sp.Symbol("x")
x_1 = sp.nsolve(f(x), x, -1)
x_2 = sp.nsolve(f(x), x, 1)
print("x1 = ", x_1, "x2 = ", x_2)
plt.show()