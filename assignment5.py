#QUESTION 1

a=int(input("enter any year"))
if(a%4==0):
    print("a leap year")
else:
    print("not a leap year")
#end

#QUESTION 2
l=int(input("enter the length"))
b=int(input("enter the breadth"))
if(l==b):
    print("square")
else:
    print("rectangle")
#end

#QUESTION 3

a=int(input("age of naveen"))
b=int(input("age of  aayu"))
c=int(input("age of rock"))
if(a>b) and (a>c):
    print("naveen is oldest")
elif(a<b) and (a<c):
    print("naveen is youngest")
if(b>a) and (b>c):
    print("aayu is oldest")
elif(b<a)and(b<c):
    print("aayu is youngest")
if(c > a) and (c > b):
    print("rock is oldest")
elif(c<a)and(c<b):
     print("rock is youngest")
else:
    print("same age")
#end

#QUESTION 4

a=int(input("enter the point scored"))
if(a>=1)and(a<=50):
    print("sorry this time no prize")
elif(a>=51)and(a<=150):
    print("your prize is wooden dog")
elif ( a>=151)and(a<=180):
    print("your prize is book")
elif(a>=181)and(a<=200):
    print("your prize is chocolate")
else:
     print("invalid score")
#end

#QUESTION 5
quantity=int(input("enter the quantity"))
price=quantity*100
if(price>1000):
    total_discount=price*10/100
    total_price=price-total_discount
    print("total price is",total_price)
else:
    print(price)
#end