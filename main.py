import turtle
import time
from snake import Snake
import food
from scorekeeper import Score
# preparing the screen for our game
screen = turtle.Screen()
screen.setup(width=600, height=600)
NUM = 290
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
# making the objects snake, food and score
snake = Snake()
snake.makesnake()
food = food.Food()
score = Score()
# using keyboard to move the snake
screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left_go, key="Left")
screen.onkey(fun=snake.right_go, key="Right")

# different segments of snake move as it's a whole object
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 10:
        score.scorecounter()
        snake.length_grower()
        food.refresh()
    # detect collision with wall
    if snake.head.xcor() >= NUM or snake.head.xcor() <= -NUM or snake.head.ycor() >= NUM or snake.head.ycor() <= -NUM:
        game_is_on = False
        score.gameover()

    # detect collision with tail


screen.exitonclick()