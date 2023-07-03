from turtle import Screen
from paddle import Paddle
from ball import Ball

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
ball = Ball()


screen.listen()
scree.onkey(r_paddle.go_up, "Up")
scree.onkey(r_paddle.go_down, "Down")
scree.onkey(l_paddle.go_up, "w")
scree.onkey(l_paddle.go_down, "s")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    
    #Detect the colision with wall 
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    # Detect collision with  both paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320 :
        ball.bounce_x()
    # Detect R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
    
    
    # Detect L paddle misses
    if ball.xcor() > -380:
        ball.reset_position()
    
screen.exitonclick()
