#QUESTION 1
print("We represent time in a way that’s easy for us to understand.Python stores it in tuples.These python tuples are made of nine numbers.these are year,month,day,hour,minute,second,day of week ,day of year,dst")


#QUESTION 2


import time
print(time.strftime("%H:%M:%S"))


#QUESTION 3
import datetime
a='2018-06-21'
d=datetime.date.today()

datetime.date.today().strftime("%m,%Y,%d")
print(d.month)


#QUESTION 4
import datetime
d=(datetime.datetime.now())
newd=d.strftime("%A")
print(newd)

#QUESTION 5

import datetime
a='11/01/2021'
newd=(datetime.datetime.strptime(a,"%d/%m/%Y"))
print(newd.day)


#QUESTION 6
import time
a=time.localtime()
print(a)


#QUESTION 7
import math
n=int(input("enter any number"))
print("The factorial is:", end=" ")
print(math.factorial(n))


#QUESTION 8
import math
a=int(input("enter any number"))
b=int(input("enter any number"))
print(math.gcd(a,b))


#QUESTION 9
#(i)

import os
print(os.getcwd())
#(ii)

import os
print(os.environ)
