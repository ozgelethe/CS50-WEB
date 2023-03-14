# Object Oriented Programming is a programming paradigm, 
# or a way of thinking about programming, that is centered 
# around objects that can store information and perform actions.

#  Here’s a class that defines a two-dimensional point:

class Point():
    def __init__(self, inputx, inputy):
        self.x = inputx
        self.y = inputy

# Note that in the above code, we use the keyword self to represent 
# the object we are currently working with. self should be the first 
# argument for any method within a Python class.

p = Point(2, 8)

print(p.x)
print(p.y)