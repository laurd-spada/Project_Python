# This a program that runs basic arithmetics
# defining a addition function
from art import logo
print("Welcome to Basic Calculator")
print("Provide the requested details and begin \n")


def add(n1, n2):
    return n1 + n2


# defining a subtract function
def sub(n1, n2):
    return n1 - n2


# defining a division function
def div(n1, n2):
    return n1 / n2


# defining a multiplication function
def multi(n1, n2):
    return n1 * n2


operation = {
    "+": add,
    "-": sub,
    "/": div,
    "*": multi
}


def calculator():
    print(logo)

    num1 = int(input("Input first number: "))
    for symbols in operation:
        print(symbols)

    should_continue = True
    while should_continue:
        operation_symbol = input("Pick an operation symbol: ")
        num2 = int(input("input next number: "))

        calculation_function = operation[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")
        if input(f"Type y to continue calculating with {answer} or type n to exit: ") == "y":
            num1 = answer
        else:
            should_continue = False


calculator()
