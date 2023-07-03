from turtle import Turtle


class Paddle(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("White")
        self.shapesize(stretch_wid=5, stretch_len=1)
        sefl.penup()
        self.goto(350,0)
    
    def go_up(sefl):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)



    def go_down(sefl):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
