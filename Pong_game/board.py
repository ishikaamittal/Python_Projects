from turtle import Turtle


class Board(Turtle):
    def __init__(self, position_axis):
        super().__init__()

        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position_axis)

    def go_up(self):
        new_y = self.ycor() + 25
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y_down = self.ycor() - 25
        self.goto(self.xcor(), new_y_down)

