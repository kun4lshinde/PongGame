# Getting Started

import turtle

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
score_1 = 0
score_2 = 0

# Player 1
player1 = turtle.Turtle()
player1.speed(0)
player1.shape("square")
player1.color("white")
player1.shapesize(stretch_wid=5 , stretch_len=1)
player1.penup()
player1.goto(-350, 0)

# Player 2
player2 = turtle.Turtle()
player2.speed(0)
player2.shape("square")
player2.color("white")
player2.shapesize(stretch_wid=5 , stretch_len=1)
player2.penup()
player2.goto(350, 0)


# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("lightgreen")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2
ball.dy = -0.2

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player1: 0  Player2: 0", align="center", font=("Courier", 24, "normal"))


# Actions
def player1_up():
	y = player1.ycor()
	y += 20
	player1.sety(y)

def player1_down():
	y = player1.ycor()
	y -= 20
	player1.sety(y)


def player2_up():
	y = player2.ycor()
	y += 20
	player2.sety(y)

def player2_down():
	y = player2.ycor()
	y -= 20
	player2.sety(y)

# Keyboard Input
wn.listen()
wn.onkeypress(player1_up, "w")
wn.onkeypress(player1_down, "s")
wn.onkeypress(player2_up, "Up")
wn.onkeypress(player2_down, "Down")

# Main Game
while True:
	wn.update()


	# Move ball
	ball.setx(ball.xcor() + ball.dx)
	ball.sety(ball.ycor() + ball.dy)

	# Border Check
	if ball.ycor() > 290:
		ball.sety(290)
		ball.dy *= -1

	if ball.ycor() < -290:
		ball.sety(-290)
		ball.dy *= -1

	if ball.xcor() > 390:
		ball.goto(0,0)
		ball.dx *= -1

	if ball.xcor() < -390:
		ball.goto(0,0)
		ball.dx *= -1

	# Ball bounce
	if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < player2.ycor() + 40 and ball.ycor() > player2.ycor() - 40):
		ball.setx(340)	
		ball.dx *= -1	

	if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < player1.ycor() + 40 and ball.ycor() > player1.ycor() - 40):
		ball.setx(-340)	
		ball.dx *= -1