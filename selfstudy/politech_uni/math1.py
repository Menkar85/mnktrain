from math import sqrt

def side_len(x_0, y_0, x_1, y_1):
    lenght = sqrt((x_1 - x_0) ** 2 + (y_1 - y_0) ** 2)
    return lenght


# input of coordinates
x_a = float(input("x_a = "))
y_a = float(input("y_a = "))
x_b = float(input("x_b = "))
y_b = float(input("y_b = "))
x_c = float(input("x_c = "))
y_c = float(input("y_c = "))

# determine lenghts

a = side_len(x_b, y_b, x_c, y_c)
b = side_len(x_a, y_a, x_c, y_c)
c = side_len(x_a, y_a, x_b, y_b)


# half perimeter [p]
p = (a + b + c) / 2

# square [s]
s = sqrt(p * (p - a) * (p - b) * (p - c))

if a >= b + c or b >= a + c or c >= a + b:
    print("There is no triangle at all!")
else:
    r_in = sqrt((p - a) * (p - b) * (p - c) / p)
    r_out = a * b * c / (4 * s)
    m_a = 0.5 * sqrt(2 * (c ** 2 + b ** 2) - a ** 2)
    m_b = 0.5 * sqrt(2 * (c ** 2 + a ** 2) - b ** 2)
    m_c = 0.5 * sqrt(2 * (a ** 2 + b ** 2) - c ** 2)
    print("Inside radius = ", round(r_in, 4))
    print("Outside radius = ", round(r_out, 4))
    print("Median sum = ", round(m_a + m_b + m_c, 4))