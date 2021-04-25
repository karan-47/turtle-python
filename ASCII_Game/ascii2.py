import turtle
import time
import random

turtle.tracer(0)
screen = turtle.Screen()
ship = turtle.Turtle()
ship.shape('triangle')
ship.up()
ship.goto(200, 350)
ship.x_dir = -1
ship.setheading(180)
ship.level = 1
ship.word = -1

print_word = turtle.Turtle()
print_word.up()
print_word.ht()
print_word.goto(-350, 365)


bullets = []
tanks = []
alphabets = []
for i in range(26):
    alphabets.append(i)
x_list = []
val = -350
while val < 350:
    x_list.append(val)
    val += 50


def set_tanks():
    global alphabets, tanks, x_list
    for i in range(len(tanks)-1, -1, -1):
        tanks[i].clear()
        tanks[i].ht()
        tanks.remove(tanks[i])
    temp_list = []
    temp_list2 = []
    for i in range(5):
        tank = turtle.Turtle()
        ch = random.choice(alphabets)
        alphabets.remove(ch)
        temp_list.append(ch)
        tank.word = ch
        tank.penup()
        tanks.append(tank)
        temp = random.choice(x_list)
        temp_list2.append(temp)
        x_list.remove(temp)
        tank.goto(temp, -350)
        tank.write(str(ch+65), font=('Arial', 18, 'normal'))
    alphabets = alphabets + temp_list
    ship.word = random.choice(temp_list)
    x_list = x_list + temp_list2


def set_left():
    ship.x_dir = -1
    ship.setheading(180)


def set_right():
    ship.x_dir = 1
    ship.setheading(0)


def set_ship():
    if ship.xcor() < -400:
        set_right()
    if ship.xcor() > 400:
        set_left()
    ship.goto(ship.xcor() + ship.x_dir * ship.level, 350)


def set_bullet():
    if len(bullets) == 5:
        return
    x = ship.xcor()
    y = ship.ycor()
    direction = ship.x_dir
    bullet1 = turtle.Turtle()
    bullet1.shape('circle')
    bullet1.penup()
    bullet1.goto(x, y)
    bullets.append(bullet1)
    bullet1.direction = direction


def move_bullet(self):
    if self.xcor() > 400 or self.xcor() < -400 or self.ycor() < -350:
        self.ht()
        self.clear()
        bullets.remove(self)
    self.goto(self.xcor() + self.direction * ship.level * 2 / 5, self.ycor() - 3 * ship.level * 2 / 5)


def clear_bullets():
    global bullets
    for b in range(len(bullets)-1, -1, -1):
        bullets[b].clear()
        bullets[b].ht()
        bullets.remove(bullets[b])


def check_collision_tank(bullet):
    global flag
    for tank in tanks:
        if bullet.distance(tank) < 20:
            if tank.word == ship.word:
                ship.level += 1
                set_tanks()
                display_word()
            else:
                flag = False
            clear_bullets()


def display_word():
    print_word.clear()
    print_word.write(chr(ship.word+65))


turtle.listen()


turtle.onkeypress(set_left, 'Left')
turtle.onkeypress(set_right, 'Right')
turtle.onkeypress(set_bullet, 'space')


flag = True

set_tanks()
display_word()

while flag and ship.level != 6:
    turtle.update()
    time.sleep(0.015)
    set_ship()
    for t in bullets:
        move_bullet(t)
    for t in bullets:
        check_collision_tank(t)

screen.clear()
if not flag:
    import gameover
else:
    import congrats
