import sympy as sp
import matplotlib.pyplot as plt


def y(x):
    y = 2 * x - 6
    return y

def f(x):
    z = x ** 3 - 6 * x ** 2 + x + 5
    return z


# a = -2 
# b = 8
# n = 100
# h = (b - a) / (n - 1)

# x_list = [a + i * h for i in range(n)]
# y_list = [y(x) for x in x_list]
# f_list = [f(x) for x in x_list]

# plt.plot(x_list, y_list, "g-")
# plt.plot(x_list, f_list, "b-")

# plt.gca().spines['left'].set_position('zero')
# plt.gca().spines['bottom'].set_position('zero')
# plt.gca().spines['top'].set_visible(False)
# plt.gca().spines['right'].set_visible(False)


x = sp.Symbol("x")
x_0 = sp.nsolve(f(x) - y(x), x, -2)
x_1 = sp.nsolve(f(x) - y(x), x, 2)
x_2 = sp.nsolve(f(x) - y(x), x, 6)

print("cross points are x1=%5.3f, x2=%5.3f, x3=%5.3f" % (x_0, x_1, x_2))

s_1 = sp.integrate(f(x) - y(x), (x, x_0, x_1))
s_2 = sp.integrate(y(x) - f(x), (x, x_1, x_2))
s = s_1 + s_2

print("finals sqare is", round(s, 3))