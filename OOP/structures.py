import turtle
import random
import math


class Snake:
    def __init__(self, limit):
        # setting a limiting range for snake movement
        self.limit = limit // 2 - 5

        # setting up the snake's head
        self.head = turtle.Turtle()
        self.head.width(10)
        self.head.speed(0)
        self.head.speed(0)

        # setting up the snake's tail
        self.tail = turtle.Turtle()
        self.tail.width(10)
        self.tail.color('white')
        self.tail.hideturtle()
        self.tail.speed(0)

        # setting up the snake's body
        self.body = []
        for i in range(50):
            temp = []
            u = self.head.xcor()
            v = self.head.ycor()
            temp.append(u)
            temp.append(v)
            self.body.append(temp)
            self.head.fd(1)

    def h_cord(self):
        # getting the snake's head location
        position = []
        x = self.head.xcor()
        y = self.head.ycor()
        position.append(x)
        position.append(y)
        return position

    def body_bite(self):
        # checking for snake bite with the body
        bite = False
        if Snake.h_cord(self) in self.body:
            bite = True
        return bite

    def wall_collision(self):
        # checking for snake collision with wall limit
        collision = False
        if (Snake.h_cord(self)[0] == self.limit
                or Snake.h_cord(self)[0] == -1 * self.limit
                or Snake.h_cord(self)[1] == self.limit
                or Snake.h_cord(self)[1] == -1 * self.limit):
            collision = True
        return collision

    def grow(self, length=10):
        # increasing the snake's length after it is being fed
        for p in range(length):
            self.head.fd(1)
            el = []
            x = self.head.xcor()
            y = self.head.ycor()
            el.append(x)
            el.append(y)
            self.body.append(el)

    def fed(self, food_range):
        eaten = False
        if Snake.h_cord(self) in food_range:
            eaten = True
        return eaten

    def move(self):
        # simultaneously moving the snake's head and tail forward
        self.head.fd(1)
        self.body.append(Snake.h_cord(self))

        self.tail.goto(self.body[0][0], self.body[0][1])
        self.body.remove(self.body[0])


class Food:
    def __init__(self, limit):
        self.limits = limit // 2 - 5  # initialising food limit
        self.food = turtle.Turtle()  # initialising food
        self.food_range = []  # initialising food range

        # initialising food range determiner
        self.food_line = turtle.Turtle()
        self.food_line.hideturtle()
        self.food_line.up()

        # setting up food initial position
        a = random.randint(-self.limits, self.limits)
        b = random.randint(-self.limits, self.limits)

        # setting up food parameters
        self.food.shape('circle')
        self.food.width(10)
        self.food.color('blue')
        self.food.up()
        self.food.goto(a, b)
        self.food.setheading(90)
        self.food.fd(5)
        self.food.down()

        # getting initial food range
        self.food_line.goto(a, b)
        for o in range(360):
            test = []
            self.food_line.fd(0.2)
            self.food_line.left(1)
            u = math.ceil(self.food_line.xcor())
            v = math.ceil(self.food_line.ycor())
            test.append(u)
            test.append(v)
            self.food_range.append(test)

    def position(self):
        # getting the food's location range
        position = []
        x = self.food.xcor()
        y = self.food.ycor()
        position.append(x)
        position.append(y)
        return position

    def range(self):
        # getting foods range
        self.food_range = []
        self.food_line.goto(Food.position(self)[0], Food.position(self)[1])
        for o in range(360):
            test = []
            self.food_line.fd(0.2)
            self.food_line.left(1)
            u = math.ceil(self.food_line.xcor())
            v = math.ceil(self.food_line.ycor())
            test.append(u)
            test.append(v)
            self.food_range.append(test)
        return self.food_range

    def change_location(self, snake_body):
        # setting new food position
        a = random.randint(-self.limits, self.limits)
        b = random.randint(-self.limits, self.limits)
        food_pos = [a, b]
        while food_pos in snake_body:
            a = random.randint(-190, 190)
            b = random.randint(-190, 190)
            food_pos = [a, b]
        self.food.up()
        self.food.goto(a, b)
        self.food.fd(5)


class Board:
    def __init__(self, dimension):
        dimension = dimension // 2
        grid = turtle.Turtle()
        grid.hideturtle()
        grid.up()
        grid.goto(-dimension, -dimension)
        grid.down()
        grid.goto(-dimension, dimension)
        grid.goto(dimension, dimension)
        grid.goto(dimension, -dimension)
        grid.goto(-dimension, -dimension)


class Control:
    # Snake control functions
    def __init__(self, scrn, snake):
        def up(head=snake.head):
            if head.heading() != 90 and head.heading() != 270:
                head.setheading(90)

        def left(head=snake.head):
            if head.heading() != 0 and head.heading() != 180:
                head.setheading(180)

        def down(head=snake.head):
            if head.heading() != 270 and head.heading() != 90:
                head.setheading(270)

        def right(head=snake.head):
            if head.heading() != 0 and head.heading() != 180:
                head.setheading(0)

        # configuring control commands
        scrn.listen()
        scrn.onkeypress(up, 'Up')
        scrn.onkeypress(left, 'Left')
        scrn.onkeypress(down, 'Down')
        scrn.onkeypress(right, 'Right')