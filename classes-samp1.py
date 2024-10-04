class Animal:
    def hop(self):
        return "Hopping!!"


class Goat(Animal):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bleat(self):
        return "me-ehh-ehh!"

hoofy = Goat("Hoofy", 5)

print(hoofy.name)
print(hoofy.age)
print(hoofy.bleat())
print(hoofy.hop())