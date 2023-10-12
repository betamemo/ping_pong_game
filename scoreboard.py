from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.left_score = 0
        self.right_score = 0
        self.print_score()

    def print_score(self):
        self.goto(0, 200)
        self.write(f'{self.left_score}\t:\t{self.right_score}', align='center', font=('Arial', 50, 'normal'))

    def update_left(self):
        self.left_score += 10
        self.clear()
        self.print_score()

    def update_right(self):
        self.right_score += 10
        self.clear()
        self.print_score()

    def print_winner(self, winner_name):
        self.goto(0,0)
        self.write(f'{winner_name} win!',align='center',font=('Arial',100, 'normal'))

