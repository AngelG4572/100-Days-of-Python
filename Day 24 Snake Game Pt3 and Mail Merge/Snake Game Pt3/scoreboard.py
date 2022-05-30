from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Times New Roman", 15, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=270)
        self.score = 0
        with open("data.txt", mode="r") as file:
            self.high_score = int(file.read())
        self.update()

    def update(self):
        self.clear()
        self.write(arg=f"Score: {self.score},  High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def score_up(self):
        self.score += 1
        self.update()

    def reset(self):
        if self.score > self.high_score:
            with open("data.txt", mode="w") as file:
                self.high_score = self.score
                file.write(f"{self.high_score}")
        self.score = 0
        self.update()
