from turtle import Turtle
class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.speed(0)
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def go_up(self):
        y = self.ycor()
        y += 20
        self.goto(self.xcor(), y)

    def go_down(self):
        y = self.ycor()
        y -= 20
        self.goto(self.xcor(), y)