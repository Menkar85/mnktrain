# Дано число, введенное с клавиатуры.
# Определите сумму квадратов нечетных цифр в числе.

from math import pow


in_str = input("Please enter some number: ")
sum = 0
for figure in in_str:
    if int(figure) % 2 == 1:
        sum = sum + pow(int(figure), 2)

print(sum)
