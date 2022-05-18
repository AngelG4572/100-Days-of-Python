from turtle import Turtle, Screen

jimmy = Turtle()
screen = Screen()


def move_forwards():
    jimmy.forward(10)


def move_backwards():
    jimmy.backward(10)


def turn_counterclockwise():
    jimmy.left(10)


def turn_clockwise():
    jimmy.right(10)


def clear_screem():
    screen.resetscreen()

screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="a", fun=turn_counterclockwise)
screen.onkey(key="d", fun=turn_clockwise)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="c", fun=clear_screem)

screen.exitonclick()
