#In this example, we have two parent classes Parent1 and Parent2,
# each with their own methods method1() and method2(), respectively.
# We then define a child class Child that inherits from both Parent1 and Parent2 and adds its own method method3().
# Finally, we create an object child1 of Child class and call its methods. The output of the program will be:

# Parent class 1
class Parent1:
    def method1(self):
        print("This is method 1 of Parent1.")

# Parent class 2
class Parent2:
    def method2(self):
        print("This is method 2 of Parent2.")

# Child class inheriting from Parent1 and Parent2
class Child(Parent1, Parent2):
    def method3(self):
        print("This is method 3 of Child.")

# Creating object of Child class
child1 = Child()

# Calling methods
child1.method1()
child1.method2()
child1.method3()


