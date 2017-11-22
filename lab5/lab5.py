from turtle import *
import random
class Square(Turtle):
    def __init__(self,size):
        Turtle.__init__(self)
        self.shapesize(size)
        self.shape("square")
    def random_color(self):
        a = random.randint(0,255)
        b = random.randint(0,255)
        c = random.randint(0,255)
        self.color(a,b,c)
        
     
s1 = Square(5)
s1.random_color()
