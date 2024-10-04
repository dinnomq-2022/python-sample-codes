from functools import reduce

fruit_costs = [('Apple', 10), ('Orange', 8)]

'''
fruit_costs = [('Apple', 10), ('Orange', 8), ('Mango',13)]
sum = 0
for cost in fruit_costs:
    sum += cost[1] '''

sum = reduce(lambda a, b, : a[1] + b[1],  fruit_costs)

print(sum)