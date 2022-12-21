

from turtle import Turtle


class Paddle(Turtle):

    def __init__(self,position) -> None:
        
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=1,stretch_wid=5)
        self.color("white")
        self.penup()
        self.goto(position)


    def go_up(self):
      ny=self.ycor()+20
      self.goto(self.xcor(),ny)

    def go_down(self):
      ny=self.ycor()-20
      self.goto(self.xcor(),ny)     
