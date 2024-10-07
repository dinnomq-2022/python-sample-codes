'''
Define a function named product, that when passed a number (assume it's an integer), returns the product of positive integers from 1 to that number (inclusive).

For example, if the number is 5, return 1*2*3*4*5 = 120.

For any number less than 1, return 1.
'''

def product(x):
    if x < 1:
        return 1
    result = 1

    for n in range(1, x + 1):
        result *= n
    return result

print(product(5))
print(product(10))
print(product(-6))
print(product(0))