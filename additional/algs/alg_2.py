# Напишите калькулятор, который вычисляет арифметические выражения,
# заданные пользователем в постфиксной записи (обратная польская запись).

# Мы добавляем числа в стек. Когда мы сталкиваемся с оператором,
# то извлекаем из стека столько элементов, сколько нужно в качестве
# операндов, производим операцию и помещаем результат в стек. В итоге
# результат оказывается на самом верху стека
# (и единственным его элементом).


stack = []

while True:
    input_str = input("Enter digit, operator or exit: ")
    if input_str.isnumeric():
        stack.append(float(input_str))
        print(stack)
    elif input_str in {'+', '-', '*', '/'}:
        match input_str:
            case "+":
                y = stack.pop()
                x = stack.pop()
                z = x + y
                stack.append(z)
                print(stack)
            case "-":
                y = stack.pop()
                x = stack.pop()
                z = x - y
                stack.append(z)
                print(stack)
            case "*":
                y = stack.pop()
                x = stack.pop()
                z = x * y
                stack.append(z)
                print(stack)
            case "/":
                y = stack.pop()
                x = stack.pop()
                z = x / y
                stack.append(z)
                print(stack)
            case _:
                print("unknown operator")
                exit()
    elif input_str == "exit":
        print("Bye!")
        exit()
    else:
        print("unknown symbol")
        exit()
