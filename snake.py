from turtle import Turtle

STARTING_POSITION_SNAKE = [(0, 0), (-20, 0), (-40, 0)]
DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:
    def __init__(self):
        self.body_of_snake = []
        self.create_snake()
        self.head_of_snake = self.body_of_snake[0]
        self.head_of_snake.shape("circle")
        self.head_of_snake.shapesize(2, 2)

    def create_snake(self):
        for position in STARTING_POSITION_SNAKE[1:]:
            self.add_to_body_snake(position)

    def reset_snake(self):
        for seg in self.body_of_snake:
            seg.goto(1000, 1000)
        self.body_of_snake.clear()
        self.create_snake()
        self.head_of_snake = self.body_of_snake[0]
        self.head_of_snake.shape("circle")
        self.head_of_snake.shapesize(2, 2)

    def add_to_body_snake(self, position):
        snake = Turtle()
        snake.color("green")
        snake.shape("square")
        snake.penup()
        snake.goto(position)
        snake.speed("fastest")
        self.body_of_snake.append(snake)

    def add_to_body(self):
        self.add_to_body_snake((self.body_of_snake[-1].xcor() - DISTANCE, self.body_of_snake[-1].ycor() - DISTANCE))
        # self.snake_movement()

    def move_snake(self):
        for snake_piece in range(len(self.body_of_snake) - 1, 0, -1):
            new_x = self.body_of_snake[snake_piece - 1].xcor()
            new_y = self.body_of_snake[snake_piece - 1].ycor()
            self.body_of_snake[snake_piece].goto(new_x, new_y)
        self.head_of_snake.forward(DISTANCE)

    def up(self):
        if self.head_of_snake.heading() != DOWN:
            self.head_of_snake.setheading(UP)

    def down(self):
        if  self.head_of_snake.heading() != UP:
            self.head_of_snake.setheading(DOWN)

    def left(self):
        if self.head_of_snake.heading() != RIGHT:
            self.head_of_snake.setheading(LEFT)

    def right(self):
        if self.head_of_snake.heading() != LEFT:
            self.head_of_snake.setheading(RIGHT)

