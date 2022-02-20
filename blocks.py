from turtle import Turtle
import random as r
COLORS = ["red", "blue", "pink", "purple", "orange", "black", "yellow"] #Base of colors for ours cars 

class Blocks(Turtle):

    def __init__(self):
        super().__init__()
        self.list = []




    def create_block(self):
        x = r.randint(1,6)     #Creating a car(potential obstacle).  
        if x == 1 or x == 6:   #I have used an asbtract motive of throwing dices to limit generation-
            block = Turtle()   #-to limit generation of cars and below to choose a starting position
            block.shape("square")
            block.color(r.choice(COLORS))
            block.penup()
            x = r.randint(0,3)
            if x == 0:
                block.setheading(0)
                block.goto(x =-250, y = r.randint(-250,250))
            elif x == 1:
                block.setheading(180)
                block.goto(x = 250, y = r.randint(-250,250))
            elif x == 2:
                block.setheading(270)
                block.goto(x = r.randint(-250,250), y = 250)          
            else:
                block.setheading(90)
                block.goto(x = r.randint(-250,250), y = -250)
            self.list.append(block)


    def move_block(self):
        for blck in self.list:
            blck.forward(10)   