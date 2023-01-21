import random
from colorama import Fore

rock = 'Rock'
paper = 'Paper'
scissors = 'Scissors'


def player_chooses(some_char):
    if some_char == 'r':
        player = rock
    elif some_char == 'p':
        player = paper
    elif some_char == 's':
        player = scissors
    return player


def computer_chooses():
    computer_random = random.randint(1, 3)
    if computer_random == 1:
        computer = rock
    elif computer_random == 2:
        computer = paper
    else:
        computer = scissors
    return computer


wins = 0
draws = 0
loses = 0

command = input('Choose [r]ock, [p]aper or [s]cissors: ')
while command != 'end':
    if command == 'r' or command == 'p' or command == 's':
        player_move = player_chooses(command)
        print(f'You chose {player_move}')
        computer_move = computer_chooses()
        print(f'Computer chooses {computer_move}')
        if player_move == computer_move:
            print(Fore.YELLOW + 'Draw!')
            draws += 1
        elif (player_move == rock and computer_move == scissors) \
                or (player_move == scissors and computer_move == paper) \
                or (player_move == paper and computer_move == rock):
            print(Fore.GREEN + 'You win! Computer loses!')
            wins += 1
        else:
            print(Fore.RED + 'Computer wins! You lose!')
            loses += 1
    else:
        print('Invalid choice. Try again, please...')
        pass
    command = input(Fore.RESET + 'Choose [r]ock, [p]aper or [s]cissors: ')
else:
    print(f'Wins:Draws:Loses - {wins}:{draws}:{loses}')
    print('Bye, bye!')
