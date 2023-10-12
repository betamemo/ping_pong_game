from turtle import Turtle

N = 270


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('circle')
        # self.goto(random.randint(-N, N), random.randint(-N, N))
        self.x_speed = -10
        self.y_speed = -10

    def move(self):
        self.goto(self.xcor() + self.x_speed, self.ycor() + self.y_speed)

    def bounce_wall(self):
        self.y_speed *= -1
        print('wall')

    def bounce_paddle(self):
        self.x_speed *= -1
        print('paddle')