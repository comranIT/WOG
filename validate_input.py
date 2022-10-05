def validate_user_name(user_name):
    while True:
        if user_name.isdigit() or '.' in user_name:
            user_name = input("Please enter letters Only \n"
                              "Type your name again: ")
        else:
            return user_name


def validate_user_choice(user_choice):
    while True:
        if not user_choice.replace('.', '', 1).isdigit():
            user_choice = input('Enter numbers only \n')
        else:
            return user_choice


def validate_difficulty(difficulty):
    difficulty = validate_user_choice(difficulty)
    while True:
        if '.' in difficulty or int(difficulty) < 1 or int(difficulty) > 5:
            difficulty = validate_user_choice(input('Enter choice between [1-5] \n'))
        else:
            return difficulty
