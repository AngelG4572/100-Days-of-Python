from art import logo

# import only system from os
from os import system, name

# define our clear function
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

print(logo)
print("Welcome to the secret auction program.")

bidders_dict = {}

while True:
    user = input("What's your name? ")
    bid = int(input("What's your bid? $"))
    bidders_dict[user] = bid
    add_bidder = input("Are there any other bidders? Type 'yes' or 'no'. ")

    if add_bidder == "no":
        break
    else:
        clear()

highest_bid = 0
winner = ''
for bidder in bidders_dict:
    if bidders_dict[bidder] >= highest_bid:
        highest_bid = bidders_dict[bidder]
        winner = bidder

clear()
print(f"The highest bidder is {winner} at ${highest_bid}.")