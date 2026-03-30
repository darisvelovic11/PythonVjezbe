from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def speak(self):
        pass

    @abstractmethod
    def move(self):
        pass

    def describe(self):
        print(f"I am {self.name}, age {self.age}")


class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def speak(self):
        print(f"{self.name} says: Woof!")

    def move(self):
        print(f"{self.name} runs")


class Bird(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def speak(self):
        print(f"{self.name} says: Tweet!")

    def move(self):
        print(f"{self.name} flies")


class Fish(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def speak(self):
        print(f"{self.name} says: ...")

    def move(self):
        print(f"{self.name} swims")


# Loop through all animals
animals = [Dog("Rex", 3), Bird("Tweety", 1), Fish("Nemo", 2)]

for animal in animals:
    animal.describe()
    animal.speak()
    animal.move()
    print("---")

# Bonus — try instantiating Animal directly
#a = Animal("Test", 1)   # ❌ TypeError: Can't instantiate abstract class Animal
