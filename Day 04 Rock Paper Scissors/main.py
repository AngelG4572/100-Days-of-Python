rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
hand = [rock, paper, scissors]

print("Welcome to rock, paper, scissors<3")
user_choice = int(input("What do you choose? 0 for rock, 1 for paper, and 2 for scissors. "))
computer = random.randint(0,2)
computer_choice = hand[computer]

message = hand[user_choice] + "\nComputer chose:\n" + computer_choice
print(message)


if computer == user_choice:
  print("It's a draw.")
elif hand[user_choice] == hand[computer - 1]:
  print("You lose.")
elif hand[computer] == hand[user_choice - 1]:
  print("You win.")
else:
  print("You broke it dawg")

#I doubt you ever will but, beb if you're reading this, I love you <3