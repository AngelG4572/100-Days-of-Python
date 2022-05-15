from art import logo
import random

number = random.randint(1, 100)
print(logo)

HARD_CHANCES = 5
EASY_CHANCES = 10

print("Welcome to the Number Guessing Game! I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

if difficulty == "easy":
    lives = EASY_CHANCES
else:
    lives = HARD_CHANCES


def check_number(user_guess, answer):
    if user_guess > answer:
        print("Too High.")
        return lives - 1
    elif user_guess < answer:
        print("Too Low.")
        return lives - 1
    elif user_guess == answer:
        print(f"You got it! The number was {answer}.")
        return 100


while lives > 0:
    print(f"You have {lives} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    lives = check_number(user_guess=guess, answer=number)
    if lives == 100:
        break
else:
    print("You've run out of guesses, you lose.")
