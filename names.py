from turtle import Turtle

class StateName(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
    
    def write_it(self, state_name, x, y):
        self.goto(x, y)
        self.write(state_name, align="center", font=("Calibri", 8, "bold"))