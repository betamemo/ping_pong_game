import time
from turtle import Screen

from ball import Ball
from paddle import Paddle

screen = Screen()
screen.screensize(100, 100, 'lightyellow')
# screen.tracer(0)
# screen.update()
screen.listen()

# turtle = Turtle()
# turtle.hideturtle()

p1 = Paddle((300, 0))
p2 = Paddle((-300, 0))

ball = Ball()

while True:
    time.sleep(0.1)  # ball's speed
    ball.move()
