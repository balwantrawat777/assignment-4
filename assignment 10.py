#QUESTION 1

class Animal:
    def __init__(self):
        pass
    def eat(self):
        print("eating")

class Tiger(Animal):
    def colour(self):
        print("brown")

    pass

d=Tiger()
d.eat()
d.colour()

#QUESTION 2

#The output of print a.f() will be A & B
#The output of print b.f() will be A & B


#QUESTION 3

class Cop:
    def __init__(self,name,age,workexperience,designation):
        self.name=name
        self.age=age
        self.workexperience=workexperience

        self.designation=designation

    def add(self):
        place=input("enter any place")
        self.place=place

    def display(self):
        print("name is ",self.name)
        print("age is ", self.age)
        print("work experience is ",self.workexperience)
        print("designation is ",self.designation)
        print("working place is ",self.place)

    def update(self):
        name=input("enter any name")
        self.name=name
        age=input("enter age")
        self.age=age
        workexperience=input("enter work expereince")
        self.workexperience=workexperience
        designation=input("enter designation")
        self.designation=designation
        place=input("enter any place")
        self.place=place
        print("update information is ")
        c.display()
name=input("enter name")
age=input("enter age")
workexperience=input("enter work experience")
designation=input("enter designation")
place=input("enter place")
class Mission(Cop):
    def add_mission_details(self):
        pass

c=Cop(name,age,workexperience,designation)
m=Mission(name,age,workexperience,designation)
c.add()
c.display()
c.update()
m.display

#QUESTION 4

class Shape:
    length= float(input("enter length"))
    breadth=float(input("enter breadth"))
    def __init__(self):
        pass
class Rectangle(Shape):
    area=Shape.length*Shape.breadth
    print("area of rectangle is:",area)
class Sqaure(Shape):
    area=Shape.length**2
    print("area of square is",area)
a=Shape()
r=Rectangle()
s=Sqaure()