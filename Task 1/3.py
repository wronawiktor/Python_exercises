'''

Make a two-player Rock-Paper-Scissors game.

(Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner,
and ask if the players want to start a new game)

Remember the rules:

Rock beats scissors
Scissors beats paper
Paper beats rock

'''

from os import system

game_menu = """
1. Rock
2. Paper
3. Scissors
"""


def decision(player_num):
    global choice
    print(game_menu)
    while True:
        try:
            choice = int(input("Player {}, please input your choice: ".format(player_num)))
            if choice not in range(1, 4):
                raise IndexError
            else:
                break
        except ValueError:
            print("Please enter correct number! ")
        except IndexError:
            print("Please enter a number within the range! ")

    system('cls')
    return(choice)


while True:

    system('cls')
    print("Rock, paper, scissors game!")
    choice_1 = decision(1)
    choice_2 = decision(2)

    if choice_1 == 1:
        if choice_2 == 2:
            print("Player 2 wins")
        elif choice_2 == 3:
            print("Player 1 wins")

    elif choice_1 == 2:
        if choice_2 == 3:
            print("Player 2 wins")
        elif choice_2 == 1:
            print("Player 1 wins")

    elif choice_1 == 3:
        if choice_2 == 1:
            print("Player 2 wins")
        elif choice_2 == 2:
            print("Player 1 wins")

    else:
        print("Draw!")

    next_game = input("Rematch? Enter 'y' or 'n': ")

    if next_game in ["Y", "y", "yes", "YES"]:
        continue
    else:
        break

