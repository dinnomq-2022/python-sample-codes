'''
Define an instance method named area 
inside class Rectangle that returns the area of the calling object.
'''

class Rectangle:
    def __init__(self, len, bre):
        self.length = len
        self.breadth = bre

    def area(self):
        return self.length * self.breadth
    

r = Rectangle(2.5, 1.5)
print(r.area())
s = Rectangle(1.2, 2.4)
print(s.area())
t = Rectangle(10, 20)
print(t.area())