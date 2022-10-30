#coding by raNi TRIXCKER 
#fb Id'z https://www.facebook.com/mistyxd0.2

# https://youtube.com/channel/UCbT--Z1XzQpSUgjD6bfzzUA

#coding=utf


import turtle

t = turtle.Turtle()

s = turtle.Screen ()

s.bgcolor('black') 

t.hideturtle()

t.goto (0,-10)

t.pensize (3) 

t.color('red')

t.begin_fill()

t.left(140)

t.forward (180)

t.circle(-90,200)

t.setheading (60)

t.circle(-90,200)

t.forward(178)

t.end_fill()

t.penup()

t.goto (-75,130)

t.pendown()

t.color('white')

t.write("I Love You", ("Verdana", 25, "bold"))

t.penup() 
t.goto (-220,-180)

t.pendown ()

t.color('white')

t.write("Smart Programming",font=("Verdana", 15, "bold"))

turtle.done()
