from art import art, win, lose
Replay = True
while Replay:
    print(art)
    print("Welcome to Treasure Island.")
    print("Your mission is to find the treasure.")

    stage_1 = input("After running 10 minutes been chased by a tiger You have arrived  at the front of a strange looking"
                    " cave, alone would you like to go into the cave ? 'y' or 'n' \n").lower()
    if stage_1 == "y":
        print("Good choice, you rain in just in time to escape the tiger")
        stage_2 = input("You are now inside the cave, you see a gun and a stick, which do you pick ? 'y' for stick"
                        " or 'n' for gun \n").lower()
        if stage_2 == "n":
            print("Good job, a wolf came out of a cave and you were able to chase it out with your gun")
            stage_3 = input("After finding you way into the cave you came across 3 doors, Red, Yellow or Blue.\n"
                            "There is an art on the wall telling you to choose out of the three to take you to the room\n"
                            " where the treasure is at and the other two would lead you to your death. Which would you \n"
                            "choose ? \n").lower()
            if stage_3 == "yellow":
                print("Lucky you. You are victorious")
                print(win)
            elif stage_3 == "red":
                print("Sorry, you were not luck. Red was not the color")
                print(lose)
            elif stage_3 == "blue":
                print("Sorry, you were not luck. Blue was not the color")
                print(lose)
        else:
            print("A wolf came out from one of the chambers in the cave and chased you away.")
            print(lose)
    else:
        print("The tiger found you, and you have no where to go.")
        print(lose)
    Run_again = input("Will you like to play again, 'Y' for yes and 'N' for no: \n")
    if Run_again == "y":
        Replay = True
    else:
        Replay = False
