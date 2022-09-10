import random

num1 = 0
num2 = 3


def play():
    number = random.randint(num1, num2)
    print(number)

    if int(input(f'guess a number between {num1} and {num2}\n')) == number:
        print('Correct ✔')
    else:
        print('Wrong ❌')

    if input('Play again?? [1/0]\n') == '1':
        play()

play()
