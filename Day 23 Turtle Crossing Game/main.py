import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Crossy Turtle")
screen.tracer(0)
screen.colormode(255)
scoreboard = Scoreboard()
jimmy = Player()
car_manager = CarManager()

screen.listen()
screen.onkeypress(fun=jimmy.move_forward, key="w")

time_delay = 0.05
game_is_on = True
while game_is_on:
    time.sleep(time_delay)
    screen.update()
    car_manager.move_cars()
    car_manager.create_car()

    if jimmy.ycor() > 280:
        jimmy.new_start()
        scoreboard.score_up()
        time_delay *= 0.9

    for car in car_manager.all_cars:
        if car.distance(jimmy) < 22:
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()
