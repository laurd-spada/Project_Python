#
from art import logo

print(logo)
print("Welcome to the Love Calculator!")

name1 = input("What is your name ? : ")
name2 = input("What is their name ? : ")

combination = name1.lower() + name2.lower()
t = combination.count("t")
r = combination.count("r")
u = combination.count("u")
e = combination.count("e")

true = t + r + u + e

l = combination.count("l")
o = combination.count("o")
v = combination.count("v")
e = combination.count("e")

love = l + o + v + e

string_combination = str(true) + str(love)
final_combination = int(string_combination)

if (final_combination < 10) or (final_combination > 90):
    print(f"Your score is {final_combination}, you go together like coke and mentors.")

elif (final_combination >= 40) and (final_combination <= 50):
    print(f"Your score is {final_combination}, you are alright together.")

else:
    print(f"Your score is {final_combination}.")
