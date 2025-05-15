class Animal:
    def voice(self):
        pass

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
