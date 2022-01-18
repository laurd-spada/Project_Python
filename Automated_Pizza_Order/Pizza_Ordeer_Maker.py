# This is an automated program that takes in the input of users preferred order, and cumulate the prize for payment
from art import pizza, thanks

print(pizza)
print("Welcome to Python Pizza Deliveries!")
print("Please find below the current price roster: \n"
      "Small-Pizza = $15, Medium-Pizza = $20, Large-Pizza = $25 \n"
      "Additional-Peperoni = $2, Extra-Cheese = $1")
print("Please make a selection from the available choices to customize your order \n")

Replay = True
while Replay:
    size = input("What size pizza do you want? 'S' for small, 'M' for medium, or 'L' for large : ").lower()
    add_pepperoni = input("Do you want pepperoni? 'Y' or 'N' : ").lower()
    extra_cheese = input("Do you want extra cheese? 'Y' or 'N' : ").lower()

    s = 15
    m = 20
    l = 25

    peperoni = 2
    extra_cheeses = 1

    price = 0
    if size == "s":
        price += s
        if add_pepperoni == "y":
            price += peperoni
        if extra_cheese == "y":
            price += extra_cheeses
        print(f"Your total bill is cumulated to ${price}, Thank you.")
        print(thanks)

    if size == "m":
        price += m
        if add_pepperoni == "y":
            price += peperoni
        if extra_cheese == "y":
            price += extra_cheeses
        print(f"Your total bill is cumulated to ${price}, Thank you.")
        print(thanks)

    if size == "l":
        price += l
        if add_pepperoni == "y":
            price += peperoni
        if extra_cheese == "y":
            price += extra_cheeses
        print(f"Your total bill is cumulated to ${price}, Thank you. \n")
        print(thanks)

    # A re-run loop to take additional order
    Run_again = input("Will you like to make another purchase order, 'Y' for yes and 'N' for no: \n")
    if Run_again == "y":
        Replay = True
    else:
        Replay = False
