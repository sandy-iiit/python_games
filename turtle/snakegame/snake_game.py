import time
from turtle import Turtle,Screen
import turtle as t
from snake import Snake
from food import Food 
from scoreboard import Scoreboard 
tur=Turtle()
sc=Screen()
tur.speed("fastest")
t.colormode(255)
sc.setup(width=600,height=600)
sc.bgcolor("black")
sc.title("My snake game")
sc.tracer(0)


snake=Snake()
food=Food()
sb=Scoreboard()


sc.listen()
sc.onkeypress(snake.up,"Up")
sc.onkeypress(snake.down,"Down")
sc.onkeypress(snake.left,"Left")
sc.onkeypress(snake.right,"Right")

is_on=True

while is_on:
    sc.update()
    time.sleep(0.12)
    snake.move()
    
    if snake.head.distance(food)<15:
        
        food.refresh()
        sb.incr_score()
        snake.extend()
    
    if snake.head.xcor()>280 or snake.head.ycor()>280 or snake.head.xcor()<-280 or snake.head.ycor()<-280:
        
        # is_on=False
        sb.reset()
        snake.reset()

    for segment in snake.segments[1:]: 
        # if segment==snake.head:
        #     pass
        if snake.head.distance(segment)<10:
            # is_on=False
            sb.reset()
            snake.reset()

 






sc.exitonclick() 
