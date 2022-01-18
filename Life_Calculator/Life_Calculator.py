# This adopts a simple operation of providing multiple result of operation on a single line of string data

print("This program calculates the time you have left to spend or the time you have spent ")
Replay = True
while Replay:
    Choice = int(input("Which would you like to know, Select : \n"
                       "'1' to know how long you have spent alive. \n"
                       "'2' to know how long you have left to live: \n"))

    if Choice == 1:
        age = int(input("What is your current age? : "))
        expectancy = int(input("What is you expected life expectancy? : "))

        # 365(days), 52(weeks), 12(months)
        answer = expectancy - age
        days = answer * 365
        weeks = answer * 52
        months = answer * 12

        print(f"You have {days} days, {weeks} weeks, and {months} months left to live \n")

    if Choice == 2:
        age = int(input("What is your current age? : "))

        # 365(days), 52(weeks), 12(months)
        days = age * 365
        weeks = age * 52
        months = age * 12

        print(f"You have lived for {days} days, {weeks} weeks, and {months} months. \n")

    # A re-run loop
    Run_again = input("Will you like to Try it out again, 'Y' for yes and 'N' for no: \n")
    if Run_again == "y":
        Replay = True
    else:
        Replay = False
