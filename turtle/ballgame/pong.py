
from turtle import Turtle,Screen

from paddle import Paddle

from ball import Ball

from scoreboard import Scoreboard

import time


tur=Turtle()
sc=Screen()

sc.bgcolor("black")
tur.speed("fastest")
sc.setup(width=800,height=600)
sc.title("Pong")
sc.tracer(0)


lpaddle=Paddle((-350,0))
rpaddle=Paddle((350,0))
b=Ball()
s=Scoreboard()



   

sc.listen()
sc.onkeypress(lpaddle.go_up,"w")
sc.onkeypress(lpaddle.go_down,"s")


sc.onkeypress(rpaddle.go_up,"Up")
sc.onkeypress(rpaddle.go_down,"Down")


ison=True

while ison:
    time.sleep(b.ball_speed)

    sc.update()

    b.move()
    if b.ycor()>280 or b.ycor()<-280:
        b.bounceY()
    if b.distance(rpaddle)<50 and b.xcor()>320 or b.distance(lpaddle)<50 and b.xcor()<-320:
        b.bounceX()
    if b.xcor()>380  :
        b.reset_position()
        s.lpoint()
    if b.xcor()<-380:
        b.reset_position()   
        s.rpoint()





sc.exitonclick()
