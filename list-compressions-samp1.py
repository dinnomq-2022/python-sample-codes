
'''
numbers = [1, 2, 3, 4, 5]

numbers_power_3 = [n**3 for n in numbers]

print(numbers_power_3)
'''
#or
'''
numbers = [1, 2, 3, 4, 5]
numbers_power_3 = []
for n in numbers:
    numbers_power_3.append(n**3)

print(numbers_power_3)
'''

#or

numbers = [1, 2, 3, 4, 5]
numbers_power_3 = list(map(lambda n : n**3, numbers))
print(numbers_power_3)