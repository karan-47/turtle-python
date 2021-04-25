import turtle

screen = turtle.Screen()

screen.setup(800, 800)

turtle.tracer(0)
'''sets automatic screen update to zero we use turtle.update to update screen manually it makes our code run smoother 
and faster '''
flag = True


def set_flag():
    global flag
    flag = False


turtle.listen()


turtle.onkey(set_flag, 'Return')
pen = turtle.Turtle()
pen.ht()
pen.write('Press Enter to start')

while flag:
    turtle.update()
pen.clear()
import ascii2