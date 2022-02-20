from turtle import * 
from warrior import Warrior
import time as t
from blocks import Blocks
from food import Food
from scoreboard import Scoreboard
screen = Screen()   #Setup our arena
screen.title("Game")
screen.setup(width=500, height=500)
screen.tracer(0)
game_on = True
food = Food()
ninja = Warrior()
block = Blocks()
scoreboard = Scoreboard()
block.hideturtle()
screen.onkey(ninja.up, "Up")    #Control of our ninja 
screen.onkey(ninja.down, "Down")
screen.onkey(ninja.left, "Left")
screen.onkey(ninja.right, "Right")
screen.listen()

while game_on:
    block.create_block()
    block.move_block()
    scoreboard.update()
    t.sleep(0.1)
    for piece in block.list:   #Detecting collision with blocks
        if ninja.distance(piece) < 20:
            scoreboard.reset()
            game_on = False
    if food.distance(ninja) < 10:  #Detecting collision with food
        food.change_pos()
        scoreboard.increase_score()
    
    
    
    
    
    
    
    screen.update()





screen.exitonclick()
