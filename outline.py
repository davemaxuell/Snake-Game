from turtle import Turtle

class Outline(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.speed(0)
        self.pencolor("white")
        self.penup()
        self.teleport(290, 290)
        self.pendown()
        self.goto(290, -290)
        self.goto(-290, -290)
        self.goto(-290, 290)
        self.goto(290, 290)