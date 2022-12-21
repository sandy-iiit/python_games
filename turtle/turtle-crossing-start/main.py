import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

p=Player()
cars=CarManager() 
screen.listen()
score=Scoreboard()

screen.onkeypress(p.go_up,"Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_car()
    cars.move()
    
    for car in cars.all_cars:
        if car.distance(p)<20:
            score.gameover()
            game_is_on=False


    if p.finished():
        p.go_to_start()        
        cars.speed_up()
        score.levelup()




screen.exitonclick()        