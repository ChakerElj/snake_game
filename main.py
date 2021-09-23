from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("Snake Game")

snake = Snake()
food = Food()
score = Score()
print(snake.head_of_snake.width())
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    screen.listen()
    time.sleep(0.1)
    snake.move_snake()
    if snake.head_of_snake.xcor() >= 298 or snake.head_of_snake.xcor() <= -298 or snake.head_of_snake.ycor() >= 298 or snake.head_of_snake.ycor() <= -298:
        snake.reset_snake()
        score.reset()

    if snake.head_of_snake.distance(food) < 15:
        food.position_of_food()
        snake.add_to_body()
        score.increase_score()
    for snake_piece in snake.body_of_snake[1:]:
        if snake_piece.distance(snake.head_of_snake) < 15:
            snake.reset_snake()
            score.reset()



screen.exitonclick()
