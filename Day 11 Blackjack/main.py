import random
from tabnanny import check
from art import logo
from os import system, name

def clear():
    '''Clears the screen (substitute for repl.it function)'''
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def deal_card(player_cards):
    '''Gives the player/computer a card.'''
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    player_cards.append(random.choice(cards))

def score(player_cards):
    '''Checks the score of the player/computer's cards, and decide if they have Blackjack and/or if Ace is worth 1 or 11.'''
    if (sum(player_cards) == 21) and (len(player_cards) == 2):
        return 0

    if (sum(player_cards) > 21) and (11 in player_cards):
        player_cards.insert(player_cards.index(11), 1)
        player_cards.remove(11)

    return sum(player_cards)

def check_winner(user_cards, computer_cards):
    '''Compares scores and checks if they won or lost.'''
    if score(user_cards) == 0:
        if score(computer_cards) == 0: 
            print("You lost. Computer has blackjack.")
        else:
            print("You win! You got blackjack.")
    elif score(user_cards) > 21:
        print("You went over. You lost.")
    elif score(computer_cards) > 21:
        print("You won!")
    elif score(user_cards) == score(computer_cards):
        print("Draw.")
    elif (score(user_cards) > score(computer_cards)):
        print("You win<3")
    elif (score(user_cards) < score(computer_cards)):
        print("You lost.")

    
def scoreboard(user_cards, computer_cards):
    '''prints the cards and scores.'''
    print(f"Your cards: {user_cards}, current score: {score(user_cards)}")
    print(f"Computer's first card: {computer_cards[0]}")

def new_game():
    user_cards = []
    computer_cards = []
    running = True
    clear()
    print(logo)
    for x in range(2):
        deal_card(user_cards)
        deal_card(computer_cards)

    scoreboard(user_cards, computer_cards)
    while running:
        if score(user_cards) > 21: 
            break
        elif score(user_cards) == 0 or score(computer_cards) == 0:
            break
        elif score(user_cards) <= 21: 
            choice = input("Do you want to draw another card? ")
            if choice == "y":
                deal_card(user_cards)
                scoreboard(user_cards, computer_cards)
            elif choice == "n":
                while score(computer_cards) < 17:
                    deal_card(computer_cards)
                break

    print(f"Your final cards are: {user_cards}, and score is: {score(user_cards)}.")
    print(f"The computer's final cards are: {computer_cards}, and score is: {score(computer_cards)}.")
    check_winner(user_cards, computer_cards)
    if input("Do you want to play again? Type 'y' or 'n': ") == 'y':
        new_game()
    else:
        print("bye i guess :(")

if input("Would you like to play a game of blackjack? Type 'y' or 'n': ") == 'y':
    new_game()    
else:
    print("rude :(")

#This project is dedicated to beb, thanks for helping me debug my code <333