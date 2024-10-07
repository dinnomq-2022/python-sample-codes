'''
Define the instance method __eq__ inside class Rectangle that when
 passed another object (not necessarily of type Rectangle), 
 returns True if the calling object and the passed object are "equal" 
 (both Rectangle with same dimensions). 
Note that rectangles of 4 by 6 and 6 by 4 are equal.

'''

class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            # Check if both rectangles have the same dimensions or swapped dimensions
            return (
                (self.length == other.length and self.breadth == other.breadth) or
                (self.length == other.breadth and self.breadth == other.length)
            )
        return False
    
r = Rectangle(2.5, 1.5)
s = Rectangle(1.5, 2.5)
print(r == s)
print(s == r)
t = Rectangle(2.5, 20)
print(r == t)
print(s == t)
v = Rectangle(2.5, 20.0)
print(v == t)
print(t == v)