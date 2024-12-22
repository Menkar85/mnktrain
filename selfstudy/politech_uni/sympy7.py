import sympy as sp
import matplotlib.pyplot as plt

# formula is y = kx + b, where k = lim (f(x) / x) b = lim (f(x) - kx)
# f(x) = sqrt(x^2+1)


def f(x):
    z = sp.sqrt(x ** 2 + 1)
    return z

x = sp.Symbol("x")
k_1 = sp.limit(f(x) / x, x, sp.oo)
k_2 = sp.limit(f(x) / x, x, -sp.oo)
b_1 = sp.limit(f(x) - k_1*x, x, sp.oo)
b_2 = sp.limit(f(x) - k_2*x, x, -sp.oo)
print("Formula for asimptote is y1 = %5.2f * x + %5.2f" % (k_1, b_1))
print("Formula for asimptote is y2 = %5.2f * x + %5.2f" % (k_2, b_2))