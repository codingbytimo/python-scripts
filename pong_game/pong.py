# little pong game

import turtle

window = turtle.Screen()
window.title("Pong game by Timo")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

# pad left
padLeft = turtle.Turtle()
padLeft.speed(0)
padLeft.shape("square")
padLeft.color("blue")
padLeft.shapesize(stretch_wid=5, stretch_len=1)
padLeft.penup()
padLeft.goto(-350, 0)

# pad right
padRight = turtle.Turtle()
padRight.speed(0)
padRight.shape("square")
padRight.color("red")
padRight.shapesize(stretch_wid=5, stretch_len=1)
padRight.penup()
padRight.goto(350, 0)

# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("yellow")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2
ball.dy = 0.2

# writing

# padMovement
def padLeft_up():
    y = padLeft.ycor()
    y += 25
    padLeft.sety(y)

def padLeft_down():
    y = padLeft.ycor()
    y -= 25
    padLeft.sety(y)

def padRight_up():
    y = padRight.ycor()
    y += 25
    padRight.sety(y)

def padRight_down():
    y = padRight.ycor()
    y -= 25
    padRight.sety(y)

# keyboard bindings
window.listen()
window.onkeypress(padLeft_up, "w")
window.onkeypress(padLeft_down, "s")
window.onkeypress(padRight_up, "Up")
window.onkeypress(padRight_down, "Down")

# main game
while True:
    window.update()
    # moving the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # border check
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1

    # paddle and ball collision
    if ball.xcor() < -340 and ball.ycor() < padLeft.ycor() + 50 and ball.ycor() > padLeft.ycor() - 50:
        ball.dx *= -1 
    
    elif ball.xcor() > 340 and ball.ycor() < padRight.ycor() + 50 and ball.ycor() > padRight.ycor() - 50:
        ball.dx *= -1
        
    