import turtle

# made one turtle
squirtle_turtle = turtle.Turtle()

# giving the turtle more speed
squirtle_turtle.speed(10)
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

# counting the numbers from 0 to 10 based on the range using for loop
for count in range(11):
    print(count)

# drawing 20 squares using for loop
for square in range(21):
    squirtle()

#drawing 21 triangles using for loop
for triangle in range(22):
    staryu()