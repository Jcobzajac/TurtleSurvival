from turtle import Turtle
import random as r
class Food(Turtle):
    
    def __init__(self): 
        super().__init__()
        self.color("blue")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.penup()
        self.shape("circle")
        self.goto(x = r.randint(-220,220), y = r.randint(-220,220))

    def change_pos(self): #Changing location of food after collision
        self.goto(x = r.randint(-220,220), y = r.randint(-220,220))