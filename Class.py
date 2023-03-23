#Python Program to create a two boxex

class Box:
    def setDimension(self,x,y,z):
        self.length=x
        self.breadth=y
        self.height=z
    def Volume(self):
        v=self.length*self.breadth*self.height
        print("Volume is",v)       

a=Box()
b=Box()
a.setDimension(5,6,7)
b.setDimension(2,3,4)
a.Volume()
b.Volume()



#Python Program to create a two worker type of object

class Worker:
    def setData(self,n,w,d):
        self.name=n
        self.wages=w
        self.wdays=d
    def showdata(self):
        print("Name is",self.name)
        print("wages is",self.wages)
        print("Wdays is",self.wdays)
    def payment(self):
        p=self.wages*self.wdays
        print("Payment is",p)

a=Worker()
b=Worker()
a.setData("Raja",500,5)
b.setData("Gaja",400,8)
a.showdata()
a.payment()
b.showdata()
b.payment()


#Python program to find length breadth and area of rectangle

class Rectangle:
	def setDimension(self,x,y):
		self.length=x
		self.breadth=y
	def area(self):
		a=self.length*self.breadth
		return a
a=Rectangle()
b=Rectangle()
a.setDimension(5,7)
b.setDimension(10,20)
z=a.area()+b.area()
print("Total is",z)
print("Area of a is",a.area())
print("Area of b is",b.area())

#Python Program to find total marks,percentage and also show student is pass or fail

class Student():
    def setData(self,rn,nm,**mks):
        self.rollno=rn
        self.name=nm
        self.marks=mks
    def showdata(self):
        print("Roll no is",self.rollno)
        print("Name is",self.name)
        print("Marks is",self.marks)
    def Total(self):
        t=0
        for mk in self.marks:
            t=t+mks
        return(t)
    def Percentage(self):
        c=0
        for mk in self.mks:
            c=c+1
            m=self.sum()/c
        return(m)
    def Result(self):
        for mk in self.mks:
            if mk<40:
                return "Fail"
        else:
            return "Pass"
a=Student()
a.setData(1145,"Tanvi",Eng=45,Math=67,Mar=56,PMP=45)
a.showdata()
print("Total is",a.Total)
print("Percentage is",a.Percentage)
print("Result is",a.Result)