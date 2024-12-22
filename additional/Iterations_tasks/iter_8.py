# Найдите сумму чисел, вводимых с клавиатуры. Количество вводимых чисел
# заранее неизвестно. Окончание ввода — слово «Стоп». При ошибке ввода
#  попросить повторить ввод числа.

final_sum = 0
while True:
    in_str = input("Please enter number or 'stop' for calculation: ")
    if not in_str.isnumeric() and in_str != 'stop':
        print("Enter correct data!")
    elif in_str.isnumeric():
        final_sum = final_sum + int(in_str)
    else:
        break
print("Sum is: ", final_sum)
