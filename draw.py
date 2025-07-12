from turtle import Turtle, Screen, clearscreen
import numpy as np

tim = Turtle()
screen= Screen()
screen.setup(height=500,width=400)
user_draw = np.zeros((500, 400), dtype=int)

def move_forwards():
    tim.forward(10)
    print(tim.pos())
    print(round(tim.pos()[0]))
    print(round(tim.pos()[1]))
    for i in range(11):
        user_draw[round(tim.pos()[1])+250][round(tim.pos()[0])+200+i] = 1
    #tim.goto(x=tim.pos()[0] + 10.0,y=tim.pos()[1])


def move_backward():
    tim.backward(10)
    print(tim.pos())
    print(round(tim.pos()[0]))
    print(round(tim.pos()[1]))
    user_draw[round(tim.pos()[1])+250][round(tim.pos()[0])+200] = 1

def turn_left():
    tim.seth(tim.heading() + 10)
    print(tim.pos())
    print(tim.heading())

def turn_right():
    tim.seth(tim.heading() - 10)
    print(tim.pos())
    print(tim.heading())

def clear_screen():
    tim.penup()
    tim.clear()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear_screen)

screen.exitonclick()

np.savetxt('basic_array.csv', user_draw, delimiter=',')