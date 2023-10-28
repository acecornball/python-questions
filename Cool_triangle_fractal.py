hacktoberfest-acceptedimport turtle

# Function to draw a Sierpinski Triangle
def sierpinski_triangle(turtle, order, size):
    if order == 0:
        for _ in range(3):
            turtle.forward(size)
            turtle.left(120)
    else:
        size /= 2
        sierpinski_triangle(turtle, order - 1, size)
        turtle.forward(size)
        sierpinski_triangle(turtle, order - 1, size)
        turtle.backward(size)
        turtle.left(60)
        turtle.forward(size)
        turtle.right(60)
        sierpinski_triangle(turtle, order - 1, size)
        turtle.left(60)
        turtle.backward(size)
        turtle.right(60)

# Create a Turtle screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a Turtle object
t = turtle.Turtle()
t.speed(0)  # Set the drawing speed (0 is the fastest)

# Define the Sierpinski Triangle parameters
order = 4  # Change the order as desired
size = 200

# Move the turtle to the starting position
t.penup()
t.goto(-size / 2, -size / 2)
t.pendown()

# Call the Sierpinski Triangle function
sierpinski_triangle(t, order, size)

# Close the Turtle graphics window on click
screen.exitonclick()
