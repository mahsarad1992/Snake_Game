import turtle
ALIGNMENT = "center"
FONT = ("Arial", 14, "normal")
GAMEOVERFONT = ("courier", 28, "normal")
class Score(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(x=0, y=280)
        self.write(f"Score {self.score}", align=ALIGNMENT, font=FONT)
        self.hideturtle()

    def gameover(self):
        self.goto(x=0, y=0)
        self.write("G A M E    O V E R", align= ALIGNMENT, font=GAMEOVERFONT)

    def scorecounter(self):
        self.score += 1
        self.clear()
        self.write(f"Score {self.score}", align=ALIGNMENT, font=FONT)

