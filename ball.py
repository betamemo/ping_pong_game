import random
from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('circle')
        self.x_speed = random.choice([-10, 10])
        self.y_speed = random.choice([-10, 10])

    def move(self):
        self.goto(self.xcor() + self.x_speed, self.ycor() + self.y_speed)

    def bounce_wall(self):
        self.y_speed *= -1

    def bounce_paddle(self):
        self.x_speed *= -1

    def to_center(self):
        self.goto(0, 0)
