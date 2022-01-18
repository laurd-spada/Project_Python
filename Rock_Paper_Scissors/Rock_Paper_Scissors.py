# This is a program design that adopts the randomization capability of python on matching to a user choice of data.
import random
from Art import rock, paper, scissors, intro

Go_again = True
while Go_again:
    print(intro)
    print("Welcome to a Game of rock, paper and scissors")
    print("Test your luck against the random capability of python and see if you win.\n")

    Human_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors : \n"))
    r_p_s = [rock, paper, scissors]
    # rock = 0
    # paper = 1
    # scissors = 2

    comp = random.randint(0, 2)
    comp_rps = r_p_s[comp]
    human_rps = r_p_s[Human_input]
    print(comp)

    if Human_input == 0:
        print(human_rps)
        print("computer choose :")
        print(comp_rps)
        if comp == 2:
            print("You win")
        elif human_rps == comp_rps:
            print("It was a draw")
        else:
            print("you loose")

    if Human_input == 1:
        print(human_rps)
        print("computer choose :")
        print(comp_rps)
        if comp == 0:
            print("You win")
        elif human_rps == comp_rps:
            print("It was a draw")
        else:
            print("you loose")

    if Human_input == 2:
        print(human_rps)
        print("computer choose :")
        print(comp_rps)
        if comp == 1:
            print("You win")
        elif human_rps == comp_rps:
            print("It was a draw")
        else:
            print("you loose")

    Replay = input("Would you like to play again ? Type 'y' for yes and 'n' for no : ")
    if Replay == "y":
        Go_again = True
    else:
        Go_again = False
