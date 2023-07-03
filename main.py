from turtle import Screen
from paddle import Paddle

Screen = Screen()
screen.bgcolor = ("black")
screen.setup(width=800, height=600)
screen.title("Pong")
scree.tracer(0)

paddle = Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=5, stretch_len=1)
paddle.penup()
paddle.goto(350,0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))

screen.listen()
scree.onkey(r_paddle.go_up, "Up")
scree.onkey(r_paddle.go_down, "Down")
scree.onkey(l_paddle.go_up, "w")
scree.onkey(l_paddle.go_down, "s")


game_is_on = True
while game_is_on:
    screen.update()
    
    
screen.exitonclick()
