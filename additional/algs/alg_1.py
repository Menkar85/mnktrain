# Напишите функцию, которая для целочисленного списка из 1000 случайных
# элементов определяет, сколько отрицательных элементов располагается
# между его максимальным и минимальным элементами включительно.

from random import randint


lst = [randint(-50, 50) for i in range(0, 1000)]

min_ix = lst.index(min(lst))
max_ix = lst.index(max(lst))
if min_ix > max_ix:
    min_ix, max_ix = max_ix, min_ix
neg_qty = 0
for i in range(min_ix, max_ix + 1):
    if lst[i] < 0:
        neg_qty += 1

print(neg_qty)
