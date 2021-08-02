from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_Score = 0
        self.right_Score = 0
        self.update()

    def update(self):
        self.clear()
        self.goto(-80, 210)
        self.write(self.left_Score, align="center", font=("Courier", 50, "normal"))
        self.goto(80, 210)
        self.write(self.right_Score, align="center", font=("Courier", 50, "normal"))

    def increase_right_score(self):
        self.right_Score += 1
        self.update()

    def increase_left_score(self):
        self.left_Score += 1
        self.update()