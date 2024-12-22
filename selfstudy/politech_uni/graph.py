from math import e, log, sin, cos, radians, degrees
import matplotlib.pyplot as plt


def f_x(x):
    z = radians(x)
    fx = e ** cos(z) + log((sin(0.8 * z)) ** 2 + 1) * cos(z)
    return fx


def y_x(x):
    z = radians(x)
    yx = 2 + log((cos(z) + sin(z)) ** 2 + 1.7)
    return yx


x_list = range(-240, 360)
f_list = [f_x(x) for x in x_list]
y_list = list(map(y_x, x_list))

f_line = plt.plot(x_list, f_list)
y_line = plt.plot(x_list, y_list)

plt.setp(f_line, color="blue", label="f(x)")
plt.setp(y_line, color="red", label="y(x)")

plt.gca().spines['left'].set_position("center")
plt.gca().spines['bottom'].set_position('zero')
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['top'].set_visible(False)

plt.legend(loc="center left")
plt.title("Graphs of functions")
plt.show()
