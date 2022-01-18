# This code calculates the average score of any provided data.
from art import logo, thanks

print(logo)
print("Welcome to Average Data Cumulate")
Replay = True
while Replay:
    print("Please provide the necessary information lets get started \n")

    option = input("What is the name of the data you are working with ? : ")
    Number_value = input("Input a list of values of numbers separated by a single space : ").split()
    for n in range(0, len(Number_value)):
        Number_value[n] = float(Number_value[n])

    Sum_value = 0
    for Unit in Number_value:
        Sum_value += Unit

    Total_unit = 0
    for student in Number_value:
        Total_unit += 1

    Average = round(Sum_value / Total_unit, 2)

    print(f"The calculated average of '{option}' is = {Average}")
    print(thanks)

    # A re-run loop
    Run_again = input("Will you like to make further calculation, 'Y' for yes and 'N' for no: \n")
    if Run_again == "y":
        Replay = True
    else:
        Replay = False
