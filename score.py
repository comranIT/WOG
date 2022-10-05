import utils


# Score.py
# A package that is in charge of managing the scores file.
# The scores file at this point will consist of only a number. That number is the accumulation of the
# winnings of the user. Amount of points for winning a game is as follows:
# POINTS_OF_WINNING = (DIFFICULTY X 3) + 5
# Each time the user is winning a game, the points he one will be added to his current amount of
# point saved in a file.
# Methods
# 1. add_score - The function’s input is a variable called difficulty. The function will try to read
# the current score in the scores file, if it fails it will create a new one and will use it to save
# the current score.


def find_winner():
    utils.scores_file_name.close()
    winner = open("scores.txt", "r")
    total = 0
    count = 0
    score_list = []
    name = winner.readline().split()[0]
    winner.seek(0, 0)
    for i in winner.readlines():
        x = i.split()
        if x[0] == name:
            total += int(x[1])
            name = x[0]
        else:
            print(f'total score for {name} is {total}')
            score_list.append({'player': name, 'score': total})
            total = int(x[1])
            name = x[0]
            count += 1
    open('scores.txt', 'w').close()
    score_list.append({'player': name, 'score': total})
    print(f'Total score for {name} is {total}')
    winner_up = sorted(score_list, key=lambda k: k['score'], reverse=True)      # מסודר לפי ניקוד
    print(winner_up)
    winner = open("scores.txt", "a")
    for i in range(len(winner_up)):
        user_with_score = list(winner_up[i].values())
        print(user_with_score)
        winner.writelines(str(user_with_score) + '\n')
    winner.close()


# ===================================================================================================


def add_score(difficulty, player_name):
    level_score = (int(difficulty) * 3) + 5
    utils.scores_file_name.writelines([player_name + ' ', str(level_score) + '\n'])










# >>> knights = {'gallahad': 'the pure', 'robin': 'the brave'}
# >>> for k, v in knights.iteritems():
# ...     print k, v
# ...
# gallahad the pure
# robin the brave