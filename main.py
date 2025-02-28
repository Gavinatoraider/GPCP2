# Evan McCabe, Asher Wangia, Connor Pavicic, Gavin Pierce Highscore Tracker


#██████╗  ██████╗ ███╗   ██╗████████╗    ██████╗ ███████╗██╗     ███████╗████████╗███████╗
#██╔══██╗██╔═══██╗████╗  ██║╚══██╔══╝    ██╔══██╗██╔════╝██║     ██╔════╝╚══██╔══╝██╔════╝
#██║  ██║██║   ██║██╔██╗ ██║   ██║       ██║  ██║█████╗  ██║     █████╗     ██║   █████╗  
#██║  ██║██║   ██║██║╚██╗██║   ██║       ██║  ██║██╔══╝  ██║     ██╔══╝     ██║   ██╔══╝  
#██████╔╝╚██████╔╝██║ ╚████║   ██║       ██████╔╝███████╗███████╗███████╗   ██║   ███████╗
#╚═════╝  ╚═════╝ ╚═╝  ╚═══╝   ╚═╝       ╚═════╝ ╚══════╝╚══════╝╚══════╝   ╚═╝   ╚══════╝

import random

# Global variable for tracking streak (wins in a row)
tic_tac_toe_highscore = 0

def tic_tac_toe():
    global tic_tac_toe_highscore  # Access the global high score variable
    
    rows = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    choice = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    display_count = 1
    for row in range(3):
        for col in range(3):
            print(display_count, end=' ')
            display_count += 1
        print()

    while True:
        count = 0
        num = input('Enter a number on the board: ')

        if num == '1' and '1' in choice:
            for row in range(3):
                for column in range(3):
                    if num == '1':
                        if row == 0 and column == 0:
                            print('X', end=' ')
                            rows[count] = 'X'
                            choice.remove('1')
                            count += 1
                        else:
                            print(rows[count], end=' ')
                            count += 1
                print()

        if num == '2' and '2' in choice:
            for row in range(3):
                for column in range(3):
                    if num == '2':
                        if row == 0 and column == 1:
                            print('X', end=' ')
                            rows[count] = 'X'
                            choice.remove('2')
                            count += 1
                        else:
                            print(rows[count], end=' ')
                            count += 1
                print()

        if num == '3' and '3' in choice:
            for row in range(3):
                for column in range(3):
                    if num == '3':
                        if row == 0 and column == 2:
                            print('X', end=' ')
                            rows[count] = 'X'
                            choice.remove('3')
                            count += 1
                        else:
                            print(rows[count], end=' ')
                            count += 1
                print()

        if num == '4' and '4' in choice:
            for row in range(3):
                for column in range(3):
                    if num == '4':
                        if row == 1 and column == 0:
                            print('X', end=' ')
                            rows[count] = 'X'
                            choice.remove('4')
                            count += 1
                        else:
                            print(rows[count], end=' ')
                            count += 1
                print()

        if num == '5' and '5' in choice:
            for row in range(3):
                for column in range(3):
                    if num == '5':
                        if row == 1 and column == 1:
                            print('X', end=' ')
                            rows[count] = 'X'
                            choice.remove('5')
                            count += 1
                        else:
                            print(rows[count], end=' ')
                            count += 1
                print()

        if num == '6' and '6' in choice:
            for row in range(3):
                for column in range(3):
                    if num == '6':
                        if row == 1 and column == 2:
                            print('X', end=' ')
                            rows[count] = 'X'
                            choice.remove('6')
                            count += 1
                        else:
                            print(rows[count], end=' ')
                            count += 1
                print()

        if num == '7' and '7' in choice:
            for row in range(3):
                for column in range(3):
                    if num == '7':
                        if row == 2 and column == 0:
                            print('X', end=' ')
                            rows[count] = 'X'
                            choice.remove('7')
                            count += 1
                        else:
                            print(rows[count], end=' ')
                            count += 1
                print()

        if num == '8' and '8' in choice:
            for row in range(3):
                for column in range(3):
                    if num == '8':
                        if row == 2 and column == 1:
                            print('X', end=' ')
                            rows[count] = 'X'
                            choice.remove('8')
                            count += 1
                        else:
                            print(rows[count], end=' ')
                            count += 1
                print()

        if num == '9' and '9' in choice:
            for row in range(3):
                for column in range(3):
                    if num == '9':
                        if row == 2 and column == 2:
                            print('X', end=' ')
                            rows[count] = 'X'
                            choice.remove('9')
                            count += 1
                        else:
                            print(rows[count], end=' ')
                            count += 1
                print()

        print()

        # Check if the player wins (for 'X')
        if rows[0] == rows[1] and rows[1] == rows[2] and rows[0] == 'X':
            print('You won!')
            tic_tac_toe_highscore += 1
            print(f"Current Streak: {tic_tac_toe_highscore}")
            break
        elif rows[3] == rows[4] and rows[4] == rows[5] and rows[3] == 'X':
            print('You won!')
            tic_tac_toe_highscore += 1
            print(f"Current Streak: {tic_tac_toe_highscore}")
            break
        elif rows[6] == rows[7] and rows[7] == rows[8] and rows[6] == 'X':
            print('You won!')
            tic_tac_toe_highscore += 1
            print(f"Current Streak: {tic_tac_toe_highscore}")
            break
        elif rows[0] == rows[3] and rows[3] == rows[6] and rows[0] == 'X':
            print('You won!')
            tic_tac_toe_highscore += 1
            print(f"Current Streak: {tic_tac_toe_highscore}")
            break
        elif rows[1] == rows[4] and rows[4] == rows[7] and rows[1] == 'X':
            print('You won!')
            tic_tac_toe_highscore += 1
            print(f"Current Streak: {tic_tac_toe_highscore}")
            break
        elif rows[2] == rows[5] and rows[5] == rows[8] and rows[2] == 'X':
            print('You won!')
            tic_tac_toe_highscore += 1
            print(f"Current Streak: {tic_tac_toe_highscore}")
            break
        elif rows[0] == rows[4] and rows[4] == rows[8] and rows[0] == 'X':
            print('You won!')
            tic_tac_toe_highscore += 1
            print(f"Current Streak: {tic_tac_toe_highscore}")
            break
        elif rows[2] == rows[4] and rows[4] == rows[6] and rows[2] == 'X':
            print('You won!')
            tic_tac_toe_highscore += 1
            print(f"Current Streak: {tic_tac_toe_highscore}")
            break

        # Check if the computer wins (for 'O')
        computer_choice = random.choice(choice)
        print('Computer chose:', computer_choice)
        if computer_choice == '1':
            rows[0] = 'O'
        elif computer_choice == '2':
            rows[1] = 'O'
        elif computer_choice == '3':
            rows[2] = 'O'
        elif computer_choice == '4':
            rows[3] = 'O'
        elif computer_choice == '5':
            rows[4] = 'O'
        elif computer_choice == '6':
            rows[5] = 'O'
        elif computer_choice == '7':
            rows[6] = 'O'
        elif computer_choice == '8':
            rows[7] = 'O'
        elif computer_choice == '9':
            rows[8] = 'O'
        
        choice.remove(computer_choice)

        for i in range(0, 9, 3):
            print(' '.join(rows[i:i+3]))
        print()

        # Check if the computer wins
        if rows[0] == rows[1] and rows[1] == rows[2] and rows[0] == 'O':
            print('The computer won!')
            tic_tac_toe_highscore = 0  # Reset streak on computer win
            break
        elif rows[3] == rows[4] and rows[4] == rows[5] and rows[3] == 'O':
            print('The computer won!')
            tic_tac_toe_highscore = 0
            break
        elif rows[6] == rows[7] and rows[7] == rows[8] and rows[6] == 'O':
            print('The computer won!')
            tic_tac_toe_highscore = 0
            break
        elif rows[0] == rows[3] and rows[3] == rows[6] and rows[0] == 'O':
            print('The computer won!')
            tic_tac_toe_highscore = 0
            break
        elif rows[1] == rows[4] and rows[4] == rows[7] and rows[1] == 'O':
            print('The computer won!')
            tic_tac_toe_highscore = 0
            break
        elif rows[2] == rows[5] and rows[5] == rows[8] and rows[2] == 'O':
            print('The computer won!')
            tic_tac_toe_highscore = 0
            break
        elif rows[0] == rows[4] and rows[4] == rows[8] and rows[0] == 'O':
            print('The computer won!')
            tic_tac_toe_highscore = 0
            break
        elif rows[2] == rows[4] and rows[4] == rows[6] and rows[2] == 'O':
            print('The computer won!')
            tic_tac_toe_highscore = 0
            break

        if not choice:
            print("It's a draw!")
            tic_tac_toe_highscore = 0  # Reset streak on draw
            break

def num_gussing_game():
    print("Welcome to the number guessing game!")
    rand_num = random.randint(1, 1000000)  # Generate a random number
    print("You have 5 attempts to guess the number. It is between 1 and 1,000,000.")

    attempt_num = 5  # Initialize attempts

    while attempt_num > 0:
        try:
            user_num = int(input("What is your guess? "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        # Check if the guess is too high or too low
        if rand_num > user_num:
            print("Your guess is too low.")
        elif rand_num < user_num:
            print("Your guess is too high.")
        else:
            print("Congratulations! You guessed the right number!")
            break

        attempt_num -= 1
        print(f"You have {attempt_num} attempts left.")

    if attempt_num == 0:
        print(f"Sorry! You've run out of attempts. The correct number was {rand_num}.")

def game():
    while True:
        game_to_play = input("""What game do you want to play?
                    1. Tic Tac Toe.
                    2. Number Guessing Game.
                    3. Exit.
                    (Please enter the number for your choice)
                    """)

        if game_to_play == "1":
            tic_tac_toe()
        elif game_to_play == "2":
            num_gussing_game()
        elif game_to_play == "3":
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice, please try again.")

game()
