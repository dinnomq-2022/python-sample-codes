# Define a function count_values that when passed a String->int dictionary and an integer (say, val), returns the number of keys that have val as the corresponding value.


def count_values(dict,val):
    count = 0
    for key, value in dict.items():
        if value == val:
            count = count + 1
    return count
        
d = {"a":1,"b":2,"c":4,"d":1}
v = 1
r = count_values(d, v)
print(r)


print(count_values({"a":1,"b":2,"c":4,"d":1}, 2))
print(count_values({"a":1,"b":2,"c":4,"d":1}, 4))
print(count_values({"a":1,"b":2,"c":4,"d":1}, 5))
print(count_values({}, 1))