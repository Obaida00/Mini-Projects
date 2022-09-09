import random

Qs = {
    'What country has the highest life expectancy?': 'Hong Kong',
    'Which language has the more native speakers: English or Spanish?': 'Spanish',
    'What is the most common surname in the United States?': 'Smith',
    'Who was the Ancient Greek God of the Sun?': 'Apollo',
    'What was the name of the crime boss who was head of the feared Chicago Outfit?': 'Al Capone',
    'What year was the United Nations established?': '1945',
    'Who has won the most total Academy Awards?': 'Walt Disney',
    'What artist has the most streams on Spotify?': 'Drake',
    'How many minutes are in a full week?': '10080',
    'Aureolin is a shade of what color?': 'Yellow'
    }
def play():
    score = 0

    for key in Qs.keys():
        if input(f'{key}\n') == Qs[key]:
            print('Correct👍..')
            score += 1
        else:
            print('Wrong💔..')

    print(f'You got {score} out of 10')

    if input('Play again?? (1/0)') == 1:
        play()

play()
