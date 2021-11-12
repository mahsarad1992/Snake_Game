import random
import turtle


class Food(turtle.Turtle):


    def __init__(self):
        super().__init__()

        self.shape("circle")
        self.penup()
        self.shapesize(0.4)
        self.color("SlateBlue2")

        self.speed("fastest")
        self.refresh()

    def refresh(self):
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        self.goto(x, y)
