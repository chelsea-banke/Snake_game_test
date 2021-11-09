import turtle
import structures

screen = turtle.Screen()
turtle.tracer(1, 0)
board = structures.Board(400)
food = structures.Food(400)
snake = structures.Snake(400)
key_play = structures.Control(screen, snake)

while True:
    snake.move()
    if snake.body_bite:
        break
    if snake.wall_collision():
        break
    if snake.fed(food.range()):
        snake.grow()
        food.change_location(snake.body)

screen.mainloop()

