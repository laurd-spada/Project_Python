# The BMI Calculator is based on the Body mass index algorithm calculation
from art import logo

print(logo)
print("The BMI is a convenient rule of thumb used to broadly categorize a persons weight based on mass and height.")
Replay = True
while Replay:
    print("Please provide the recommended data to get an accurate result. \n")

    height = float(input("enter your height in m: "))
    weight = float(input("enter your weight in kg: "))

    bmi = weight / height ** 2
    final = round(int(bmi))

    if final <= 18.5:
        print(f"Your B-M-I is '{final}', You are under weight  \n")
    elif final <= 25:
        print(f"Your B-M-I is '{final}', You have a normal weight \n")
    elif final <= 30:
        print(f"Your B-M-I is '{final}', You are lightly overweight \n")
    elif final <= 35:
        print(f"Your B-M-I is '{final}', You are obese \n")
    else:
        print(f"Your B-M-I is '{final}', You are clinically obese \n")

    # A re-run loop
    Run_again = input("Will you like to make further calculation, 'Y' for yes and 'N' for no: \n")
    if Run_again == "y":
        Replay = True
    else:
        Replay = False
