from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for x in range(3):
            new_square = Turtle(shape="square")
            new_square.color("white")
            new_square.penup()
            new_square.goto(x=(0 - (x * 20)), y=0)
            self.segments.append(new_square)

    def move(self):
        for square in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[square - 1].xcor()
            new_y = self.segments[square - 1].ycor()
            self.segments[square].goto(x=new_x, y=new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
