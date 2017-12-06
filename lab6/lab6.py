from turtle import *
import random
import math

class Ball(Turtle):
    def __init__(self,radius,color,speed):
        Turtle.__init__(self)
        self.shape("circle")
        self.shapesize(radius/10)
        self.radius = radius
        self.color(color)
        self.speed(speed)
        
def check_collision(ball1,ball2):
    x1=ball1.xcor()
    x2=ball2.xcor()
    y1=ball1.ycor()
    y2=ball2.ycor()
    if (ball1.radius+ball2.radius)>(math.sqrt(math.pow((x2-x1),2) + math.pow((y2-y1),2))):
        ball1.color("red")
        ball1.goto(100,100)
        ball2.goto(-100,100)
        ball2.color("yellow")
        ball2.goto(50,50)
        
ball1 = Ball(10,"green",10)
ball2 = Ball(10,"blue",15)

check_collision(ball1,ball2)
