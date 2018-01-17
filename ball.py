from turtle import Turtle

class Ball(Turtle):
    def __init__(self,x,y,dx,dy,r,color):
        Turtle.__init__(self)
        self.penup()
        self.goto(x,y)
        self.x=x
        self.y=y
        self.dx=dx
        self.dy=dy
        self.r=r
        self.shapesize(r/10)
        self.color(color)
        self.shape("circle")
        
    def move(self,screen_width,screen_height):
        current_x = self.xcor()
        new_x = current_x+self.dx
        current_y = self.ycor()
        new_y = current_y+self.dy
        right_side_ball = new_x+self.r
        left_side_ball = new_x-self.r
        up_side_ball = new_y+self.r
        down_side_ball = new_y-self.r
        self.goto(new_x,new_y)
        if screen_width<=right_side_ball:
            self.dx=-self.dx
        elif screen_width<=left_side_ball:
            self.dx=-self.dx
        elif screen_height<=up_side_ball:
            self.dy=-self.dy
        elif screen_height<=down_side_ball:
            self.dy=-self.dy
            


