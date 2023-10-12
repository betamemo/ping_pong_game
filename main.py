import time
from turtle import Screen

from ball import Ball
from paddle import Paddle

right_paddle = Paddle((330, 0))
left_paddle = Paddle((-330, -100))

screen = Screen()
screen.setup(800, 600)
screen.title('Ping Pong Game')
screen.tracer(0)
screen.listen()
screen.onkeypress(fun=right_paddle.go_up, key='Up')
screen.onkeypress(fun=right_paddle.go_down, key='Down')
screen.onkeypress(fun=left_paddle.go_up, key='w')
screen.onkeypress(fun=left_paddle.go_down, key='s')

ball = Ball()

while True:
    time.sleep(0.1)  # ball's speed
    ball.move()
    screen.update()

    # detect collision with the wall
    if ball.ycor() > 270 or ball.ycor() < -270:
        ball.bounce_wall()

    # detect collision with left paddle
    if (ball.xcor() <= -310 and
            (left_paddle.ycor() - 50 <= ball.ycor() <= left_paddle.ycor() + 50)):
        ball.bounce_paddle()

    # detect collision with right paddle
    if (ball.xcor() >= 310 and
            (right_paddle.ycor() - 50 <= ball.ycor() <= right_paddle.ycor() + 50)):
        ball.bounce_paddle()
