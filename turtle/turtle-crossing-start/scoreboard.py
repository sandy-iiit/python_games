from turtle import Turtle


FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.level=0
        self.hideturtle()
        self.penup()
        self.goto(-280,250)

    def update_score(self):
        self.clear()
        self.write(f"Level : {self.level}",align='left',font=FONT)

    def levelup(self):
        self.level+=1
        self.update_score()    

    def gameover(self):
        self.goto(0,0)
        self.write(f"Game Over",align="center",font=FONT)

    
