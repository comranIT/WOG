import random
import score
import validate_input


def generate_number(secret_range):
    secret_range = int(secret_range) + 1
    list_range = range(1, int(secret_range))
    secret_number = random.choice(list_range)
    return secret_number


def get_guess_from_user(user_input_range):
    user_input = validate_input.validate_user_choice(input(f'Enter your guess between 1 to {user_input_range}\n'
                                                           f'Good luck !\n'))
    return user_input


def compare_results(secret_number, user_guess):
    if int(secret_number) == int(user_guess):
        return True
    else:
        return False


# -------------------------------------


def play(difficulty, player_name):
    secret_number = generate_number(difficulty)
    user_guess = get_guess_from_user(difficulty)
    if compare_results(secret_number, user_guess):
        print(f'Very Good {player_name}! \n'
              'YOU GOT IT RIGHT !\n')
        score.add_score(difficulty, player_name)
        return True
    else:
        print(f'NO LUCK... \n'
              f'The correct number was {secret_number}\n'
              'TRY AGAIN\n')
        return False
