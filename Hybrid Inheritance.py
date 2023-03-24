#In this example, we have two parent classes Parent1 and Parent2, each with their own methods method1() and method2(), respectively.
# We then define two child classes Child1 and Child2 that inherit from Parent1 and Parent2, respectively, 
#and add their own methods method3() and method4(), respectively. 
#Finally, we define a grandchild class GrandChild that inherits from both Child1 and Child2 and adds its own method method5().
# We create an object grandchild1 of GrandChild class and call its meth
# Parent class 1
class Parent1:
    def method1(self):
        print("This is method 1 of Parent1.")

# Parent class 2
class Parent2:
    def method2(self):
        print("This is method 2 of Parent2.")

# Child class inheriting from Parent1
class Child1(Parent1):
    def method3(self):
        print("This is method 3 of Child1.")

# Child class inheriting from Parent2
class Child2(Parent2):
    def method4(self):
        print("This is method 4 of Child2.")

# Grandchild class inheriting from both Child1 and Child2
class GrandChild(Child1, Child2):
    def method5(self):
        print("This is method 5 of GrandChild.")

# Creating object of GrandChild class
grandchild1 = GrandChild()

# Calling methods
grandchild1.method1()
grandchild1.method2()
grandchild1.method3()
grandchild1.method4()
grandchild1.method5()