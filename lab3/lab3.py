import turtle
import random
color = ["red","blue","yellow","green","grey","black"]
i = 0
for kayvon in range(200):
    turtle.forward(150)
    turtle.right(45)
    turtle.forward(100)
    turtle.right(135)
    turtle.forward(50)
    turtle.left(1)
    turtle.color(color[i])
    i = i +1
    if i == 6:
        i = 0

       
    
