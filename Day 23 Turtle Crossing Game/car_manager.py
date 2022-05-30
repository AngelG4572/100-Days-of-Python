from turtle import Turtle
from random import randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.create_car()

    def create_car(self):
        spawn_rate = randint(0, 3)
        if spawn_rate == 0:
            new_car = Turtle()
            new_car.penup()
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color((randint(0, 255), randint(0, 255), randint(0, 255)))
            new_car.setheading(180)
            new_car.goto(x=randint(250, 500), y=randint(-240, 240))
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.forward(MOVE_INCREMENT)
