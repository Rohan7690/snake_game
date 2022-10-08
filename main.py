from turtle import Screen
from snake import Snake
from food import Food
from score_board import Score_board
import time

snake = Snake()
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
game_is_on = True
score_board = Score_board()

food = Food()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # detech collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score_board.increase_score()
    #detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor()<-290 or snake.head.ycor() >280 or snake.head.ycor()<-280:
        score_board.reset()
        snake.reset()


    #Detect collision with tail:
    for segment in snake.segments[1:]:

        if snake.head.distance(segment) < 10:
            pass
        elif snake.head.distance(segment) < 10:
            score_board.reset()
            snake.reset()

screen.exitonclick()
