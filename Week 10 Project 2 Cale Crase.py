"""
Program: Week10 Project2
Author: Cale Crase

This program prompts the user for the level of
a c-curve and draws a c-curve of that level.
"""

from turtle import Turtle, tracer, update
import random
color = ["green", "black", "white", "orange", "pink"]

def cCurve(t, x1, y1, x2, y2, level):
   
   def drawLine(x1, y1, x2, y2):
      """Draws a line segment between the endpoints."""
      t.up()
      t.goto(x1, y1)
      t.down()
      t.goto(x2, y2)
      colors = random.choice(color)
      t.color(colors)
   if level == 0:
      drawLine(x1, y1, x2, y2)
   else:
      xm = (x1 + x2 + y1 - y2) // 2
      ym = (x2 + y1 + y2 - x1) // 2
      cCurve(t, x1, y1, xm, ym, level - 1)
      cCurve(t, xm, ym, x2, y2, level - 1)

def getColor():
    return tuple(randint(0,255) for _ in range(3))

def main():
   level = int(input("Enter the level (0 or greater): "))
   t = Turtle()
   if level > 8:
      tracer(False)
   t.speed(0)
   t.hideturtle()
   cCurve(t, 50, -50, 50, 50, level)
   if level > 8:
      update()

if __name__ == "__main__":
   main()

