from turtle import Turtle, Screen


class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(x=x, y=y)

    def up(self):
        self.goto(x=self.xcor(), y=self.ycor() + 20)

    def down(self):
        self.goto(x=self.xcor(), y=self.ycor() - 20)


# right_paddle = Turtle(shape="square")
# right_paddle.shapesize(stretch_wid=5, stretch_len=1)
# right_paddle.penup()
# right_paddle.color("white")
# right_paddle.goto(x=350, y=0)
# screen.update()
#
# def up():
#     right_paddle.goto(x=right_paddle.xcor(), y=right_paddle.ycor() + 20)
#

