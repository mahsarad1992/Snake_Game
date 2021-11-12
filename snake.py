import turtle

screen = turtle.Screen()
INITIAL_POSITION = [(0, 0), (-10, 0), (-20, 0)]
MOVE_STEP = 10


class Snake:

    def __init__(self):
        self.whole_snake = []
        self.makesnake()
        self.head = self.whole_snake[0]

    def makesnake(self):
        for position in INITIAL_POSITION:
            self.add_segment(position)

    def move(self):
        for i in range(len(self.whole_snake) - 1, 0, -1):
            x_component = self.whole_snake[i - 1].xcor()
            y_component = self.whole_snake[i - 1].ycor()
            self.whole_snake[i].goto(x_component, y_component)
        self.head.forward(MOVE_STEP)

    def add_segment(self, position):
        snake = turtle.Turtle()
        snake.shape("square")
        snake.color("white")
        snake.penup()
        snake.resizemode("user")
        snake.shapesize(0.5, 0.5)
        snake.goto(position)
        self.whole_snake.append(snake)
        return self.whole_snake

    def length_grower(self):
        # add new segment to the snake
        self.add_segment(self.whole_snake[-1].position())

    def up(self):
        if self.head.heading() != 270:
            self.head.seth(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.seth(270)

    def left_go(self):
        if self.head.heading() != 0:
            self.head.seth(180)

    def right_go(self):
        if self.head.heading() != 180:
            self.head.seth(0)
