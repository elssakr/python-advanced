class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def greet(self):
        print(f"Hello, I am {self.name} and I am {self.age} years old")

Person1=Person("Elsa",17)
Person2=Person("Alisa",23)

Person1.greet()
Person2.greet()
