from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = age
        self._weight = weight
        self._height = height

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        if value <= 0:
            raise ValueError("Weight must be positive.")
        self._weight = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value <= 0:
            raise ValueError("Height must be positive.")
        self._height = value

    @abstractmethod
    def calculate_bmi(self):
        pass

    @abstractmethod
    def get_bmi_category(self, bmi):
        pass

    def print_info(self):
        bmi = self.calculate_bmi()
        print(f"\nName: {self.name}")
        print(f"Age: {self.age}")
        print(f"BMI: {bmi:.2f} ({self.get_bmi_category(bmi)})")


class Adult(Person):
    def calculate_bmi(self):
        return self.weight / (self.height ** 2)

    def get_bmi_category(self, bmi):
        if bmi < 18.5:
            return "Underweight"
        elif bmi < 24.9:
            return "Normal"
        elif bmi < 29.9:
            return "Overweight"
        else:
            return "Obese"


class Child(Person):
    def calculate_bmi(self):
        return (self.weight / (self.height ** 2)) * 1.3

    def get_bmi_category(self, bmi):
        if bmi < 14:
            return "Underweight"
        elif bmi < 18:
            return "Normal"
        elif bmi < 24:
            return "Overweight"
        else:
            return "Obese"


class BMIApp:
    def __init__(self):
        self.people = []

    def add_person(self, person):
        self.people.append(person)

    def collect_data(self):
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        weight = float(input("Enter weight (kg): "))
        height = float(input("Enter height (m): "))

        if age < 18:
            person = Child(name, age, weight, height)
        else:
            person = Adult(name, age, weight, height)

        self.add_person(person)
        print(f"{name} added successfully!")

    def run(self):
        while True:
            print("\n1 - Add person")
            print("2 - Show all results")
            print("3 - Exit")
            choice = input("Choose: ")

            if choice == "1":
                self.collect_data()
            elif choice == "2":
                if not self.people:
                    print("No data yet.")
                else:
                    for p in self.people:
                        p.print_info()
            elif choice == "3":
                print("Exiting... Bye!")
                break
            else:
                print("Invalid choice, try again!")


if __name__ == "__main__":
    BMIApp().run()
