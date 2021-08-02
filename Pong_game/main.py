from turtle import Screen
from board import Board
from ball import Ball
from time import sleep
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("PONG GAME")

screen.tracer(0)

right_board = Board((350, 0))
left_board = Board((-350, 0))
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkeypress(right_board.go_up, "Up")
screen.onkeypress(right_board.go_down, "Down")
screen.onkeypress(left_board.go_up, "w")
screen.onkeypress(left_board.go_down, "s")

game_on = True
while game_on:
    sleep(ball.speed_track)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    # collision between right board and ball
    if ball.distance(right_board) < 40 and ball.xcor() > 320 or ball.distance(left_board) < 40 and ball.xcor() < -320:
        ball.bounce_back()

    # collision of ball to edge
    if ball.xcor() > 380:
        ball.reset_position()
        score.increase_left_score()

    if ball.xcor() < -380:
        ball.reset_position()
        score.increase_right_score()

screen.exitonclick()
