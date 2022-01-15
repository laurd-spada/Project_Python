from replit import clear
# you may need to install the replit package to be able to use the clear() function
from art import logo

# the logo is imported from an external python file named art


# The code will keep running in a loop until the user gives an "n" command
Take_another_turn = True
while Take_another_turn:
    print(logo)
    print("Welcome To Band Name Generator Program")
    print("Generating names for bands")

    User_City = input("What city did you grow up in? \n").lower()
    User_Pet = input("What is the name of your favourite pet? \n").lower()
    
    Combination = User_City + User_Pet

    print(f"The name of your band is called the {Combination}.")

    Re_do = input("Do you wand to generate another name, 'y' for yes or 'n' for no ").lower()
    # if the response selected is either "y" or "n", the if statement would run
    if Re_do == "y":
        clear()
        Take_another_turn = True

    else:
        clear()
        Take_another_turn = False
