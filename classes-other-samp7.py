'''
Add an instance method named inverse in class Fraction that returns an object representing the inverse of the calling object.

For example, the inverse of 3/5 is 5/3. The inverse of 12/100 is 100/12.

If the denominator of the calling object is 0, return None.
'''

class Fraction:
    def __init__(self, n, d):
        if d == 0:
             raise ValueError("Denominator cannot be zero.")
        self.num = n
        self.den = d

    def inverse(self):
        if self.num == 0:
            return None
        return Fraction(self.den, self.num)
    
f = Fraction(3, 10)
g = f.inverse()
print(g.num,g.den)

f = Fraction(-3, 10)
g = f.inverse()
print(g.num,g.den)

f = Fraction(0, 10)
g = f.inverse()
print(g)

f = Fraction(8, 0)
g = f.inverse()
print(g)