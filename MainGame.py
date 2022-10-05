import live
import main_score
import score


is_quit = True
while is_quit:
    if is_quit == str("q"):
        users_score = score.find_winner()
        main_score.table_score()
        open('scores.txt', 'w').close()
        break
    else:
        player_name = live.welcome()
        print()
        is_quit = False
        while not is_quit:
            live.load_game()
            print()
            choice = live.get_choice()
            difficulty = live.get_difficulty()
            live.start_game(choice, difficulty, player_name)
            is_quit = input('You can press "Enter" key to keep playing or any key to switch user \n\n'
                            '<Press "q" to quit Game and view score>- ')


print('That is it for now')
#open('scores.txt', 'w').close()

