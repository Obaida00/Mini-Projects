import random


move = ('R', 'P', 'S')

def play():

    player = input('Rock(R) / Paper(P) / Scissors(S) ???\n')
    bot = move[random.randint(0,2)]

    print('Bot Chose :', bot)
    # Game Conditions
    if player == 'R':
        if bot == 'R':
            print('Draw..!!! Next round...')
            play()
        elif bot == 'P':
            print('Lost.. Next round...')
            play()
        else:
            print('WIN.!!! Next round...')
    elif player == 'P':
        if bot == 'R':
            print('WIN.!!! Next round...')
            play()
        elif bot == 'P':
            print('Draw..!!! Next round...')
            play()
        else:
            print('Lost.. Next round...')
    elif player == 'S':
        if bot == 'R':
            print('Lost.. Next round...')
            play()
        elif bot == 'P':
            print('WIN.!!! Next round...')
            play()
        else:
            print('Draw..!!! Next round...')
    else:
        print('INVALID ROUND!#@@!... Next round')
        play()


play()

