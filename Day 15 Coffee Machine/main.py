MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
money = 0


def report():
    """Prints a report of the resources and profit."""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")


def check_resources(drink):
    """Compares the drink ingredients against the resources to see if there's enough to make the coffee."""
    for ingredient in MENU[drink]["ingredients"]:
        if resources[ingredient] < MENU[drink]["ingredients"][ingredient]:
            print(f"Sorry, there's not enough {ingredient}.")
            return False
    return True


def check_money():
    """Take's in the user's coins and calculates their value."""
    print("Please insert coins.")
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickels = int(input("How many nickels? "))
    pennies = int(input("How many pennies? "))
    total = (quarters * 0.25) + (dimes * 0.1) + (nickels * 0.05) + (pennies * 0.01)
    return total


running = True
while running:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        running = False
    elif choice == "report":
        report()
    elif choice == "espresso" or "latte" or "cappuccino":
        if check_resources(drink=choice):
            amount = check_money()
            if amount < MENU[choice]["cost"]:
                print("Sorry, that's not enough money. Money refunded.")
            else:
                change = round(amount - MENU[choice]["cost"], 2)
                if change != 0:
                    print(f"Here is ${change} in change.")
                money += MENU[choice]["cost"]
                for x in MENU[choice]["ingredients"]:
                    resources[x] -= MENU[choice]["ingredients"][x]
                print(f"Here is your {choice}. Enjoy!")
