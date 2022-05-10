from art import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    print(logo)
    n1 = float(input("What's the first number?: "))

    for symbol in operations:
        print(symbol)

    calculating = True
    while calculating == True: 
        choice = input("Pick an operation: ")
        n2 = float(input("What's the next number?: "))
        calculation = operations[choice]
        answer = calculation(n1, n2)
        print(f"{n1} {choice} {n2} = {answer}")

        if input(f"Type 'y' to continue working with {answer}, or type 'n' to start a new calculation. ") == "y":
            n1 = answer
        else:
            calculating = False
            calculator()

calculator()