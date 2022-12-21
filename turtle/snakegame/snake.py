from mimetypes import init
from random import choice
from turtle import Turtle
colors=["red","blue","violet","white","yellow","orange","cyan","pink","green"]

starting_positions=[(0,0),(-20,0),(-40,0)]
forward_dist=20
Left=180
Right=0
Up=90
Down=270

class Snake:
   def __init__(self) -> None:
      self.segments=[]
      self.createsnake()
      self.head=self.segments[0]
    
   def createsnake(self):
      for position in starting_positions:
          self.add_segment(position)

   def add_segment(self,position):
         segment=Turtle(shape="square")
         segment.color("light blue")
         segment.penup()
         segment.goto(position)
         self.segments.append(segment)
   def extend(self):
         self.add_segment(self.segments[-1].position())
   def move(self):
        for seg_num in range(len(self.segments)-1,0,-1):
            new_x=self.segments[seg_num-1].xcor()
            new_y=self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x,new_y)
        self.head.forward(forward_dist)    
   
   def up(self):
      if self.head.heading()!=Down:
         self.head.setheading(Up)
   def down(self):
     if self.head.heading()!=Up:
        self.head.setheading(Down)
   def left(self):
      if self.head.heading()!=Right:

         self.segments[0].setheading(Left)            
   def right(self):
      if self.head.heading()!=Left:

         self.segments[0].setheading(Right)      

   def reset(self):
      for seg in self.segments:
         seg.goto(1000,2000)
      self.segments.clear()
      self.createsnake()
      self.head=self.segments[0]





