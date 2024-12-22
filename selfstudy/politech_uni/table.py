from math import atan, pi

C = 172
T_1 = 2000
TAU = 45

def compute_population(t):
    N = (C / TAU) * (pi / 2 - atan((T_1 - t) / TAU))
    return N

line = input("Enter years separated by space: ")
years_str_list = line.split()
n = len(years_str_list)
years_int_list = [int(years_str_list[i]) for i in range(n)]
population_list = [compute_population(years_int_list[j]) for j in range(n)]
for i in range(n):
    print("%5d - %6.3f billions" % (years_int_list[i], population_list[i]))