import turtle
from turtle import Turtle
import random
import math

# setting up Initial food position parameters
food_pos=[]
a = random.randint(-190, 190)
b = random.randint(-190, 190)
foodline_pos = Turtle()
foodline_pos.hideturtle()
foodline_pos.up()
foodline_pos.goto(a,b)
foodline = []

#Score display
score= 0
pen = turtle.Turtle()
pen.goto(0,0)
pen.speed(0)
pen.shape("square")
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  ", align="center", font=("Courier", 24, "normal"))

grid=Turtle()
grid.hideturtle()
grid.up()
grid.goto(-200,-200)
grid.down()
grid.goto(-200,200)
grid.goto(200,200)
grid.goto(200,-200)
grid.goto(-200,-200)

#setting up screen parameters
scrn = turtle.Screen()
#scrn.setup(width = 400, height = 400)
turtle.tracer(0,0)

#Setting up bite parameters
bite = False
store = []

##setting up snakehead parameters
hd = Turtle()
hd.width(10)
hd.speed(0)

#seting up snake tail tracer parameters
tl = Turtle()
tl.width(10)
tl.color('white')
tl.hideturtle()
tl.speed(0)

# Setting up turtle food parameters
food = Turtle()
food.shape('circle')
food.width(10)
food.color('blue')
food.up()
food.goto(a,b)
food.setheading(90)
food.fd(5)
food.down()

# Initialising food position
for o in range(360):
    test = []
    foodline_pos.fd(0.2)
    foodline_pos.left(1)
    u = math.ceil(foodline_pos.xcor())
    v = math.ceil(foodline_pos.ycor())
    test.append(u)
    test.append(v)
    foodline.append(test)

#colour changing function
def col(cl, head=hd):
    head.color(cl)

#Snake control functions
def up(head=hd):
    if head.heading() != 90 and head.heading() != 270:
            head.setheading(90)


def left(head=hd):
    if head.heading() != 0 and head.heading() != 180:
            head.setheading(180)


def down(head=hd):
    if head.heading() != 270 and head.heading() != 90:
            head.setheading(270)


def right(head=hd):
    if head.heading() != 0 and head.heading() != 180:
            head.setheading(0)


scrn.listen()
scrn.onkeypress(up, 'Up')
scrn.onkeypress(left, 'Left')
scrn.onkeypress(down, 'Down')
scrn.onkeypress(right, 'Right')

#creating initial snake body
for i in range(50):
    temp = []
    u = hd.xcor()
    v = hd.ycor()
    temp.append(u)
    temp.append(v)
    store.append(temp)
    hd.fd(1)

#setting up clour changing variables
clr=0
num=0
colors = ['green', 'red', 'yellow']

while bite == False:
    turtle.update()
    hd.speed(0)
    tl.speed(0)
    #Changing snake colour
    if clr % 10 == 0:
        col(colors[num])
        num += 1
        if num == 3:
            num = 0
    turtle.update()
    hd.fd(1)
    scrn.update()

    #geting snake current head position and stores in pos
    pos = []
    x = hd.xcor()
    y = hd.ycor()
    pos.append(x)
    pos.append(y)

    #checking for bites with the body
    for j in store:
        if j == pos:
            bite = True
            pen.clear()
            pen.write(f"GAME OVER!!! Score: {score}".format(score), align="center", font=("Courier", 24, "normal"))
            break

    #checking for collisions with wall
    if x == 195 or x == -195 or y == 195 or y == -195:
        bite = True
        pen.clear()
        pen.write(f" GAME OVER!!! Score: {score}".format(score), align="center", font=("Courier", 24, "normal"))

    #checking for snake contact with food
    for l in foodline:
        if pos == l:
            score+=1
            for p in range(10):
                hd.fd(1)
                el=[]
                x = hd.xcor()
                y = hd.ycor()
                el.append(x)
                el.append(y)
                store.append(el)

            pen.clear()
            pen.write(f"Score: {score}".format(score), align="center", font=("Courier", 24, "normal"))

            #setting food new position
            a = random.randint(-190, 190)
            b = random.randint(-190, 190)
            food_pos=[a,b]
            for i in store:
                if i == food_pos or [0,0]:
                    a = random.randint(-190, 190)
                    b = random.randint(-190, 190)
                    food_pos = [a, b]
                else:
                    continue
            food.up()
            food.goto(a, b)
            food.fd(5)
            food.down
            turtle.tracer(0, 0)

            foodline_pos.goto(a, b)
            foodline = []
            for o in range(360):
                test = []
                foodline_pos.fd(0.2)
                foodline_pos.left(1)
                u = math.ceil(foodline_pos.xcor())
                v = math.ceil(foodline_pos.ycor())
                test.append(u)
                test.append(v)
                foodline.append(test)
            break
        else:
            continue

    #Erasing snake traces
    store.append(pos)
    pos = store[0]
    x = pos[0]
    y = pos[1]
    tl.goto(x, y)
    store.remove(store[0])
    clr += 1

scrn.mainloop()