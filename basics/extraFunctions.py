
import random


def greatester():
    temporaryGreatestNumber = 0
    inputElements = input("Enter numbers: ")
    inputElementsList = list(inputElements.split(' '))
    for element in inputElementsList:
        if int(temporaryGreatestNumber) < int(element):
            temporaryGreatestNumber = element
    print('The greates number is: ', temporaryGreatestNumber)


# greatester()


def Averager():
    pNoCount, nNoCount, zNoCount = 0, 0, 0
    pNoSum, nNoCount, zNoCount = 0, 0, 0
    pNoAvg, nNoAvg, zNoAvg = 0, 0, 0
    inputElements = input("Enter numbers for average: ")
    inputElementsList = list(inputElements.split(' '))
    for element in inputElementsList:
        if(int(element) == 0):
            zNoCount += 1
        if(int(element) > 0):
            pNoCount += 1
        if(int(element) < 0):
            nNoCount += 1
    print('The +ve numbers average is: ', pNoCount/len(inputElementsList))
    print('The -ve numbers average is: ', nNoCount/len(inputElementsList))
    print('The zero numbers average is: ', zNoCount/len(inputElementsList))


# Averager()


def rockPaperScissors():
    rpsPriority = {
        'rock': '''
    ___
---'   __)
      (___)
      (___)
      (__)
---._(__)
''',
        'paper': '''
    ___
---'   _)_
          __)
          ___)
         ___)
---.____)
''',
        'scissors': '''
    ___
---'   _)_
          __)
       ____)
      (__)
---._(__)
'''}

    game_entities = ['rock', 'paper', 'scissors']
    user_won, computer_won, match_draw = False, False, False

    user_won_conditions = [('rock', 'scissors'),
                           ('paper', 'rock'), ('scissors', 'paper')]
    draw_cases = [('rock', 'rock'), ('paper', 'paper'),
                  ('scissors', 'scissors')]

    user_choice = int(
        input("Type 0 for Rock, 1 for Paper, and 2 for Scissors:\n "))
    user_choice = 'rock' if user_choice == 0 else (
        'paper' if user_choice == 1 else 'scissors')

    computer_choice = random.choice(game_entities)

    for choice in user_won_conditions:
        if (user_choice, computer_choice) == choice:
            user_won = True

    for choice in draw_cases:
        if (user_choice, computer_choice) == choice:
            match_draw = True

    print(f'User Chose {user_choice}: {rpsPriority[user_choice]}')
    print(
            f'Computer Chose {computer_choice}: {rpsPriority[computer_choice]}')

    if user_won:
        print(f'You are the winner')
    elif match_draw:
        print('Match is drawn')
    else:
        print('Computer is the winner')


rockPaperScissors()
