from turtle import Turtle, Screen
import random

running = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
count = 0
all_turtles = []
for color in colors:
    count += 1
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(color)
    new_turtle.goto(x=-230, y=-140 + (count * 40))
    all_turtles.append(new_turtle)

if user_bet:
    running = True

while running:
    for turtle in all_turtles:
        if turtle.xcor() >= 230:
            running = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You won! The {winning_color} turtle is the winner!")
            else:
                print(f"You lost! The {winning_color} turtle is the winner!")
        turtle.forward(random.randint(0, 10))

screen.exitonclick()
