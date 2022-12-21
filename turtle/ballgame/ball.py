
from turtle import Turtle


class Ball(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.xmove=10
        self.ymove=10
        self.ball_speed=0.1

    def move(self):
        nx=self.xcor()+self.xmove
        ny=self.ycor()+self.ymove
        self.goto(nx,ny)

    def bounceY(self):

        self.ymove*=-1
        self.ball_speed*=0.9
    
    def bounceX(self):

        self.xmove*=-1
        self.ball_speed*=0.9


    def reset_position(self):

        self.goto(0,0)
        self.ball_speed=0.1
        self.bounceX()    
    

