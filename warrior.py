from turtle import Turtle


class Warrior(Turtle):

    def __init__(self):
        super().__init__()
        self.create()




    def create(self):
        self.penup()
        self.color("green")
        self.shape("turtle")


    def up(self):
        self.forward(15)
    def down(self):
        self.backward(15)
    def right(self):
        self.setheading(self.heading() - 30)
    def left(self):
        self.setheading(self.heading() + 30)
