import time
from turtle import Screen

from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard

WIN_SCORE = 10

right_paddle = Paddle((330, 0))
left_paddle = Paddle((-330, -100))

ball = Ball()

scoreboard = Scoreboard()
screen = Screen()
screen.setup(800, 600)
screen.title('Ping Pong Game')
screen.tracer(0)
screen.listen()
screen.onkeypress(fun=right_paddle.go_up, key='Up')
screen.onkeypress(fun=right_paddle.go_down, key='Down')
screen.onkeypress(fun=left_paddle.go_up, key='w')
screen.onkeypress(fun=left_paddle.go_down, key='s')

game_on = True

while game_on:
    time.sleep(0.1)  # ball's speed
    ball.move()
    screen.update()

    # detect collision with the wall
    if ball.ycor() > 270 or ball.ycor() < -270:
        ball.bounce_wall()

    # detect collision with left paddle
    if (ball.xcor() <= -305 and
            (left_paddle.ycor() - 50 <= ball.ycor() <= left_paddle.ycor() + 50)):
        ball.bounce_paddle()

    # detect collision with right paddle
    if (ball.xcor() >= 305 and
            (right_paddle.ycor() - 50 <= ball.ycor() <= right_paddle.ycor() + 50)):
        ball.bounce_paddle()

    # right win
    if ball.xcor() < -380:
        scoreboard.update_right()  # update score
        ball.to_center()  # place ball to the center

    # left win
    if ball.xcor() > 380:
        scoreboard.update_left()  # update score
        ball.to_center()  # place ball to the center

    if scoreboard.left_score >= WIN_SCORE:
        scoreboard.print_winner('Left')
        game_on = False

    if scoreboard.right_score >= WIN_SCORE:
        scoreboard.print_winner('Right')
        game_on = False

# screen.exitonclick()
screen.mainloop()