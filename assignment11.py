#QUESTION 1

import threading
from threading import Thread
import time

class Threads(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)


    def run(self):
        time.sleep(5)
        print("acad view")

t=Threads()
t.start()

#QUESTION 2

import threading
from threading import Thread
import time

class Mythread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)


    def run(self):
        for i in range(0,10):
            time.sleep(1)
            j=i+1
            print(j)
c=Mythread()
c.start()


#QUESTION 3

import threading
from threading import Thread
import time
class Mythread(threading.Thread):
    def __init__(self,list1):
        threading.Thread.__init__(self)
        self.list1=list1
    def run(self):
        count=0
        for i in self.list1:
            count +=2
            time.sleep(count)
            print(i)

list1=[]
n=int(input("enter elements"))
for i in range(n):
    j=input("enter elements")
    list1.append(j)

t=Mythread(list1)
t.start()

#QUESTION 4

import threading
from threading import Thread
import time
import math
class Fact(threading.Thread):
    def __init__(self,f):
        threading.Thread.__init__(self)
        self.f=f
    def run(self):
        print("factorial of",self.f,"is",math.factorial(self.f))
f=int(input("enter a number"))
f1=Fact(f)
f1.start()