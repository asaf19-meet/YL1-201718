##list = [1,2,3]
##for i in range(3):
##    print(list[i])
##    list[i] = list[i]*2
##    print(list[i])
##print(list[0]+list[1]+list[2])
import turtle
turtle.penup()
##turtle.begin_fill()
##turtle.goto(100,0)
##turtle.goto(100,100)
##turtle.goto(0,100)
##turtle.goto(0,0)
##turtle.end_fill()
turtle.color("blue")
turtle.goto(-50,50)
turtle.pendown()
turtle.circle(35)
turtle.penup()
turtle.color("yellow")
turtle.goto(-25,25)
turtle.pendown()
turtle.circle(35)
turtle.penup()
turtle.color("black")
turtle.goto(0,50)
turtle.pendown()
turtle.circle(35)
turtle.penup()
turtle.color("green")
turtle.goto(25,25)
turtle.pendown()
turtle.circle(35)
turtle.penup()
turtle.color("red")
turtle.goto(50,50)
turtle.pendown()
turtle.circle(35)
turtle.penup()
turtle.mainloop()
