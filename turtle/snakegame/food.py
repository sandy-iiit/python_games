import random
from turtle import Turtle


class Food(Turtle):
   def __init__(self):
      super().__init__()
      self.shape("circle")
      self.penup()
      self.shapesize(stretch_len=0.6,stretch_wid=0.6)
      self.speed("fastest")
      self.color("red")
      self.refresh()

   def refresh(self):
       x_cor=random.randint(-280,280)
       y_cor=random.randint(-280,280)
       self.goto(x_cor,y_cor)