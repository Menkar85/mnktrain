# Напишите программу-игру. Компьютер загадывает случайное число,
# пользователь пытается его угадать. Пользователь вводит число до тех
# пор, пока не угадает или не введет слово «Выход». Компьютер сравнивает
# число с введенным и сообщает пользователю, больше оно или меньше
#  загаданного. Количе- ство попыток ограничено и указывается в программе.
from random import randint

max = 20
tries = 4
num = randint(1, max)
i = 0
print(f"Computer have chosen a number from 1 to {max}")
print("You have three tries to guess")

while i < tries:
    guess = input("Try to guess or print 'exit': ")
    if guess == 'exit':
        print('Bye!')
        exit()
    elif int(guess) > num:
        print("Failed! Try smaller number!")
        i += 1
    elif int(guess) < num:
        print("Failed! Try bigger number next time!")
        i += 1
    else:
        print("Congratulations!", num)
        exit()
print("No more tries. Game over!")
print(f"The chosen number was {num}.")
