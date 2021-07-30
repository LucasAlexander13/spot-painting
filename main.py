from colors import color_list
from random import choice
import turtle as turtle_module


screen = turtle_module.Screen()
tim = turtle_module.Turtle()
turtle_module.colormode(255)
tim.penup()
tim.setposition(-300, -255)

for i in range(11):
    for j in range(13):
        tim.dot(15, choice(color_list))
        tim.forward(50)
    tim.setposition(-300, i * 50 - 255)
    tim.left(90)
    tim.forward(50)
    tim.right(90)
