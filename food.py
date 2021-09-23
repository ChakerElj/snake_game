from turtle import Turtle
import random



class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.color("red")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.shape("circle")
        self.position_of_food()

    def position_of_food(self):
        food_pos_x = random.randint(-280, 280)
        food_pos_y = random.randint(-280, 280)
        position = (food_pos_x, food_pos_y)
        self.goto(position)
