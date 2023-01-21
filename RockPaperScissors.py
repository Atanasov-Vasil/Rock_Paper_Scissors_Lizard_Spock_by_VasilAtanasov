import random
from colorama import Fore

rock = 'Rock'
paper = 'Paper'
scissors = 'Scissors'
lizard = 'Lizard'
spock = 'Spock'


def player_chooses(some_char):
    if some_char == 'r':
        player = rock
    elif some_char == 'p':
        player = paper
    elif some_char == 's':
        player = scissors
    elif some_char == 'l':
        player = lizard
    else:
        player = spock
    return player


def computer_chooses():
    computer_random = random.randint(1, 5)
    if computer_random == 1:
        computer = rock
    elif computer_random == 2:
        computer = paper
    elif computer_random == 3:
        computer = scissors
    elif computer_random == 4:
        computer = lizard
    else:
        computer = spock
    return computer


wins = 0
draws = 0
loses = 0

print(Fore.BLUE + 'This is a game of Rock/Paper/Scissors/Lizard/Spock!')
print(Fore.BLUE + 'For exit, type "end"!')
command = input(Fore.RESET + 'Choose [r]ock, [p]aper, [s]cissors, [l]izard or [v] for Spock: ')
while command != 'end':
    if command == 'r' or command == 'p' or command == 's' or command == 'v' or command == 'l':
        player_move = player_chooses(command)
        print(f'You chose {player_move}')
        computer_move = computer_chooses()
        print(f'Computer chooses {computer_move}')
        if player_move == computer_move:
            print(Fore.YELLOW + 'Draw!')
            draws += 1
        elif (player_move == rock and (computer_move == scissors or computer_move == lizard)) \
                or (player_move == scissors and (computer_move == paper or computer_move == lizard)) \
                or (player_move == paper and (computer_move == rock or computer_move == spock)) \
                or (player_move == lizard and (computer_move == paper or computer_move == spock)) \
                or (player_move == spock and (computer_move == scissors or computer_move == rock)):
            print(Fore.GREEN + 'You win! Computer loses!')
            wins += 1
        else:
            print(Fore.RED + 'Computer wins! You lose!')
            loses += 1
    else:
        print('Invalid choice. Try again, please...')
        pass
    command = input(Fore.RESET + 'Choose [r]ock, [p]aper, [s]cissors, [l]izard or [v] for Spock: ')
else:
    print(f'Wins:Draws:Loses - {wins}:{draws}:{loses}')
    print('live long and prosper!')
