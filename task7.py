class Animal:
    _count = 0

    def __init__(self):
        Animal._count += 1

    def voice(self):
        pass

    def get_instance_count():
        return Animal._count

class Dog(Animal):
    def voice(self):
        return "Dog"

class Cat(Animal):
    def voice(self):
        return "Cat"

class Cow(Animal):
    def voice(self):
        return "Cow"

dog = Dog()
cat = Cat()
cow = Cow()

print(dog.voice())
print(cat.voice())
print(cow.voice())

print(Animal.get_instance_count())
