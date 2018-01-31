import turtle
import time
import random
import math 
from ball import Ball

turtle.tracer(0)
turtle.hideturtle()

writer=turtle.clone()
eaten_balls=0
running = True
sleep = 0.0077
screen_width=turtle.getcanvas().winfo_width()/2
screen_height=turtle.getcanvas().winfo_height()/2

MY_BALL=Ball(0,0,0,0,50,"green")

number_of_balls = 5
min_ball_r=10
max_ball_r=50
min_ball_dx=-5
max_ball_dx=5
min_ball_dy=-5
max_ball_dy=5

BALLS=[]

for i in range(number_of_balls):
    x = random.randint(-screen_width+max_ball_r,screen_width-max_ball_r)
    y = random.randint(-screen_height+max_ball_r,screen_height-max_ball_r)
    dx = random.randint(min_ball_dx,max_ball_dx)
    dy = random.randint(min_ball_dy,max_ball_dy)
    while dx==0 and dy==0:
        dx = random.randint(min_ball_dx,max_ball_dx)
        dy = random.randint(min_ball_dy,max_ball_dy)
    radius = random.randint(min_ball_r,max_ball_r)
    color = (random.random(),random.random(),random.random())
    ball=Ball(x,y,dx,dy,radius,color)
    BALLS.append(ball)

def move_all_balls():
    for ball in BALLS:
        ball.move(screen_width,screen_height)
    
def collide(ball_a,ball_b):
    d = math.sqrt(math.pow((ball_b.xcor()-ball_a.xcor()),2) + math.pow((ball_b.ycor()-ball_a.ycor()),2))
    if ball_a == ball_b:
        return False
    elif d+10<=ball_b.r+ball_a.r:
        return True
    else:
        return False

def check_all_balls_collision():
    for ball_a in BALLS:
        for ball_b in BALLS:
            if collide(ball_a,ball_b) == True:
                if ball_a.r*ball_a.r*3.1415926535 > ball_b.r*ball_b.r*3.1415926535:
                    ball_a.r+=1
                    ball_a.shapesize(ball_a.r/10)
                    x = random.randint(-screen_width+max_ball_r,screen_width-max_ball_r)
                    y = random.randint(-screen_height+max_ball_r,screen_height-max_ball_r)
                    ball_b.goto(x,y)
                    while ball_b.dx==0 or ball_b.dy==0:
                        ball_b.dx = random.randint(min_ball_dx,max_ball_dx)
                        ball_b.dy = random.randint(min_ball_dy,max_ball_dy)
                    ball_b.r = random.randint(min_ball_r,max_ball_r)
                    ball_b.shapesize(ball_b.r/10)
                    ball_b.color(random.random(),random.random(),random.random())
                elif ball_a.r*ball_a.r*3.1415926535 < ball_b.r*ball_b.r*3.1415926535:
                    ball_b.r+=1
                    ball_b.shapesize(ball_b.r/10)
                    x = random.randint(-screen_width+max_ball_r,screen_width-max_ball_r)
                    y = random.randint(-screen_height+max_ball_r,screen_height-max_ball_r)
                    ball_a.goto(x,y)
                    while ball_a.dx==0 or ball_a.dy==0:
                        ball_a.dx = random.randint(min_ball_dx,max_ball_dx)
                        ball_a.dy = random.randint(min_ball_dy,max_ball_dy)
                    ball_a.r = random.randint(min_ball_r,max_ball_r)
                    ball_a.shapesize(ball_a.r/10)
                    ball_a.color(random.random(),random.random(),random.random())
def check_myball_collision():
    for ball_c in BALLS:
        if collide(ball_c,MY_BALL) == True:
            if ball_c.r>MY_BALL.r:
                print("TOU LOST, LOOSERRRR")
                return False
            else:
                MY_BALL.r+=3
                global eaten_balls
                eaten_balls+=1
                MY_BALL.shapesize(MY_BALL.r/10)
                if MY_BALL.r>screen_width or MY_BALL.r>screen_height:
                    print("YOU WON, Well Done!!")
                    return False
                ball_c.x = random.randint(-screen_width+max_ball_r,screen_width-max_ball_r)
                ball_c.y = random.randint(-screen_height+max_ball_r,screen_height-max_ball_r)
                ball_c.goto(ball_c.x, ball_c.y)
                while ball_c.dx==0 or ball_c.dy==0:
                    ball_c.dx = random.randint(min_ball_dx,max_ball_dx)
                    ball_c.dy = random.randint(min_ball_dy,max_ball_dy)
                ball_c.r = random.randint(min_ball_r,max_ball_r)
                ball_c.shapesize(ball_c.r/10)
                ball_c.color(random.random(),random.random(),random.random())
    return True

def movearound(event):
    MY_BALL.goto(event.x-screen_width,screen_height-event.y)
turtle.getcanvas().bind("<Motion>", movearound)
turtle.listen()

while running == True:
    screen_width = turtle.getcanvas().winfo_width()/2
    screen_height = turtle.getcanvas().winfo_height()/2
    move_all_balls()
    check_all_balls_collision()
    running = check_myball_collision()
    turtle.getscreen().update()
    time.sleep(sleep)
    writer.penup()
    writer.goto(230,-250)
    writer.clear()
    writer.write("you ate " + str(eaten_balls) + " balls and your radius is " + str(MY_BALL.r), align = "center")

turtle.mainloop()

