from turtle import Turtle

class Ball(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("Circle")
        self.penup()
        self.x_move= 10
        self.y_move= 10


    def move(self):
        new_x = self.xcor() + 10 
        new_y = self.ycor() + 10
        self.goto(new_x, new_y)
        
    def bounce_y(self):
        self.y_move *= -1
    
    def bounce_x(self):
        self.x_move *= -1
        