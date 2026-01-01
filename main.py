from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from score import Score
game_is_on = True

screen = Screen()
screen.setup(width=800, height=600)
screen.title('Ping Pong Game')
screen.bgcolor('black')
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
coin  = Ball()
score = Score()

screen.listen()
screen.onkey(r_paddle.go_up,'w')
screen.onkey(r_paddle.go_down,'s')
screen.onkey(l_paddle.go_up,'Up')
screen.onkey(l_paddle.go_down,'Down')

while game_is_on:
    time.sleep(coin.speeding)
    screen.update()
    coin.move()

    if coin.ycor() > 280 or coin.ycor() < -280:
        coin.bounce_y()

    if coin.distance(r_paddle) < 40 and coin.xcor() > 320 or coin.distance(l_paddle) < 40 and coin.xcor() < -320:
        coin.bounce_x()

    if coin.xcor() > 380:
        coin.reset_ball()
        score.increase_l_score()
        score.update_score()
        screen.update()

    if coin.xcor() < -380:
        coin.reset_ball()
        score.increase_r_score()
        score.update_score()

    if score.l_score == 10 or score.r_score == 10:
        game_is_on = False

screen.exitonclick()