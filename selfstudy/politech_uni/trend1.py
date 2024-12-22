import numpy as np


def calc_3(x, a):
    y = a[0] * x ** 3 + a[1] * x ** 2 + a[2] * x + a[3]
    return y 

def calc_4(x, a):
    y = a[0] * x ** 4 + a[1] * x ** 3 + a[2] * x **2 + a[3] * x + a[4]
    return y 

def delta(x, y):
    z = (x - y) / x * 100
    return z


month = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8 , 9, 10, 11])
temps = np.array([4, 8, 14, 19, 23, 27, 29, 28, 25, 18, 11, 6])

k_poly_3 = np.polyfit(month, temps, 3)
k_poly_4 = np.polyfit(month, temps, 4)

t_temps_3 = np.array([calc_3(month, k_poly_3)])
t_temps_4 = np.array([calc_4(month, k_poly_4)])

delta_3 = np.mean(np.abs(np.array([delta(temps, t_temps_3)])))
delta_4 = np.mean(np.abs(np.array([delta(temps, t_temps_4)])))

print("for n = 3: ", k_poly_3)
print("Delta: ", np.round(delta_3, 2))
print("for n = 4: ", k_poly_4)
print("Delta: ", np.round(delta_4, 2))