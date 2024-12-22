import sympy as sp
import matplotlib.pyplot as plt


# defining functions
def y(k, x, b):
    y = k * x + b
    return y

def f(x):
    z = (x ** 3) - 6 * (x ** 2) + x + 5
    return z


x_0 = -2
x_1 = 3
x = sp.Symbol("x")

d_f = sp.diff(f(x), x)

d_f_x_0 = d_f.evalf(subs = {x : x_0})
d_f_x_1 = d_f.evalf(subs = {x : x_1})
f_x_0 = f(x).evalf(subs = {x : x_0})
f_x_1 = f(x).evalf(subs = {x : x_1})

k_0 = d_f_x_0
b_0 = f_x_0 - d_f_x_0 * x_0

k_1 = d_f_x_1
b_1 = f_x_1 - d_f_x_1 * x_1

print("x0 touch line is y = %5.2f * x + %5.2f" % (k_0, b_0))
print("x1 touch line is y = %5.2f * x + %5.2f" % (k_1, b_1))

a = -4
b = 5
n = 100

h = (b - a) / (n - 1)

x_list = [a + i * h for i in range(n)]

f_list = [f(x) for x in x_list]
y0_list = [y(k_0, x, b_0) for x in x_list ]
y1_list = [y(k_1, x, b_1) for x in x_list]

plt.plot(x_list, f_list, "b-", label='function')
plt.plot(x_list, y0_list, "g-", label='touch in x0')
plt.plot(x_list, y1_list, "r-", label="touch in x1")
plt.plot(x_0, f(x_0), "go")
plt.plot(x_1, f(x_1), "go")

plt.gca().spines['left'].set_position('zero')
plt.gca().spines['bottom'].set_position('zero')
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

plt.legend()
plt.show()
