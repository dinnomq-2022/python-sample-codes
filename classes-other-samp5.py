class Rectangle:
    def __init__(self, len, bre):
        self.length = len
        self.breadth = bre
        
    def area(self):
        return self.length * self.breadth
    
    def __eq__(self, other):
        if isinstance(other, Rectangle):    
            if self.length == other.length and self.breadth == other.breadth:
                return True
            if self.length == other.breadth and self.breadth == other.length:
                return True
        return False
        
    def __str__(self):
        return str(self.length) + " by " + str(self.breadth)
        

if __name__ == "__main__":
    # Create a Rectangle r with length as 1.2 and breadth as 1.5
    r = Rectangle(1.2, 1.5)
    
    # Display the object r
    print(r)
    
    # Create a Rectangle s with length as 1.5 and breadth as 1.2
    s = Rectangle(1.5, 1.2)
    
    # Display the object s
    print(s)
    
    # Display the outcome of comparing r with s for equality
    print(r == s)
