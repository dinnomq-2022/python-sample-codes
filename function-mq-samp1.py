def sign(x,y):
    if x >0 and y >0:
        return 1
    elif x <0 and y < 0:
        return -1
    else:
        return 0

print(sign(10, 20))
print(sign(10, 0))
print(sign(-10000, -51))
print(sign(0, -555))