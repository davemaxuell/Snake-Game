from food import Food

class Scoreboard(Food):

    def __init__(self):
        super().__init__()
        self.point = -1
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=260)
        self.pendown()
        self.pencolor("white")
        self.write(f"{self.point}", align="center", font=("Arial", 20, "bold"))
        self.update()
        
    def update(self):
        self.clear()
        self.point += 1
        self.write(f"{self.point}", align="center", font=("Arial", 20, "bold"))
