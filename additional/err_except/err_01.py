# Напишите программу для суммирования произвольного количества целых чисел,
# введенных пользователем с клавиатуры, чтобы при вводе строки вместо числа
# программа не завершалась с ошибкой.

sum = 0
while True:
    in_str = input("Enter a number or 'stop': ")
    if in_str != "stop":
        try:
            num = int(in_str)
            sum += num
        except ValueError:
            print("Value should be integer!")
    else:
        print("Sum of numbers is: ", sum)
        exit()
