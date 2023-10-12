from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.penup()
        self.shape('square')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.setposition(pos)
