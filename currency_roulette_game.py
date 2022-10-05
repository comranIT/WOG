from currency_converter import CurrencyConverter
import random
import score
import validate_input


def get_money_interval():
    generated_range = range(1, 101)
    t = random.choice(generated_range)
    print(f'Try to convert {t}$ to Israeli SHEKEL\n')
    return t


def get_currency(t):
    c = CurrencyConverter()
    ils = (c.convert(t, 'USD', 'ILS'))
    return round(ils)


def check_guess(d, ils):
    user_guess = validate_input.validate_user_choice(input())
    low = int(ils) - (5 - int(d))
    high = int(ils) + (5 - int(d))
    if str(ils) in user_guess or low <= float(user_guess) <= high:
        return True
    else:
        return False


# ----------------------------------------


def play(difficulty, player_name):
    t = get_money_interval()
    ils = get_currency(t)
    if check_guess(difficulty, ils):
        print(f' GREAT {player_name} !! \n'
              'YOU SCORED IT !!\n')
        print(f'The exact amount is {ils}\n')
        score.add_score(difficulty, player_name)
        return True
    else:
        print(f'NO LUCK ...'
              f'The exact amount is {ils}\n'
              f'TRY AGAIN\n')
        return False
