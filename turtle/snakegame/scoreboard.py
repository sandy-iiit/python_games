

from turtle import Turtle


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score=0
        with open("./highscore.txt","r") as g:
            self.highscore=int(g.read())
            g.close()
        self.penup()
        self.goto(0,275)
        self.color("white")
       
        self.write(f"Score = {self.score} High Score= {self.highscore}",align="center",font=("Arial",24,"normal"))
        self.hideturtle()


    def incr_score(self):
        self.score+=1
        self.clear()
        self.update_scoreboard()


    def reset(self):
        if self.score>self.highscore:
            self.highscore=self.score
            with open("./highscore.txt","w") as f:
                f.write(f"{self.highscore}")
                f.close()
        self.score=0 
        self.update_scoreboard()    

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER🙃!",align="center",font=("Algerian",32,"normal"))

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score = {self.score} High Score={self.highscore}",align="center",font=("Arial",24,"italic"))





