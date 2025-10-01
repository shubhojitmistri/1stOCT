#Import turtle
import turtle
import turtle as t

#set speed of the turtle
t.speed(20)
pattern=0

#set the screen to pink color
scr=turtle.Screen()
scr.bgcolor("pink")


for i in range(100):
    for color in  ["blue","green"]:
        t.color(color)
        t.forward(pattern)
        t.right(90)
        t.right(1)
        pattern+=1

turtle.done