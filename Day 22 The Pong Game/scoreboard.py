from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Times New Roman", 30, "normal")

class Scoreboard(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x=x, y=y)
        self.score = 0
        self.update_score()

    def update_score(self):
        self.write(arg=self.score, align=ALIGNMENT, font=FONT)

    def score_up(self):
        self.score += 1
        self.clear()
        self.update_score()

