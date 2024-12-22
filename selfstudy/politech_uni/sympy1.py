import sympy as sp

x = sp.Symbol("x")

y = ((x ** 2 - 1) / (x ** 3 - 1))
fract = sp.fraction(y)
eq_1 = fract[0]
eq_2 = fract[1]

f_1 = sp.factor(eq_1)
f_2 = sp.factor(eq_2)

simp = sp.simplify(f_1 / f_2)

print(simp)