import turtle
import random

def move_forward():
      turtle.setheading(90)
      turtle.forward(50)
      turtle.stamp()

def move_right():
      turtle.setheading(0)
      turtle.forward(50)
      turtle.stamp()

def move_left():
      turtle.setheading(180)
      turtle.forward(50)
      turtle.stamp()

def move_back():
      turtle.setheading(270)
      turtle.forward(50)
      turtle.stamp()

def restart():
      turtle.reset()

turtle.shape('turtle')

turtle.onkey(move_forward, 'w')
turtle.onkey(move_right, 'd')
turtle.onkey(move_left, 'a')
turtle.onkey(move_back, 's')
turtle.onkey(restart, 'Escape')

turtle.listen()
      
