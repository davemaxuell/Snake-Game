import time
from turtle import Turtle, Screen


MOVE_DISTANCE = 20


class Snake:

    def __init__(self):
        self.snake_part = []
        self.tail = []
        self.go = True
        self.create_snake()
        self.head = self.snake_part[0]

    def create_snake(self):
        length = 3
        i = 0
        while i < length:
            turtle = Turtle(shape="square")
            turtle.color("white")
            turtle.shapesize(stretch_wid=1, stretch_len=1)
            turtle.penup()
            turtle.goto(x=i * 20, y=0)
            turtle.speed(0)
            self.snake_part.append(turtle)
            i += 1
        self.head = self.snake_part[0]

    def upwards(self):
        if self.head.heading() != 270:
            self.snake_part[0].setheading(90)
        
    def downwards(self):
        if self.head.heading() != 90:
            self.snake_part[0].setheading(270)

    def rightwards(self):
        if self.head.heading() != 180:
            self.snake_part[0].setheading(0)

    def leftwards(self):
        if self.head.heading() != 0:
            self.snake_part[0].setheading(180)
    
    def snake_move(self):
        for part in range(len(self.snake_part) - 1, 0, -1):
            new_x = self.snake_part[part - 1].xcor()
            new_y = self.snake_part[part - 1].ycor()
            self.snake_part[part].goto(new_x, new_y)
        self.snake_part[0].forward(MOVE_DISTANCE)
        for segment in self.snake_part[3:]:
            if self.head.distance(segment) < 10:
                self.go = False
        self.tail = self.snake_part[len(self.snake_part) - 1].position()
        
    def make_new(self):
        new = Turtle(shape="square")
        new.speed(0)
        new.penup()
        new.teleport(x= self.tail[0], y= self.tail[1])
        new.color("white")
        new.shapesize(stretch_wid=1, stretch_len=1)
        self.snake_part.append(new)