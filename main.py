import turtle as t
import random


tim =t.Turtle()
my_screen = t.Screen()
tim.speed("fastest")
t.colormode(255)



def my_color():
    g = random.randint(0,255)
    b = random.randint(0,255)
    r = random.randint(0,255)
    color = (r ,g, b)
    return color

# circles
def set_distance(d,):
    for i in range(int(360/d)):
        tim.color(my_color())
        tim.circle(100)
        tim.setheading(tim.heading()+d)
    
set_distance(90)
my_screen.exitonclick()