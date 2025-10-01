import turtle

# object
pen = turtle.Turtle() 

# function
def ring(col, rad):
    pen.fillcolor(col)
    pen.begin_fill()
    pen.circle(rad)
    pen.end_fill()

# ears
pen.up()
pen.setpos(-35, 95)
pen.down()
ring('black', 15)

pen.up()
pen.setpos(35, 95)
pen.down()
ring('black', 15)

# face
pen.up()
pen.setpos(0, 35)
pen.down()
ring('white', 40)

# eyes
pen.up()
pen.setpos(-18, 75)
pen.down()
ring('black', 8)

pen.up()
pen.setpos(18, 75)
pen.down()
ring('black', 8)

# pupils
pen.up()
pen.setpos(-18, 77)
pen.down()
ring('white', 4)

pen.up()
pen.setpos(18, 77)
pen.down()
ring('white', 4)

# nose
pen.up()
pen.setpos(0, 55)
pen.down()
ring('black', 5)


# end
pen.hideturtle()
turtle.done()