import turtle

# made one turtle
squirtle_turtle = turtle.Turtle()

# creating a function to make a square
def squirtle():
    squirtle_turtle.forward(200)
    squirtle_turtle.right(90)
    squirtle_turtle.forward(200)
    squirtle_turtle.right(90)
    squirtle_turtle.forward(200)
    squirtle_turtle.right(90)
    squirtle_turtle.forward(200)
    squirtle_turtle.showturtle()

# creating a function to make a triangle
def staryu():
    squirtle_turtle.forward(200)
    squirtle_turtle.right(120)
    squirtle_turtle.forward(200)
    squirtle_turtle.right(120)
    squirtle_turtle.forward(200)

# creating power levels of various one piece characters
# powerlevel max is 100 which is pirate king
# getting katakuri and big mom powerlevel
katakuri_powerlevel = 50
bigmom_powerlevel = 90

# creating an if statement
# if katakuri's powerlevel is less than big mom's powerlevel then draw a square
# else draw a triangle
# should be true
if katakuri_powerlevel < bigmom_powerlevel:
    squirtle()
else:
    staryu()
