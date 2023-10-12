import random
from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('circle')
        self.goto(random.randint(-300, 300), random.randint(-300, 300))
        self.x_speed = 10
        self.y_speed = 10

    def move(self):
        print(self.pos())
        self.goto(self.xcor() + self.x_speed, self.ycor() + self.y_speed)
