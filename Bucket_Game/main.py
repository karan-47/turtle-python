import turtle
import tkinter
import random
import time

screen = turtle.Screen()
screen.setup(700, 700)
screen.tracer(0)

pen = turtle.Turtle()
pen.speed(0)
pen.penup()
pen.hideturtle()

score = 0

small_bucket = tkinter.PhotoImage(file='bucket.gif').subsample(2, 2)
screen.addshape('bucketright', turtle.Shape('image', small_bucket))

ball_images = []
for i in range(4):
    screen.addshape('ball' + str(i + 1) + '.gif')
    ball_images.append('ball' + str(i + 1) + '.gif')


class Sprite():
    def __init__(self, x, y, shape, color):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = color
        self.speedx = 0
        self.speedy = 0

    def render(self):
        pen.goto(self.x, self.y)
        pen.color(self.color)
        pen.shape(self.shape)
        pen.stamp()

    def update(self):
        self.x += self.speedx
        self.y += self.speedy


class Bucket(Sprite):
    def __init__(self, x, y, shape, color):
        Sprite.__init__(self, x, y, shape, color)

    def left(self):
        self.x -= 5

    def right(self):
        self.x += 5

    def rest(self):
        self.speedx = 0


class Display(Sprite):
    def __init__(self, x=0, y=0, shape='turtle', color='red'):
        Sprite.__init__(self, x, y, shape, color)
        self.x = -300
        self.y = 300
        self.text = "score : 0"

    def update(self):
        global score
        self.text = "score : " + str(score)

    def render(self):
        pen.goto(self.x, self.y)
        pen.color('red')
        pen.hideturtle()
        pen.write(self.text)


class Ball(Sprite):

    def __init__(self):
        Sprite.__init__(self, random.randrange(-330, 330), random.randrange(400, 450), random.choice(ball_images),
                        'red')
        self.speedy = random.choice([-2, -1, -.9, -.8, -.7, -.6, -0.5, -0.4, -0.3, -0.2, -0.1])

    def check_screen(self):
        global score
        if abs(bucket.x - self.x) < 30 and -240 > self.y > -255:
            score += 10
            print(score)
            return True
        if self.y < -300.0:
            return True
        return False


bucket = Bucket(0, -270, 'bucketright', 'red')

sprites = [bucket]

balls = []
for i in range(8):
    b = Ball()
    balls.append(b)
    sprites.append(b)

screen.listen()

screen.onkeypress(bucket.left, 'Left')
screen.onkeypress(bucket.right, 'Right')

screen.onkeyrelease(bucket.rest, 'Left')
screen.onkeyrelease(bucket.rest, 'Right')


while True:
    # screen.delay(100)
    pen.clear()

    for s in sprites:
        s.update()
    time.sleep(0.008)
    for s in sprites:
        s.render()

    for b in balls:
        if b.check_screen():
            b.x = 1000
            b.y = 1000
            balls.remove(b)
            sprites.remove(b)
            a = Ball()
            balls.append(a)
            sprites.append(a)
    screen.update()
