import random

def rockpaperscissors():
    player_score = 0
    computer_score = 0
    play_or_quit = input('play or quit')
    while play_or_quit != 'quit':
        user_choise = input('rock,paper,scissors or quit')
        if user_choise.lower() == 'quit':
            print(f"the final score is PLAYER: {player_score} COMPUTER: {computer_score}")
            if player_score > computer_score:
                return "CONGRATS YOU WIN, THANKS FOR PLAYING"
            elif computer_score > player_score:
                return "SORRY YOU LOSE, THANKS FOR PLAYING"
            else:
                return "ITS A TIE, THANKS FOR PLAYING"
        computer_choice_number = random.randrange(1, 4, 1)
        if computer_choice_number == 1:
            computer_choice = 'rock'
        elif computer_choice_number == 2:
            computer_choice = 'paper'
        elif computer_choice_number == 3:
            computer_choice = 'scissors'
        else:
            return 'error'

        if computer_choice == user_choise.lower():
            print( 'Tie')
        elif computer_choice == 'rock' and user_choise.lower() == 'paper':
            player_score += 1
            print(f'you win the score is now  you:{player_score} Computer {computer_score}')
        elif computer_choice == 'paper' and user_choise.lower() == 'scissors':
            player_score += 1
            print(f'you win the score is now  you:{player_score} Computer {computer_score}')
        elif computer_choice == 'scissors' and user_choise.lower() == 'rock':
            player_score += 1
            print(f'you win the score is now  you:{player_score} Computer {computer_score}')
        elif computer_choice == 'rock' and user_choise.lower() == 'scissors':
            computer_score += 1
            print(f'you lose the score is now  you:{player_score} Computer {computer_score}')
        elif computer_choice == 'paper' and user_choise.lower() == 'rock':
            computer_score += 1
            print(f'you lose the score is now  you:{player_score} Computer {computer_score}')
        elif computer_choice == 'scissors' and user_choise.lower() == 'paper':
            computer_score += 1
            print(f'you lose the score is now  you:{player_score} Computer {computer_score}')
        else:
            print('That is not a valid input')




print(rockpaperscissors())