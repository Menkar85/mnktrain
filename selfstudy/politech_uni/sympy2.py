import sympy as sp


x = sp.Symbol("x")

y = (x ** 2 + 1) / (x ** 2 - 3)

fract = sp.fraction(y)
eq_1 = fract[0]
eq_2 = fract[1]

result = sp.solve(eq_2)

print("Bottom", eq_2, "not equal to zero")
print("Function not defined at x = ", result)

z = sp.ln(x ** 2 + 1) - 1
answ = sp.solve(z)
print(answ)
print("x0 = ", answ[0].evalf(4), "x1 = ", sp.N(answ[1], 4))
str.split
