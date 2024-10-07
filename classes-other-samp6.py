'''
1. Define a class named Date that has three instance variables: 
day, month, year. Implement the __init__ method that is passed 
values for each of the instance variables. 
2. Define a class named Time that has three instance variables: 
hour, minute, second. Implement the __init__ method that is passed
 values for each of the instance variables. 
3. Define a class named Testing that contains one Date object and 
one Time object (named date, time). Implement the __init__ method that 
is passed a Date object and Time object, and they are copied into the 
instance variables/attributes.
'''

class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

class Testing:
    def __init__(self, date, time):
        self.date = date
        self.time = time

# Example usage:
if __name__ == "__main__":
    d = Date(13, 4, 2011)
    t = Time(10, 30, 0)
    dt = Testing(d, t)
    
    # Accessing and displaying the Date attributes
    print(dt.date.day)
    print(dt.date.month)
    print(dt.date.year)
    
    # Accessing and displaying the Time attributes
    print(dt.time.hour)
    print(dt.time.minute)
    print(dt.time.second)

