from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("highscore.txt") as high:
            self.highscore = int(high.read())
        self.color("black")     
        self.penup()
        self.goto(10, 210)
        self.hideturtle()
        self.update()
    

    def update(self):
        self.clear()
        self.write(f"Score: {self.score} Highscore: {self.highscore}", align="center", font=("Sans-serif", 18, "normal",'normal', 'bold', 'italic'))

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("highscore.txt", mode="w") as high:
                high.write(f"{self.highscore}") #Updating highscore
        self.score = 0

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update()