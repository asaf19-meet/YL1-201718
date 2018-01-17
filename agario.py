import turtle
import time
import random
import math 
from ball import Ball

#turtle.tracer(0,1)
turtle.hideturtle()

running = True
sleep = 0.0077
screen_width=turtle.getcanvas().winfo_width()/2
screen_height=turtle.getcanvas().winfo_height()/2

MY_BALL=Ball(5,5,8,8,50,"green")

number_of_balls = 5
min_ball_r=10
max_ball_r=100
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
    radius = random.randint(min_ball_r,max_ball_r)
    color = (random.random(),random.random(),random.random())
    ball=Ball(x,y,dx,dy,radius,color)
    BALLS.append(ball)

for ball in BALLS:
    ball.move(screen_width,screen_height)
    
def collide(ball_a,ball_b):
    d = math.sqrt(math.pow((ball_b.x-ball_a.x),2) + math.pow((ball_b.y-ball_a.y),2))
    if ball_a.r == ball_b.r and ball_a.x==ball_b.x and ball_a.y==ball_b.y:
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
                    ball_a.r=+1
                    ball_b.x = random.randint(-screen_width+max_ball_r,screen_width-max_ball_r)
                    ball_b.y = random.randint(-screen_height+max_ball_r,screen_height-max_ball_r)
                    ball_b.goto(x,y)
                    ball_b.dx = random.randint(min_ball_dx,max_ball_dx)
                    ball_b.dy = random.randint(min_ball_dy,max_ball_dy)
                    ball_b.radius = random.randint(min_ball_r,max_ball_r)
                    ball_b.shapesize(radius/10)
                    ball_b.color(random.random(),random.random(),random.random())
                elif ball_a.r*ball_a.r*3.1415926535 < ball_b.r*ball_b.r*3.1415926535:
                    ball_b.r=+1
                    ball_a.x = random.randint(-screen_width+max_ball_r,screen_width-max_ball_r)
                    ball_a.y = random.randint(-screen_height+max_ball_r,screen_height-max_ball_r)
                    ball_a.goto(x,y)
                    ball_a.dx = random.randint(min_ball_dx,max_ball_dx)
                    ball_a.dy = random.randint(min_ball_dy,max_ball_dy)
                    ball_a.radius = random.randint(min_ball_r,max_ball_r)
                    ball_a.shapesize(radius/10)
                    ball_a.color(random.random(),random.random(),random.random())
def check_myball_collision():
    for ball_c in BALLS:
        if collide(ball_c,MY_BALL) == True:
            if ball_c.r>MY_BALL.r:
                return False
            elif ball_c.r<MY_BALL.r:
                MY_BALL.r=+1
                ball_c.x = random.randint(-screen_width+max_ball_r,screen_width-max_ball_r)
                ball_c.y = random.randint(-screen_height+max_ball_r,screen_height-max_ball_r)
                ball_c.goto(x,y)
                ball_c.dx = random.randint(min_ball_dx,max_ball_dx)
                ball_c.dy = random.randint(min_ball_dy,max_ball_dy)
                ball_c.radius = random.randint(min_ball_r,max_ball_r)
                ball_c.shapesize(radius/10)
                ball_c.color(random.random(),random.random(),random.random())
    return True

def movearound(event):
    MY_BALL.goto(evet.x-screen_width,screen_height-event.y)

while running == True:
    screen_width = turtle.getcanvas().winfo_width()/2
    screen_height = turtle.getcanvas().winfo_height()/2
    for ball in BALLS:
        ball.move(screen_width,screen_height)
    check_myball_collision()
    check_all_balls_collision()
    MY_BALL.move(screen_width,screen_height)
    
    
        
    

    


