from turtle import Turtle, Screen
import random

color_list = [(54, 108, 149), (225, 201, 108), (134, 85, 58), (224, 141, 62), (197, 144, 171), (143, 180, 206),
              (137, 82, 106), (210, 90, 68)]

jimmy = Turtle()
screen = Screen()
screen.colormode(255)
jimmy.penup()
jimmy.hideturtle()
jimmy.speed(10)

starting_x = -240
starting_y = -240
jimmy.goto(starting_x, starting_y)

for y in range(10):
    for x in range(10):
        jimmy.dot(20, random.choice(color_list))
        jimmy.forward(50)
    jimmy.goto(starting_x, jimmy.ycor() + 50)


screen.exitonclick()
