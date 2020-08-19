class Animals:
    def __init__(self, color):
        self.color = color

    def colorPet(self):
        return(self.color)

class Dog(Animals):
    def speak(self):
        return "bhoooo bhoooo"

class Cat(Animals):
    def speak(self):
        return "Meow Meow"

d = Dog("red")
print(d.speak())
print(d.colorPet())

c = Cat("Blue")
print(c.speak())
print(c.colorPet())