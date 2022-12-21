from random import random
from turtle import Turtle
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    
    def __init__(self) -> None:
        self.all_cars=[]

    def create_car(self):
        chance=random.randint(1,6)
        if chance==1:
            new_car=Turtle("square")
            new_car.shapesize(stretch_wid=1,stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            rand_y=random.randint(-250,250)
            new_car.goto(300,rand_y)
            self.all_cars.append(new_car)
            self.car_speed=STARTING_MOVE_DISTANCE

    def move(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def speed_up(self):
        self.car_speed+=MOVE_INCREMENT





