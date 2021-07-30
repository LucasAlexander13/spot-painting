from colors import color_list
from random import choice
from turtle import Screen, Turtle

screen = Screen()
tim = Turtle()
tim.shape('circle')

for i in range(50):
    color = choice(color_list)
    tim.color(color[0], color[1], color[2])
    tim.forward(20)
