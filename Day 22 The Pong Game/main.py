from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle(x=350, y=0)
l_paddle = Paddle(x=-350, y=0)
ball = Ball()
r_score = Scoreboard(30, 260)
l_score = Scoreboard(-30, 260)

screen.listen()
screen.onkeypress(fun=l_paddle.up, key="w")
screen.onkeypress(fun=l_paddle.down, key="s")
screen.onkeypress(fun=r_paddle.up, key="Up")
screen.onkeypress(fun=r_paddle.down, key="Down")


running = True
while running:
    time.sleep(ball.move_speed)
    screen.update()

    if -280 < ball.ycor() < 290:
        ball.move()
    else:
        ball.y_bounce()

    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.x_bounce()
        ball.speed_up()
    elif ball.xcor() >= 380:
        ball.reset()
        l_score.score_up()
    elif ball.xcor() <= -380:
        ball.reset()
        r_score.score_up()


screen.exitonclick()