import turtle
# win
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("f_pong game")
wn.setup(width=800, height=600)
wn.tracer(0)

# paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.color("white")
paddle_a.shape("square")
paddle_a.shapesize(5,1)
paddle_a.penup()
paddle_a.setpos(-350,0)

# paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.color("red")
paddle_b.shape("square")
paddle_b.shapesize(5,1)
paddle_b.penup()
paddle_b.setpos(350,0)

# Ball

ball = turtle.Turtle()
ball.color("blue")
ball.speed(0)
ball.shape("circle")
ball.shapesize(1,1)
ball.penup()
ball.setpos(0,0)
ball_dx = 2
ball_dy = 2


# paddles movement function

def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


# keyboard binding

wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")


while True:
    wn.update()

    #ball movement
    ball.setx(ball.xcor() + ball_dx)
    ball.sety(ball.ycor() + ball_dy)

    # define the boarder
    if ball.ycor() > 290:
        ball.sety(290)
        ball_dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball_dy *= -1


