#This program illustrates the concept of inheritance
#Python looks up for method in following order: Instance attributes, class attributes and the
#from the base class

class Data(object):
    def getData(self):
        print('In data!')

class Time(Data):           #Inheriting from Data class
    def getTime(self):
        print('In Time!')

if __name__ == '__main__':
    data = Data()
    time = Time()

    data.getData()
    time.getTime()
    time.getData()          #Inherited Data method




    
#Inheritance method in python
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

# Creating objects
cat1 = Cat("Whiskers", "Felis catus", "white")
dog1 = Dog("Buddy", "Canis lupus familiaris", "Golden Retriever")

# Calling methods
cat1.eat()
cat1.sleep()
cat1.purr()

dog1.eat()
dog1.sleep()
dog1.bark()
