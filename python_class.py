class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"


bingo = Dog("bingo", 9)
buddy = Dog("buddy", 4)

print(buddy.name)
print(buddy.age)
print()
print(bingo.name)
print(bingo.age)
