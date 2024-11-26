from turtle import Turtle

class Gameover(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=180)
        self.pendown()
        self.pencolor("red")
        self.write("GAME OVER", align="center", font=("Arial", 40, "bold"))