"""
Program: Week10 Project 1
Author: Cale Crase
Drawing Circle
"""
from turtle import Turtle
import math
def drawCircle(t, x, y, r):
    t.up()
    t.goto(x + r, y)
    t.setheading(90)
    t.down()
    for count in range(120):
        t.left(3)
        t.forward(2.0 * math.pi * r / 120)
    
