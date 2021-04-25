import turtle
alphabets = []
answer = ""
current = ""
guessedanswer = []
count = 10
clearedlist = []
isGuessed = False


display_turtle = turtle.Turtle()
display_turtle.hideturtle()
display_turtle.speed(0)


display_count = turtle.Turtle()
display_count.hideturtle()
display_count.speed(0)

turtle.tracer(0)


def countDisplay():
    global count
    display_count.clear()
    display_count.hideturtle()
    display_count.penup()
    display_count.goto(100, 100)
    display_count.write(count)

def displayAnswer():
    global current
    display_turtle.clear()
    display_turtle.hideturtle()
    display_turtle.penup()
    display_turtle.goto(0,100)
    cn = ""
    for i in range (len(current)):
        cn += current[i]+" "
    display_turtle.write(cn)

def setAnswer():
    global alphabets,answer,guessedanswer,isGuessed,current,clearedlist,count
    setAlphabets()
    count = 10
    answer = 'hello'.upper()
    for i in range(len(answer)):
        current = current + '_'
    guessedanswer = list(current)
    clearedlist = []
    isGuessed = False

def resetAnswer():
    global alphabets,answer,guessedanswer,isGuessed,current,clearedlist,count
    current = ''
    count = 10
    clearedlist = []
    alphabets = []
    answer = ""
    guessedanswer = []
    isGuessed = False

def setAlphabets():
    global alphabets
    for i in range(26):
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.speed(0)
        alphabets.append(t)
        t.goto(i*25 - 320, -200)
        t.write(chr(i+65))
def removeAlphabets():
    global alphabets
    for i in range(26):
        alphabets[i].clear()

def checkAnswer( char ):
    global answer,clearedlist,count
    global guessedanswer,current,alphabets
    if char not in clearedlist:
        clearedlist.append(char)
        if char in answer and char not in current:
            for i in range(len(answer)):
                if answer[i] == char:
                    guessedanswer[i] = char
            current = "".join(guessedanswer)
        else:
            count -= 1
    displayAnswer()
    countDisplay()
    t1 = list(char)
    clearAlphabet(ord(t1[0])-65)

def clearAlphabet(i):
    global alphabets
    alphabets[i].clear()

def a():
    checkAnswer('A')
def b():
    checkAnswer('B')
def c():
    checkAnswer('C')
def d():
    checkAnswer('D')
def e():
    checkAnswer('E')
def f():
    checkAnswer('F')
def g():
    checkAnswer('G')
def h():
    checkAnswer('H')
def i():
    checkAnswer('I')
def j():
    checkAnswer('J')
def k():
    checkAnswer('K')
def l():
    checkAnswer('L')
def m():
    checkAnswer('M')
def n():
    checkAnswer('N')
def o():
    checkAnswer('O')
def p():
    checkAnswer('P')
def q():
    checkAnswer('Q')
def r():
    checkAnswer('R')
def s():
    checkAnswer('S')
def t():
    checkAnswer('T')
def u():
    checkAnswer('U')
def v():
    checkAnswer('V')
def w():
    checkAnswer('W')
def x():
    checkAnswer('X')
def y():
    checkAnswer('Y')
def z():
    checkAnswer('Z')

turtle.listen()

setAnswer()
displayAnswer()
countDisplay()


turtle.onkey(a,"a")
turtle.onkey(b,"b")
turtle.onkey(c,"c")
turtle.onkey(d,"d")
turtle.onkey(e,"e")
turtle.onkey(f,"f")
turtle.onkey(g,"g")
turtle.onkey(h,"h")
turtle.onkey(i,"i")
turtle.onkey(j,"j")
turtle.onkey(k,"k")
turtle.onkey(l,"l")
turtle.onkey(m,"m")
turtle.onkey(n,"n")
turtle.onkey(o,"o")
turtle.onkey(p,"p")
turtle.onkey(q,"q")
turtle.onkey(r,"r")
turtle.onkey(s,"s")
turtle.onkey(t,"t")
turtle.onkey(u,"u")
turtle.onkey(v,"v")
turtle.onkey(w,"w")
turtle.onkey(x,"x")
turtle.onkey(y,"y")
turtle.onkey(z,"z")

# while True:
#     turtle.update()
#     turtle.tracer(0, 0)

turtle.mainloop()