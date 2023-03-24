#This example shows the use of __init__ constructor

class Vehicle():
    #__init__ is used to set values as soon as new object are created
    #__init__ is a keyword hence it has to be named like it is
    def __init__(self):     #called automatically hence known as magic method
        print('Calling init')
        self.val = 0
        self.cost = 10000   #Setting the default value when the object is created

    def incrementVehicle(self):
        self.val += 1


car = Vehicle()     #__init__ is called
print('First obj value:',car.val)
car.incrementVehicle()
car.incrementVehicle()
print('First obj value after incrementing:',car.val)      #2

bike = Vehicle()       #__init__ is called makes val 0 for this ANOTHER instance
print('Second obj value:',bike.val)




#Use of constructor in python
#__init__(constructor)
#Design a class whose object  can be initialize while they are created
class Student:
    def __init__ (self,nm,rn,br,*mks):
        self.Name=nm
        self.Rollno=rn
        self.Branch=br
        self.Marks=mks
    def showdata(self):
        print("Name is",self.Name)
        print("Rollno is",self.Rollno)
        print("Branch is",self.Branch)
        print("Marks is",self.Marks) 
    def Total(self):
        t=0
        for mk in self.Marks:
            t=t+mk
            return(t)
    def Percentage(self):
        c=0
        for mk in self.Marks:
            c=c+1
        p=self.total()/c
        return p
    def result(self):
        for mk in self.Marks:
            if m<40:
                return "fail"
            else:
                return "Pass"

a=Student(4117,"Tanvi karale",AIDS,95,98,89)
a.showdata()
print("Total is",a.total())
print("Percentage is",a.percentage) 
print("Result is",a.result())     




   

    
 