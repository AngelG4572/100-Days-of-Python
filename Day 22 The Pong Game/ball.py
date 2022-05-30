from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.y_move = 10
        self.x_move = 10
        self.move_speed = 0.09

    def move(self):
        self.goto(x=(self.xcor() + self.x_move), y=(self.ycor() + self.y_move))

    def y_bounce(self):
        self.y_move *= -1
        self.move()

    def x_bounce(self):
        self.x_move *= -1
        self.move()

    def reset(self):
        self.goto(x=0, y=0)
        self.move_speed = 0.09
        self.x_bounce()

    def speed_up(self):
        self.move_speed *= 0.9

