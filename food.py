from  turtle import Turtle
import random
import time

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("yellow")
        self.speed(0)
        self.eaten()
        
    def eaten(self):
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        self.goto(x, y)