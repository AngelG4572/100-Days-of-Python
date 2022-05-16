import art
from game_data import data
import random
from os import system, name


def clear():
    """Clears the screen (substitute for the repl.it function)"""
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def create_person():
    """Picks a random person/dictionary from game_data."""
    return random.choice(data)


def print_person(person):
    """Formats the data so it prints readably."""
    return f"{person['name']}, a {person['description']}, from {person['country']}."


def compare_candidates(first_choice, second_choice):
    """Compares the two choices and returns which one has more followers."""
    if first_choice["follower_count"] > second_choice["follower_count"]:
        return "A"
    else:
        return "B"


def game():
    print(art.logo)
    score = 0
    candidate_a = create_person()
    candidate_b = create_person()
    if candidate_b == candidate_a:
        candidate_b = create_person()
    running = True

    while running:
        print(f"Compare A: {print_person(candidate_a)}")
        print(art.vs)
        print(f"Against B: {print_person(candidate_b)}")

        guess = input("Who has more followers? Type 'A' or 'B': ").upper()
        clear()
        print(art.logo)

        if guess == compare_candidates(first_choice=candidate_a, second_choice=candidate_b):
            score += 1
            candidate_a = candidate_b
            candidate_b = create_person()
            print(f"You're right! Current score: {score}")
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            running = False


game()
