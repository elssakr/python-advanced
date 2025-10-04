class Dog:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print(f"{self.name} make this sound:Woof")


class Cat:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print(f"{self.name} make this sound:Mewoo")


class Bird:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print(f"{self.name} make this sound:Ciuciu")

dog = Dog ("Bred")
cat = Cat ("lili")
bird = Bird("pop")

for animal in (dog,cat,bird):
    animal.sound()