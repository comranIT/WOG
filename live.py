import validate_input
import guess_game
import memory_game
import currency_roulette_game


def welcome():
    user_name = validate_input.validate_user_name(input('Please enter your name: \n'))
    print()
    print(f'Hello {user_name} and welcome to the World of Games (WoG) \n'
          'Here you can find many cool games to play.')
    return user_name


def load_game():
    print('Please choose a game to play: \n'
          '1.   Memory Game - a sequence of numbers will appear for 1 second \n'
          '     and you have to guess it back.\n'
          '2.   Guess Game - guess a number and see if you choose like the computer. \n'
          '3.   Currency Roulette - try and guess the value of a random amount of USD in ILS.')


def get_choice():
    choice = validate_input.validate_user_choice(input('Please enter your choice : \n'))
    while True:
        if '.' in choice or (int(choice) < 1) or (int(choice) > 3):
            choice = validate_input.validate_user_choice(input('Enter choice between [1-3] \n'))
        else:
            return choice


def get_difficulty():
    difficulty = validate_input.validate_difficulty(input('Please choose game difficulty from 1 to 5: \n'))
    return difficulty


# =========================== The Game ============================#


def start_game(choice, difficulty, player_name):
    if choice == '1':
        memory_game.play(difficulty, player_name)
    elif choice == '2':
        guess_game.play(difficulty, player_name)
    elif choice == '3':
        currency_roulette_game.play(difficulty, player_name)
