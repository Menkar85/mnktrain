import random

L = ['airplane', 'kettle', 'notebook', 'pen', 'icecream']

while True:
    word_rand = random.randint(1, len(L)-1)
    word = L[word_rand]
    letter_rand = random.randint(1, len(word)-1)
    letter = word[letter_rand]
    letters_list = list(word)
    letters_list[letter_rand] = '?'
    new_word = ''.join(letters_list)
    print(new_word)
    guess = input("Please guess the letter: ").lower()
    if guess == letter:
        print("Hooray, you are right!")
        break
    else:
        print("Try again")