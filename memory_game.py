import random
import validate_input
import score
import time


def generate_sequence(long):
    list_to_sample = range(1, 101)
    random_sequence = random.sample(list_to_sample, int(long))
    return random_sequence


def get_list_from_user(list_length):
    user_list_input = []
    for i in range(int(list_length)):
        if i == 0:
            user_list_input.insert(i, int(validate_input.validate_user_choice(input(f'please enter {i + 1}st number \n'))))
        elif i == 1:
            user_list_input.insert(i, int(validate_input.validate_user_choice(input(f'please enter {i + 1}nd number \n'))))
        elif i == 2:
            user_list_input.insert(i, int(validate_input.validate_user_choice(input(f'please enter {i + 1}rd number \n'))))
        else:
            user_list_input.insert(i, int(validate_input.validate_user_choice(input(f'please enter {i + 1}th number \n'))))
    print()
    return user_list_input


def is_list_equal(computer_list, user_list):
    if computer_list == user_list:
        return True
    else:
        return False


# ---------------------------------


def play(difficulty, player_name):
    sequence = generate_sequence(difficulty)
    input('When ready press Enter\n')
    for i in range(2):  # Show generated list for a 0.7 second
        if i == 0:
            print(sequence, end='')
            time.sleep(0.7)
        else:
            print(sequence, end='\r')
    user_list = get_list_from_user(difficulty)
    print(user_list)
    if is_list_equal(sequence, user_list):
        print(f'Very Good {player_name}! \n'
              'Your memory is fenomenal\n')
        score.add_score(difficulty, player_name)
        return True
    else:
        print('  YOU FAILED ! \n\n')
        print(f'The correct answer is \n '
              f'{sequence}\n')
        return False
