import turtle

my_wn = turtle.Screen()   # ✅ Capital 'S'
t = turtle.Turtle()       # ✅ Create a Turtle object
t.speed(2)

for i in range(30):
    t.circle(5 * i)
    t.circle(-5 * i)
    t.left(i)

turtle.exitonclick()
