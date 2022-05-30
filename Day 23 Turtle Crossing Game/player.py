from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 7


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.setheading(90)
        self.new_start()

    def move_forward(self):
        self.forward(MOVE_DISTANCE)

    def new_start(self):
        self.goto(STARTING_POSITION)
