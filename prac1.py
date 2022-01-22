"""fruit = {'apple': 50, 'banana': 20, 'orange': 50, 'peach': 100}
print(type(fruit))
# print(fruit.keys())
# print(fruit.values())
# print(fruit.items())
fruit['mango'] = 120
print(fruit)
fruit['apple'] = 10
print(fruit)"""


# Dictionary functions

fruit1 = {'apple': 100, 'mango': 200}
fruit2 = {'guava': 30, 'grapes': 60}

fruit1.update(fruit2)

print(fruit1)
fruit1.pop('apple')
print(fruit1)
