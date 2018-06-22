#QUESTION 1

class Circle():
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14*( self.radius**2)
    def circumference(self):
        return 2*3.14*(self.radius)
r=int(input("enter radius"))
a=Circle(r)
b=Circle(r)
a.area()
b.circumference
print(a.area())
print(b.circumference())

#QUESTION 2
class Student():
    name= input("enter any name")
    rollno= int(input("enter any number"))
    def __init__(self):
        pass
    def display(self):
        print("the name is"+self.name)
        print("the rollno is",(self.rollno))
a=Student()
a.display()


#QUESTION 3
class Temperature():
    c = float(input("enter temperature in celsius"))
    f = float(input("enter temperature farenheit"))

    def __init__(self):
        pass
    def convertfarenheit(self):
        c=self.f*1.8+32
        print("temperature in farenheit is ",c)
    def convertcelsius(self):
        f=self.c *1.8-32
        print("temperature is celcius",f)

a=Temperature()
a.convertfarenheit()
a.convertcelsius()



#QUESTION 4

class MovieDetails():
    def __init__(self):
        pass
    def display(self,movieName,artistName,yearOfRelease,ratings):
        self.m=movieName
        self.a=artistName
        self.y=yearOfRelease
        self.r=ratings
        print(self.m,self.a,self.y,self.r)
    def update(self,movieName,artistName,yearOfRelease,ratings):
        self.m=input("enter the movie name")
        self.a = input("enter the artist name")
        self.y = int(input("enter the year of release"))
        self.r=float(input("enter the ratings"))
        print(self.m,self.a,self.y,self.r)
x=MovieDetails()
x.display("MS DHONI","Sushant Rajput",'2017','8.0')
y=MovieDetails()
y.update("m","a","y","r")


#QUESTION 5
class Expenditure():
    expense= float(input("enter expenditure"))
    save=float(input("enter savings"))
    def __init__(self):
        pass
    def display(self):
        print("expenditure is",self.expense)
        print("saving is ",self.save)
    def calculate_salary(self):
        total_salary=self.expense+self.save
        return total_salary
    def display_salary(self):
        print("total salary is ",e.calculate_salary())
e=Expenditure()
e.display()
e.calculate_salary()
e.display_salary()