#In this example, we have a parent class Animal with two methods eat() and sleep(). 
#We then define three child classes Cat, Dog, and Horse that inherit from Animal and
#add their own methods purr(), bark(), and gallop(), respectively. Finally, we create
#objects cat1, dog1, and horse1 and call their methods. The output of the program will be:

# Parent class
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

# Child class inheriting from Animal
class Cat(Animal):
    def __init__(self, name, species, color):
        super().__init__(name, species)
        self.color = color

    def purr(self):
        print(f"{self.name} is purring.")

# Child class inheriting from Animal
class Dog(Animal):
    def __init__(self, name, species, breed):
        super().__init__(name, species)
        self.breed = breed

    def bark(self):
        print(f"{self.name} is barking.")

# Child class inheriting from Animal
class Horse(Animal):
    def __init__(self, name, species, color):
        super().__init__(name, species)
        self.color = color

    def gallop(self):
        print(f"{self.name} is galloping.")

# Creating objects
cat1 = Cat("Whiskers", "Felis catus", "white")
dog1 = Dog("Buddy", "Canis lupus familiaris", "Golden Retriever")
horse1 = Horse("Thunder", "Equus ferus caballus", "brown")

# Calling methods
cat1.eat()
cat1.sleep()
cat1.purr()

dog1.eat()
dog1.sleep()
dog1.bark()

horse1.eat()
horse1.sleep()
horse1.gallop()