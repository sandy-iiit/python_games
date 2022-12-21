import math
from turtle import Turtle,Screen
import turtle as t
from prettytable import PrettyTable
import random
import colorgram
tur=Turtle()
sc=Screen()
tur.speed("fastest")
t.colormode(255)


def colour():
    r=random.randint(40,255)
    b=random.randint(40,255)
    g=random.randint(40,255)
    return (r,b,g)
# { this is polygon project
# def draw(sides):
#     for i in range(sides): 
#        tur.forward(50)
#        tur.right(angle)
#        print(angle) 
# sides=2
# for _ in range(50):
#     tur.color(colour())  

#     sides+=1
#     angle=360/sides
#     draw(sides)

# }



#{ this is random walk project
# l1=[0,90,180,270]




# def random_walk():
#     for _ in range(150):
#         tur.forward(45)
#         tur.color(colour())
#         tur.pensize(10)
#         tur.setheading(random.choice(l1))

# random_walk()     

#}

# {
# def spiral(k):
#  for _ in range(math.floor(360/k)):   
#   tur.circle(110)
#   tur.color(colour())

#   cur_heading=tur.heading()
#   tur.setheading(cur_heading+k)
#   tur.speed("fastest")

# spiral(10)
# }   



#dots game
# l2=[]
# colors=colorgram.extract("/Users/dattasandeepchoragudi/python/turtle/hirst.jpeg",20)
# for color in colors:
#     r=color.rgb.r
#     b=color.rgb.b
#     g=color.rgb.g
#     tup=(r,b,g)
#     l2.append(tup)

# tur.penup()
# tur.hideturtle()
# tur.setheading(225)
# tur.forward(300)
# tur.setheading(0)
# num=10


# for i in range(1,num+1):
  
#   for _ in range(10):  
#    tur.forward(50)
#    tur.dot(23,random.choice(l2))

#   if num%10==0:
#     tur.setheading(90)
#     tur.forward(50)
#     tur.setheading(180)
#     tur.forward(500)
#     tur.setheading(0)

#turtle race
sc.setup(width=500,height=400)

guess=sc.textinput(title="Make your bet",prompt="Which turtle will win the race?")

a=Turtle(shape="turtle")
b=Turtle(shape="turtle")
c=Turtle(shape="turtle")
d=Turtle(shape="turtle")
e=Turtle(shape="turtle")
f=Turtle(shape="turtle")
g=Turtle(shape="turtle")

l=[a,b,c,d,e,f,g]
c=["violet","indigo","blue","green","yellow","orange","red"]
k=150
for _ in range(7):
    l[_].penup()
    l[_].goto(x=-240,y=k)
    l[_].color(c[_])
    k-=50

if guess:
    is_on=True

while is_on:
 for i in l:
    if i.xcor()>230:
        is_on=False
        win=i.pencolor()
        if win==guess:
            print(f"You have won!{win} turtle won thw race")
        else:
            print(f"You have lost!{win} turtle won thw race")

    i.forward(random.randint(0,15))

# a.goto(x=-240,y=150)
# b.goto(x=-240,y=100)
# c.goto(x=-240,y=50)
# d.goto(x=-240,y=0)
# e.goto(x=-240,y=-50)
# f.goto(x=-240,y=-100)



sc.exitonclick() 
















# table=PrettyTable()
# print(table)
# table.add_column("Pokemon Name",["Pikachu","Eevee","Calyrex"])
# table.add_column("Type",["Electric","Normal","Fairy"])
# table.align="r"

# print(table)

