# Tip Calculator is a program that calculates a tip that could be sheared amongst individuals in splitting a bill evenly
from art import logo


Re_run = True
while Re_run:
    print(logo)
    print("Welcome to Tip calculator")
    print("This is a tip generating program based of on the data provided by users \n")

    # Here the value of data inputed by the user is converted into float(data type) for computational purposes
    Total_bill = float(input("Type in the amount of Total Bill: "))
    Split = float(input("Type in  the number of individuals to shear the bill: "))
    Tip = float(input("State the percentage to split the bill ? 5%, 10% or 15% : "))

    # Hear the process for the percentage calculation is carried out
    Tip_percentage = Tip / 100
    Tip_percentage = float(Tip_percentage)
    Overall_Tip_Of_Bill = Total_bill * Tip_percentage


    Sum_Of_Bill = Total_bill + Overall_Tip_Of_Bill

    Sum_Of_Split = float(Sum_Of_Bill / Split)
    Final_Sum = round(Sum_Of_Split, 2)

    print(f"The amount bill that will be sheared amongst the individual is, ${Final_Sum} \n\n")
    Run_again = input("Would you like to re-run the process again? select 'y' for yes and 'n' for no: ")
    if Run_again == "y":
        Re_run = True
    elif Run_again == "n":
        Re_run = False

