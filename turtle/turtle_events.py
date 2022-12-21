import math
from turtle import Turtle,Screen
import turtle as t
from prettytable import PrettyTable
import random
import colorgram
tur=Turtle()
sc=Screen()


def move_forward():
    tur.forward(15)

def move_backward():
    tur.backward(15)

def anticlockwise():
   new_heading= tur.heading()+10
   tur.setheading(new_heading)

def clockwise():
    new_heading=tur.heading()-10
    tur.setheading(new_heading)

def clearscr():
    tur.clear()
    tur.penup()
    tur.home()
    tur.pendown()

sc.listen()
sc.onkey(key="Up",fun=move_forward)
sc.onkey(key="Down",fun=move_backward)
sc.onkey(key="Left",fun=anticlockwise)
sc.onkey(key="Right",fun=clockwise)
sc.onkey(key="space",fun=clearscr)

sc.exitonclick() 
