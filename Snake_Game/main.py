from turtle import *
import time
import random

screen = Screen()

screen.setup(800, 800)
screen._root.resizable(False,False)
screen.tracer(0)

pen = Turtle()
pen.penup()
pen.hideturtle()
pen.goto(390, 390)
pen.color('black')
pen.pendown()
pen.goto(390, -390)
pen.goto(-390, -390)
pen.goto(-390, 390)
pen.goto(390, 390)
pen.penup()

player = Turtle()
player.penup()
player.x_dir = 1
player.y_dir = 0
player.color('BLACK')
player.shape('square')

body = []

ball = Turtle()
ball.shape('circle')
ball.penup()
ball.goto(random.randrange(-360, 360), random.randrange(-360, 360))


def check_collision1():
    if player.distance(ball) < 20:
        ball.goto(random.randrange(-360, 360), random.randrange(-360, 360))
        layer = Turtle()
        layer.shape('square')
        layer.color('RED')
        layer.penup()
        body.append(layer)


def move_body():
    for i in range(len(body) - 1, 0, -1):
        x = body[i-1].xcor()
        y = body[i-1].ycor()
        body[i].goto(x, y)
    if len(body) > 0:
        body[0].goto(player.xcor(), player.ycor())


def up():
    if player.y_dir == -1:
        return
    player.x_dir = 0
    player.y_dir = 1
    player.setheading(90)


def down():
    if player.y_dir == 1:
        return
    player.x_dir = 0
    player.y_dir = -1
    player.setheading(270)


def left():
    if player.x_dir == 1:
        return
    player.x_dir = -1
    player.y_dir = 0
    player.setheading(180)


def right():
    if player.x_dir == -1:
        return
    player.x_dir = 1
    player.y_dir = 0
    player.setheading(0)


listen()

onkey(up, 'Up')
onkey(down, 'Down')
onkey(left, 'Left')
onkey(right, 'Right')


def move_player():
    player.goto(player.xcor() + player.x_dir * 22, player.ycor() + player.y_dir * 22)


def check_collision2():
    global flag
    for part in body:
        if player.distance(part) < 20:
            flag = False


def check_collision3():
    global flag
    if player.xcor() < -380 or player.xcor() > 380 or player.ycor() < -380 or player.ycor() > 380:
        flag = False


flag = True

while flag:
    time.sleep(0.1)
    check_collision1()
    check_collision2()
    check_collision3()
    move_body()
    move_player()
    update()

screen.clear()
screen.bgcolor('black')

mainloop()
