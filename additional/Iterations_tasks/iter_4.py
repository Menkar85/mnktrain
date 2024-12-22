# Напишите программный код, который будет создавать новый список,
# содержащий в качестве элементов квадратные корни всех чисел из
# списка [2, 4, 9, 16, 25]:

# на основе цикла for;
# на основе функции map;
# в виде спискового включения.
from math import sqrt

lst = [2, 4, 9, 16, 25]
sqrt_lst_1 = []

for i in lst:
    sqrt_lst_1.append(sqrt(i))

print('list 1 ', sqrt_lst_1)

sqrt_lst_2 = list(map(sqrt, lst))
print('list 2 ', sqrt_lst_2)

sqrt_lst_3 = [sqrt(i) for i in lst]
print('list 3 ', sqrt_lst_3)
