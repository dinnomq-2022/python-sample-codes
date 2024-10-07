'''Define a class named Rectangle that represents a rectangle with two attributes:
 length and breadth. Implement the __init__ method that is passed values 
 for each of the attributes, and those values are copied into the 
 respective attributes.'''

class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

r = Rectangle(2.5, 1.5)
print(r.length,r.breadth)
s = Rectangle(1.5, 2.5)
print(s.length,s.breadth)
t = Rectangle(10, 20)
print(t.length,t.breadth)