class Animal:
    def __init__(self, name):
        self.name = name
    
    def make_sound(self):
        pass
        
class Dog(Animal):
    def make_sound(self):
        return "Woof"
        
class Cat(Animal):
    def make_sound(self):
        return "Meow"
        
animals = [Dog("Rufus"), Cat("Whiskers"), Dog("Buddy"), Cat("Socks")]

for animal in animals:
    print(animal.name + ": " + animal.make_sound())