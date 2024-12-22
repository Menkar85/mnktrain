import sympy as sp


def f(x):
    z = x ** 3 - 6 * x ** 2 + x + 5
    return z


x = sp.Symbol("x")
diff_1 = sp.diff(f(x), x)
x_extr = sp.solve(diff_1)
print("Extremums: ", x_extr)

x_0 = x_extr[0]
x_1 = x_extr[1]

diff_2 = sp.diff(f(x), x, 2)

d2_x_0 = diff_2.evalf(subs={x: x_0})
d2_x_1 = diff_2.evalf(subs={x: x_1})

a = -5
b = 5

fx_x_0 = f(x_0)
fx_x_1 = f(x_1)
fa = f(a)
fb = f(b)

if x_0 >= a and x_0 <= b:
    if d2_x_0 > 0:
        print("x_0 is local min. y = ", sp.N(fx_x_0, 3))
    elif d2_x_0 < 0:
        print("x_0 is local max. y = ", sp.N(fx_x_0, 3))
    else:
        print("x_0 is bending point. y = ", sp.N(fx_x_0, 3))

if x_1 >= a and x_1 <= b:
    if d2_x_1 > 0:
        print("x_1 is local min. y = ", sp.N(fx_x_1, 3))
    elif d2_x_1 < 0:
        print("x_1 is local max. y = ", sp.N(fx_x_1, 3))
    else:
        print("x_1 is bending point. y = ", sp.N(fx_x_1, 3))

f_array = [fx_x_0, fx_x_1, fa, fb]
x_array = [x_0, x_1, a, b]
f_sorted = f_array.copy()
f_sorted.sort()
last = len(f_array) - 1
fmax = f_sorted[last]
fmin = f_sorted[0]
fmax_i = f_array.index(fmax)
fmin_i = f_array.index(fmin)

print("Max value is: ", sp.N(fmax, 3), "in the point: ", x_array[fmax_i])
print("Min value is: ", sp.N(fmin, 3), "in the point: ", x_array[fmin_i])
