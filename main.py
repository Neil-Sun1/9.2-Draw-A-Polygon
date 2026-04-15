from turtle import *

t= Turtle()
s=Screen()
s.bgcolor("black")
t.color("white")
t.hideturtle()
def draw_polygon(sides, length=100):
    angle = 360 / sides
    for i in range(sides):
        t.forward(length)
        t.left(angle)

def draw_rectangle(width, height):
    for i in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)

def draw_parallelogram(side1, side2, angle):
    for i in range(2):
        t.forward(side1)
        t.left(angle)
        t.forward(side2)
        t.left(180 - angle)

def draw_trapezoid():
    t.forward(150)
    t.left(120)
    t.forward(60)
    t.left(60)
    t.forward(90)
    t.left(60)
    t.forward(60)

sides = int(input("How many sides does your shape have? "))

if sides == 3:
    print("It's a Triangle!")
    draw_polygon(3)
elif sides == 4:
    parallel_pairs = input("How many pairs of parallel sides? (0, 1, or 2): ")
    
    if parallel_pairs == "0":
        print("Unknown quadrilateral")
        t.forward(100)
        t.left(100)
        t.forward(80)
        t.left(70)
        t.forward(110)
        t.goto(0,0)
        
    elif parallel_pairs == "1":
        draw_trapezoid()
        
    elif parallel_pairs == "2":
        equal_sides = input("Are all four sides equal length? (yes/no): ").lower()
        right_angles = input("Are all four angles 90 degrees? (yes/no): ").lower()
        
        if equal_sides == "yes" and right_angles == "yes":
            draw_polygon(4)
        elif right_angles == "yes":
            draw_rectangle(150, 80)
        elif equal_sides == "no":
            draw_parallelogram(120, 70, 60)
            
elif sides == 5:
    draw_polygon(5)
elif sides == 6:
    draw_polygon(6)
else:
    draw_polygon(sides)























s.exitonclick()